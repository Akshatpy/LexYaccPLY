import tkinter as tk
from tkinter import scrolledtext, font
from lexer import lexer
from parser import parser
def check_syntax():
    data = input_text.get("1.0", tk.END)
    result_label.config(text="")
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")
    if not data.strip():
        result_label.config(text="Please enter some code to check.", fg="#555")
        return
    try:
        parsed = parser.parse(data, lexer=lexer) 
        if parsed is not None:
            result_label.config(text="✅ Accepted", fg="green")
            output_text.config(state="normal")
            output_text.insert(tk.END, str(parsed))
            output_text.config(state="disabled")
        else:
            result_label.config(text="No valid construct found.", fg="#555")

    except SyntaxError as e:
        result_label.config(text=f"❌ {e}", fg="red")
    except Exception as e:
        result_label.config(text=f"An unexpected error occurred: {e}", fg="orange")
window = tk.Tk()
window.title("PLY Syntax Checker (AFLL Assignment)")
window.geometry("600x500")
main_font = font.Font(family="Arial", size=11)
code_font = font.Font(family="Courier New", size=12)
result_font = font.Font(family="Arial", size=12, weight="bold")
text_frame = tk.Frame(window, padx=10, pady=10)
text_frame.pack(fill="both", expand=True)
input_label = tk.Label(text_frame, text="Enter Python Construct:", font=main_font)
input_label.pack(anchor="w")
input_text = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, font=code_font, height=10)
input_text.pack(fill="both", expand=True, pady=(5, 10))
check_button = tk.Button(window, text="Check Syntax", font=main_font, command=check_syntax, bg="#007bff", fg="white")
check_button.pack(pady=5)
result_frame = tk.Frame(window, padx=10, pady=5)
result_frame.pack(fill="both", expand=True)
result_label = tk.Label(result_frame, text="", font=result_font, pady=5)
result_label.pack(anchor="w")
output_label = tk.Label(result_frame, text="Parsed Output (AST):", font=main_font)
output_label.pack(anchor="w", pady=(5,0))
output_text = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, font=code_font, height=5)
output_text.config(state="disabled")
output_text.pack(fill="both", expand=True, pady=(5, 10))
window.mainloop()