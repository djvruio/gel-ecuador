from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^$', 'apps.events.views.index', name='index'),
]
