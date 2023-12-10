import tkinter as tk 
import pyperclip
def leet_translate(text):
          leet_dict = { # leet keyword dictionary
                    'a': '4',
                    'b': '8', 
                    'c': '(',
                    'd': '|)',
                    'e': '3',
                    'f': '|=',
                    'g': '6',
                    'h': '|-|',
                    'i': '1',
                    'j': '_|',
                    'k': '|<',
                    'l': '|_',
                    'm': '|\/|',
                    'n': '|\|',
                    'o': '0',
                    'p': '|>',
                    'q': '(_,)',
                    'r': '|2',
                    's': '5',
                    't': '7',
                    'u': '|_|',
                    'v': '\/',
                    'w': '\/\/',
                    'x': '><',
                    'y': '`/',
                    'z': '2'
          }
          translated_text = ''
          for char in text:
                    if char.lower() in leet_dict:
                              translated_text += leet_dict[char.lower()]
                    else:
                              translated_text += char
          return translated_text

def translate_text():
          input_text = input_entry.get()
          translated_text = leet_translate(input_text)
          output_label.config(text="Leet Text " + translated_text)
          copy_button.config(state=tk.NORMAL)  # Enable the copy button

def copy_text():
          translated_text = output_label.cget("text").split(": ")[1]
          pyperclip.copy(translated_text)

# Create GUI
window = tk.Tk()
window.title("1337 Translator")

# Input text and entry
input_label = tk.Label(window, text="Text:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

# Translate button
translate_button = tk.Button(window, text="Translate", command=translate_text)
translate_button.pack()

# Output
output_label = tk.Label(window, text="")
output_label.pack()

# Copy button
copy_button = tk.Button(window, text="Copy", command=copy_text, state=tk.DISABLED)
copy_button.pack()

# Start GUI loop
window.mainloop()
