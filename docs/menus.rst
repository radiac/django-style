=====
Menus
=====

The themes have basic support for a simple single-level menu in the header and footer.

Define your links in your template context with ``site_nav`` for header links, and
``footer_nav`` for footer links - see :doc:`usage`.

These should be lists of objects with a ``url`` and ``label`` attribute - or a dict with
those keys.

For convenience Django Style comes with a ``Nav(label, view_name)`` object,
where ``view_name`` is automatically resolved to a url using ``django.urls.reverse``.

Example usage
=============

.. code-block:: python

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
