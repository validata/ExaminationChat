from tkinter import *


class port_in ( Frame ):
    def __init__(self, parent):
        Frame.__init__ ( self, parent )
        self.parent = parent
        self.pack ()
        self.widget ()

        self.label_1 = Label ( self, text="port number:" )
        self.button_1 = Button ( self, text="start" )

        self.entry_1 = Entry ( self )

        self.label_1.grid ( row=0, sticky=E )

        self.entry_1.grid ( row=0, column=1 )

        self.button_1.grid ( row=1, column=1 )

        self.pack ()

    def widget(self):
        # don't assume that self.parent is a root window.
        # instead, call `winfo_toplevel to get the root window
        self.winfo_toplevel ().title ( "server introduction" )

        def close_func():
            root.destroy ()


root = Tk ()
root.geometry ( "200x200" )
window = port_in ( root )
root.mainloop ()