from uuid import uuid4
from datetime import datetime

from app.entities.pessoa import Pessoa
from app.entities.database import LocalDatabase
from app.core.config import settings
from app.core import execution_time


class Paciente(Pessoa):

    def __init__(self):
        super().__init__()
        self.id_paciente = str(uuid4())
        self.__rg = None
        self.__cpf = None
        self.__telefone = None
        self.__convenio = None
        self.__data_de_nascimento = None
        self.__created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__parametros = ["id_pessoa", "rg", "cpf", "telefone", "convenio", "data_nascimento", "created_at"]
        self.__list_data = None
        self.__pacientes_file_path = settings.PACIENTE_DATA_PATH
        self.__entity_name = "pacientes"

    @execution_time
    def cadastrar_paciente(self):
        self.cadastrar_pessoa()
        self.__rg = str(input("Informe seu RG: "))
        self.__cpf = str(input("Informe seu CPF: "))
        self.__telefone = str(input("Informe seu telefone: "))
        self.__convenio = str(input("Informe seu convêncio médico: "))
        self.__data_de_nascimento = str(input("Informe sua data de nascimento: "))
        self.__list_data = [self.id_pessoa, self.__rg, self.__cpf,
                            self.__telefone, self.__convenio, self.__data_de_nascimento,
                            self.__created_at]
        self.__salvar_paciente()

    def listar_pacientes(self):
        LocalDatabase.select(file_path=self.__pacientes_file_path,
                             entity_name=self.__entity_name)

    def __salvar_paciente(self):
        LocalDatabase.insert(file_path=self.__pacientes_file_path, entity_name=self.__entity_name,
                             data=LocalDatabase.normalize_data(self.__parametros,
                                                               self.__list_data))
