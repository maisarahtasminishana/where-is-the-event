from tkinter import*
window=Tk()
window.geometry("200x200")
window.resizable(width=False,height=False)
def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
frm_entry=Frame(window)
ent_temperature = Entry(master=frm_entry,width=10)
lbl_temp =Label(master=frm_entry,text="\N{DEGREE FAHRENHEIT}")
ent_temperature.grid(row=0,column=0,sticky="e")
lbl_temp.grid(row=0,column=1,sticky="w")
btn = Button(window,text="-->",command=fahrenheit_to_celsius)
lbl_result=Label(window,text="\N{DEGREE CELSIUS}")
frm_entry.grid(row=0, column=0, padx=10)
btn.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
window.mainloop()
