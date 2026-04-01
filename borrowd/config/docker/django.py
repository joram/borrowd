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
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["https://*.veilstreamapp.com"])

STATIC_ROOT = os.path.join(env("PLATFORM_APP_DIR", default="/app"), "staticfiles")
DJANGO_VITE = {
    "default": {
        "dev_mode": False,
        "manifest_path": BASE_DIR / "build" / "manifest.json",  # noqa: F405
    }
}

if env.bool("LOCAL_SENTRY_ENABLED", default=False):
    sentry_sdk.init(
        dsn=SENTRY_DSN,  # noqa: F405
        send_default_pii=True,
        environment="local",
    )
