import typing as t

import botocore.session

from . import __version__


class Session:
    def __init__(
        self,
        access_key_id: t.Optional[str] = None,
        secret_access_key: t.Optional[str] = None,
        session_token: t.Optional[str] = None,
        region: t.Optional[str] = None,
        profile: t.Optional[str] = None,
    ) -> None:
        self._session = botocore.session.get_session()

        if profile is not None:
            self._session.set_config_variable("profile", profile)

        if region is not None:
            self._session.set_config_variable("region", region)

        if access_key_id or secret_access_key or session_token:
            self._session.set_credentials(
                access_key_id,
                secret_access_key,
                session_token,
            )

        self._session.user_agent_extra = f"Botocore/{self._session.user_agent_version}"
        self._session.user_agent_name = "Seda"
        self._session.user_agent_version = __version__

        identity = self.client("sts").get_caller_identity()
        self.account_id = identity.get("Account")
        self.username = identity["Arn"].rsplit("/")[-1]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.username}/{self.region}>"

    @property
    def profile(self) -> str:
        return self._session.profile or "default"

    @property
    def region(self) -> str:
        return self._session.get_config_variable("region")

    def client(self, service_name):
        return self._session.create_client(service_name)
