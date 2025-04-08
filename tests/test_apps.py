from django.conf import settings


def test_context_processor_added():
    context_processors = settings.TEMPLATES[0]["OPTIONS"]["context_processors"]
    assert "django_style.context_processors.django_style" in context_processors
