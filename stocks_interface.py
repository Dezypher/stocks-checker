import tkinter
from tkinter import Label
from tkinter import Frame
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
from tkinter import messagebox

from checker import StockChecker

class StockCheckerInterface():
    stock_checker = StockChecker()
    main_window = tkinter.Tk()
    txtv_stock_price = StringVar()
    txtv_stock_name = StringVar()

    ent_txtv_stock_name = StringVar()
    ent_txtv_interval = StringVar()
    ent_txtv_alert_price = StringVar()
    

    def initialize(self):
        self.txtv_stock_price.set("$ -.----")
        self.txtv_stock_name.set("No stock selected")

        self.ent_txtv_stock_name.set("")
        self.ent_txtv_interval.set("60")
        self.ent_txtv_alert_price.set("100.0")

        self.header()
        self.configs()
        self.main_window.title("Stock Checker")
        self.main_window.geometry('360x420')
        self.main_window.protocol("WM_DELETE_WINDOW", self.close_application)
        self.main_window.mainloop()
    
    def header(self):
        self.lbl_stock_price = Label(self.main_window, textvariable=self.txtv_stock_price, font=("Calibri Bold", 24), pady=10)
        self.lbl_stock_price.pack()
        lbl_stock_name = Label(self.main_window, textvariable=self.txtv_stock_name, font=("Calibri", 16), pady=-4)
        lbl_stock_name.pack()

    def configs(self):
        lbl_divider = Label(self.main_window, text="------------------------------------------", pady=2)
        lbl_divider.pack()

        lbl_stock_name = Label(self.main_window, text="Stock Name", pady=16)
        lbl_stock_name.pack()
        self.ent_stock_name = Entry(self.main_window, textvariable=self.ent_txtv_stock_name, width=10)
        self.ent_stock_name.pack()

        lbl_interval = Label(self.main_window, text="Interval (in seconds)", pady=16)
        lbl_interval.pack()
        self.ent_interval = Entry(self.main_window, textvariable=self.ent_txtv_interval, width=10)
        self.ent_interval.pack()
        
        lbl_alert_price = Label(self.main_window, text="Alert Price (USD)", pady=16)
        lbl_alert_price.pack()
        self.ent_alert_price = Entry(self.main_window, textvariable=self.ent_txtv_alert_price, width=10)
        self.ent_alert_price.pack()

        self.btn_apply = Button(self.main_window, text="Apply", command=self.apply_configs)
        self.btn_apply.pack()

    def apply_configs(self):
        self.stock_checker.stop_process()
        self.stock_checker = StockChecker(
            stock_ticker_name=self.ent_txtv_stock_name.get(),
            interval=int(self.ent_txtv_interval.get()),
            alert_price=float(self.ent_txtv_alert_price.get()),
            interface=self
        )
        self.stock_checker.start_process()
        self.txtv_stock_name.set(str(self.ent_stock_name.get()))
    
    def update_labels(self, current_price):
        str_price = str(round(current_price, 4))
        self.txtv_stock_price.set(str(str_price))

        if self.stock_checker.alarmed:
            self.txtv_stock_price.set(str(str_price) + " (" + str(self.stock_checker.alert_price) + " REACHED)")
            messagebox.showwarning(title="Alert", message="Price has been reached!")
            self.stock_checker.stop_process()

    def close_application(self):
        self.stock_checker.stop_process()
        self.main_window.destroy()


if __name__ == "__main__":
    StockCheckerInterface().initialize()
