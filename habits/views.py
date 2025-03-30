from rest_framework import viewsets

from habits.models import GoodHabit, NiceHabit, RelatedHabit
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import GoodHabitSerializer, NiceHabitSerializer, RelatedHabitSerializer
from habits.tasks import send_mail_time_good_habit


class GoodHabitViewSet(viewsets.ModelViewSet):
    """ Вьювсет хорошей привычки """
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    pagination_class = HabitsPaginator
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        """ При создании новой привычки проверяет, не пришло ли время выполнения других привычек """
        serializer.save(user=self.request.user)
        send_mail_time_good_habit.delay()

    def get_permissions(self):
        """ Проверяет владельц привычки пользователь или нет """
        self.permission_classes = (IsOwner,)
        return super().get_permissions()

    def get_queryset(self):
        """ Проверяет публичные привычки и возвращает их """
        queryset = super().get_queryset()
        if queryset.filter(user=self.request.user):
            return queryset
        return queryset.filter(sing_of_publicity=True)


class NiceHabitViewSet(viewsets.ModelViewSet):
    """ Вьювсет приятной привычки """
    serializer_class = NiceHabitSerializer
    queryset = NiceHabit.objects.all()
    pagination_class = HabitsPaginator


class RelatedHabitViewSet(viewsets.ModelViewSet):
    """ Вьювсет вознаграждения или связанной привычки """
    serializer_class = RelatedHabitSerializer
    queryset = RelatedHabit.objects.all()
