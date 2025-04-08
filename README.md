## Django Style

Basic tasteful designs for your Django project, with sensible defaults.

Features:

* Themes for plain CSS, Tailwind 4, and Bootstrap 5
* Mobile support
* App layout for content with a complex UI
* Basic menu support

This project won't replace a proper design, but can help make your prototypes pretty.

Pairs particularly well with [nanodjango](https://github.com/radiac/nanodjango/).

### Example

To play with a live example, download
[example.py](https://raw.githubusercontent.com/radiac/django-style/refs/heads/main/example.py)
and run with [uv](https://docs.astral.sh/uv/getting-started/installation/):

```
uvx --with django-style nanodjango run example.py
```

### Quickstart

1.  Install:
    ```
    pip install django-style
    ```

2.  Add it to `INSTALLED_APPS` in your `settings.py`, and optionally configure it:
    ```
    INSTALLED_APPS = [
        ...
        "django_style",
    ]

    STYLE_THEME = "tailwind"  # or "simple" (default) or "bootstrap"
    STYLE_IS_APP = True  # enable app layout (default is False)
    ```

3.  Extend `base.html` in your templates:
    ```
    {% extends "base.html" %}
    {% block content %}
        <p>Hello world</p>
    {% endblock %}


