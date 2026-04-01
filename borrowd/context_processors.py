from django.conf import settings


def vite(request):
    vite_settings = settings.DJANGO_VITE["default"]
    base_static_url = settings.BASE_STATIC_URL.rstrip("/")
    is_local_vite_host = settings.BASE_STATIC_HOST in {"localhost", "127.0.0.1"}
    request_host = request.get_host().split(":")[0]
    is_local_request_host = request_host in {"localhost", "127.0.0.1"}
    vite_dev_mode = (
        vite_settings["dev_mode"] and is_local_vite_host and is_local_request_host
    )

    return {
        "vite_dev_mode": vite_dev_mode,
        "vite_client_url": f"{base_static_url}/static/@vite/client",
        "vite_main_asset_url": f"{base_static_url}/static/js/main.js",
    }
