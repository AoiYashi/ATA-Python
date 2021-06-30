__author__ = 'adolezik'


from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self)
        filemenu = Menu(menubar)
        filemenu.add_command(label="Submit the file", command=self.process)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_command(label="Quit", command=window.quit)
        self.label1 = Label(self, text="Path of the file that you want to proceed:")
        self.label1.grid(row=0, columnspan=3, sticky=S)
        self.entry1 = Entry(self, width=50)
        self.entry1.grid(row=1, column=1)
        self.entry1.focus()
        self.button1 = Button(self, text="submit", command=self.process)
        self.button1.grid(row=1, column=2)
        self.label2 = Label(self, width=60)
        self.label2.grid(row=3, columnspan=3, sticky=S)
        self.button2 = Button(self, text="reset", command=self.reset)
        self.button2.grid(row=1, column=3, padx=10, pady=10)
        self.button3 = Button(self, text="yes", command=self.confirmation)
        self.button3.grid(row=1, column=4)
        window.config(menu=menubar)

    def process(self):
       if self.entry1.get() == "C:\\Users\Administrator\Desktop\dhcp.csv":
            path = self.entry1.get()
            self.path = path
            output1 = ("C:\\Users\Administrator\Desktop\dhcp.csv - is that correct?")
            self.label1['text'] = output1
       else:
           output2 = ("Incorrect assignment")
           self.label2['text'] = output2

    def reset(self):
        self.entry1.delete(0, END)

    def confirmation(self):
        app.quit()


window = Tk()
window.title("File Chooser")
window.geometry("700x80")
app = Application(window)
app.mainloop()