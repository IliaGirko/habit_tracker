from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from habits.models import NiceHabit, RelatedHabit
from users.models import User


class NiceHabitAPITestCase(APITestCase):
    """Тестирование приятной привычки"""
    def setUp(self):
        pass

    def test_create_nice_habit(self):
        """Тестирование создания приятной привычки"""
        data = {
            "place": "Душ",
            "lide_time": "2025-02-19T10:00:00+03:00",
            "action": "Прием душа",
            "time_to_complete": "00:02:00",
            "sing_of_publicity": True,
        }
        response = self.client.post("/habits/nice_habit/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
            {
                "place": "Душ",
                "lide_time": "2025-02-19T10:00:00+03:00",
                "action": "Прием душа",
                "time_to_complete": "00:02:00",
                "sing_of_publicity": True,
            },
        )
        self.assertTrue(NiceHabit.objects.all().exists())


class RelatedHabitAPITestCase(APITestCase):
    """Тестирование вознаграждения"""
    def setUp(self):
        pass

    def test_create_related_habit(self):
        """Тестирование создания вознаграждения"""
        data = {"reward": "Выпить кофе"}
        response = self.client.post("/habits/related_habit/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(), {"id": 1, "related_habit": None, "reward": "Выпить кофе"})
        self.assertTrue(RelatedHabit.objects.all().exists())

    def tearDown(self):
        pass


class GoodHabitAPITestCase(APITestCase):
    """Тестирование полезной привычки"""
    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru", telegram_id=10, password="12345")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_related_habit(self):
        """Тестирование полезной привычки"""
        self.client.get("/habits/good_habit/")
