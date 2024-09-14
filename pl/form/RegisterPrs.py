from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from be.Personel import *
from bll.blPersonel import blPersonel
from bll.blProduct import blProduct
from bll.blTotal import blTotal

class App(Frame):
    def __init__(self,screen):
        super().__init__(screen)
        self.master=screen
        self.CreateWidget()
    def CreateWidget(self):

    ############## personel ###########personel##########personel############personel########### personel ##########personel###################
        self.Name = StringVar()
        self.Family = StringVar()
        self.Shift = StringVar()
        self.NumPer = IntVar()
        self.Id = IntVar()

        self.Var = [self.Name, self.Family, self.Shift, self.NumPer, self.Id]

        color= "#7ed49c"
        self.layPers=Frame(self.master,bg=color,width=750,height=500)
        self.layPers.place(x=0,y=0)
        self.btnPer= Button(self.layPers,text="Back", width=3,height=1,bg="#7eba43",fg="#0e0e0e",padx=3, command=self.Openlay1).place(x=5,y=470)


        self.lblName = Label(self.layPers, text="نام" , bg=color).place(x=600,y=30)
        self.txtName = Entry(self.layPers,textvariable=self.Name)
        self.txtName.place(x=450,y=30)

        self.lblFamily = Label(self.layPers, text="نام خانوادگی",bg=color).place(x=600,y=70)
        self.txtFamily = Entry(self.layPers,textvariable=self.Family)
        self.txtFamily.place(x=450,y=70)

        self.lblNumPer = Label(self.layPers, text="شماره پرسونلی",bg=color).place(x=600,y=110)
        self.txtNumPer = Entry(self.layPers,textvariable=self.NumPer)
        self.txtNumPer.place(x=450,y=110)

        self.lblShift = Label(self.layPers, text="شیفت",bg=color).place(x=600,y=150)
        self.comobShift = ttk.Combobox(self.layPers, state="readonly", justify="right", textvariable=self.Shift)  # به جای (txtAge) قرار میگیرد
        self.valuesCombo = ["6-14","14-22","22-6"]
        self.comobShift["value"] = self.valuesCombo
        self.comobShift.current(0)                # پیش فرض یک سنی رو نمایش بده در کادر
        self.comobShift.place(x=450, y=150)

        self.txtId = Entry(self.layPers, textvariable=self.Id)
        self.txtId.place_forget()

        cols = ("c1", "c2", "c3","c4","c5")
        self.tbl = ttk.Treeview(self.layPers, columns=cols, show="headings", height=12)

        self.tbl.column("# 5", anchor=E, width=15)
        self.tbl.heading("# 5", text="Id")

        self.tbl.column("# 4", anchor=E, width=100)
        self.tbl.heading("# 4", text="شماره پرسونلی")

        self.tbl.column("# 3", anchor=E, width=50)
        self.tbl.heading("# 3", text="نام")

        self.tbl.column("# 2", width=70)
        self.tbl.heading("# 2", text="نام خانوادگی")

        self.tbl.column("# 1", width=50)
        self.tbl.heading("# 1", text="شیفت")


        self.tbl.bind("<Button-1>", self.GetSelection)
        self.tbl.place(x=30, y=30)

        # Constructing vertical scrollbar with treeview
        verscrlbar = ttk.Scrollbar(self.layPers, orient="vertical", command=self.tbl.yview)
        # Configuring treeview to use the scrollbar
        self.tbl.configure(xscrollcommand=verscrlbar.set)
        # Calling pack method w.r.to vertical scrollbar# # Place the scrollbar on the right side of the Treeview
        #verscrlbar.pack(side='right', fill='y')


        self.btnSend= Button(self.layPers,text="ثبت", width=3,height=1,bg="#e2a644",fg="#0e0e0e",padx=3,command=self.OnclickSave).place(x=450,y=180)

        self.btnDelete= Button(self.layPers,text="حذف", width=3,height=1,bg="#e2a644",fg="#0e0e0e",padx=3,command=self.Delete)
        #self.btnDelete.place(x=500,y=180)
        self.btnDelete.place_forget()

        self.btnEdit = Button(self.layPers, text="ویرایش",  width=4,height=1,bg="#e2a644",fg="#0e0e0e",padx=3,command=self.EditPer)  #command=self.Edit)
        #self.btnEdit.place(x=550, y=180)
        self.btnEdit.place_forget()

        self.LoadPersonel()
    ############## products ########### products ########## products ############ products ########### products ########## products ###################

        ########################################################## Buy entry
        self.NameBuy = StringVar()
        self.NUmBuy = IntVar()
        self.PerBuy = StringVar()
        self.DateBuy = StringVar()
        self.Price = StringVar()
        self.VarBuy = [self.NameBuy, self.NUmBuy, self.PerBuy, self.DateBuy, self.Price]

        self.layProd=Frame(self.master,bg=color,width=750,height=500)
        self.layProd.place(x=0,y=0)
        self.btnPer= Button(self.layProd,text="Back", width=3,height=1,bg="#7eba43",fg="#0e0e0e",padx=3, command=self.Openlay1).place(x=5,y=470)

        #self.FramBuy = Frame(self.layProd, bg="#50aac1", width=350, height=250)
        #self.FramBuy.place(x=350, y=0)

        #self.FramSell = Frame(self.layProd, bg="#7d87ba", width=350, height=250)
        #self.FramSell.place(x=350, y=250)

        self.lblBuy = Label(self.layProd, text="ورود کالا به انبار", bg="#143f2c" , fg= "white", width=30).place(x=500, y=12)

        self.lblNamePro = Label(self.layProd, text="نام کالا", bg=color).place(x=655, y=50)
        self.txtNamePro = Entry(self.layProd, textvariable=self.NameBuy)
        self.txtNamePro.place(x=520, y=50)

        self.lblNum = Label(self.layProd, text="تعداد", bg=color).place(x=655, y=80)
        self.txtNum = Entry(self.layProd, textvariable=self.NUmBuy)
        self.txtNum.place(x=520, y=80)

        self.lblPersonel = Label(self.layProd, text="متصدی", bg=color).place(x=655, y=110)
        self.txtPersonel = Entry(self.layProd, textvariable=self.PerBuy)
        self.txtPersonel.place(x=520, y=110)

        self.lblPrice = Label(self.layProd, text="قیمت خرید", bg=color).place(x=655, y=140)
        self.txtPrice = Entry(self.layProd, textvariable=self.Price)
        self.txtPrice.place (x=520, y=140)

        #self.lblDateBuy = Label(self.layProd, text="تاریخ خرید", bg=color).place(x=600, y=150)
        self.txtDateBuy = Entry(self.layProd, textvariable=self.DateBuy)
        self.txtDateBuy.place_forget()

    ########################################################## Exit entry

        self.NameExit = StringVar()
        self.NUmExit = IntVar()
        self.PerExit = StringVar()
        self.DateExit = StringVar()
        self.VarExit = [self.NameExit, self.NUmExit, self.PerExit, self.DateExit]

        self.lblExit = Label(self.layProd, text="خروج کالا از انبار", bg="#143f2c", fg="white", width=30).place(x=500, y=260)

        self.lblNameExit = Label(self.layProd, text="نام کالا", bg=color).place(x=655, y=290)
        self.txtNameExit = Entry(self.layProd, textvariable=self.NameExit)
        self.txtNameExit.place(x=520, y=290)

        self.lblNumExit = Label(self.layProd, text="تعداد", bg=color).place(x=655, y=320)
        self.txtNumExit = Entry(self.layProd, textvariable=self.NUmExit)
        self.txtNumExit.place(x=520, y=320)

        self.lblPerExit = Label(self.layProd, text="متصدی", bg=color).place(x=655, y=350)
        self.txtPerExit = Entry(self.layProd, textvariable=self.PerExit)
        self.txtPerExit.place(x=520, y=350)

        # self.lblDateBuy = Label(self.layProd, text="تاریخ خرید", bg=color).place(x=600, y=150)
        self.txtDateBuy = Entry(self.layProd, textvariable=self.DateExit)
        self.txtDateBuy.place_forget()



        self.btnAdd = Button(self.layProd, text="افزودن محصول", width=10, height=1, bg="#e2a644", fg="#0e0e0e", padx=3, command=self.OnclickSavePro).place(x=520, y=170)
        self.btnExit = Button(self.layProd, text="خروج محصول", width=10, height=1, bg="#e2a644", fg="#0e0e0e", padx=3, command=self.OnclickExit).place(x=520, y=380)
        self.btnShow = Button(self.layProd, text="نمایش موجودی کل ", width=14, height=1, bg="#e2a644", fg="#0e0e0e", padx=3, command=self.view_inventory).place(x=180, y=390)

        colspro = ("c1", "c2", "c3", "c4", "c5" , "c6")
        self.tblPro = ttk.Treeview(self.layProd, columns=colspro, show="headings", height=15)

        self.tblPro.column("# 6", anchor=E, width=60)
        self.tblPro.heading("# 6", text="نام کالا")

        self.tblPro.column("# 5", anchor=E, width=125)
        self.tblPro.heading("# 5", text="تاریخ ")

        self.tblPro.column("# 4", anchor=W, width=70)
        self.tblPro.heading("# 4", text="قیمت ")

        self.tblPro.column("# 3", anchor=CENTER , width=72)
        self.tblPro.heading("# 3", text="تعداد ورودی")

        self.tblPro.column("# 2",anchor=CENTER,  width=72)
        self.tblPro.heading("# 2", text="تعداد خروجی")

        self.tblPro.column("# 1",anchor=CENTER, width=45)
        self.tblPro.heading("# 1", text="متصدی")

        #self.tbl.bind("<Button-1>", self.GetSelectionpro)
        self.tblPro.place(x=15, y=50)

        self.LoadProduct()

    ############## first layer ########### first layer########## first layer ############ first layer ########### first layer ####################

        self.layer_1=Frame(self.master,bg="#7ed49c",width=750,height=500)
        self.layer_1.place(x=0,y=0)

        self.btnPer= Button(self.layer_1,text="پرسنل", width=15,height=2,bg="#e2a644",fg="#0e0e0e",padx=3, command=self.OpenlayPers).place(x=300,y=140)
        self.btnPer= Button(self.layer_1,text="کالاها", width=15,height=2,bg="#e2a644",fg="#0e0e0e",padx=3, command=self.OpenlayProd).place(x=300,y=190)

    ######################################### event  #############################################
    def view_inventory(self):     # نماسش کل کالاهای موجود و وارد و خارج شده به انبار

        self.inventory_window = Toplevel(self.layProd)
        self.inventory_window.geometry("%dx%d+%d+%d" % (470, 300, 500, 120))
        self.inventory_window.title("موجودی انبار")

        cols = ("c1", "c2", "c3", "c4")
        self.tblTot = ttk.Treeview(self.inventory_window, columns=cols, show="headings", height=10)

        self.tblTot.column("# 4", anchor=CENTER, width=100)
        self.tblTot.heading("# 4", text="نام کالا")

        self.tblTot.column("# 3", anchor=CENTER, width=100)
        self.tblTot.heading("# 3", text="ورودی")

        self.tblTot.column("# 2", anchor=CENTER ,width=100)
        self.tblTot.heading("# 2", anchor=CENTER , text="خروجی")

        self.tblTot.column("# 1", anchor=CENTER , width=100)
        self.tblTot.heading("# 1", text="موجود در انبار")

        #self.tblTot.bind("<Button-1>", self.GetSelectionpro)
        self.tblTot.place(x=30, y=30)

        self.LoadTotal()

    def LoadTotal(self):
        self.CleanTable(self.tblTot)
        objbltot = blTotal()
        List = objbltot.Read(total)
        for item in List:
            self.tblTot.insert('', "end",values=[item.num_Tot, item.num_sales, item.num_purchase, item.name])

    ######################################### event  #############################################

    def HideLayer_All(self):           # تابعی برای مخفی کردن همه لابه ها
        self.layer_1.place_forget()
        self.layProd.place_forget()
        self.layPers.place_forget()

    def OpenlayPers(self):
        self.HideLayer_All()
        self.layPers.place(x=0, y=0)

    def OpenlayProd(self):
        self.HideLayer_All()
        self.layProd.place(x=0, y=0)

    def Openlay1(self):
        self.HideLayer_All()
        self.layer_1.place(x=0,y=0)

    def CleanTable(self, table):
        print("CHCHCHCHCHCHCH",table.get_children() )
        for item in table.get_children():
            table.delete(item)

