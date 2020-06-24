from controller import *
from main import *
from tkinter import *
from tkinter import filedialog
import os

# main structure of the program
class Application:

    def __init__(self, master):
        self.master = master
        self.directory = ""

        # heading
        self.heading = Label(master, text="File Management", font=("arial 15 bold"))
        self.heading.pack()

        # instructions label
        self.instruction = Label(master, text="Please select the directory to manage", font=("arial 15 bold"))
        self.instruction.place(x=120, y=160)

        # button 
        self.selectBtn = Button(master, text="Open Directory", width=25, height=2, command=self.ask)
        self.selectBtn.place(x=200, y=250)

        # dummy text to change later
        self.dummy = Label(master, text="Current: ", font=("arial 15 italic"))
        self.dummy.place(x=120, y=320)
        self.dummy2 = Label(master, text="", font=("arial 15 italic"), fg="green")
        self.dummy2.place(x=120, y=400)

    # ask method to store location
    def ask(self):
        location = filedialog.askdirectory()
        
        # set the value of directory
        self.directory = location
        self.dummy["text"] = "Current: " + location

        # create execute button
        self.executeBtn = Button(self.master, text="Manage", width=25, height=2, command=self.manage)
        self.executeBtn.place(x=200, y=360)


    # manage function to call from the main method
    def manage(self):
        file_manage(self.directory)
        print("managed")
        self.dummy2["text"] = "Completed"
        # open the file location once done
        os.startfile(self.directory)
root = Tk()
app = Application(root)
root.geometry("600x600+500+100")
root.mainloop()