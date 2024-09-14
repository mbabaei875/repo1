from tkinter import messagebox
from be.Personel import personel
from dal.Repository import Repository

from sqlalchemy import create_engine,Column,String,TEXT,Integer,ForeignKey,select,join,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker,relationship,declarative_base

engen = create_engine("sqlite:///inventory2.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engen)
session = Session()

class blProduct():

    def Add(self, obj):
        repos = Repository()
        return repos.Add(obj)

    def Read(self, obj):
        repos = Repository()
        return repos.Read(obj)

    def ReadById(self, obj, id):
        repos = Repository()
        repos.ReadById(obj, id)

    def ReadByCol(self, tablename, col, val):
        repos = Repository()
        return repos.ReadByCol(tablename, col, val)

    def update(self, obj, id):
        repos = Repository()
        repos.update(obj, id)

    def delete(self, obj):
        repos = Repository()
        return repos.delete(obj, id)

"""
    def Exist(self, name , family , age):
        obj = dalPerson()
        return obj.Exist( name , family , age)
"""


