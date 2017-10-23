from tkinter import*

class iden_port(Frame):


    def __init__(self,parent):

        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.widget()

        self.label_1 = Label ( self, text="user:" )
        self.label_2 = Label ( self, text="Password:" )

        self.button_1 = Button ( self, text="Log in" )
        self.button_2 = Button ( self, text="Register" )

        self.entry_1 = Entry ( self )
        self.entry_2 = Entry ( self )


        self.label_1.grid ( row=0, sticky=E )
        self.label_2.grid ( row=1, sticky=E )


        self.entry_1.grid ( row=0, column=1 )
        self.entry_2.grid ( row=1, column=1 )


        self.button_1.grid ( row=2, column=0)
        self.button_2.grid ( row=2, column=2)


        self.pack ()



    def widget(self):
        # don't assume that self.parent is a root window.
        # instead, call `winfo_toplevel to get the root window
        self.winfo_toplevel().title("Client login")



root = Tk ()
root.geometry("200x200")
window = iden_port(root)
root.mainloop()




