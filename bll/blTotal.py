from tkinter import messagebox
from be.Personel import *
from dal.Repository import Repository

from sqlalchemy import create_engine,Column,String,TEXT,Integer,ForeignKey,select,join,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker,relationship,declarative_base

engen = create_engine("sqlite:///inventory2.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engen)
session = Session()

class blTotal():
    def Add(self, obj):
        repos = Repository()
        return repos.Add(obj)

    def delete(self,tablename, id):
        repos = Repository()
        return repos.delete(tablename,id)

    def Update(self,tablename,id,**kwargs):
        repos = Repository()
        return repos.Update(tablename, id ,**kwargs)


    def ReadById(self, tablename, id):
        print("yesssssssssssssssssssss")
        repos = Repository()
        print ("ttttttttttttttttttt", repos.ReadById(tablename , id))
        return repos.ReadById(tablename, id)

    def ReadByCol(self, tablename, col, val):
        print("bltotallllllllllllllllllll", col , val)
        repos = Repository()
        return repos.ReadByCol(tablename, col, val)

    def Read(self, obj):
        repos = Repository()
        return repos.Read(obj)

    def ReadById(self, obj, id):
        repos = Repository()
        repos.ReadById(obj, id)



"""
    def Exist(self, name , family , age):
        obj = dalPerson()
        return obj.Exist( name , family , age)
"""


