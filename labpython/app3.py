import sqlite3
from sqlite3 import Cursor
from dotenv import dotenv_values
from use_cases.patient_use_case import patient_use_case
from infra.repositories.patient_repository import patient_repository

def create_table(cur: Cursor) -> None:

    query = """
    CREATE TABLE IF NOT EXISTS Paciente(
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NOME TEXT NOT NULL, 
        CPF TEXT NOT NULL, 
        DATA_NASCIMENTO TEXT NOT NULL, 
        ENDERECO TEXT NOT NULL) ;"""

    cur.execute(query)


if __name__ == "__main__":

    conn = None
    
    try:

        config = dotenv_values('.env.ambient')

        path_db = config.get("PATH_DATABASE") or ""

        if path_db == "":
            raise Exception("PATH_DATABASE não identificado")

        conn = sqlite3.connect(path_db)

        cur = conn.cursor()

        create_table(cur)

        patients = [['José Carlos', '987.654.321-00', '20/10/1990', 'Av. Paulista, São Paulo'],
                     ['Jessica Santana', '123.456.789-12', '12/12/1999', 'Av. Brigadeiro, São Paulo']]

        cadastro, = patient_use_case(patient_repository(cur))

        cadastro(patients[0])

        cadastro(patients[1])

        conn.commit()

    except Exception as e:
        
        if conn:
            conn.rollback()

        print("ERRO>>", e)
    
    finally:
        
        if conn:
            conn.close()