######################################### personel events
    #        self.Var = [self.Name, self.Family, self.Shift, self.NumPer, self.Id]
    def OnclickSave(self):
        if self.txtName.get() == "" or self.txtFamily.get() == "" or self.txtNumPer.get() == ():
            messagebox.showerror("خطا", "لطفا کادرها را پر کنید")

        elif not self.txtNumPer.get().isnumeric():
            self.txtNumPer.focus_set()
            messagebox.showerror("خطا", "لطفا شماره پرسونلی را عدد وارد کنید")

        else:
            obj = personel(self.txtName.get(), self.txtFamily.get(), self.comobShift.get(), self.txtNumPer.get())
            #print("the name of object's model: " , obj.__class__.__tablename__)
            #print (obj.per_num)
            #num = obj.per_num
            objblper = blPersonel()
            result = objblper.Add(obj)
            if result:
                messagebox.showinfo("تایید", "ثبت شد")
                self.LoadPersonel()
                self.ClearEntryPer()
            else:
                messagebox.showerror("خطا", "در دیتابیس ذخیره نشد")

    def LoadPersonel(self):
        self.CleanTable(self.tbl)
        objblper = blPersonel()
        List = objblper.Read(personel)
        for item in List:
            self.tbl.insert('', "end", values=[item.per_shift, item.per_family, item.per_name, item.per_num, item.id])

    def GetSelection(self,e):                 # انتخاب یک سطر جدول و نمایش آنها در انتری ها
        self.btnDelete.place(x=500,y=180)
        self.btnEdit.place(x=550,y=180)
        Select=self.tbl.selection()
        #print(Select)
        if Select!=():
            id=self.tbl.item(Select)["values"][4]
            self.Id.set(id)

            num = self.tbl.item(Select)["values"][3]
            self.NumPer.set(num)

            name = self.tbl.item(Select)["values"][2]
            self.Name.set(name)
            #self.Name.set(result.name)

            family = self.tbl.item(Select)["values"][1]
            self.Family.set(family)

            shift = self.tbl.item(Select)["values"][0]
            self.Shift.set(shift)

    def Delete(self):
        r=messagebox.askyesno("توجه",f"آیا از حذف داده اطمینان دارید")
        if r==True:
            objbl=blPersonel()
            result=objbl.delete(personel , self.Id.get())
            if result==True:
                self.LoadPersonel()
                self.ClearEntryPer()
                messagebox.showinfo("حذف","یک پرسونل حذف شد")

    def EditPer(self):            # رویداد دکمه ادیت
        objbl=blPersonel()
        r=objbl.Update(personel, self.Id.get(), per_name = self.Name.get(),
                                                per_family = self.Family.get(),
                                                per_num = self.NumPer.get(),
                                                per_shift = self.Shift.get() )
        if r==True:
            self.LoadPersonel()
            self.ClearEntryPer()
            messagebox.showinfo("ویرایش","با موفقیت ویرایش شد ")

    def ClearEntryPer(self):
        for i in self.Var:
            i.set("")
        self.Shift.set("6-14")
        self.NumPer.set("0")
