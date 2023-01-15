

def setupe():
        
    query = """CREATE TABLE EXAMS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                event_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_update DATETIME NULL);"""
