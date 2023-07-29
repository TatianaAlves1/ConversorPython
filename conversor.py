import requests
from datetime import datetime

class Conversor:
    def __init__(self,url,valor) -> None:
        self.__url = url
        self.__valor = valor
        self.__data = datetime.now()

    def obter_valor_dolar(self):
        dolar = requests.get(self.__url).json()
        print("valor atual: ",dolar)
        print("Data atual: ", self.__data)



teste = Conversor('http://economia.awesomeapi.com.br/json/last/USD-BRL',200)
teste.obter_valor_dolar()