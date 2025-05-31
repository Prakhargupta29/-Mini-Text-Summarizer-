import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from collections import Counter
import string
import re

def preprocess_text(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    stop_words = set([
        'the', 'is', 'in', 'it', 'of', 'and', 'a', 'to', 'with', 'that', 'on', 'as', 'are', 'this',
        'an', 'for', 'by', 'was', 'be', 'has', 'at', 'or', 'from', 'but', 'have', 'not'
    ])
    filtered_words = [word for word in words if word not in stop_words]
    return sentences, filtered_words

def score_sentences(sentences, word_freq):
    sentence_scores = {}
    for sentence in sentences:
        words = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split()
        score = sum(word_freq[word] for word in words if word in word_freq)
        sentence_scores[sentence] = score
    return sentence_scores

def get_summary(sentences, sentence_scores, top_n=2):
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    top_sentences = sorted(sorted_sentences[:top_n], key=sentences.index)
    return top_sentences

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        input_text.delete('1.0', tk.END)
        input_text.insert(tk.END, content)

def summarize_text():
    text = input_text.get('1.0', tk.END).strip()
    if not text:
        messagebox.showwarning("Empty", "Please load or enter text first.")
        return

    try:
        top_n = int(summary_length.get())
    except ValueError:
        messagebox.showwarning("Invalid", "Enter a number for summary length.")
        return

    sentences, filtered_words = preprocess_text(text)
    word_freq = Counter(filtered_words)
    sentence_scores = score_sentences(sentences, word_freq)
    summary = get_summary(sentences, sentence_scores, top_n)

    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, '\n'.join(summary))

def save_summary():
    summary = output_text.get('1.0', tk.END).strip()
    if not summary:
        messagebox.showinfo("Nothing to Save", "Generate a summary first.")
        return
    with open("summary.txt", "w", encoding='utf-8') as f:
        f.write(summary)
    messagebox.showinfo("Saved", "Summary saved to summary.txt")

def draw_gradient(canvas, width, height, r1, g1, b1, r2, g2, b2):
    steps = 100
    for i in range(steps):
        r = int(r1 + (r2 - r1) * i / steps)
        g = int(g1 + (g2 - g1) * i / steps)
        b = int(b1 + (b2 - b1) * i / steps)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_rectangle(0, i * (height/steps), width, (i+1)*(height/steps), outline="", fill=color)

root = tk.Tk()
root.title("📝 Mini Text Summarizer")
root.geometry("850x600")

canvas = tk.Canvas(root, width=850, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)
draw_gradient(canvas, 850, 600, 0, 190, 255, 255, 105, 180)  # gradient from #00beff to #ffb4b4

# Choose a bg color matching gradient start (RGB 0,190,255 = #00beff)
gradient_start_color = '#00beff'

main_frame = tk.Frame(root, bg=gradient_start_color)
canvas.create_window(425, 300, window=main_frame, width=840, height=580)

label_title = tk.Label(main_frame, text="Mini Text Summarizer", font=('Helvetica', 20, 'bold'), bg=gradient_start_color)
label_title.pack(pady=(10, 15))

control_frame = tk.Frame(main_frame, bg=gradient_start_color)
control_frame.pack(pady=10)

btn_open = tk.Button(control_frame, text="📂 Open Text File", command=load_file, font=('Arial', 12, 'bold'), bg="#ffcccb", fg="black")
label_num = tk.Label(control_frame, text="Number of Summary Sentences:", font=('Arial', 12), bg=gradient_start_color)
summary_length = tk.Entry(control_frame, width=5, font=('Arial', 12))
summary_length.insert(0, "2")
btn_summarize = tk.Button(control_frame, text="🧠 Summarize", command=summarize_text, font=('Arial', 12, 'bold'), bg="#c5e1a5", fg="black")
btn_save = tk.Button(control_frame, text="💾 Save Summary", command=save_summary, font=('Arial', 12, 'bold'), bg="#ffcc80", fg="black")

btn_open.grid(row=0, column=0, padx=10, pady=10)
label_num.grid(row=0, column=1, padx=5)
summary_length.grid(row=0, column=2)
btn_summarize.grid(row=0, column=3, padx=10)
btn_save.grid(row=0, column=4, padx=10)

input_section = tk.Frame(main_frame, bg=gradient_start_color)
input_section.pack(pady=(10, 5), fill='both', expand=True)

label_input = tk.Label(input_section, text="📥 Input Text (Loaded or Entered):", font=('Arial', 13, 'bold'), anchor="w", bg=gradient_start_color)
label_input.pack(anchor="w", padx=10, pady=(0, 2))

input_text = scrolledtext.ScrolledText(input_section, height=10, font=('Arial', 11), wrap=tk.WORD, bg='white')
input_text.pack(fill='both', expand=True, padx=10)

output_section = tk.Frame(main_frame, bg=gradient_start_color)
output_section.pack(pady=(10, 10), fill='both', expand=True)

label_output = tk.Label(output_section, text="📄 Summary Output:", font=('Arial', 13, 'bold'), anchor="w", bg=gradient_start_color)
label_output.pack(anchor="w", padx=10, pady=(0, 2))

output_text = scrolledtext.ScrolledText(output_section, height=8, font=('Arial', 11), wrap=tk.WORD, bg='white')
output_text.pack(fill='both', expand=True, padx=10)

root.mainloop()
