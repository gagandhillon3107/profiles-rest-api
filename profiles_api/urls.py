from django.urls import path, include
from rest_framework.routers import DefaultRouter


from profiles_api import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register("profile", views.UserProfileViewset)
router.register("feed", views.ProfileFeedViewset)

urlpatterns = [
    path("hello-view/", views.HelloAPIView.as_view()),
    path("login/", views.UserLoginAPIView.as_view()),
    path("", include(router.urls)),
]
