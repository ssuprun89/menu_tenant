from django.urls import path, include

urlpatterns = [
    path("user/", include("users.urls"), name="user"),
    path("client/", include("clients.urls"), name="client"),
    path("categories/", include("foods.urls"), name="tables"),
]
