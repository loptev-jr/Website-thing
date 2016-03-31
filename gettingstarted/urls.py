from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import portfolio.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', portfolio.views.index, name='index'),
    url(r'^db', portfolio.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
