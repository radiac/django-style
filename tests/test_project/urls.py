from django.urls import path
from django.views.generic import TemplateView

from django_style import Nav, get_base

context = {
    "site_title": "Django-Style Example",
    "title": "Django-Style Example",
    "site_nav": [
        Nav("Simple", "simple"),
        Nav("Bootstrap", "bootstrap"),
        Nav("Tailwind", "tailwind"),
    ],
    "footer_nav": [
        Nav("Simple", "simple"),
        Nav("Bootstrap", "bootstrap"),
        Nav("Tailwind", "tailwind"),
    ],
}

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="test.html",
            extra_context=context,
        ),
        name="simple",
    ),
    path(
        "simple/",
        TemplateView.as_view(
            template_name="test.html",
            extra_context={"STYLE_BASE": get_base("simple"), **context},
        ),
        name="simple",
    ),
    path(
        "bootstrap/",
        TemplateView.as_view(
            template_name="test.html",
            extra_context={"STYLE_BASE": get_base("bootstrap"), **context},
        ),
        name="bootstrap",
    ),
    path(
        "tailwind/",
        TemplateView.as_view(
            template_name="test.html",
            extra_context={"STYLE_BASE": get_base("tailwind"), **context},
        ),
        name="tailwind",
    ),
]