############################################################################################## product events
    #self.VarBuy = [self.NameBuy, self.NUmBuy, self.PerBuy, self.DateBuy, self.Price]
    # product(id, pro_name ,pro_num, pro_price, per_id ,pro_date)
    # total(name, num_purchase, num_sales , num_Tot)
    def ExsistBuy (self):       # بررسی میشود از محصول خریداری شده قبلا هم داشتیم یا خیر. اگر داشتیم به مقدار آن در جدول کل اضافه میشود و اگر محصول جدبد بود به جدول کل اضافه میشود
        objbltot = blTotal()
        resultName = objbltot.ReadByCol(total , "name" , str(self.NameBuy.get()))
        if len(resultName) == 0:
            messagebox.showinfo("توجه", " محصول جدید است. ")
            obj = total(self.NameBuy.get() , self.NUmBuy.get(), 0 )
            objbltot.Add(obj)
        else:
            newNum=resultName[0].num_purchase + self.NUmBuy.get()
            objbltot.Update(total, resultName[0].id , num_purchase = newNum , num_Tot = newNum - resultName[0].num_sales)
            #messagebox.showinfo("تایید", "اضافه شد")

    def OnclickSavePro(self):
        self.ExsistBuy()

        objblper = blPersonel()
        result = objblper.ReadByCol(personel , "per_num" , self.PerBuy.get())
        if self.NameBuy.get() == "" or self.NUmBuy.get() == "" or self.PerBuy.get() == "" or self.Price.get() == "":
            messagebox.showerror("خطا", "لطفا کادرها را پر کنید")

        # elif not self.NUmBuy.get().isnumeric() or not self.Price.get().isnumeric() :
        #    messagebox.showerror("خطا", "لطفا تعداد و قیمت را عدد وارد کنید")

        elif not self.PerBuy.get().isnumeric():
            messagebox.showerror("خطا", "لطفا شماره پرسونلی را عدد وارد کنید")

        elif len(result) == 0:
            messagebox.showerror("خطا", "شخصی با این شماره پرسونلی وجود ندارد")
        else:
            id_per = result[0].id
            namePersonel = result[0].per_name + "" + result[0].per_family
            print (id_per , namePersonel)
            obj = product(self.NameBuy.get(), self.NUmBuy.get(), "",self.Price.get() , id_per)

            objblpro = blProduct()
            result = objblpro.Add(obj)
            if result:
                messagebox.showinfo("تایید", "ثبت شد")
                self.LoadProduct()
                self.ClearEntryPro()

            else:
                messagebox.showerror("خطا", "در دیتابیس ذخیره نشد")
    # product(id, pro_name ,pro_num, pro_price, per_id ,pro_date)


    def LoadProduct(self):
        self.CleanTable(self.tblPro)
        objblpro = blProduct()
        List = objblpro.Read(product)
        for item in List:
            #id = item.per_id
            #print("itemmmmmmmmmmmmmmmmmmmmmm", item.per_id)
            #objblper = blPersonel()
            #obj = objblper.ReadById(personel,id)
            #print ("idididddddddddddddddddddd",obj)
            #name = obj.per_name
            self.tblPro.insert('', "end",values=[item.per_id, item.pro_numExit, item.pro_numbuy , item.pro_price, item.pro_date, item.pro_name])

    def ClearEntryPro(self):
        #self.VarBuy = [self.NameBuy, self.NUmBuy, self.PerBuy, self.DateBuy , self.Price]
        for i in self.VarBuy:
            print(i)
            i.set("")
        self.NUmBuy.set("0")

