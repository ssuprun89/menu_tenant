from rest_framework.routers import DefaultRouter

from users.controller import UserViewSet

urlpatterns = []

routers = DefaultRouter()
routers.register("", UserViewSet, basename="user")

urlpatterns += routers.urls
