def get_weather():
    import requests

    # Замените YOUR_API_KEY на ваш API ключ OpenWeatherMap
    API_KEY = 'bd5e378503939ddaee76f12ad7a97608'
    CITY_NAME = 'Москва'

    # Формируем URL для запроса
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&lang=ru'

    # Отправляем GET запрос и получаем данные о погоде
    response = requests.get(url)
    data = response.json()

    # Извлекаем данные о погоде
    max_temp = data['main']['temp_max']
    min_temp = data['main']['temp_min']
    # Выводим данные о погоде
    return [min_temp, max_temp]
