import json
from pathlib import Path

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

    if vite_dev_mode:
        return {
            "vite_dev_mode": True,
            "vite_client_url": f"{base_static_url}/static/@vite/client",
            "vite_main_asset_url": f"{base_static_url}/static/js/main.js",
            "vite_css_urls": [],
        }

    static_prefix = f"/{settings.STATIC_URL}"
    js_url = f"{static_prefix}js/main.js"
    css_urls = []
    try:
        manifest_path = vite_settings.get("manifest_path")
        manifest = json.loads(Path(manifest_path).read_text())
        entry = manifest["static/js/main.js"]
        js_url = f"{static_prefix}{entry['file']}"
        css_urls = [f"{static_prefix}{css}" for css in entry.get("css", [])]
    except (TypeError, FileNotFoundError, KeyError, json.JSONDecodeError):
        pass

    return {
        "vite_dev_mode": False,
        "vite_client_url": None,
        "vite_main_asset_url": js_url,
        "vite_css_urls": css_urls,
    }
