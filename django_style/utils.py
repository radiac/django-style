from django.urls import reverse


class Nav:
    """
    Describe a navigation item
    """

    def __init__(self, label: str, view: str):
        self.label = label
        self.view = view
        self.url = reverse(view)


def get_base(theme: str) -> str:
    """
    Given a theme name, generate the STYLE_BASE value

    May be useful if wanting to override the STYLE_BASE in a context, eg:

        render(..., context={"STYLE_BASE": get_base("simple")})
    """
    return f"django_style/{theme}/base.html"
