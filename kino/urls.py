from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from films import views

router = routers.DefaultRouter()
router.register(r'films', views.FilmsViewSet)
# router.register(r'rubs', views.RubsViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'kino.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('films.urls')),
    url(r'^api', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
