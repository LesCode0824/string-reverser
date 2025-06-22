import tkinter as tk
from tkinter import ttk

class StringReverser:
    def __init__(self, root):
        self.root = root
        self.root.title("String Reverser")
        self.root.geometry("500x300")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Title label
        title_label = ttk.Label(main_frame, text="String Reverser", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Input label
        input_label = ttk.Label(main_frame, text="Enter a string:")
        input_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        # Input entry
        self.input_entry = ttk.Entry(main_frame, width=50, font=("Arial", 10))
        self.input_entry.grid(row=2, column=0, columnspan=2, pady=(0, 15), sticky="ew")
        self.input_entry.focus()
        
        # Button frame for Reverse and Clear buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        # Reverse button
        reverse_button = ttk.Button(button_frame, text="Reverse", command=self.reverse_string)
        reverse_button.grid(row=0, column=0, padx=(0, 10))
        
        # Clear button
        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_all)
        clear_button.grid(row=0, column=1)
        
        # Result label
        result_label = ttk.Label(main_frame, text="Reversed string:")
        result_label.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        
        # Result display
        self.result_text = tk.Text(main_frame, height=5, width=50, font=("Arial", 10), 
                                  wrap=tk.WORD, state=tk.DISABLED)
        self.result_text.grid(row=5, column=0, columnspan=2, pady=(0, 15), sticky="ew")
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Configure root window grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
    
    def reverse_string(self, event=None):
        """Reverse the input string and display the result"""
        input_text = self.input_entry.get()
        reversed_text = input_text[::-1]
        
        # Update result text
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, reversed_text)
        self.result_text.config(state=tk.DISABLED)
    
    def clear_all(self):
        """Clear both input and result fields"""
        self.input_entry.delete(0, tk.END)
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
        self.input_entry.focus()

def main():
    root = tk.Tk()
    app = StringReverser(root)
    root.mainloop()

if __name__ == "__main__":
    main() 