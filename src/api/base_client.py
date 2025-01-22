"""módulo para servir como base das requisições"""
import requests


from time import sleep


class BaseClient:
    """
    Classe responsável por realizar requisições GET para a API do DataLake do Tesouro Nacional.

    Attributes:
        BASE_URL (str): URL base para as requisições.
        RATE_LIMIT (int): Tempo de espera entre as requisições em segundos.
        endpoint (str): O endpoint da API a ser utilizado na requisição.
    """

    BASE_URL = "https://apidatalake.tesouro.gov.br/ords/custos/tt/"
    RATE_LIMIT = 1  # Atraso de 1 segundo entre as requisições

    def __init__(self, endpoint):
        """
        Inicializa a classe BaseClient com o endpoint especificado.

        Args:
            endpoint (str): O endpoint da API a ser utilizado.
        """
        self.endpoint = endpoint

    def get(self, params=None):
        """
        Realiza uma requisição GET para o endpoint especificado.

        Args:
            params (dict, optional): Parâmetros adicionais para a requisição.

        Returns:
            dict: Resposta da API em formato JSON.

        Raises:
            Exception: Se ocorrer algum erro durante a requisição.
        """
        url = f"{self.BASE_URL}{self.endpoint}"

        # Atraso entre requisições para respeitar o rate limit
        sleep(self.RATE_LIMIT)

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro na requisição: {e}") from e

        return response.json()
