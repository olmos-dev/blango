from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from blog.api.views import UserDetail, PostViewSet,TagViewSet

router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("tags", TagViewSet)


urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    path("", include(router.urls)),
]

#urlpatterns = format_suffix_patterns(urlpatterns) 