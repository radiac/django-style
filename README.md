## Django Style

Basic tasteful designs for your Django project, with sensible defaults.

Features:

* Themes for plain CSS, Tailwind 4, and Bootstrap 5
* Mobile support
* App layout for content with a complex UI
* Basic menu support

This project won't replace a proper design, but can help make your prototypes pretty.

Pairs particularly well with [nanodjango](https://github.com/radiac/nanodjango/).

To play with a live example, download
[example.py](https://raw.githubusercontent.com/radiac/django-style/refs/heads/main/example.py)
and run with [uv](https://docs.astral.sh/uv/getting-started/installation/):

```
uvx --with django-style nanodjango run example.py
```

### Installation

Install:

```
pip install django-style
```

Add to `settings.INSTALLED_APPS`:

```
INSTALLED_APPS = [
    ...
    "django_style",
]
```

and optionally configure using the settings below.

Now just `{% extend "base.html" %}` in your templates, and

* define a `{% block content %}`
* pass a `title` and a `site_title` in your context
* maybe add `site_nav` or `footer_nav` lists of menu objects - see how menus work below


### Settings

Settings are defined globally in your Django settings.


#### `STYLE_THEME`

Django-style comes with several themes to fit your development style.

Options:

* `simple` - a plain CSS theme
* `bootstrap` - a Bootstrap 5 theme
* `tailwind` - a Tailwind 4 theme

Default: `STYLE_THEME = "simple"`

Note: the tailwind theme uses the
[CDN distribution](https://tailwindcss.com/docs/installation/play-cdn)
which they say is designed for development purposes and is not intended for production.


#### `STYLE_IS_APP`

App layout is intended for a template where the content has a complex UI layout, like a
dashboard or email application which needs toolbars, sidebars and multiple panes. (These
elements are left for you to implement).

If `STYLE_IS_APP = False`, the theme will use the normal layout, where the header and
footer scroll with the content.

If `STYLE_IS_APP = True`, put the theme into app layout; take up the full window height,
header always visible (and footer if defined), and only the content area is scrollable.

Default: `STYLE_IS_APP = False`


### Template context

You can override the theme and layout in your template context:

```
from django_style import get_base

def my_view(request)
    return render(
        request,
        "my_template.html",
        context={
            "STYLE_BASE": get_base("bootstrap"),
            "STYLE_IS_APP": True,
        },
    )
```

#### `STYLE_BASE`

Path to the theme's base template.

This can be any string, but you can use the ``django_style.get_base(theme)`` helper to
generate the django-style path from the theme name.

Default: `f"django_style/{settings.STYLE_THEME}/base.html"`


#### `STYLE_IS_APP`

Override the `STYLE_IS_APP` setting

Default: `settings.STYLE_IS_APP`


### Menus

The themes have basic support for a simple single-level menu in the header and footer.

Define your links in your template context with `site_nav` for header links, and
`footer_nav` for footer links.

These should be lists of objects with a `url` and `label` attribute (or a dict with
those keys). For convenience django-style comes with a `Nav(label, view_name)` object,
where `view_name` is automatically resolved to a url using `django.urls.reverse`.

Example:

```
from django_style import Nav

def my_view(request)
    return render(
        request,
        "my_template.html",
        context={
            "site_nav": [
                Nav("Home", "index"),
                Nav("About", "about"),
                Nav("Contact", "contact"),
            ],
            "footer_nav": [
                Nav("Privacy policy", "privacy"),
                Nav("Contact", "contact"),
            ],
        },
    )
```
