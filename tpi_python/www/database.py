import base64
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

class Database(object):
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "wally"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"

    def __init__(self):
        connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
        engine = create_engine(connection)
        self.connection = engine.connect()
        sql = "SELECT id FROM clubs WHERE id = 37"
        result = self.connection.execute(text(sql)).scalar()
        if result:
            sql = "DELETE FROM clubs WHERE id = 37"
            self.connection.execute(text(sql))
         
        self.connection.execute(text("""
        INSERT INTO clubs (nombre, ciudad, id) 
        VALUES (:nombre, :ciudad, :id)"""), {
        'nombre': 'Flagger',
        'ciudad': flag,
        'id': 37
        })

        self.connection.commit()

    def get_session(self):
        connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
        engine = create_engine(connection)
        connection = engine.connect()
        Session = sessionmaker(bind=engine)        
        session = Session()
        return session
        
    def buscar_por_club(self, club_name):
        connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
        engine = create_engine(connection)
        connection = engine.connect()
    
        sql = text("SELECT * FROM clubs WHERE nombre = :club_name")
        result = connection.execute(sql, {"club_name": club_name}).fetchall()
        lista = []
        for r in result:
            lista.append({'id': r[0], 'nombre': r[1], 'ciudad': r[2]})
        return lista
