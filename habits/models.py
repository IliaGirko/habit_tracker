from django.db import models

from config.settings import AUTH_USER_MODEL


class NiceHabit(models.Model):
    """ Модель приятной привычки. """
    place = models.CharField(max_length=100, verbose_name="Место")
    lide_time = models.DateTimeField(verbose_name="Дата и время выполнения привычки")
    action = models.CharField(max_length=500, verbose_name="Действие")
    time_to_complete = models.TimeField(verbose_name="Время на выполнениe привычки")
    sing_of_publicity = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return f"Приятная привычка {self.action}"

    class Meta:
        verbose_name = "Приятная привычка"
        verbose_name_plural = "Приятные привычки"


class RelatedHabit(models.Model):
    """ Модель связанной привычки или вознаграждения """
    related_habit = models.ForeignKey(
        NiceHabit, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Связанная привычка"
    )
    reward = models.CharField(max_length=250, blank=True, null=True, verbose_name="Вознаграждение")

    def __str__(self):
        if self.related_habit:
            return f"Связанная привычка {self.related_habit}"
        else:
            return f"Вознаграждение {self.reward}"

    class Meta:
        verbose_name = "Связанная привычка или вознаграждение"
        verbose_name_plural = "Связанные привычки или вознаграждения"


class GoodHabit(models.Model):
    """ Модель полезной привычки """
    choice_of_periodicity = [
        ("Ежедневно", "Ежедневно"),
        ("Раз в два дня", "Раз в два дня"),
        ("По четным дням", "По четным дням"),
        ("По нечетным дням", "По нечетным дням"),
        ("Раз в неделю", "Раз в неделю"),
    ]

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    place = models.CharField(max_length=100, verbose_name="Место")
    lide_time = models.DateTimeField(verbose_name="Дата и время выполнения привычки")
    action = models.CharField(max_length=500, verbose_name="Действие")
    related_habit = models.ForeignKey(
        RelatedHabit, on_delete=models.CASCADE, verbose_name="Связанная привычка или вознаграждение"
    )
    periodicity = models.CharField(
        max_length=20, choices=choice_of_periodicity, default="Ежедневно", verbose_name="Переодичность"
    )
    time_to_complete = models.TimeField(verbose_name="Время на выполнениe привычки")
    sing_of_publicity = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return f"Хорошая привычка {self.action}"

    class Meta:
        verbose_name = "Хорошая привычка"
        verbose_name_plural = "Хорошие привычки"
