import tkinter
from tkinter import messagebox
import os,sys
import mysql.connector as ms
import customtkinter as c
from CTkTable import *
from CTkXYFrame import *
dbs_list=list("1234567")

c.set_default_color_theme("dark-blue")
c.set_appearance_mode("dark")
user_db_check=False



prev_commands_list=[]

tracker=0


popularsqlcodes=["create database if not exists db_name",
"show databases",
"drop database db_name",
"create table if not exists tb_name (col_name datatype tab_constraint,col_name datatype tab_constraint)",
"desc tb_name",
"show tables",
"alter table tb_name add col_name datatype,add col_name datatype",
"alter table tb_name modify col_name datatype",
"alter table tb_name drop column col_name",
"alter table tb_name add constraint_name(col_name)",
"alter table tb_name drop constraint_name",
"drop table tb_name",
"insert into tb_name (col1,col2) values (v1,v2)",
"insert into tb_name values (v1,v2)",
"update tb_name set col_name=new_val ,col_name=new_val where condi",
"delete from tb_name where condi",
"select * from tb_name",
"select * from tb_name where condition group by col_name having condition order by col_name asc|desc",
"select col_name as alias_col_name from tb_name" ,
"select * from tb_name where col_name=value",
"select * from tb_name where col_name like '%value%'",
"select * from tb_name where col_name like '__value%'",
"select * from tb_name where col_name is null",
"select * from tb_name where col_name is not null",
"select * from tb_name where col_name in (v1,v2,v3,v4)",
"select * from tb_name where condi1 and condi2",
"select count(col_name|*) as alias_name from tb_name where condi",
"select count(distinct col_name) as alias_name from tb_name",
"select sum(col_name) from tb_name",
"select min(col_name) from tb_name",
"select max(col_name) from tb_name",
"select avg(col_name) from tb_name",
"select col_name from tb1_name join tb2_name on tb1_name.col_name=tb2_name.col_name where condi",
"select * from tb1_name cross join tb2_name",
"select t1.col_name from tb1_name as t1 inner join tb2_name as t2 on t1.col_name=tb2.col_name",
"select * from tb1_name natural join tb2_name"]





class User:
    def __init__(self, name="root", password="", host="localhost", charset="utf8", database=""):
        self.database = database
        self.db = ms.connect(user=name, password=password, host=host, charset=charset, database=database)

    def execute(self, command):
        try:
            cur = self.db.cursor()
            cur.execute(command)
            data = cur.fetchall()
            try:
                col_name=[i[0] for i in cur.description]
                data.insert(0,col_name)
            except:
                pass
            cur.close()
            self.db.commit()
            return {"status":True,"data":data}


        except Exception as e:
            return {"status":False,"data":e}

    @staticmethod
    def find_dbs(name="root", password="", host="localhost", charset="utf8"):
        try:
            db = ms.connect(user=name, password=password, host=host, charset=charset)
            cur=db.cursor()
            cur.execute("show databases")
            return {"status":True,"data":cur.fetchall()}
        except Exception as e:
            return {"status":False,"data":str(e)}

    @staticmethod
    def create_new(name="root", password="", host="localhost", charset="utf8",database=""):
        try:
            db = ms.connect(user=name, password=password, host=host, charset=charset)
            cur = db.cursor()
            cur.execute(f"create database {database}")
            return {"status": True, "data": cur.fetchall()}
        except Exception as e:
            return {"status": False, "data": str(e)}


    def test(self):
        return self.db









def run_mi_code(haha=""):
    if user_db_check:
        data=user_db.execute(com.get("0.0","end"))
        if data["status"]:
            global tracker
            tracker=0
            prev_commands_list.append(com.get("0.0","end"))
            prev_commands.configure(values=prev_commands_list)
            print(data["data"])
            if len(data["data"])!=0:
                table.configure(values=data["data"],rows=len(data["data"]),columns=len(data["data"][0]))
            else:
                table.configure(values=[["it worked but cant display it sorry for the inconvenience"]],rows=1,columns=1)


        else:
            messagebox.showerror(title="error", message=data["data"])



    else:
        messagebox.showerror(title="error",message="connect to a database or create new one")






def resource_path(relative_path):
#""" Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)



class App(c.CTk):
    def __init__(self):
        super().__init__(fg_color = "#252933")

        self.bind("<Control-q>", run_mi_code)
        self.title("buy me coffee (strong preferred)")
        self.iconbitmap(resource_path("batman.ico"))

        self.geometry('1920x1080')
        c.CTkLabel(self,text="jiduk.me /// github.com/jidukrishna // insta:jidukrishnapj").pack()
        usernamesetting(self)
        Result_frame(self)
        prompt(self)


        def prev_com_add(k):
            com.delete("0.0","end")
            com.insert("0.0",justavalue.get())


        def up(k):
            global tracker

            if tracker*-1==len(prev_commands_list):
                return
            else:

                tracker -= 1
                print(tracker)
                com.delete("0.0","end")
                com.insert("0.0",prev_commands_list[tracker])

        def down(k):
            global tracker

            if tracker ==-1:
                return
            else:
                tracker += 1
                print(tracker)
                com.delete("0.0", "end")
                com.insert("0.0", prev_commands_list[tracker])




        self.bind("<Shift-Up>",up )
        self.bind("<Shift-Down>",down )

        def pop_add(k):
            com.delete("0.0", "end")
            com.insert("0.0", popv.get())


        global prev_commands
        justavalue=tkinter.StringVar()
        justavalue.set("prev commands")
        popv = tkinter.StringVar()
        popv.set("popular commands")
        prev_commands=c.CTkOptionMenu(self,values=prev_commands_list,variable=justavalue,command=prev_com_add,fg_color="#233b7a",button_color="#233b7a")
        prev_commands.pack(side="left",ipady=5,padx=(15))
        popular = c.CTkOptionMenu(self, values=popularsqlcodes, variable=popv, command=pop_add,fg_color="#233b7a",button_color="#233b7a")
        popular.pack(side="left", ipady=5, padx=(60))

        self.mainloop()




