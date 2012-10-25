.. Djecipes documentation master file, created by
   sphinx-quickstart on Wed Oct 24 13:44:06 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Djecipes's documentation!
====================================

Contents:

.. toctree::
   :maxdepth: 2

About Django
============

• Web application framework
• Written in Python
• Free software (BSD)
• Lots of documentation


Philosophy
----------

• Rapid development
• Loose coupling TODO
• Reusable applications
• DRY: Don't repeat yourself

Arkitektur
----------

(TODO)

Useful parts
------------

• Sessions
• Forms
• Validation
• Authentication
• Admin
• Serialization (JSON, XML++)
• Syndication (RSS, Atom)
• Testing
• Caching
• Localization (l10n) and internationalization (i18n)
• GeoDjango
• Built-in webserver
• Interactive shell

Starting a project
==================

Find a place where you want your project, and create a virtual environment to
keep your requirements and dependencies separated from the rest of your python
system. And activate your new virtual environment::

    virtualenv --no-site-packages .
    source bin/activate

Install Django::

    pip install django

Start a new django project. I have named mine Djecipes::

    ./bin/django-admin.py startproject djecipes

Go into the **project folder**, make the ``manage.py`` script runnable and
start the *built-in webserver* and go to ``localhost:8000`` in your web
browser::

    cd djecipes
    chmod 755 manage.py
    ./manage.py runserver

It tells you that something is working and that to continue, you should update
your settings and create an **app**.  The apps are meant to be reusable
components that you can tie together when building projects.

Have a look around in your project folder. You will see a folder with the same
name as your project, *djecipes*. This is where central project configuration
and common code will live.

.. TODO: Output from ls

Create an app using the ``manage.py`` command::

    ./manage.py startapp recipes

Go into djecipes/settings.py and setup your database settings: Append
``sqlite3`` to the ENGINE field and add a database name to the NAME field.

The database name will be the name of a local file in your project folder.
Sqlite is a single-file database system that is easy to use when developing,
but not usable in a large system.

Refresh the browser. (TODO). It is useful to keep a terminal always running manage.py
runserver.

Models, views, templates?
=========================

.. Todo: Output from ls

Have a look around in the *app* folder. You should see models and views. Later
we will have templates as well, but it is up to you if wants to place templates
in the project level folder or the app level folder, so it is not already
created for you.

.. TODO: Create graphic

*Model view controller* is probably the most used user interaction pattern in
the industry. It has been widely used and misused by different web frameworks
where the framework has either been built around the pattern or parts of the
framework has been given these names just to make it match the pattern.

The architecture of Django does separate functionality into models, views and
controllers, as it does not fit. The separation is done between models, views
(parts of the traditional controller code, but also parts of the traditional
view code) and templates (parts of the traditional view code), There is a lot
to say about this, but the important part is to separate functionality into
*database-near*, *templates* and other distinct functionality.

If you are coming from another language or framework, you will probably see
that the templates are stricter than you are used to. You are not allowed to
put tons of functionality into the template code  A graphical designer should
be able to understand and change the templates without knowing Python or
Django.

Your first model
----------------

That's enough theory for a while. Now we will add a very simple model to
``models.py``. This is the model for all the types of food we will use in the
recipes. It will only have one field we need to know of. Django will
automatically give it an **id** field for the primary key. Add the following::

    from django.db import models

    class Food(models.Model):
        name = models.CharField(max_length=20)

Now we will utilize the built-in **admin** interface of Django. In ``urls.py``
in the project folder, uncomment the lines regarding *admin* (not admindoc).
Also make a new line to forward all urls starting with *recipes* to your app::

    from django.conf.urls import patterns, include, url

    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
                           # Examples:
                           # url(r'^$', 'djecipes.views.home', name='home'),
                           # url(r'^djecipes/', include('djecipes.foo.urls')),

                           # Uncomment the admin/doc line below to enable admin documentation:
                           # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                           # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),

                           url(r'^recipes/', include('recipes.urls'))
    )

