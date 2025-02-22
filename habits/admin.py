from django.contrib import admin

from habits.models import GoodHabit, NiceHabit, RelatedHabit


@admin.register(RelatedHabit)
class RelatedHabitAdmin(admin.ModelAdmin):
    list_display = ("id", "related_habit", "reward")


@admin.register(NiceHabit)
class NiceHabitAdmin(admin.ModelAdmin):
    list_display = ("id", "place", "lide_time", "action")


@admin.register(GoodHabit)
class GoodHabitAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "place", "lide_time", "action")
