from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import myapp.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', myapp.views.index, name='index'),
    url(r'^db', myapp.views.db, name='db'),
    url(r'^McGill', myapp.views.mcgill, name='mcgill'),
    url(r'^PacificAcademy', myapp.views.pacificacademy, name='pacificacademy'),
    url(r'^Projects', myapp.views.projects, name='projects'),
    url(r'^Programming/DataStructure', myapp.views.datastructure, name='datastructure'),
    url(r'^Programming/DesignPattern', myapp.views.designpattern, name='designpattern'),
    url(r'^admin/', include(admin.site.urls)),
]
