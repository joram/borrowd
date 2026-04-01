# for some unknown reason, pre-commit cannot find sentry_sdk
import sentry_sdk  # type: ignore[import-not-found]

from borrowd.config.env import env

from ..base import *  # noqa: F403

if env("DEBUG", cast=str, default="true").lower() in ("1", "t", "true", "yes", "y"):
    DEBUG = True
else:
    print("running server with DEBUG mode OFF")
    DEBUG = False
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

VITE_DEV_MODE = DEBUG and BASE_STATIC_HOST in {"localhost", "127.0.0.1"}  # noqa: F405

STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405
_django_vite_config = {
    "dev_mode": VITE_DEV_MODE,
    "dev_server_protocol": BASE_STATIC_PROTOCOL,  # noqa: F405
    "dev_server_host": BASE_STATIC_HOST,  # noqa: F405
    "manifest_path": BASE_DIR / "build" / "manifest.json",  # noqa: F405
}
if BASE_STATIC_PORT is not None:  # noqa: F405
    _django_vite_config["dev_server_port"] = BASE_STATIC_PORT  # noqa: F405

DJANGO_VITE = {
    "default": _django_vite_config,
}

if env.bool("LOCAL_SENTRY_ENABLED", default=False):
    sentry_sdk.init(
        dsn=SENTRY_DSN,  # noqa: F405
        send_default_pii=True,
        environment="local",
    )
