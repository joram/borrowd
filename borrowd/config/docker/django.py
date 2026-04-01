from borrowd.config.dev.django import *  # noqa: F401, F403

from borrowd.config.env import env

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", default="borrowd"),
        "USER": env("POSTGRES_USER", default="borrowd"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="borrowd"),
        "HOST": env("POSTGRES_HOST", default="db"),
        "PORT": env("POSTGRES_PORT", default="5432"),
    }
}

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405
_django_vite_config = {
    "dev_mode": DEBUG,
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
