import os
import sys
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector as sqlcon
import creatinguser as cu


class Db:
    def __init__(self, tup):
        c = sqlcon.connect(host='localhost', user='shubham', password='Shubh@m98', database='dds')
        s = c.cursor()
        print('Connected To The Server....')
        s.execute("insert into SIGNUP values (%s, %s, %s)", tup)
        print('Records Inserted Successfully....')
        c.commit()
        s.close()
        c.close()
        print('Disconnected From Server....')
        messagebox.showinfo("New User", "Details saved successfully")
        self.root.destroy()
        obj=cu.User()
        obj.widget()

class SignUp(Db):
    def __init__(self):
        self.root = Tk()
        self.root.title('WELCOME | Sign Up')
        #self.root.iconbitmap("signup.ico")

        app_width = 1200
        app_height = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.x = (screen_width / 2) - (app_width / 2)
        self.y = (screen_height / 2) - (app_height / 2)
        self.cent = f'{app_width}x{app_height}+{int(self.x)}+{int(self.y)}'
        centt = "1140x640+140+40"
        self.root.geometry(centt)

        self.f = Frame(self.root)
        self.f.pack(side=TOP, fill=BOTH)
        self.can = Canvas(self.f, height=700, width=1200, bd=0, highlightthickness=0)
        self.can.pack(fill='both', expand=True)

        self.my1 = Image.open("signup1.jpg")
        self.new1 = self.my1.resize((1200, 700), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(self.new1)

        self.my2 = Image.open("signup2.png")
        self.new2 = self.my2.resize((1060, 560), Image.ANTIALIAS)
        self.bg2 = ImageTk.PhotoImage(self.new2)

        self.my3 = Image.open("signup3.png")
        self.new3 = self.my3.resize((550, 520), Image.ANTIALIAS)
        self.bg3 = ImageTk.PhotoImage(self.new3)

        self.my4 = Image.open("signup4.png")
        self.new4 = self.my4.resize((470, 520), Image.ANTIALIAS)
        self.bg4 = ImageTk.PhotoImage(self.new4)

        self.my5 = Image.open("signup2.png")
        self.new5 = self.my5.resize((720, 460), Image.ANTIALIAS)
        self.bg5 = ImageTk.PhotoImage(self.new5)

        self.my6 = Image.open("signup.png")
        self.new6 = self.my6.resize((200, 200), Image.ANTIALIAS)
        self.bg6 = ImageTk.PhotoImage(self.new6)

        self.can.create_image(0, 0, image=self.bg1, anchor='nw')
        self.can.create_image(70, 70, image=self.bg2, anchor='nw')
        self.can.create_image(90, 90, image=self.bg3, anchor='nw')
        self.can.create_image(640, 90, image=self.bg4, anchor='nw')
        self.can.create_image(360, 120, image=self.bg5, anchor='nw')
        self.can.create_image(125, 220, image=self.bg6, anchor='nw')

    def widget(self):
        self.can.create_text(525, 190, text='Name', font=('Helvetica', 30, 'bold'))

        self.can.create_text(525, 303, text='Email Address', font=('Helvetica', 30, 'bold'))

        self.can.create_text(525, 416, text='Phone No', font=('Helvetica', 30, 'bold'))

        self.can.create_text(225, 450, text='Sign Up', font=('Helvetica', 35, 'bold'))

        self.e1 = Entry(self.root, font=('Helvetica', 25, ), bg='#dbdbdb', width=20, bd=0.5, highlightthickness=0)
        self.e2 = Entry(self.root, font=('Helvetica', 25), bg='#dbdbdb', width=20, bd=0.5, highlightthickness=0)
        self.e3 = Entry(self.root, font=('Helvetica', 25), bg='#dbdbdb', width=20, bd=0.5, highlightthickness=0)

        self.e1_window = self.can.create_window(700, 170, anchor='nw', window=self.e1)
        self.e2_window = self.can.create_window(700, 282, anchor='nw', window=self.e2)
        self.e3_window = self.can.create_window(700, 395, anchor='nw', window=self.e3)

        self.b = Button(self.root, text='Next', width=10, bd=1, bg='#f7b100', font=('Helvetica', 20, 'bold'),
                        activebackground='#dbdbdb', cursor='hand2', command=self.inputs)
        self.b_window = self.can.create_window(630, 500, anchor='nw', window=self.b)

        self.root.mainloop()

    def inputs(self):
        if self.e1.get() == "" or self.e2.get() == "" or self.e3.get() == "":
            messagebox.showerror("Alert!", "All fields are required")
        else:
            data = (self.e1.get(), self.e2.get(), self.e3.get())
        super().__init__(data)
        #ob = Db(data)

#ob = SignUp()
#ob.widget()
