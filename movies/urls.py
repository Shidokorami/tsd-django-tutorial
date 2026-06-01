from rest_framework.routers import DefaultRouter

from movies.views import ModelApiViewSet

router = DefaultRouter()
router.register('models', ModelApiViewSet, basename='model')  # TODO: Task 3.4

urlpatterns = router.urls
