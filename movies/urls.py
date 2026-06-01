from rest_framework.routers import DefaultRouter

from movies.views import MovieViewSet

# TODO: Task 3.4 - Register ViewSet in router as 'movies'. Remember to provide basename.
router = DefaultRouter()
router.register("movies", MovieViewSet, "movie")

urlpatterns = router.urls
