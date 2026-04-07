=====
Usage
=====

Django Style makes the theme's base template available at ``base.html``:

.. code-block:: html+django

    {% extends "base.html" %}
    {% block content %}
      <h1>My page</h1>
      <p>My content</p>
    {% endblock %}


Template blocks
===============

The base templates define the following empty blocks for you to add content:

* ``{% block head_title %}`` - the ``<head><title>`` contents
* ``{% block content %}`` - the main content of the page
* ``{% block extra_head %}`` - at the bottom of the ``<head>``

Example usage:

.. code-block:: html+django

    {% block extra_head %}
      <script src="{% static "site.js" %}"></script>
    {% endblock %}


They also wrap their elements with the following blocks, for you to extend or override:

* ``{% block body %}`` - the ``<body>`` contents
* ``{% block header %}`` - the top header block
* ``{% block main %}`` - wrapper for the content of the page (title plus content)
* ``{% block site_nav_items %}`` - the site nav items
* ``{% block footer_nav_items %}`` - the footer nav items
* ``{% block footer %}`` - the bottom footer block

Example usage:

.. code-block:: html+django

    {% block site_nav_items %}
      {{ block.super }}
      <li><img src="{% static "images/smiley-face.webp" %}"></li>
    {% endblock %}


Template variables
==================

The base templates use the following template variables:

* ``site_title`` - name of your site, used in ``<head><title>`` and the heading in the ``header`` block
* ``title`` - title used for the ``<head><title>`` and the heading in the ``main`` block
* ``site_nav`` - a list of menu items - see :doc:`menus` for more information
* ``footer_nav`` - a list of menu items - see :doc:`menus` for more information

``site_title``, ``site_nav`` and ``footer_nav`` can be set globally via
:ref:`settings` (``STYLE_SITE_TITLE``, ``STYLE_SITE_NAV``, ``STYLE_FOOTER_NAV``).
Values passed in the view context will override the global settings.


Override settings
=================

You can override the project-wide theme and layout from :ref:`settings` in your template
context:

.. code-block:: python

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


``STYLE_BASE``
--------------

Override the ``STYLE_THEME`` setting by passing the path to the theme's base template.

The ``django_style.get_base(theme)`` helper will generate the django-style path from the
theme name, eg:

.. code-block:: python

    context={
      "STYLE_BASE": get_base("tailwind"),
    }


Default is the path to the current ``STYLE_THEME``


``STYLE_IS_APP``
----------------

Override the ``STYLE_IS_APP`` setting

Default: ``settings.STYLE_IS_APP``

