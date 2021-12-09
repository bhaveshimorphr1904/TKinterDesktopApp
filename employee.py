from tkinter import *
from employee_backend import *


class EmployeeApp:

    database = EmployeeDB("employee.db") # Initilize the DB

    def __init__(self, window):
        window.wm_title("Employee Book")

        self.lblName = Label(window, text="Name")
        self.lblName.grid(row=0, column=0)

        self.nameText = StringVar()
        self.nameEntry = Entry(window, textvariable=self.nameText)
        self.nameEntry.grid(row=0, column=1)

        self.lblMobile = Label(window, text="Mobile")
        self.lblMobile.grid(row=0, column=2)

        self.mobileText = StringVar()
        self.mobileEntry = Entry(window, textvariable=self.mobileText)
        self.mobileEntry.grid(row=0, column=3)

        self.lblEmail = Label(window, text="Email")
        self.lblEmail.grid(row=1, column=0)

        self.emailText = StringVar()
        self.emailEntry = Entry(window, textvariable=self.emailText)
        self.emailEntry.grid(row=1, column=1)

        self.listBox = Listbox(window, height=6, width=35)
        self.listBox.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.scrollBar = Scrollbar(window)
        self.scrollBar.grid(row=2, column=2, rowspan=6)

        self.listBox.configure(yscrollcommand=self.scrollBar.set)
        self.scrollBar.configure(command=self.listBox.yview)
        self.listBox.bind("<<ListboxSelect>>", self.GetSelectedRow)

        self.btnView = Button(window, text="View All",
                              width=12, command=self.ViewCommand)
        self.btnView.grid(row=2, column=3)

        self.btnSearch = Button(window, text="Search",
                                width=12, command=self.SearchCommand)
        self.btnSearch.grid(row=3, column=3)

        self.btnAdd = Button(window, text="Add", width=12,
                             command=self.AddCommand)
        self.btnAdd.grid(row=4, column=3)

        self.btnUpdate = Button(window, text="Update",
                                width=12, command=self.UpdateCommand)
        self.btnUpdate.grid(row=5, column=3)

        self.btnDelete = Button(window, text="Delete",
                                width=12, command=self.DeleteCommand)
        self.btnDelete.grid(row=6, column=3)

        self.btnClose = Button(window, text="Close", width=12,
                               command=window.destroy)
        self.btnClose.grid(row=7, column=3)

# Start : Command Methods
    def GetSelectedRow(self, event):
        try:
            global selectedRow
            if len(self.listBox.curselection()) > 0:
                index = self.listBox.curselection()[0]
                selectedRow = self.listBox.get(index)

                self.nameEntry.delete(0, END)
                self.nameEntry.insert(END, selectedRow[1])

                self.mobileEntry.delete(0, END)
                self.mobileEntry.insert(END, selectedRow[2])

                self.emailEntry.delete(0, END)
                self.emailEntry.insert(END, selectedRow[3])
        except:
            pass

    def clearControl(self):
        self.nameEntry.delete(0, END)
        self.mobileEntry.delete(0, END)
        self.emailEntry.delete(0, END)

    def ViewCommand(self):
        self.listBox.delete(0, END)

        for row in self.database.view():
            self.listBox.insert(END, row)

        self.clearControl()

    def SearchCommand(self):
        self.listBox.delete(0, END)
        for row in self.database.search(self.nameText.get(), self.mobileText.get(), self.emailText.get()):
            self.listBox.insert(END, row)
        self.clearControl()

    def AddCommand(self):
        self.database.insert(self.nameText.get(), self.mobileText.get(), self.emailText.get())
        self.SearchCommand()

    def UpdateCommand(self):
        self.database.update(
            selectedRow[0], self.nameText.get(), self.mobileText.get(), self.emailText.get())
        self.SearchCommand()

    def DeleteCommand(self):
        self.database.delete(selectedRow[0])
        self.ViewCommand()

# End : Command Methods
