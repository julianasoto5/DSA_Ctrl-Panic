import base64
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class Database(object):
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "wally"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"


    def get_session(self):
        connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
        engine = create_engine(connection)
        connection = engine.connect()
        Session = sessionmaker(bind=engine)        
        session = Session()
        return session

    def get_user_by_id(self, idUser):
        connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
        engine = create_engine(connection)
        connection = engine.connect()
        session = self.get_session()
        sql = "SELECT * FROM acounts WHERE id = '" + (str(idUser)) + "';"
        result=connection.execute(sql).fetchall()
        session.close()
        lista=[]
        for r in result:
            lista.append({'id': r[0], 'username':r[1],'password':r[2],'club':r[3],})
        return lista 
