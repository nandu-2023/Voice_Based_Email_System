import tkinter
import customtkinter
from PIL import ImageTk,Image


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...

        img1=customtkinter.CTkImage(
                                    light_image=Image.open("mail.jpg"),
                                    dark_image=Image.open("mail.jpg"),
                                    size=(1300,1000))

        self.l1=customtkinter.CTkButton(master=self,image=img1)


        self.l1.place(relx=0.53, rely=0.5, anchor=tkinter.CENTER)
        text_var = tkinter.StringVar(value="आवाज नियंत्रित ईमेल सेवा")
        self.label = customtkinter.CTkLabel(master=self,
                               textvariable=text_var,
                               width=800,
                               height=55,
                               font=("Helvatical bold",40),
                               text_color=("white"),
                               fg_color=("#2D2D30"),
                               corner_radius=8)
        self.label.grid(row=0, column=0, padx=20)
        self.label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        button = customtkinter.CTkButton(master=self,
                                 width=240,
                                 height=150,
                                 border_width=0,
                                 corner_radius=8,
                                 text="लिखें " ,
                                 fg_color=("#2D2D30")
                                 )


        button.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

        button = customtkinter.CTkButton(master=self,
                                        width=240,
                                        height=150,
                                        border_width=0,
                                        corner_radius=8,
                                        text="इनबॉक्स",
                                        fg_color=("#2D2D30")
                                        )


        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button = customtkinter.CTkButton(master=self,
                                        width=240,
                                        height=150,
                                        border_width=0,
                                        corner_radius=8,
                                        text="बाहर निकलना",
                                        fg_color=("#2D2D30")
                                        )


        button.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1360x768")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
       


app = App()
app.title = "आवाज नियंत्रित ईमेल सेवा"
app.mainloop()