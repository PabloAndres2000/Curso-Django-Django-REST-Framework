from rest_framework import routers

from store.apps.users.api.views.user import UserViewSet

router = routers.SimpleRouter()

router.register(r"users/user", UserViewSet, basename="users")


urlpatterns = router.urls
