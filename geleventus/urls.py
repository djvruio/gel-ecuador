from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'geleventus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.events.urls')),
    url(r'^admin/', include(admin.site.urls)),
] 

if not settings.DEBUG:
	urlpatterns += patterns("",
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT,}
		),
	)

