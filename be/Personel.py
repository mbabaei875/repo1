from sqlalchemy import create_engine,Column,String,TEXT,Integer,ForeignKey,select,join,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker,relationship,declarative_base
from datetime import datetime


engen = create_engine("sqlite:///inventory2.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engen)
session = Session()

##############################################################################
class personel(Base):
    __tablename__="personel"
    id=Column(Integer,primary_key=True)
    per_name=Column(String)
    per_family=Column(String)
    per_num = Column(Integer)
    per_shift = Column(String)

    product = relationship("product", back_populates="personel")
    def __init__(self,name="",family="", shift="", num=""):
        self.per_name=name
        self.per_family=family
        self.per_shift=shift
        self.per_num = num

#############################################################################
class product (Base):
    __tablename__="product"
    id=Column(Integer,primary_key=True)
    pro_name=Column(String)
    pro_numbuy= Column(Integer)
    pro_numExit= Column(Integer)
    pro_price= Column(Integer)
    pro_date = Column(String)

    per_id = Column(Integer, ForeignKey("personel.id"))
    personel = relationship("personel", back_populates="product")

    def __init__(self,name="", numbuy="", numExit="" , price="", IdOwner=""):
        self.pro_name =name
        self.pro_numbuy = numbuy
        self.pro_numExit = numExit
        self.pro_price = price
        self.per_id= IdOwner
        self.pro_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#############################################################################

class total (Base):
    __tablename__ = "total"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    num_purchase = Column(Integer)
    num_sales = Column(Integer)
    num_Tot= Column(Integer)

    def __init__(self, name="", num_purchase="", num_sales=""):
        self.name = name
        self.num_purchase = num_purchase
        self.num_sales = num_sales
        self.num_Tot = num_purchase - num_sales

Base.metadata.create_all(engen)       #

