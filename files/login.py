import subprocess
import tkinter
import customtkinter
from PIL import ImageTk,Image


customtkinter.set_appearance_mode("light") 
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green") 
window= tkinter.Tk()
window.title("login")
window.geometry('600x440')
window.configure(bg='#0066FF')
window.title('Login Page')


#function you can connect database here
def login():
    
    pwd = "elzpxssdtvxyboea"
    unm = "vcontrolproject@gmail.com"
    if entry1.get()==unm and entry2.get()==pwd:
        p1=subprocess.Popen('python sub_mainpage.py', shell=True)
 
    else:
        print("Invalid login")
#backgroung image 
img1=customtkinter.CTkImage(
                            light_image=Image.open("vmail.jpg"),
                            dark_image=Image.open("vmail.jpg"),
                            size=(1300,1000))

l1=customtkinter.CTkButton(master=window,image=img1)


l1.place(relx=0.53, rely=0.5, anchor=tkinter.CENTER)



#creating custom frame
frame=customtkinter.CTkFrame(master=window, 
width=520, height=400, corner_radius=0,fg_color=("#2D2D30"))

frame.place(relx=0.5, rely=0.5, 
anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, 
text="Log into your account",font=('bold',30),text_color=("#ffffff"))

l2.place(x=100, y=45)

entry1=customtkinter.CTkEntry(master=frame, 
width=300, placeholder_text='Username',font=('italic',15))

entry1.place(x=100, y=110)

entry2=customtkinter.CTkEntry(master=frame, 
width=300, placeholder_text='Password', show="*",font=('italic',15))

entry2.place(x=100, y=165)

l3=customtkinter.CTkLabel(master=frame,
text="Forget password?",font=('italic',15),text_color=("#ffffff"))

l3.place(x=100,y=195)

#login button
button1 = customtkinter.CTkButton(master=frame,
width=300, text="Login", corner_radius=6,font=('italic',25), command=login)#what should be done after clicking login
button1.place(x=100, y=240)



window.mainloop()