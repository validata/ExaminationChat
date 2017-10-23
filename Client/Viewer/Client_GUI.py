from tkinter import*

class Client(Frame):


    def __init__(self,parent):

        Frame.__init__(self,parent)

        self.parent = parent
        self.pack()
        self.widget()



        self.label_1= Label ( self, text="DISPLAY: " )
        self.label_2 = Label ( self, text="Write your message here to clients: " )

        self.button_1 = Button ( self, text="Send", background = "GREEN" )
        self.button_2 = Button ( self, text="close", background="white", command =close_func )


        self.entry1 = Entry( self, width = 50)
        self.entry2 = Entry ( self, width = 40 )


        self.label_1.grid ( row=0, sticky=W )
        self.label_2.grid ( row=40, sticky=W )

        self.entry1.grid ( row=0, column= 2)
        self.entry2.grid ( row=40, column= 2 )

        self.button_1.grid ( row=40, column=3 )
        self.button_2.grid(row= 60, column =2)

        self.pack()

    def widget(self):

        self.winfo_toplevel().title("Client CHAT")

def close_func():
    root.destroy ()


root = Tk ()
root.geometry("800x340")
window = Client(root)
root.mainloop()