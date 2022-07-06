from uuid import uuid4
from datetime import datetime

from app.core import execution_time
from app.entities.database import LocalDatabase
from app.core.config import settings


class Agenda:

    def __init__(self) -> None:
        self.id_agenda = str(uuid4())
        self.__crm_medico = None
        self.__cpf_paciente = None
        self.__dia = None
        self.__mes = None
        self.__ano = None
        self.__hora = None
        self.__observacao = None
        self.__created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__parametros = ["id", "crm_medico", "cpf_paciente",
                             "dia", "mes", "ano", "hora", "observacao", "created_at"]
        self.__list_data = None
        self.__agendas_file_path = settings.AGENDA_DATA_PATH
        self.__entity_name = "agendas"

    @execution_time
    def cadastrar_agenda(self) -> None:
        self.__crm_medico = str(input("Informe o CRM do médico: "))
        self.__cpf_paciente = int(input("Informe o CPF do paciente: "))
        self.__dia = str(input("Informe o dia da consulta: "))
        self.__mes = str(input("Informe o mes da consulta: "))
        self.__ano = str(input("Informe o ano da consulta: "))
        self.__hora = str(input("Informe a hora da consulta: "))
        self.__observacao = str(input("Informe uma observacao importante para a consulta: "))
        self.__list_data = [self.id_agenda, self.__crm_medico, self.__cpf_paciente,
                            self.__dia, self.__mes, self.__ano,
                            self.__hora, self.__observacao, self.__created_at]
        self.__salvar_agenda()

    def listar_agendas(self):
        LocalDatabase.select(file_path=self.__agendas_file_path,
                             entity_name=self.__entity_name)

    def __salvar_agenda(self) -> None:
        LocalDatabase.insert(file_path=self.__agendas_file_path, entity_name=self.__entity_name,
                             data=LocalDatabase.normalize_data(self.__parametros,
                                                               self.__list_data))
