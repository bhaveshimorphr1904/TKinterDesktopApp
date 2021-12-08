from tkinter import *
from employee import *


# Generate manage employee window
def main():
    window = Tk()
    app = EmployeeApp(window)
    window.mainloop()


if __name__ == '__main__':
    main()
