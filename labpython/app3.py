import os, traceback
import sqlite3
from sqlite3 import Cursor
from dotenv import dotenv_values
from use_cases.patient_use_case import insert_new_patient
from infra.repositories.patient_repository import patient_repository
from infra.email_sender import email_sender 
from core.domain.patient import Patient
from typing import Callable, Dict, Tuple, Any, List

def create_table(cur: Cursor) -> None:

    query = """
    CREATE TABLE IF NOT EXISTS Paciente(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        CPF TEXT NOT NULL, 
        BIRTH_DATE TEXT NOT NULL, 
        ZIP_CODE TEXT NOT NULL,
        NUMBER INTEGER NOT NULL);"""

    cur.execute(query)


def menu():
    
    import sys
    import time

    # while True:

    print(args := sys.argv[1:])
        
    def formulario():
        print("""
        Iinforme as pções de cadastro
        1 - Informe um nome:
        2 - Informe um cpf:
        3 - Informe uma data de nascimento:
        4 - Informe um endereço:
        """)

        while (val := input("Informe uma opção: ")) != "2":

            if "1" == val:
                formulario()
                print(f"Valor {val}")

            elif "2" == val:
                print("Programa encerrado")

            else:
                print("( ˘︹˘ ) -- Informe apenas os códigos válidos para menu")

            time.sleep(1)
    
    # from sys import getsizeof

    # print(getsizeof(main_menu), getsizeof(val))
    # print(main_menu)
    conn = ""
    def executa_cadastro_paciente(conn):
        print("CHEGANDO AQUI 1")

        def create(dados):

            if dados == {}:
                return

            print("dados>>>>>>", dados)

        return create

    def deep_menu(option: str | None) -> dict:

        if option is None:
            return {}
        else:
            roteiro = """
            INFORME OS CAMPOS PARA CADASTRO\n
            1 - nome:
            2 - email:
            3 - cpf:
            4 - data de nascimento:
            5 - cep:
            6 - número de endereço:
            7 - Confirmar:
            """
            
            dados = {"nome": "",
                     "email": "",
                     "cpf": "",
                     "data_nascimento": "",
                     "cep": "",
                     "numero": 0}

            message = "Informe um código"


            def check_form(dados: Dict) -> List:
                
                occurrences = []

                if dados["nome"] == "":
                    occurrences.append("1 - *Nome obrigatório")
                if dados["email"] == "":
                    occurrences.append("2 - *Email obrigatório")
                if dados["cpf"] == "":
                    occurrences.append("3 - *CPF obrigatório")
                if dados["data_nascimento"] == "":
                    occurrences.append("4 - *Data de nascimento obrigatória")
                if dados["cep"] == "":
                    occurrences.append("5 - *CEP obrigatório")
                if dados["numero"] == "":
                    occurrences.append("6 - *Número de endereço obrigatório")

                return occurrences
            
            status = True
            
            while True:

                os.system('clear')

                print(roteiro)
                
                if status is False:
                    print(">> Campos obrigatórios:")
                    for occ in check_form(dados):
                        if occ:
                            print(occ)

                print(f"\nFormulário:{dados}")

                match code := input(f"\n{message}: "):

                    case "1":
                        dados["nome"] = input("Informe um nome:")

                    case "2":
                        dados["email"] = input("Informe um email:")

                    case "3":
                        dados["cpf"] = input("Informe um cpf:")

                    case "4":
                        dados["data_nascimento"] = input(
                            "Informe uma data de nascimento:")

                    case "5":
                        dados["cep"] = input("Informe um cep:")

                    case "6":
                        dados["numero"] = input(
                            "Informe um número de endereço:")

                    case "7":
                        
                        if [] == check_form(dados):
                            break
                        
                        status = False

                    case _:
                        message = "( ˘︹˘ ) - Informe um código válido para campo"

                if code in (1, 2, 3, 4, 8, 6):
                    message = "Informe um código"

            return dados


    def main_menu(val: str) -> str | None:
        print("CHEGANDO AQUI 2")
        match val:
            case "1":
                return "1"

            case "2":

                if input("Encerrar menu? [s]:").lower() == "s":
                    return

                main_menu(input("Informe uma opção: "))

            case _:
                main_menu(
                    input("( ˘︹˘ ) - Informe um código válido de menu:"))

    try:
        
        roteiro = """
        MENU PRINCIPAL

        1 ☀︎ Cadastro de paciente
        2 ☽ Sair
        
        Informe uma opção: """
        
        executa_cadastro_paciente(conn)(
            (code := main_menu(input(roteiro)), deep_menu(code))
        )

    except Exception as e:
        print(traceback.format_exc())

    # while (val := input("Informe uma opção: ")) != "2":

    #     match val.split():
    #         case ["1"]:
    #             formulario()
    #         case ["2"]:

    #             print("Programa encerrado")
    #         case _:
    #             print("( ˘︹˘ ) -- Informe apenas os códigos válidos para menu")


        # time.sleep(1)





if __name__ == "__main__":

    conn = None

    paciente = menu()

    exit()


    try:




        config = dotenv_values('.env.ambient')

        path_db = config.get("PATH_DATABASE") or ""

        if path_db == "":
            raise Exception("PATH_DATABASE não identificado")

        conn = sqlite3.connect(path_db)

        cur = conn.cursor()

        create_table(cur)

        create = insert_new_patient(patient_repository(cur), email_sender())

        create(Patient('Julia Alessandra Letícia Souza',
                       'julia-souza77@gmailo.com',
                       '892.734.075-28',
                       '08/01/1957',
                       '89256-540',
                       '935'))

        create(Patient('Mariana Jéssica Giovanna Rezende',
                       'mariana.jessica.rezende@onset.com.br',
                       '185.517.827-38',
                       '09/01/1988',
                       '76960-180',
                       '313'))

        conn.commit()

    except Exception as e:
        
        if conn:
            conn.rollback()

        print("ERRO>>", e)
    
    finally:
        
        if conn:
            conn.close()
