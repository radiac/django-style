# /// script
# dependencies = ["nanodjango", "django-style"]
# ///
"""
Example demonstrating all the themes and layout options

Usage::

    uv run example.py

or if you want to call nanodjango directly::

    uvx --with django-style nanodjango run example.py

Thanks to Pirate Ipsum (https://pirateipsum.me/) for the sample copy.
"""

from django import forms
from django.contrib import messages as django_messages
from nanodjango import Django

from django_style import Nav, get_base

app = Django(
    STYLE_IS_APP=False,
)


def render(request, *args, **kwargs):
    # Helper so we can set django messages using the querystring
    for level in ("debug", "info", "success", "warning", "error"):
        for text in request.GET.getlist(level):
            getattr(django_messages, level)(request, text)
    return app.render(request, *args, **kwargs)


class SimpleForm(forms.Form):
    name = forms.CharField(help_text="Your full name")
    subscribe = forms.BooleanField(help_text="Subscribe to the newsletter")
    image = forms.ImageField(help_text="Upload an image")
    text = forms.CharField(widget=forms.Textarea())


@app.route("/")
def simple(request):
    return render(
        request,
        "simple.html",
        context={
            "site_title": "Django-Style Example",
            "title": "Simple theme",
            "form": SimpleForm(label_suffix=""),
            # Normally you'd build a nav centrally; in this demo we'll just write it out
            "site_nav": [
                # Nav(label, url or view_name)
                Nav("Simple", "simple"),
                Nav("Simple App", "simple_app"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Tailwind", "tailwind"),
            ],
            "footer_nav": [
                Nav("Simple", "simple"),
                Nav("Simple App", "simple_app"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Tailwind", "tailwind"),
                Nav("Support Django", url="https://www.djangoproject.com/fundraising/"),
            ],
        },
    )


@app.route("/app/", name="simple_app")
def simple_app(request):
    return render(
        request,
        "simple_app.html",
        context={
            "site_title": "Django-Style Example",
            "title": "Simple theme, app layout",
            "site_nav": [
                Nav("Simple", "simple"),
                Nav("Simple App", "simple_app"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Tailwind", "tailwind"),
            ],
            "footer_nav": [
                Nav("Simple", "simple"),
                Nav("Simple App", "simple_app"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Tailwind", "tailwind"),
                Nav("Support Django", url="https://www.djangoproject.com/fundraising/"),
            ],
            "STYLE_IS_APP": True,
        },
    )


app.templates["simple.html"] = """
    {% extends 'base.html' %}
    {% block content %}
        {% include "simple_content.html" %}
    {% endblock %}
"""
app.templates["simple_app.html"] = """
    {% extends 'base.html' %}
    {% block main %}
        <div style="padding: 1rem">
            {% include "simple_content.html" %}
        </div>
    {% endblock %}
"""
app.templates["simple_content.html"] = """
    <p>
        This is a template for <a href="https://www.djangoproject.com/" target="_blank">Django</a>.
        See it <a href=".?success=Success message!&error=Error message">with messages</a>.
    </p>

    <h2>Heading Level 2</h2>
    <p>Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.</p>
    <p>Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.</p>

    <form action=".">
    {{ form.as_p }}
    <div class="buttons">
        <input type="submit">
        <a href="." class="button secondary">Cancel</a>
    </div>
    </form>

    <h3>Heading Level 3</h3>
    <p>Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.</p>
    <table>
        <thead><tr><th>Ship</th><th>Captain</th><th>Cargo</th><th>Status</th></tr></thead>
        <tbody>
            <tr><td>The Jolly Roger</td><td>Jack Sparrow</td><td>Rum</td><td>At sea</td></tr>
            <tr><td>The Black Pearl</td><td>Hector Barbossa</td><td>Gold</td><td>In port</td></tr>
            <tr><td>The Flying Dutchman</td><td>Davy Jones</td><td>Souls</td><td>Cursed</td></tr>
        </tbody>
        <tfoot><tr><td colspan="4">3 vessels listed</td></tr></tfoot>
    </table>
    <p>Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.</p>

    <h4>Heading Level 4</h4>
    <p>Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.</p>
    <p>Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.</p>
"""


class BootstrapForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your name", "class": "form-control"}
        ),
    )
    subscribe = forms.BooleanField(
        label="Subscribe to the newsletter",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    image = forms.ImageField(
        label="Upload an Image",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter your message",
                "class": "form-control",
                "rows": 4,
            }
        ),
    )


@app.route("/bootstrap/", name="bootstrap")
def boostrap(request):
    return render(
        request,
        "bootstrap.html",
        context={
            "site_title": "Django-Style Example",
            "title": "Bootstrap theme",
            "form": BootstrapForm(label_suffix=""),
            "site_nav": [
                Nav("Simple", "simple"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Bootstrap App", "bootstrap_app"),
                Nav("Tailwind", "tailwind"),
            ],
            "footer_nav": [
                Nav("Simple", "simple"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Bootstrap App", "bootstrap_app"),
                Nav("Tailwind", "tailwind"),
                Nav("Support Django", url="https://www.djangoproject.com/fundraising/"),
            ],
            "STYLE_BASE": get_base("bootstrap"),
            "STYLE_IS_APP": False,
        },
    )


@app.route("/bootstrap/app/", name="bootstrap_app")
def boostrap_app(request):
    return render(
        request,
        "bootstrap_app.html",
        context={
            "site_title": "Django-Style Example",
            "title": "Bootstrap theme, app layout",
            "form": BootstrapForm(label_suffix=""),
            "site_nav": [
                Nav("Simple", "simple"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Bootstrap App", "bootstrap_app"),
                Nav("Tailwind", "tailwind"),
            ],
            "footer_nav": [
                Nav("Simple", "simple"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Bootstrap App", "bootstrap_app"),
                Nav("Tailwind", "tailwind"),
                Nav("Support Django", url="https://www.djangoproject.com/fundraising/"),
            ],
            "STYLE_BASE": get_base("bootstrap"),
            "STYLE_IS_APP": True,
        },
    )


app.templates["bootstrap.html"] = """
    {% extends 'base.html' %}
    {% block content %}
        {% include "bootstrap_content.html" %}
    {% endblock %}
"""
app.templates["bootstrap_app.html"] = """
    {% extends 'base.html' %}
    {% block main %}
        <div style="padding: 1rem">
            {% include "bootstrap_content.html" %}
        </div>
    {% endblock %}
"""
app.templates["bootstrap_content.html"] = """
    <p>
        This is a template for <a href="https://www.djangoproject.com/" target="_blank">Django</a>.
        See it <a href=".?success=Success message!&error=Error message">with messages</a>.
    </p>

    <h2>Heading Level 2</h2>
    <p>Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.</p>
    <p>Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.</p>

    <form action=".">
    {{ form.as_p }}
    <div class="my-4">
        <input type="submit" class="btn btn-primary">
        <a href="." class="btn btn-secondary">Cancel</a>
    </div>
    </form>

    <h3>Heading Level 3</h3>
    <p>Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.</p>
    <p>Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.</p>

    <h4>Heading Level 4</h4>
    <p>Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.</p>
    <p>Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.</p>
"""


class TailwindForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your name",
                "class": "border border-gray-300 rounded-md p-2 w-full mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500",
            }
        ),
    )
    subscribe = forms.BooleanField(
        label="Subscribe to the newsletter",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-checkbox h-5 w-5 rounded-md text-blue-600 ml-4 mb-4 focus:ring-blue-500 border-gray-300 rounded",
            }
        ),
    )
    image = forms.ImageField(
        label="Upload an Image",
        widget=forms.ClearableFileInput(
            attrs={
                "class": "border border-gray-300 rounded-md p-2 w-full mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500",
            }
        ),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter your message",
                "class": "border border-gray-300 rounded-md p-2 w-full mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "rows": 4,
            }
        ),
    )


