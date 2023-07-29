import requests
from datetime import datetime

class Conversor:
    url = "http://economia.awesomeap.com.br/json/last/USD-BRL"

    def __init__(self,valor) -> None:
        self.__valor = valor
        self.__data = datetime.now()

    @staticmethod
    def verificar_disponibilidade():
        try: 
            cotacao = requests.get(Conversor.url).status_code
            if cotacao == 200: 
                return True
            return False
        except:
            print("Ocorreu um erro ao acessar") 
            return False
        
    def obter_valor_dolar(self) -> None:
        cotacao = requests.get(self.__url).json()
        dolar  = float(cotacao['USDBRL']['bid'])
        print(f"Valor atual do dólar R$ {dolar:.2f}")
        print("Data atual: ", self.__data)



print(Conversor.verificar_disponibilidade())