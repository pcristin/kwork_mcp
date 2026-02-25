import pytest

from kwork.agent.config import AgentConfigError, ClientConfig


def test_client_config_env_and_overrides_precedence() -> None:
    env = {
        "KWORK_LOGIN": "env_login",
        "KWORK_PASSWORD": "env_password",
        "KWORK_TIMEOUT": "15",
        "KWORK_RETRY_MAX_ATTEMPTS": "3",
        "KWORK_RELOGIN_ON_AUTH_ERROR": "1",
    }

    cfg = ClientConfig.from_sources(
        env=env,
        login="cli_login",
        timeout=20.0,
        retry_max_attempts=2,
    )

    assert cfg.login == "cli_login"
    assert cfg.password == "env_password"
    assert cfg.timeout == 20.0
    assert cfg.retry_max_attempts == 2
    assert cfg.relogin_on_auth_error is True


def test_client_config_invalid_env_boolean_raises() -> None:
    with pytest.raises(AgentConfigError):
        ClientConfig.from_sources(
            env={
                "KWORK_LOGIN": "x",
                "KWORK_PASSWORD": "y",
                "KWORK_RELOGIN_ON_AUTH_ERROR": "maybe",
            }
        )
