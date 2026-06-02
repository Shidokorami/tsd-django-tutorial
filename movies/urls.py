from rest_framework.routers import DefaultRouter

from movies.views import MovieViewSet

router = DefaultRouter()

# TODO: Task 3.5 - Register MovieViewSet on the router
# router.register(...)

urlpatterns = router.urls
