from pytube import YouTube
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests

tk = Tk()
tk.title("YouTube Mp4 İndirici v0.9.1 | Tkinter - Cyloun")
tk.geometry("390x220")
tk.resizable(0,0)

L3 = Label(tk)
L3.place(x=148,y=200)


def giris():

    if E2.get() == str("mrcylounsunar"):
        try:
            yt = YouTube("{}".format(E1.get()))
        except:
            messagebox.showerror("Hata!","Bİr hata tespit edildi, lütfen linkinizi kontrol ediniz!")
        else:            
            try:
                yuu = yt.streams.filter(progressive="True",res=str(E3.get())).first()
                yuu.download()
            except AttributeError:
                messagebox.showerror("Hata!","Belirtilinen video kalitesi bulunumadı!")
            else:                   
                messagebox.showinfo("Başarılı", "İndirme işlemi tamamlandı!")
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
E2 = Entry(tk,width=25,show="*")
E2.place(x=30,y=140)

try:
 resim = Image.open(requests.get("https://i.imgur.com/FpwHmmL.png", stream = True).raw)
 resim.save("youtube.png")
 resim2 = resim.resize((125,125))
 resim3 = ImageTk.PhotoImage(resim2)
 L4 = Label(tk,image=resim3)
 L4.place(x=250,y=40)
except:
    messagebox.showerror("Hata!","Bağlantı hatası tespit edildi!\nLütfen internetinizi kontrol ediniz!")
    tk.destroy()

bt = Button(tk,text="İndir",padx="20",pady="5",command=giris)
bt.place(x=30,y=170)
tk.mainloop()