The last line forwards everything starting with *recipes/* to the python module *recipes.urls*. There is more than one way to create this module, but the
simplest way is to add a new ``urls.py`` to your *app* folder. Copy the one
from the project folder into the app folder, and remove the lines *inside* the
*patterns* parentheses.

It should look similar to::

    from django.conf.urls import patterns, url

    urlpatterns = patterns('',
                           )

#TODO Try to run

In settings.py, find INSTALLED_APPS and uncomment the line
``'django.contrib.admin',`` as well as add your own app ``'recipes',`` to the
bottom of the list. Also add a line containing ``'south',`` to allow for
semi-automatic database migrations. You will also need to install the south
module::

    pip install south

When changing the database layout, it is very useful to be able to script your
changes. Migration of database schema and data is usually done by the
third-party app named **south**. 

If you now have a look at ``localhost:8000``, you should se an error telling you that one of the database tables does not exist. Now create a migration to do the database work needed::

    ./manage.py schemamigration recipes --init

This will not do the actual migration, just create the script needed for you.
And running it will not touch anything else. You need to run set up django's
tables too. The command ``syncdb`` will run everyhing needed to get the
database up and running, but will not touch apps where there are migrations
defined. You can run migrations separately using the ``migrate`` command, or
run a combined command, like this, that will do everything::

    ./manage.py syncdb --migrate

#TODO: sjekk at admin.py er laget over

To log into admin, you need a user, and creating users are done in the admin. So the first time this script is run for an application, it asks if you want to short-circut this loop by creating a user for you. Go on by filling in usernames, passwords, etc.

The output from the syncdb command clearly states that the django apps specified in INSTALLED_APPS, except for your recipes, has been set up using the normal sync, and that your recipes app has been set up using a migration.

.. TODO: Add output from syncdb

Now, have a look in your browser. It should tell you that you have set up some routes. One to *recipes* and one to *admin*. Try to append ``admin`` to the url.

You should now be able to log in and have a look around. You should see some predefined classes from Django like User and Group, but also your very own Food. Click on it and add some food using the *Add food* button in the top right corner.

When looking at the list, you see that you have created a *Food object*. When you have created more, this is not so useful. In your models.py add a function named ``__unicode__`` to your Food class. Make it to return self.name, like this::

    def __unicode__(self):
        return self.name

When refreshing the list, your table should look more useful. The __unicode__
is utilized by Django to write a human readable version of the object. Later,
for example in templates, you could just print the object, instead of
specifying what fields you want to print each time, you can let the __unicode__
do the magic.

Your first view
---------------

Open up ``views.py`` and paste in this code::

    from django.shortcuts import render_to_response
    from django.template import RequestContext
    from recipes.models import Food

    def food_list(request):
        food = Food.objects.all()
        return render_to_response('recipes/food_list.html', {'object_list': food}, context_instance=RequestContext(request))

Go to your app's urls.py and add an import statement to the top::

    from recipes.views import food_list

And a line to the pattern list to get all food::

    url(r'^food/$', food_list, name='food-list'),

Now ``/recipes/food/`` should trigger the newly created ``food_list`` function.

Try it and see that you get an error message. It tells you to make a template
named "recipes/food_list.html". We will make this template in the app level (to
keep away from configuring too much in the settings file)::

    mkdir -p templates/recipes  # from the app folder

And create a file in the newly created folder called ``food_list.html``
containing (copied from
http://twitter.github.com/bootstrap/getting-started.html)::

    <!DOCTYPE html>
    <html>
    <head>
    <title>Bootstrap 101 Template</title>
    <!-- Bootstrap -->
    <link href="{{ STATIC_URL }}css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    <h1>Hello, world!</h1>
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="{{ STATIC_URL }}js/bootstrap.min.js"></script>
    </body>
    </html>

*Twitter Bootstrap* is a good default to use when creating web projects. It is
free and easy to use, also commercially.

This template needs some files from the Twitter Bootstrap project, so in your
app folder, download twitter bootstrap static files, unzip and rename the
directory to ``static``::

    wget http://twitter.github.com/bootstrap/assets/bootstrap.zip
    unzip bootstrap.zip
    rm bootstrap.zip
    mv bootstrap static

Have a look at the file structure there and compare to the explanations at
http://twitter.github.com/bootstrap/getting-started.html.

Head over to the web browser and see the page saying Hello, world!. Add a *div* tag with class *container* around the *h1* and see how the page changes. Change the template by changing the *h1* tag and the title, and add some contents after the h1::

    <ul>
    {% for object in object_list %}
    <li>{{ object }}</li>
    {% endfor %}
    </ul>

Now, add empty links (a href="") around the {{ object }}. We want to see some
details about the food we have created. Also add an empty link at the bottom
that will later be used for adding more food to our list.

A second view
-------------

It shoudn't be much harder than the first one. But first, we will change the first view to be a **Class based generic view**.

The rewritten view file should look like::

    from recipes.models import Food
    from django.views.generic import ListView

    class FoodListView(ListView):
        model = Food

And the urls.py should import the new FoodListView instead of food_list, and
the pattern should be changed to this::

    url(r'^food/$', FoodListView.as_view(), name='food-list'),

Here, instead of calling the view function directly, we are now calling the
``as_view`` function on the FoodListView class.

Have a look in the browser. The functionality is the same, the code a lot
shorter.

Now we will make that second view. To the django.views import statement, add ``DetailView`` (comma separated), and add another class at the bottom of the file::

    class FoodDetailView(DetailView):
        model = Food

Add another pattern to the urls.py::

    url(r'^food/(?P<pk>\d+)/$', FoodDetailView.as_view(), name='food-detail'),

And now, insert the url you need into the address field of the first template,
so the line becomes::

    <li><a href="{% url food-detail object.id %}">{{ object }}</a></li>

Here we are utilizing the *named url* concept. You probably noticed the last
parameter in the url patterns. Also, the url patterns take in parameters. The
``<pk>`` is a generic way to say that you want the primary key field of the
object. The url patterns are used for both matching *and* link generation.

When you have a look at the web browser now, you see by hovering the mouse over
the links that they point somewhere. Try clicking one of them. Ooops, we need
to make another template. *templates/food_detail.html* is missing.

Copy the template you already have to food_detail.html in the same folder.
Change the new template to add a new title, h1 and the contents itself. The
contents is not too much fun as we do only have one field in the Food model.
Add a few <p> with the object id and name, and a link back to the list, like
this::

    <p><a href="{% url food-list %}">Back to food list</a></p>

    <p>{{ object.id }}</p>
    <p>{{ object.name }}</p>

When you look at the two templates, you see that there is a lot of common code in them. Create a new template one folder level up called ``base.html`` with the common code, like this::

    <!DOCTYPE html>
    <html>
    <head>
    <title>{% block title %}Generic title{% endblock %}</title>
    <!-- Bootstrap -->
    <link href="{{ STATIC_URL }}css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    <div class="container">
    {% block content %}
    <h1>Generic title</h1>

    Nothing interesting yet

    {% endblock %}
    </div>
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="{{ STATIC_URL }}js/bootstrap.min.js"></script>
    </body>
    </html>

You see some placeholder text in there, inside some blocks ``{% block content %}``. Blocks are made to be overridden in templates extending them.

Now remove the common code from the other two templates and add a line to tell them to extend the new base template. Then override the two blocks, title and content in both templates. The list template now looks like this::

    {% extends "base.html" %}

    {% block title %}Food list{% endblock %}

    {% block content %}
    <h1>Food list</h1>
    <ul>
    {% for object in object_list %}
    <li><a href="{% url food-detail object.id %}">{{ object }}</a></li>
    {% endfor %}
    </ul>
    <a href="{% url food-create %}" class="btn btn-primary">Add new</a>
    {% endblock %}

You already have a *create* link in the list page, now we'll add the
functionality. Add a CreateView to the import at the top of views.py, and
create a new view like::

    class FoodCreateView(CreateView):
        model = Food

In the urls.py, add the new FoodCreateView to the import at the top, and add a new url pattern::

    url(r'^food/new/', FoodCreateView.as_view(), name='food-create'),

Now you can update the create link in the list template to use the new and named ``food-create``.

Clicking the new link will also give an error about a missing template. Create t
he missing *food_form.html*. It will look very similar to the other two templates, but with a form in it::

    {% extends "base.html" %}

    {% block title %}Add food{% endblock %}

    {% block content %}
    <h1>Add food</h1>

    <form method="post">
    {{ form }}
    <button type="submit">Save</button>
    </form>
    {% endblock %}

Have a look at the form in the browser. Ok? Then add ``class="btn
btn-primary"`` to the submit button. Looks better? This is because of the
styling we get from Twitter Bootstrap.

We will also make the form layout a bit nicer with the third party **Crispy
Forms** module. To INSTALLED_APPS add ``crispy_forms`` and install
django-crispy-forms with pip::

    pip install django-crispy-forms

Below the extends line in the form, add::

    {% load crispy_forms_tags %}

And add the ``crispy`` filter to the form variable. Not the best example with only one variable in the form.


• Trykk på save uten endringer
• Legg på method=post
• Legg på csrf_token
• Legg på get_absolute_url
• PAUSE
• Tegning av recipe-obj med ingredient av food
• Legg til ingredient og recipe i modell
TODO: Referanse til dok
• med __unicode__
• Og i admin
• Legg til ny oppskrift - se at vi mangler felt - legg til blank=True
• Legg til ingrediens i admin fra oppskriftsida
• Legg til __unicode__ med get_measurement_display()
• Først med %f så %.2f
• Change admin to show which recipe an ingredient belongs to list_display = ('food', 'amount', 'measurement', 'recipe') LATER
• PAUSE
• List pancakes
• Copy-paste templates
• Legg til description med default: "No description"
• Lag add recipe i lista
• Lag url og view
• Test og se at det knekker
• Lag template
• Test og se at det knekker
• Lag get_absolute_url
• PAUSE
• Lag edit description på recipe-objeketet
• Legg til i models og urls
• PAUSE
• Add view to add ingredients
• Add url
• Add template
• See that you choose recipe in list
• Add get_initial
• Lag forms.py (model = Ingredient, recipe widget HiddenInput)
• Test og se at det mangler get_success_url
• Lag funksjon, og legg inn args=[self.kwargs['slug']]
• PAUSE
• Lag delete-link med icon-remove
• Se at det ikke virker, og lag ingredient_conform_delete.html
• Husk å få med form med submit og cancel
• (vis objektene i cancel)
• Se at vi mangler get_success_url: bruk samme som sist
• PAUSE
• Markdown i skrivefelt: i toppen og django.contrib.markup i settings
• Se at det feiler og installer markdown
• Toppmeny - lim inn fra bootstrap


Later lessions:
• debugging with ipython, pdb, web error
• unit testing
• authentication


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

