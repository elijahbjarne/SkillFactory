import requests
import json

# Класс-расчетчик курса
class RequestProvider:
    def __init__(self):
        pass

    # Посчитать курс
    @staticmethod
    def get_price(base, quote, amount):
        request = requests.get("https://v6.exchangerate-api.com/v6/4b4a7b33c8e2e978998bf91a/latest/EUR")
        result = json.loads(request.content)
        money_dict = result['conversion_rates']
        v1 = money_dict[base]
        v2 = money_dict[quote]

        #Идет просчет через Евро по стандарту
        value = amount / (v1 / v2)
        return value