class usernamesetting(c.CTkFrame):
    def __init__(self,win):
        super().__init__(win,fg_color = "#252933")

        username_db = tkinter.StringVar()
        username_db.set("root")
        password_db = tkinter.StringVar()
        password_db.set('""')
        charset_db = tkinter.StringVar()
        charset_db.set("utf8")
        host_db = tkinter.StringVar()
        host_db.set("localhost")
        database_db = tkinter.StringVar()
        database_db.set("select db")

        def get_db_list():
            global dbs_list,db_w
            print(username_db.get(),password_db.get(),host_db.get(),charset_db.get())
            stat=User.find_dbs(username_db.get(),password_db.get(),host_db.get(),charset_db.get())
            if not stat["status"]:
                messagebox.showerror(title="Error",message=stat["data"])
                return
            else:
                values=stat["data"]
                if len(values)==0:
                    messagebox.showerror(title="Error",message="database kuch be nahi hae")
                    return
                else:

                    dbs_list=[i[0] for i in values]
                    messagebox.showinfo(title="success",message="found dbs click on select db option to proceed")
                    choose_db.configure(values=dbs_list)



        def create_new_one():

            if name_of_database.get()=="":return
            ask=messagebox.askyesno(title="u sure",message=f"new db called {name_of_database.get()} will be created")
            if not ask:
                return
            global dbs_list, db_w
            stat = User.create_new(username_db.get(),password_db.get(),host_db.get(),charset_db.get(),name_of_database.get())
            if not stat["status"]:
                messagebox.showerror(title="Error", message=stat["data"])
                return
            else:

                messagebox.showinfo(title="success", message="successfully created new dbs . select db option to proceed")





        def connectkarona():
            try:
                global user_db,user_db_check
                user_db=User(username_db.get(),password_db.get(),host_db.get(),
                   charset_db.get(),choose_db.get())
                messagebox.showinfo(title="success",message=f"connected to {choose_db.get()}")
                user_db_check = True

            except:
                messagebox.showerror(title="error",message="check everything properly")






        user=c.CTkLabel(self,text="user:")
        user.grid(column=0,row=0)
        user_entry=c.CTkEntry(self,textvariable=username_db)
        user_entry.grid(column=1,row=0)

        password = c.CTkLabel(self, text="password:")
        password.grid(column=0, row=1)
        password_entry = c.CTkEntry(self, textvariable=password_db)
        password_entry.grid(column=1, row=1)



        host = c.CTkLabel(self, text="host:")
        host.grid(column=2,row=1)
        host_entry = c.CTkEntry(self,textvariable=host_db)
        host_entry.grid(column=3,row=1)


        charset = c.CTkLabel(self, text="charset:")
        charset.grid(column=2,row=0)
        charset_entry = c.CTkEntry(self,textvariable=charset_db)
        charset_entry.grid(column=3,row=0)


        c.CTkButton(self,text="find dbs",command=get_db_list,fg_color="#233b7a").grid(column=4,row=0)
        choose_db=c.CTkOptionMenu(self,variable=database_db,values=[],fg_color="#233b7a",button_color="#233b7a")
        choose_db.grid(column=4,row=1)


        name_of_database = c.CTkEntry(self, placeholder_text="enter database name")
        name_of_database.grid(column=6,row=0)


        c.CTkButton(self,text="create new",command=create_new_one,fg_color="#233b7a").grid(column=6,row=1)


        connect=c.CTkButton(self,text="connect",command=connectkarona,fg_color="#233b7a")
        connect.grid(column=7,row=0,rowspan=2,sticky="nsew")

        self.pack()





class prompt(c.CTkFrame):
    def __init__(self,win):

        super().__init__(win)


        global com

        c.CTkButton(self,text="RUN\n(or press ctrl+Q)",height=150,width=150,command=run_mi_code,fg_color="#233b7a").pack(side="right")

        com=c.CTkTextbox(self,height=150,width=1250,font=("calibiri",14))
        com.pack()




        self.pack(pady=15)



class Result_frame(c.CTkFrame):
    def __init__(self,win,resvalues=(("",),)):
        super().__init__(win,height=500,width=1400)
        self.pack_propagate(False)

        res=CTkXYFrame(self)
        res.pack(fill="both",expand="True")
        value = resvalues
        global table
        table = CTkTable(master=res, row=0, column=0, values=value)
        table.grid(column=0,row=0,sticky="nswe",padx=20, pady=20)

        self.pack()


App()
