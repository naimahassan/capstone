from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.index, name = 'index'),
    url('^$',views.post, name = 'post'),
    url('^detail(\d+)',views.detail, name = 'detail'),
    url('^create/new_post',views.new_post, name = 'new_post'),
    url('^profile',views.profile, name = 'profile' )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)