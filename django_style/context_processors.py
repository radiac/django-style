from django.conf import settings

from .utils import get_base

DEFAULT_THEME = "simple"
_app_name = (
    getattr(settings, "ND_APP_NAME", None)
    or getattr(settings, "ROOT_URLCONF", "").split(".")[0]
)
DEFAULT_SITE_TITLE = _app_name.replace("_", " ").title()


def django_style(request):
    theme = getattr(settings, "STYLE_THEME", DEFAULT_THEME)
    return {
        "STYLE_BASE": get_base(theme),
        "STYLE_IS_APP": getattr(settings, "STYLE_IS_APP", False),
        "site_title": getattr(settings, "STYLE_SITE_TITLE", DEFAULT_SITE_TITLE),
        "site_nav": getattr(settings, "STYLE_SITE_NAV", []),
        "footer_nav": getattr(settings, "STYLE_FOOTER_NAV", []),
    }
