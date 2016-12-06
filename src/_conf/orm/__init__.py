from sqlalchemy import create_engine

class orm:
    def newEng(self):
        engine = create_engine("mysql://scott:tiger@hostname/dbname",encoding='latin1', echo=True)