from uuid import uuid4
from typing import Dict, Any
from datetime import datetime

from app.entities.endereco import Endereco
from app.entities.database import LocalDatabase
from app.core.config import settings


class Pessoa:

    def __init__(self):
        self.id_pessoa = str(uuid4())
        self.__nome = None
        self.__celular = None
        self.__email = None
        self.__endereco = Endereco()
        self.__created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__parametros = ["id", "nome", "celular", "email", "enderecos", "created_at"]
        self.__list_data = None
        self.__pessoas_file_path = settings.PESSOA_DATA_PATH
        self.__entity_name = "pessoas"

    def cadastrar_pessoa(self):
        self.__nome = str(input("Informe o Nome: "))
        self.__celular = int(input("Informe o numero de telefone: "))
        self.__email = str(input("Informe o email: "))
        self.__endereco.cadastrar_endereco()
        self.__list_data = [self.id_pessoa, self.__nome, self.__celular,
                            self.__email, self.__endereco.id_endereco,
                            self.__created_at]
        self.__salvar_pessoa()

    def listar_pessoas(self):
        LocalDatabase.select(file_path=self.__pessoas_file_path,
                             entity_name=self.__entity_name)
        self.__endereco.listar_enderecos()

    def __salvar_pessoa(self):
        LocalDatabase.insert(file_path=self.__pessoas_file_path, entity_name=self.__entity_name,
                             data=LocalDatabase.normalize_data(self.__parametros,
                                                               self.__list_data))
