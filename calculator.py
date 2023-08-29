import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x400")
        self.configure(background="#97FFFF")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.result_label = tk.Label(self, textvariable=self.result_var, font=("Helvetica", 24), anchor="e")
        self.result_label.pack(fill=tk.BOTH, padx=10, pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row, col = 0, 0
        for button_text in buttons:
            tk.Button(button_frame, text=button_text,bg="#ADD8E6",fg="#1A1A1A",font=("Helvetica", 16), width=5, height=2,
                      command=lambda text=button_text: self.on_button_click(text)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, text):
        if text == 'C':
            self.result_var.set('')
        elif text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except Exception:
                self.result_var.set('Error')
        else:
            self.result_var.set(self.result_var.get() + text)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
