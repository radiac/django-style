from django.urls import reverse_lazy

from .constants import THEMES


class Nav:
    """
    Describe a navigation item
    """

    def __init__(self, label: str, view: str):
        self.label = label
        self.view = view
        self.url = reverse_lazy(view)


def get_base(theme: str) -> str:
    """
    Given a theme name, generate the STYLE_BASE value

    May be useful if wanting to override the STYLE_BASE in a context, eg:

        render(..., context={"STYLE_BASE": get_base("simple")})
    """
    if theme not in THEMES:
        raise ValueError(f"Unknown django-style theme: {theme}")
    return f"django_style/{theme}/base.html"
