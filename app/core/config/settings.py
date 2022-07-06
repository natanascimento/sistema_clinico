from os.path import abspath, join, dirname


class Settings:

    ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))

    DATA_PATH = join(ROOT_PATH, "data")

    ENDERECO_DATA_PATH = join(DATA_PATH, "enderecos.json")
    PESSOA_DATA_PATH = join(DATA_PATH, "pessoas.json")
    PACIENTE_DATA_PATH = join(DATA_PATH, "pacientes.json")
    AGENDA_DATA_PATH = join(DATA_PATH, "agendas.json")
    MEDICO_DATA_PATH = join(DATA_PATH, "medicos.json")

    NOME_SISTEMA = "SISTEMA CLINICO"
