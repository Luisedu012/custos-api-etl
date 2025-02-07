# pylint: disable=line-too-long

"""
Código para Realizar requisição na consulta de demais custos do tesouro nacional
"""
import os
import requests

from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class PessoalInativoCustos:
    """
    Inicializando PessoalInativoCustos com os parâmetros necessários
    """

    def __init__(
        self,
        start_year: int = 2015,
        end_year: int = 2024,
        legal_nature: Optional[int] = None,
        org_level_1: Optional[str] = None,
        org_level_2: Optional[str] = None,
        org_level_3: Optional[str] = None,
    ) -> None:

        if start_year > end_year:
            raise ValueError("Ano de inicio não pode ser maior que ano final")

        self.start_yaer = start_year
        self.end_year = end_year
        self.legal_nature = legal_nature
        self.org_level_1 = org_level_1
        self.org_level_2 = org_level_2
        self.org_level_3 = org_level_3
        self.url = os.getenv("DEM_URL_PESSOAL_INATIVO")

    def _build_params(self, year: int, month: int) -> dict:
        """
        Construindo as querys para Requisições da API

        Parameters:
            year (int): Ano para requisição da Api.
            month (int): Mês para a requisição da Api.

        Returns:
            dict: Dicionários das consultas dos Parâmetros.
        """
        return {
            "ano": year,
            "mes": month,
            "natureza_legal": self.legal_nature,
            "organizacao_n1": self.org_level_1,
            "organizacao_n2": self.org_level_2,
            "organizacao_n3": self.org_level_3,
        }

    def fetch_data(self) -> None:
        """
        Busca pelos dados de custos de Pessoal Inativo entre os anos de 2015 á 2024.

        Printa o Ano, Mês e quantidade de dados retornados.

        """
        total_data_count = 0

        for year in range(self.start_yaer, self.end_year + 1):
            for month in range(1, 13):
                params = self._build_params(year, month)
                try:
                    response = requests.get(self.url, params=params, timeout=10)
                    response.raise_for_status()

                    data = response.json()
                    data_count = len(data.get("items", []))

                    print(f"Year: {year}, Month: {month} - Data_count: {data_count}")
                    total_data_count += data_count
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred for {year}-{month}: {e}")

        print(f"\nTotal Data Colleted: {total_data_count}")


fetcher = PessoalInativoCustos()
fetcher.fetch_data()
