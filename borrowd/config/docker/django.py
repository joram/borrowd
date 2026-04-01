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

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
] + MIDDLEWARE[1:]  # noqa: F405

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

DJANGO_VITE["default"]["dev_mode"] = False  # noqa: F405
