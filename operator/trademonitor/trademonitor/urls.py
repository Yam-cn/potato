from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trademonitor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#)
urlpatterns = patterns('',
    # ... the rest of your URLconf goes here ...
)
urlpatterns += patterns('trademonitor.controller.stratgyController',
    url(r'^strategy/$', 'strategy'),
    url(r'^addAccount/$', 'addAccount'),
    url(r'^deleteAccount/$', 'deleteAccount'),
    url(r'^addStrategy/$', 'addStrategy'),
    url(r'^stopStrategy/$', 'stopStrategy'),
    url(r'^deleteStrategy/$', 'deleteStrategy'),
    url(r'^addTradeDetail/$', 'addTradeDetail'),
    url(r'^queryAccount/$', 'queryAccount'),
    url(r'^queryAllAccount/$', 'queryAllAccount'),
    url(r'^queryStrategy/$', 'queryStrategy'),
    url(r'^queryAllStrategy/$', 'queryAllStrategy'),
    url(r'^queryTradeDetail/$', 'queryTradeDetail'),
    url(r'^queryAllTradeDetail/$', 'queryAllTradeDetail'),
)
urlpatterns += patterns('trademonitor.controller.genuuidController',
    url(r'^genuuid/$', 'genuuid'),
)

# This will work if DEBUG is True
urlpatterns += staticfiles_urlpatterns()

#urlpatterns += staticfiles_urlpatterns()
from django.conf import settings
urlpatterns += patterns('',
   (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)