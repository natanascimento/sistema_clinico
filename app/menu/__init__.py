from app.core.config import settings
from app.menu.design import MenuDesign
from app.entities import Medico, Paciente, Pessoa, Agenda


class MainMenu:

    @staticmethod
    def start():

        while True:
            MenuDesign.made_terminal_component(settings.NOME_SISTEMA, fill_char="=")
            MenuDesign.made_terminal_component("\n1 - Agenda "
                                               "\n2 - Paciente "
                                               "\n3 - Medico "
                                               "\n4 - Pessoas"
                                               "\n\n0-Sair\n", fill_char=" ")
            MenuDesign.made_terminal_component("|", fill_char="=")
            option = int(input("\nSelecione opção que deseja: "))
            MenuDesign.made_terminal_component("|")
            if option == 1:
                MenuDesign.made_terminal_component(" AGENDA ", fill_char="=")
                MenuDesign.made_terminal_component("\n1 - Cadastrar \n2 - Exibir agendas "
                                                   "\n\n0 - Sair\n", fill_char=" ")
                MenuDesign.made_terminal_component("|", fill_char="=")
                sub_option = int(input("\nSelecione opção que deseja: "))
                MenuDesign.made_terminal_component("|")
                if sub_option == 1:
                    Agenda().cadastrar_agenda()
                elif sub_option == 2:
                    Agenda().listar_agendas()
                elif sub_option == 0:
                    break
            elif option == 2:
                MenuDesign.made_terminal_component(" PACIENTE ", fill_char="=")
                MenuDesign.made_terminal_component("\n1 - Cadastrar \n2 - Exibir Pacientes "
                                                   "\n\n0 - Sair\n", fill_char=" ")
                MenuDesign.made_terminal_component("|", fill_char="=")
                sub_option = int(input("\nSelecione opção que deseja: "))
                MenuDesign.made_terminal_component("|")
                if sub_option == 1:
                    Paciente().cadastrar_paciente()
                elif sub_option == 2:
                    Paciente().listar_pacientes()
                elif sub_option == 0:
                    break

            elif option == 3:
                MenuDesign.made_terminal_component(" MEDICO ", fill_char="=")
                MenuDesign.made_terminal_component("\n1 - Cadastrar \n2 - Exibir Medicos "
                                                   "\n\n0 - Sair\n", fill_char=" ")
                MenuDesign.made_terminal_component("|", fill_char="=")
                sub_option = int(input("\nSelecione opção que deseja: "))
                MenuDesign.made_terminal_component("|")

                if sub_option == 1:
                    Medico().cadastrar_medico()
                elif sub_option == 2:
                    Medico().listar_medicos()
                elif sub_option == 0:
                    break

            elif option == 4:
                MenuDesign.made_terminal_component(" PESSOA ", fill_char="=")
                MenuDesign.made_terminal_component("\n1 - Exibir Pessoas "
                                                   "\n\n0 - Sair\n", fill_char=" ")
                MenuDesign.made_terminal_component("|", fill_char="=")
                sub_option = int(input("\nSelecione opção que deseja: "))
                MenuDesign.made_terminal_component("|")

                if sub_option == 1:
                    Pessoa().listar_pessoas()
                elif sub_option == 0:
                    break

            elif option == 0:
                break
            else:
                MenuDesign.made_terminal_component("Opção inválida, tente novamente", 80, "#")
