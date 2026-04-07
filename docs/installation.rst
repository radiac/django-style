============
Installation
============

First install using pip (or other package manager):


.. code-block:: bash

    pip install django-style


Then add to ``settings.INSTALLED_APPS``:


.. code-block:: python

    INSTALLED_APPS = [
        ...
        "django_style",
    ]

This will also register a template context manager, and should be all most projects
need.

Installing with Nanodjango
--------------------------

Nanodjango has a plugin system which will automatically detect when django-style is in
your python environment, and add it to the ``INSTALLED_APPS``.

Once you have run ``pip install django-style`` you can move straight on to
:ref:`settings` or :doc:`usage`.


Further Django setup
--------------------

This section applies if you have made changes to your ``TEMPLATES`` setting, so in most
cases, you can skip to :ref:`settings`.

Django Style currently only provides Django templates, so you need to be using the
Django template engine.

Django also needs to be configured to check app dirs.

You either need:


.. code-block:: python

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": True,
            ...
        }
    ]


or if you specify your own template ``loaders``, you will need to include
the `app_directories.Loader <https://docs.djangoproject.com/en/5.2/ref/templates/api/#django.template.loaders.app_directories.Loader>`_.

.. _settings:

Configure Django Style
======================

These settings are defined globally in your Django settings. They can also be
overridden by individual views - see :doc:`usage` for more information.

For a full Django installation, put these settings in your ``settings.py``, or for
nanodjango pass them into the ``Django(..)`` constructor.


``STYLE_THEME``
---------------

Select the theme to use.

Django Style comes with several themes to fit your development preferences.

Options:

* ``simple`` - a plain CSS theme
  (`demo <https://radiac-django-style-demo.nanodjango.dev/?autorun=1>`_,
  `app demo <https://radiac-django-style-demo.nanodjango.dev/app/>`_)
* ``bootstrap`` - a Bootstrap 5 theme
  (`demo <https://radiac-django-style-demo.nanodjango.dev/bootstrap/>`_,
  `app demo <https://radiac-django-style-demo.nanodjango.dev/bootstrap/app/>`_)
* ``tailwind`` - a Tailwind 4 theme
  (`demo <https://radiac-django-style-demo.nanodjango.dev/tailwind/>`_,
  `app demo <https://radiac-django-style-demo.nanodjango.dev/tailwind/app/>`_)

Default: ``STYLE_THEME = "simple"``

Note: the tailwind theme uses the
`CDN distribution <https://tailwindcss.com/docs/installation/play-cdn>`_ of Tailwind,
which they say is designed for development purposes and is not intended for production.


``STYLE_IS_APP``
----------------

Control the layout of the theme.

App layout is intended for a template where the content has a fixed fixed header and
footer, like a dashboard or email application.

If ``STYLE_IS_APP = False``, the theme will use the normal layout, where the header and
footer scroll with the content, and there is a comfortable maximum width.

If ``STYLE_IS_APP = True``, the theme will use the app layout; take up the full window
height, the header is always visible (and footer if defined), and only the content area
is scrollable.

Note that the content area will have no padding in app mode - this means you can define
your own sidebars or toolbars, but will have to have add padding yourself.

Default: ``STYLE_IS_APP = False``


``STYLE_SITE_TITLE``
--------------------

Default site title, shown in the header and ``<title>`` tag.
Can be overridden by a view's context.

If not set, Django Style will attempt to detect a sensible default from the project name
(using ``ND_APP_NAME`` for nanodjango projects, or the first segment of
``ROOT_URLCONF`` for standard Django projects).

Set to an empty string to keep this blank: ``STYLE_SITE_TITLE = ""``


``STYLE_SITE_NAV``
------------------

Default navigation menu items shown in the header.
Can be overridden by a view's context.

The standard templates expect a list of :doc:`menu items <menus>`.

Default: ``STYLE_SITE_NAV = []``


``STYLE_FOOTER_NAV``
--------------------

Default navigation menu items shown in the footer.
Can be overridden by a view's context.

The standard templates expect a list of :doc:`menu items <menus>`.

Default: ``STYLE_FOOTER_NAV = []``


