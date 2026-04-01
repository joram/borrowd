from django.conf import settings


def vite(request):
    vite_settings = settings.DJANGO_VITE["default"]
    base_static_url = settings.BASE_STATIC_URL.rstrip("/")

    return {
        "vite_dev_mode": vite_settings["dev_mode"],
        "vite_client_url": f"{base_static_url}/static/@vite/client",
        "vite_main_asset_url": f"{base_static_url}/static/js/main.js",
    }
