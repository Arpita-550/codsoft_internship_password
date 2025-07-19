import tkinter as tk
import secrets
import string

class CustomPasswordApp:
    def __init__(self, window):
        self.window = window
        self.window.title("My Password Tool")
        self.window.geometry("420x320")
        self.window.configure(bg= "#f0dede")

        title = tk.Label(window, text= "Password Generator App", font=("Times New Roman", 18, "bold"), bg= "#ffffff", fg= "#333333")
        title.pack(pady=12)

        frame = tk.Frame(window, bg= "#7B2626")
        frame.pack()

        tk.Label(frame, text= "Password Length", font=("Times New Roman",12), bg= "#ffffff").grid(row=0,column=0,padx=6)
        self.length_field = tk.Entry(frame, font=("Times New Roman",12), width=6,justify="center")
        self.length_field.grid(row=0,column=1)
        self.length_field.insert(0,"10")


        self.opt_small = tk.BooleanVar(value=True)
        self.opt_caps = tk.BooleanVar(value=True)
        self.opt_num = tk.BooleanVar(value=True)
        self.opt_sym = tk.BooleanVar(value=True)

        options = tk.Frame(window, bg= "#DFD5D5")
        options.pack(pady=10)

        tk.Checkbutton(options, text="Lowercase(a-z)", variable=self.opt_small, bg= "#9ed081",  font=("Times New Roman",12)).grid(row=0, column=0,padx=10)
        tk.Checkbutton(options, text="Uppercase(A-Z)", variable=self.opt_caps, bg= "#9ed081",  font=("Times New Roman",12)).grid(row=0, column=1,padx=10)
        tk.Checkbutton(options, text="Number(0-9)", variable=self.opt_num, bg= "#9ed081",  font=("Times New Roman",12)).grid(row=1, column=0,padx=10)
        tk.Checkbutton(options, text="Symbol(@#$%&)", variable=self.opt_sym, bg= "#9ed081",  font=("Times New Roman",12)).grid(row=1, column=1,padx=10)

        generate_btn = tk.Button(window,text="Generate Password", command=self.make_password,bg= "#d55778", fg="white",font=("Times New Roman",12,"bold"),width=20)
        generate_btn.pack(pady=5)

        self.output = tk.Label(window,text="",bg= "#ffffff", fg="#000000",font=("Times New Roman",14,))
        self.output.pack(pady=5)

    def make_password(self):
        try:
            size = int(self.length_field.get())
            if size < 4:
                raise ValueError
        except:
            self.output.config(text="Invalid length", fg="red")
            return
        pool = ""
        if self.opt_small.get():
            pool += string.ascii_lowercase
        if self.opt_caps.get():
            pool += string.ascii_uppercase
        if self.opt_num.get():
            pool += string.digits
        if self.opt_sym.get():
            pool += "!@#$%^&*"

        if not pool:
            self.output.config(text="Select at least one option", fg="red")
            return
        result = '' .join(secrets.choice(pool) for _ in range(size))
        self.output.config(text=result, fg="red")

        self.window.clipboard_clear()
        self.window.clipboard_append(result)

if __name__ == "__main__":
    win = tk.Tk()
    app = CustomPasswordApp(win)
    win.mainloop()

        





