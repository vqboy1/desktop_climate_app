def get_weather(town):

    import requests

#  Пример словаря данных {'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 804, 'main': 'Clouds',
    #  'description': 'пасмурно', 'icon': '04d'}],
#      'base': 'stations', 'main': {'temp': 269.32, 'feels_like': 264.18, 'temp_min': 268.79, 'temp_max': 269.9,
    #      'pressure': 1036, 'humidity':
#         95, 'sea_level': 1036, 'grnd_level': 1016}, 'visibility': 10000,
    #         'wind': {'speed': 3.98, 'deg': 241, 'gust': 10.72}, 'clouds': {'all': 99}
#     , 'dt': 1706519011, 'sys': {'type': 2, 'id': 47754, 'country': 'RU', 'sunrise': 1706506213, 'sunset': 1706536477},
    #     'timezone': 10800, 'id': 524901,
#      'name': 'Москва', 'cod': 200}

    # Замените YOUR_API_KEY на ваш API ключ OpenWeatherMap
    API_KEY = 'bd5e378503939ddaee76f12ad7a97608'
    CITY_NAME = town

    # Формируем URL для запроса
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&lang=ru'

    # Отправляем GET запрос и получаем данные о погоде
    response = requests.get(url)
    data = response.json()

    # Извлекаем данные о погоде
    # Выводим данные о погоде
    return data