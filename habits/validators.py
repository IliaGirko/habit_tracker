import datetime

from rest_framework.serializers import ValidationError


class FillingOneFields:
    """ Валидатор проверки заполенения полей по правилу """
    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, value):
        if dict(value).get(self.reward) and dict(value).get(self.related_habit):
            raise ValidationError("Необходимо заполнить одно поле")


class TimingCheck:
    """ Валидатор проверки указанного времения выполнения на привычку """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        result = dict(value).get(self.field)
        if result > datetime.time(minute=2):
            raise ValidationError("Время на приятную привычку не должно превышать две минуты")
