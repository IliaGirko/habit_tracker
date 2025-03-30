import datetime

import requests
from celery import shared_task

from config.settings import TOKEN_TG_BOT

from .models import GoodHabit


@shared_task
def send_mail_time_good_habit():
    """ Переодическое выполнение задачи отправки писем """
    times_good_habit = GoodHabit.objects.all()
    for time_good_habit in times_good_habit:
        if time_good_habit.lide_time == datetime.datetime.now():
            tg_id = times_good_habit.user.telegram_id
            params = {"text": "Настало время для выполнения привычки", "chat_id": tg_id}
            requests.get(f"https://api.telegram.org/bot{TOKEN_TG_BOT}/sendMessage", params=params)