#######################################################
    # total(name, num_purchase, num_sales , num_Tot)
    def Exsist (self):       # بررسی میکند که محصول درخواست شده برای خروج از انبار وجود دارد و اگر هست تعداد درخواستی نباید بیشتر از موجودی کل کالا باشد
        objbltot = blTotal()
        resultName = objbltot.ReadByCol(total, "name", str(self.NameExit.get()))
        if len(resultName) == 0:
            messagebox.showerror("خطا", "این کالا وجود ندارد.")

        elif len(resultName) > 0 and self.NUmExit.get() > resultName[0].num_Tot:
            messagebox.showerror("خطا", "مقدار درخواستی بیشتر از موجودی است.")

        else:
            newNum=resultName[0].num_sales + self.NUmExit.get()
            objbltot.Update(total, resultName[0].id , num_sales = newNum , num_Tot = resultName[0].num_purchase - newNum)

    def OnclickExit(self):
       # self.VarExit = [self.NameExit, self.NUmExit, self.PerExit, self.DateExit]

       objblper = blPersonel()
       result = objblper.ReadByCol(personel, "per_num", self.PerExit.get())

       if self.NameExit.get() == "" or self.NUmExit.get() == "" or self.PerExit.get() == "" :
           messagebox.showerror("خطا", "لطفا کادرها را پر کنید")

       elif len(result) == 0:
           messagebox.showerror("خطا", "شخصی با این شماره پرسونلی وجود ندارد")

       else:
           self.Exsist()

           id_per = result[0].id
           namePersonel = result[0].per_name + "" + result[0].per_family
           print(id_per, namePersonel)
           obj = product(self.NameExit.get(), "", self.NUmExit.get(), "", id_per)

           objblpro = blProduct()
           result = objblpro.Add(obj)
           if result:
               messagebox.showinfo("تایید", "ثبت شد")
               self.LoadProduct()
               self.ClearEntryExit()

           else:
               messagebox.showerror("خطا", "در دیتابیس ذخیره نشد")
               # product(id, pro_name ,pro_num, pro_price, per_id ,pro_date)

    def LoadProduct(self):
        self.CleanTable(self.tblPro)
        objblpro = blProduct()
        List = objblpro.Read(product)
        for item in List:
            self.tblPro.insert('', "end",values=[item.per_id, item.pro_numExit, item.pro_numbuy , item.pro_price, item.pro_date, item.pro_name])

    def ClearEntryExit(self):
        for i in self.VarExit:
            print(i)
            i.set("")
        self.NUmBuy.set("0")


