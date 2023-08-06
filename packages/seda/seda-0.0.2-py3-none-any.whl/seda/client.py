import base64
import json
import string
import typing as t

from botocore.client import BaseClient
from typing_extensions import Literal

from seda import exceptions
from seda.session import Session


class Client:
    def __init__(self, session: Session) -> None:
        self._client_cache: t.Dict[str, BaseClient] = {}
        self.session = session

    def client(self, service_name: str) -> BaseClient:
        if service_name not in self._client_cache:
            self._client_cache[service_name] = self.session.client(service_name)
        return self._client_cache[service_name]

    def dumps(self, data: t.Any) -> str:
        class TemplateEncoder(json.JSONEncoder):
            def default(_, o: t.Any) -> t.Any:
                if isinstance(o, string.Template):
                    return o.substitute(
                        region=self.session.region,
                        account_id=self.session.account_id,
                    )
                return super().default(o)

        return json.dumps(data, indent=2, cls=TemplateEncoder)

    def get_role(self, role_name: str) -> bool:
        client = self.client("iam")
        try:
            return client.get_role(RoleName=role_name)
        except client.exceptions.NoSuchEntityException:
            raise exceptions.ResourceDoesNotExist("Role not found")

    def create_role(self, name: str, trust_policy: t.Any, policy: t.Any) -> str:
        client = self.client("iam")
        result = client.create_role(
            RoleName=name,
            AssumeRolePolicyDocument=self.dumps(trust_policy),
        )
        try:
            self.put_role_policy(
                role_name=name,
                policy_name=name,
                policy_document=policy,
            )
        except client.exceptions.MalformedPolicyDocumentException as e:
            self.delete_role(name=name)
            raise e
        return result["Role"]["Arn"]

    def put_role_policy(
        self,
        role_name: str,
        policy_name: str,
        policy_document: t.Any,
    ) -> None:
        client = self.client("iam")
        client.put_role_policy(
            RoleName=role_name,
            PolicyName=policy_name,
            PolicyDocument=self.dumps(policy_document),
        )

    def delete_role(self, name: str) -> None:
        client = self.client("iam")
        for policy_name in client.list_role_policies(RoleName=name)["PolicyNames"]:
            self.delete_role_policy(name, policy_name)
        client.delete_role(RoleName=name)

    def delete_role_policy(self, role_name: str, policy_name: str) -> None:
        client = self.client("iam")
        client.delete_role_policy(RoleName=role_name, PolicyName=policy_name)

    def get_schedule_group(self, name: str) -> t.Any:
        client = self.client("scheduler")
        try:
            return client.get_schedule_group(Name=name)
        except client.exceptions.ResourceNotFoundException:
            raise exceptions.ResourceDoesNotExist("Schedule group not found")

    def create_schedule_group(self, name: str) -> str:
        client = self.client("scheduler")
        result = client.create_schedule_group(Name=name)
        return result["ScheduleGroupArn"]

    def delete_schedule_group(self, name: str) -> None:
        client = self.client("scheduler")
        try:
            client.delete_schedule_group(Name=name)
        except client.exceptions.ResourceNotFoundException:
            raise exceptions.ResourceDoesNotExist("Schedule group not found")

    def list_schedules(self, group_name: str) -> t.Any:
        client = self.client("scheduler")
        try:
            return client.list_schedules(GroupName=group_name)
        except client.exceptions.ResourceNotFoundException:
            raise exceptions.ResourceDoesNotExist("Schedule group not found")

    def get_schedule(self, name: str, group_name: str) -> t.Any:
        client = self.client("scheduler")
        try:
            return client.get_schedule(Name=name, GroupName=group_name)
        except client.exceptions.ResourceNotFoundException:
            raise exceptions.ResourceDoesNotExist("Schedule not found")

    def create_schedule(
        self,
        name: str,
        group_name: str,
        expression: str,
        target_arn: str,
        role_arn: str,
        *,
        timezone: t.Optional[str] = None,
        target_input: t.Optional[t.Any] = None,
        time_window: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> str:
        client = self.client("scheduler")

        data = {
            "Name": name,
            "GroupName": group_name,
            "ScheduleExpression": expression,
            "Target": {
                "Arn": target_arn,
                "RoleArn": role_arn,
                "Input": json.dumps(target_input or {}),
            },
            "FlexibleTimeWindow": (
                {"Mode": "OFF"} if time_window is None else time_window
            ),
        }
        if timezone is not None:
            data["ScheduleExpressionTimezone"] = timezone
        return client.create_schedule(**data)["ScheduleArn"]

    def delete_schedule(self, name: str, group_name: str) -> None:
        client = self.client("scheduler")
        try:
            client.delete_schedule(Name=name, GroupName=group_name)
        except client.exceptions.ResourceNotFoundException:
            raise exceptions.ResourceDoesNotExist("Schedule not found")

    def invoke_function(
        self,
        name: str,
        *,
        invocation_type: Literal[
            "Event", "RequestResponse", "DryRun"
        ] = "RequestResponse",
        client_context: t.Optional[t.Dict[str, t.Any]] = None,
        payload: t.Optional[t.Dict[str, t.Any]] = None,
        log_type: Literal["Tail"] = "Tail",
        qualifier: str = "$LATEST",
    ) -> t.Dict[str, t.Any]:
        client = self.client("lambda")
        try:
            return client.invoke(
                FunctionName=name,
                InvocationType=invocation_type,
                ClientContext=base64.b64encode(
                    json.dumps(client_context or {}).encode()
                ).decode(),
                Payload=json.dumps(payload or {}),
                LogType=log_type,
                Qualifier=qualifier,
            )
        except client.exceptions.ResourceNotFoundException:
            raise exceptions.ResourceDoesNotExist("Function not found")
