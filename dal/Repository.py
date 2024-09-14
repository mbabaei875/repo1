from sqlalchemy import create_engine,Column,String,TEXT,Integer,ForeignKey,select,join,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker,relationship,declarative_base
from be.Personel import personel


engen = create_engine("sqlite:///inventory2.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engen)
session = Session()


class Repository():        # create read update delete # کلاسی که عملیات کراد را روی داده ها انجام میدهد(جدا از کلاس بالا نوشتیم تا برای هر کلاس دیگری قابل استفاده باشد.میشد در همانجا هم آورد)
    def Add(self, obj):      #  Add or insert an object to the table
        try:
            session.add(obj)     # شی یا نمونه ای که ساختیم را به جدول دیتابیس اضافه میکند # Add the user to the database
            session.commit()     # این متد را بعد از هر تراکنش فراخوانی کنید تا تغببرات روی جدول در اسکیولیت اعمال و ذخیره شود.
            return True
        except:
            return False

    def Read(self,tablename):         # اسم جدول یا مدل را میگیرد.
        return session.query(tablename).all()


    def ReadById(self, tablename, idd):
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        return session.query(tablename).filter(tablename.id == idd).first()


    def ReadByCol(self, tablename, col, val):
        print("dallllllllllllllllllllllllllllll", col , val ,getattr(tablename , col))

        return session.query(tablename).filter(getattr(tablename , col) == val).all()



    def Update(self,tablename,id, **kwargs):
        OldObj = self.ReadById(tablename, id)
        print(kwargs.items())
        for key,val in kwargs.items():
            setattr(OldObj,key,val)
        session.commit()
        return True

    def update2(self, obj, id):
        newObj=self.ReadById (obj, id)     # یک سرچی انجام دهیم تا رکوردی که میخواهیم تغییر دهیم را برگرداند
        newObj=obj
        session.commit()                        # تغییرات را سیو میکنیم

    def delete(self,tablename, Id):
        obj = session.query(tablename).filter(tablename.id == Id).all()
        if len(obj) > 0:
            objects = obj[0]
            session.delete(objects)
            session.commit()
            return True

"""
    def Exist(self, name , family , age):
        obj = dalPerson()
        return obj.Exist( name , family , age)
"""