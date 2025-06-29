import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Text Analyzer")
root.geometry("600x500")
root.configure(bg="blue")

# Create widgets
label = tk.Label(root, text="📝 Enter your text below:", font=("Helvetica", 14))
label.pack(pady=10)

text_input = tk.Text(root, height=15, width=70)
text_input.pack()

result_label = tk.Label(root, text="Result will appear here", font=("Helvetica", 12), justify="left",bg="black")
result_label.pack(pady=20)

def analyze_text():
    # Step 1: Get input
    full_text = text_input.get("1.0", tk.END).strip()

    if full_text == "":
        messagebox.showwarning("Empty Input", "Please enter some text.")
        return

    # Step 2: Process input
    char_count = len(full_text)
    words = full_text.split()
    word_count = len(words)
    line_count = full_text.count('\n') + 1

    # Step 3: Count word frequency manually
    word_freq = {}
    for word in words:
        clean_word = word.lower().strip(".,!?\"'")
        word_freq[clean_word] = word_freq.get(clean_word, 0) + 1

    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    top_5 = sorted_words[:5]

    # Step 4: Show result
    result = f"🅰 Characters: {char_count}\n"
    result += f"🧾 Words: {word_count}\n"
    result += f"📏 Lines: {line_count}\n"
    result += "📊 Top 5 Common Words:\n"
    for word, freq in top_5:
        result += f"   • {word}: {freq}\n"

    result_label.config(text=result)

# Analyze Button
analyze_button = tk.Button(root, text="Analyze Text", command=analyze_text, font=("Helvetica", 12), bg="#4CAF50", fg="white")
analyze_button.pack(pady=10)

# Run GUI loop
root.mainloop()
