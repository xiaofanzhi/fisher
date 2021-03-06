from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy,BaseQuery
from contextlib import contextmanager
# Flask sqlalchemy
from sqlalchemy import Column, SmallInteger, Integer
from datetime import datetime


# db = _SQLAlchemy()

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status']=1
        return super().filter_by(**kwargs)

db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    __abstract__=True
    create_time = Column('create_time',Integer)
    status = Column(SmallInteger,default = 1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())


    def set_attrs(self,arrts_dict):
        for k,v in arrts_dict.items():
            if hasattr(self,k) and k != 'id':
                setattr(self,k,v)


    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None