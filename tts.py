import os
from gtts import gTTS
from tkinter import Tk, Label, Button, Entry, filedialog, Text, Scrollbar, VERTICAL, END
import pdfplumber

def text_to_speech(text, language='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    if os.name == 'nt':
        os.system(f'start {filename}')
    elif os.name == 'posix':
        os.system(f'open {filename}')
    else:
        print("Unsupported OS, please manually play the file.")

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def browse_files():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        text = extract_text_from_pdf(file_path)
        text_entry.delete(1.0, END)
        text_entry.insert(END, text)

def convert_text():
    text = text_entry.get(1.0, END).strip()
    if text:
        text_to_speech(text)
    else:
        print("No text provided.")

# Create the GUI
root = Tk()
root.title("JESAM IS THE BEST")
root.geometry("600x400")
root.configure(bg='#2c3e50')

label = Label(root, text="Enter text or upload a PDF:", bg='#2c3e50', fg='#ecf0f1', font=("Helvetica", 14))
label.pack(pady=10)

text_frame = Text(root, wrap='word', height=10, width=70)
text_frame.pack(pady=10)

scrollbar = Scrollbar(root, orient=VERTICAL, command=text_frame.yview)
scrollbar.pack(side='right', fill='y')
text_frame.config(yscrollcommand=scrollbar.set)

text_entry = Text(text_frame, wrap='word', height=10, width=70, bg='#ecf0f1', fg='#2c3e50', font=("Helvetica", 12))
text_entry.pack()

browse_button = Button(root, text="Browse PDF", command=browse_files, bg='#3498db', fg='#ecf0f1', font=("Helvetica", 12), width=20)
browse_button.pack(pady=5)

convert_button = Button(root, text="Convert to Speech", command=convert_text, bg='#e74c3c', fg='#ecf0f1', font=("Helvetica", 12), width=20)
convert_button.pack(pady=10)

root.mainloop()
