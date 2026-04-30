=========
Changelog
=========

0.3.1 - 2026-04-30
------------------

Theme simple:

* Fix header font sizes
* Change site header from h1 to a, link to root, reduce visual importance

Bootstrap:

* Fix header link to root

Tailwind:

* Change site header from h1 to a, link to roo



0.3.0 - 2026-04-07
------------------

Features

* Add block ``messages`` to display Django's
  `messages framework <https://docs.djangoproject.com/en/6.0/ref/contrib/messages/>`_
* Add settings-level defaults for ``STYLE_SITE_TITLE``, ``STYLE_SITE_NAV`` and
  ``STYLE_FOOTER_NAV``

Changes:

* If no site title is set, it will try to detect the project's name and title-case that
* Simplify app examples to make it clearer what they do

Theme ``simple``:

* Add basic table styling
* Increase specificity of CSS form selectors - fixes select2 issues
* Hide footer if empty

Theme ``tailwind``:

* Fix app layout footer


0.2.0 - 2026-03-06
------------------

Features:

* Add block ``extra_head`` for inserting tags into the ``<head>``
* Add wrapper blocks ``body``, ``site_nav_items`` and ``footer_nav_items`` to act as
  convenient hooks.


0.1.2 - 2025-08-24
------------------

Features:

* Add a nanodjango plugin to automatically add django-style to ``INSTALLED_APPS``, if it
  isn't already.


0.1.1 - 2025-04-11
------------------

Bugfix:

* Fix package


0.1.0 - 2025-04-09
------------------

Features:

* Simple plain CSS theme
* Bootstrap theme
* Tailwind theme
* App mode
