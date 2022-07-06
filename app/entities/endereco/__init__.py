from uuid import uuid4
from datetime import datetime

from app.entities.database import LocalDatabase
from app.core.config import settings


class Endereco:

    def __init__(self) -> None:

        self.id_endereco = str(uuid4())
        self.__logradouro = None
        self.__numero = None
        self.__complemento = None
        self.__bairro = None
        self.__cidade = None
        self.__uf = None
        self.__created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__parametros = ["id", "logradouro", "numero",
                             "complemento", "bairro", "cidade", "uf", "created_at"]
        self.__list_data = None
        self.__enderecos_file_path = settings.ENDERECO_DATA_PATH
        self.__entity_name = "enderecos"

    def cadastrar_endereco(self) -> None:
        self.__logradouro = str(input("Informe o logradouro: "))
        self.__numero = int(input("Informe o numero da residencia: "))
        self.__complemento = str(input("Informe o complemento: "))
        self.__bairro = str(input("Informe o bairro: "))
        self.__cidade = str(input("Informe a cidade: "))
        self.__uf = str(input("Informe a unidade federativa: "))
        self.__list_data = [self.id_endereco, self.__logradouro, self.__numero,
                            self.__complemento, self.__bairro, self.__cidade,
                            self.__uf, self.__created_at]
        self.__salvar_endereco()

    def listar_enderecos(self):
        LocalDatabase.select(file_path=self.__enderecos_file_path,
                             entity_name=self.__entity_name)

    def __salvar_endereco(self) -> None:
        LocalDatabase.insert(file_path=self.__enderecos_file_path, entity_name=self.__entity_name,
                             data=LocalDatabase.normalize_data(self.__parametros,
                                                               self.__list_data))
