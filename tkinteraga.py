from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

tk = Tk()
tk.title("YouTube Mp4 İndirici | Tkinter - Cyloun")
tk.geometry("390x220")

L3 = Label(tk)
L3.place(x=148,y=200)

def giris():

    if E2.get() == str("mrcylounsunar"):
        yt = YouTube("{}".format(E1.get()))
        yuu = yt.streams.filter(progressive="True",res=str(E3.get())).first()
        yuu.download()       
        messagebox.showinfo("Başarılı", "Giriş onaylandı!")
    else:
        L3["text"] == ("Hatalı Giriş!")
        messagebox.showerror("Başarısız", "Girişiniz onaylanmadı!")




L1 = Label(tk, text="Link")
L1.place(x=30,y=15)
E1 = Entry(tk,width=25)
E1.place(x=30,y=40)
L3 = Label(tk,text="Video Kalitesi:")
L3.place(x=30,y=65)
E3 = Entry(tk,width=25)
E3.place(x=30,y=90)
L2 = Label(tk, text="Uygulama Şifresi:")
L2.place(x=30,y=115)
E2 = Entry(tk,width=25)
E2.place(x=30,y=140)
resim = Image.open("/home/cyloun/İndirilenler/index.jpeg")
resim2 = resim.resize((125,125))
resim3 = ImageTk.PhotoImage(resim2)
L4 = Label(tk,image=resim3)
L4.place(x=250,y=40)

bt = Button(tk,text="İndir",padx="20",pady="5",command=giris)
bt.place(x=30,y=170)
tk.mainloop()
