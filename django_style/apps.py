from django.apps import AppConfig
from django.conf import settings


class StyleConfig(AppConfig):
    name = "django_style"

    def ready(self):
        # Inject the django_style template context processor
        if hasattr(settings, "TEMPLATES"):
            for template in settings.TEMPLATES:
                if (
                    "OPTIONS" in template
                    and "context_processors" in template["OPTIONS"]
                ):
                    template["OPTIONS"]["context_processors"].append(
                        "django_style.context_processors.django_style"
                    )
