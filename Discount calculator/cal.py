import tkinter as tk

#basic window GUI
window = tk.Tk()
window.geometry("400x400")
window.title("Discount Calculator")


#input original Price
tk.Label(window, text="Original Price:").pack(pady=5)
ori= tk.Entry(window)
ori.pack(pady=5)

#input discount rate
tk.Label(window, text="Discount rate: ").pack(pady=5)
dr= tk.Entry(window)
dr.pack(pady=5)

#button & calculation
def calculation():
    try:
        ori_val=float(ori.get())
        dr_val=float(dr.get())
        
        discount = ori_val * (dr_val / 100)
        final = ori_val - discount
        result.config(text=f"Final Price: Rp.{final: .2f}")
    except ValueError:
        result.config(text="Please enter valid numbers")

b1 = tk.Button(window, text="Calculate", command=calculation)
b1.pack(pady=20)

#show result
result = tk.Label(window, text="Final Price: Rp.")
result.pack()

window.mainloop()