def setup():

    query = """
        CREATE TABLE PATIENTS_EXAMS ( 
            id_patients INTEGER NOT NULL,  
            id_exams    INTEGER NOT NULL,
            FOREIGN KEY(id_patients) REFERENCES PATIENTS(id),
            FOREIGN KEY(id_exams) REFERENCES EXAMS(id));"""
