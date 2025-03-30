from rest_framework import serializers

from habits.models import GoodHabit, NiceHabit, RelatedHabit
from habits.validators import FillingOneFields, TimingCheck


class NiceHabitSerializer(serializers.ModelSerializer):
    """Сериализатор приятной привычки"""

    class Meta:
        model = NiceHabit
        fields = ("place", "lide_time", "action", "time_to_complete", "sing_of_publicity")

        validators = [TimingCheck(field="time_to_complete")]


class RelatedHabitSerializer(serializers.ModelSerializer):
    """Сериализатор вознаграждения или полезной привычки"""

    related_habit = NiceHabitSerializer(read_only=True)

    class Meta:
        model = RelatedHabit
        fields = (
            "id",
            "related_habit",
            "reward",
        )
        validators = [FillingOneFields("related_habit", "reward")]


class GoodHabitSerializer(serializers.ModelSerializer):
    """Сериализатор хорошей привычки"""

    related_habit = RelatedHabitSerializer(read_only=True)

    class Meta:
        model = GoodHabit
        fields = "__all__"
