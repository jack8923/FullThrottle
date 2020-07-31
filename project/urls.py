from rest_framework.routers import DefaultRouter
from .views import MembersViewSet, ActivityViewSet

app_name = "project"

router = DefaultRouter()
router.register('members', MembersViewSet, basename="members")  # Members API
router.register('activity_periods', ActivityViewSet, basename="activity_periods")  # Activity_periods API

urlpatterns = router.urls
