from uuid import uuid4
from datetime import datetime

from app.entities.pessoa import Pessoa
from app.entities.database import LocalDatabase
from app.core.config import settings
from app.core import execution_time


class Medico(Pessoa):

    def __init__(self):
        super().__init__()
        self.id = str(uuid4())
        self.__crm = None
        self.__telefone = None
        self.__created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__parametros = ["id_pessoa", "crm", "telefone", "created_at"]
        self.__list_data = None
        self.__medicos_file_path = settings.MEDICO_DATA_PATH
        self.__entity_name = "medicos"

    @execution_time
    def cadastrar_medico(self):
        self.cadastrar_pessoa()
        self.__crm = str(input("Informe seu CRM: "))
        self.__telefone = str(input("Informe seu telefone: "))
        self.__list_data = [self.id_pessoa, self.__crm, self.__telefone, self.__created_at]
        self.__salvar_medico()

    def listar_medicos(self):
        LocalDatabase.select(file_path=self.__medicos_file_path,
                             entity_name=self.__entity_name)

    def __salvar_medico(self):
        LocalDatabase.insert(file_path=self.__medicos_file_path, entity_name=self.__entity_name,
                             data=LocalDatabase.normalize_data(self.__parametros,
                                                               self.__list_data))
