from rest_framework.routers import DefaultRouter

from movies.views import MovieViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')  # TODO: Task 3.4

urlpatterns = router.urls
