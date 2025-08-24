from nanodjango import hookimpl


@hookimpl
def django_pre_setup(app):
    from django.conf import settings

    app_name = "django_style"
    if app_name not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS.append(app_name)