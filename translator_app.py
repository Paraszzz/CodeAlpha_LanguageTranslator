import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
}

# ---------- Color palette (Light Theme) ----------
BG_DARK = "#f4f4f9"        # main background (light gray)
CARD_BG = "#ffffff"        # white cards
ACCENT = "#6c4ce0"         # purple accent for buttons
ACCENT_HOVER = "#5739c9"   # darker purple when hovered
TEXT_LIGHT = "#1e1e2f"     # dark text color (name is legacy from dark theme, still works fine)
TEXT_MUTED = "#6b6b80"     # muted gray-purple for subtitles

def translate_text():
    text_to_translate = input_box.get()
    source_code = LANGUAGES[source_dropdown.get()]
    target_code = LANGUAGES[target_dropdown.get()]
    translated = GoogleTranslator(source=source_code, target=target_code).translate(text_to_translate)
    result_label.config(text=translated)

def copy_text():
    translated_text = result_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(translated_text)

def on_enter(event):
    event.widget.config(bg=ACCENT_HOVER)

def on_leave(event):
    event.widget.config(bg=ACCENT)

root = tk.Tk()
root.title("TalkTranslate — Language Translator")
root.geometry("480x560")
root.configure(bg=BG_DARK)
root.resizable(False, False)

# ---------- Title section ----------
title_label = tk.Label(
    root, text="🌐 TalkTranslate",
    font=("Segoe UI", 22, "bold"),
    bg=BG_DARK, fg=TEXT_LIGHT
)
title_label.pack(pady=(25, 0))

subtitle_label = tk.Label(
    root, text="Translate text instantly, in any language",
    font=("Segoe UI", 10),
    bg=BG_DARK, fg=TEXT_MUTED
)
subtitle_label.pack(pady=(0, 20))

# ---------- Input card ----------
input_card = tk.Frame(root, bg=CARD_BG, padx=20, pady=20, highlightbackground="#e0e0eb", highlightthickness=1)
input_card.pack(padx=25, pady=10, fill="x")

tk.Label(
    input_card, text="ENTER TEXT", font=("Segoe UI", 9, "bold"),
    bg=CARD_BG, fg=TEXT_MUTED
).pack(anchor="w")

input_box = tk.Entry(
    input_card, font=("Segoe UI", 12), bg="#eeeef5", fg=TEXT_LIGHT,
    insertbackground=TEXT_LIGHT, relief="flat"
)
input_box.pack(fill="x", pady=(8, 15), ipady=8)

# Language selector row
lang_row = tk.Frame(input_card, bg=CARD_BG)
lang_row.pack(fill="x")

style = ttk.Style()
style.theme_use("default")
style.configure("Custom.TCombobox", padding=5)

tk.Label(lang_row, text="From", font=("Segoe UI", 9), bg=CARD_BG, fg=TEXT_MUTED).grid(row=0, column=0, sticky="w")
tk.Label(lang_row, text="To", font=("Segoe UI", 9), bg=CARD_BG, fg=TEXT_MUTED).grid(row=0, column=1, sticky="w", padx=(20, 0))

source_dropdown = ttk.Combobox(lang_row, values=list(LANGUAGES.keys()), state="readonly", width=14, style="Custom.TCombobox")
source_dropdown.set("English")
source_dropdown.grid(row=1, column=0, sticky="w")

target_dropdown = ttk.Combobox(lang_row, values=list(LANGUAGES.keys()), state="readonly", width=14, style="Custom.TCombobox")
target_dropdown.set("Hindi")
target_dropdown.grid(row=1, column=1, sticky="w", padx=(20, 0))

# ---------- Translate button ----------
translate_button = tk.Button(
    root, text="Translate  →", font=("Segoe UI", 12, "bold"),
    bg=ACCENT, fg="white", activebackground=ACCENT_HOVER,
    relief="flat", cursor="hand2", padx=20, pady=10,
    command=translate_text, borderwidth=0
)
translate_button.pack(pady=20)
translate_button.bind("<Enter>", on_enter)
translate_button.bind("<Leave>", on_leave)

# ---------- Result card ----------
result_card = tk.Frame(root, bg=CARD_BG, padx=20, pady=20, highlightbackground="#e0e0eb", highlightthickness=1)
result_card.pack(padx=25, pady=10, fill="x")

tk.Label(
    result_card, text="TRANSLATION", font=("Segoe UI", 9, "bold"),
    bg=CARD_BG, fg=TEXT_MUTED
).pack(anchor="w")

result_label = tk.Label(
    result_card, text="Your translated text will appear here...",
    font=("Segoe UI", 13), bg=CARD_BG, fg=TEXT_LIGHT,
    wraplength=380, justify="left", anchor="w"
)
result_label.pack(fill="x", pady=(8, 0))

# ---------- Copy button ----------
copy_button = tk.Button(
    root, text="📋 Copy to Clipboard", font=("Segoe UI", 10),
    bg=CARD_BG, fg=TEXT_LIGHT, activebackground="#eeeef5",
    relief="flat", cursor="hand2", padx=15, pady=8,
    command=copy_text, borderwidth=0
)
copy_button.pack(pady=15)

root.mainloop()