from rest_framework.routers import DefaultRouter

from habits import views

from .apps import HabitsConfig

app_name = HabitsConfig.name

router = DefaultRouter()

router.register(r"good_habit", views.GoodHabitViewSet, basename="good_habit")
router.register(r"nice_habit", views.NiceHabitViewSet, basename="nice_habit")
router.register(r"related_habit", views.RelatedHabitViewSet, basename="related_habit")

urlpatterns = [] + router.urls
