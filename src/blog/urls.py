from django.contrib import admin
from django.conf import settings
from django.urls import include, re_path, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.core.urls')),
    path('i18n/', include('django.conf.urls.i18n'))
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]