@app.route("/tailwind/", name="tailwind")
def tailwind(request):
    return render(
        request,
        "tailwind.html",
        context={
            "site_title": "Django-Style Example",
            "title": "Tailwind theme",
            "form": TailwindForm(label_suffix=""),
            "site_nav": [
                Nav("Simple", "simple"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Tailwind", "tailwind"),
                Nav("Tailwind App", "tailwind_app"),
            ],
            "footer_nav": [
                Nav("Simple", "simple"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Tailwind", "tailwind"),
                Nav("Tailwind App", "tailwind_app"),
                Nav("Support Django", url="https://www.djangoproject.com/fundraising/"),
            ],
            "STYLE_BASE": get_base("tailwind"),
            "STYLE_IS_APP": False,
        },
    )


@app.route("/tailwind/app/", name="tailwind_app")
def tailwind_app(request):
    return render(
        request,
        "tailwind_app.html",
        context={
            "site_title": "Django-Style Example",
            "title": "Tailwind theme, app layout",
            "form": TailwindForm(label_suffix=""),
            "site_nav": [
                Nav("Simple", "simple"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Tailwind", "tailwind"),
                Nav("Tailwind App", "tailwind_app"),
            ],
            "footer_nav": [
                Nav("Simple", "simple"),
                Nav("Bootstrap", "bootstrap"),
                Nav("Tailwind", "tailwind"),
                Nav("Tailwind App", "tailwind_app"),
                Nav("Support Django", url="https://www.djangoproject.com/fundraising/"),
            ],
            "STYLE_BASE": get_base("tailwind"),
            "STYLE_IS_APP": True,
        },
    )


app.templates["tailwind.html"] = """
    {% extends 'base.html' %}
    {% block content %}
        {% include "tailwind_content.html" %}
    {% endblock %}
"""
app.templates["tailwind_app.html"] = """
    {% extends 'base.html' %}
    {% block main %}
        <div style="padding: 1rem">
            {% include "tailwind_content.html" %}
        </div>
    {% endblock %}
"""
app.templates["tailwind_content.html"] = """
    <p class="text-gray-700 mb-4">
        This is a template for
        <a href="https://www.djangoproject.com/" target="_blank" class="text-blue-500 hover:underline">Django</a>.
        See it <a href=".?success=Success message!&error=Error message" class="text-blue-500 hover:underline">with messages</a>.
    </p>

    <h2 class="text-2xl font-bold text-gray-800 mt-6 mb-4">Heading Level 2</h2>
    <p class="text-gray-600 mb-4">
        Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.
    </p>
    <p class="text-gray-600 mb-4">
        Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.
    </p>

    <form action="." class="mt-6">
        {{ form.as_p }}
        <div class="my-4">
            <input type="submit" value="Submit" class="bg-blue-500 text-white
            font-semibold py-2 px-4 rounded hover:bg-blue-600 transition
            duration-200">

            <a href="." class="bg-gray-300 text-gray-800 font-semibold py-2 px-4 rounded hover:bg-gray-400 transition duration-200 inline-block">Cancel</a>
        </div>
    </form>

    <h3 class="text-xl font-semibold text-gray-800 mt-6 mb-4">Heading Level 3</h3>
    <p class="text-gray-600 mb-4">
        Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.
    </p>
    <p class="text-gray-600 mb-4">
        Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.
    </p>

    <h4 class="text-lg font-medium text-gray-800 mt-6 mb-4">Heading Level 4</h4>
    <p class="text-gray-600 mb-4">
        Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters.
    </p>
    <p class="text-gray-600 mb-4">
        Deadlights jack lad schooner scallywag dance the hempen jig carouser broadside cable strike colors. Bring a spring upon her cable holystone blow the man down spanker Shiver me timbers to go on account lookout wherry doubloon chase. Belay yo-ho-ho keelhaul squiffy black spot yardarm spyglass sheet transom heave to.
    </p>
"""
