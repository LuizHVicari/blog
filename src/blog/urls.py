from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.core.urls')),
    path('posts/', include('apps.posts.urls')),
    path('i18n/', include('django.conf.urls.i18n'))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]