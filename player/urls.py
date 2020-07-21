from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from api.views import PlayerViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    #These are the two urls that are requested
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
