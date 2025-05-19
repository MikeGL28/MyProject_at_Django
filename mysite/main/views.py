import requests
from datetime import time, datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from .api_weather import TOKEN_API_WEATHER
from .models import PostView

class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        # Получаем данные о постах
        posts = PostView.objects.all()
        post_data = []
        for post in posts:
            post_data.append({
                'title': post.title,
                'content': post.content,
                'published': post.published,
            })

        # Логика для получения погоды
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }

        city = request.GET.get('city', 'Saint Petersburg')  # По умолчанию Москва
        weather_context = {}
        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN_API_WEATHER}&units=metric&lang=ru"
            )
            data = response.json()

            if data['cod'] != 200:
                raise ValueError("City not found")

            city_name = data["name"]
            cur_weather = data["main"]["temp"]
            weather_description = data["weather"][0]["main"]
            weather_icon = code_to_smile.get(weather_description, "Посмотри за окно, не пойму что там за погода.")

            weather_context = {
                'city': city_name,
                'temperature': round(cur_weather),
                'description': weather_icon,
            }

        except Exception as e:
            weather_context = {
                'error': "Город не найден или произошла ошибка. Проверьте название города."
            }

        context = {
            'post': post_data,
            'weather': weather_context,
        }

        return render(request, 'home.html', context=context)