from django.conf import settings

from .utils import get_base

DEFAULT_THEME = "simple"


def django_style(request):
    theme = getattr(settings, "STYLE_THEME", DEFAULT_THEME)
    return {
        "STYLE_BASE": get_base(theme),
        "STYLE_IS_APP": getattr(settings, "STYLE_IS_APP", False),
    }
