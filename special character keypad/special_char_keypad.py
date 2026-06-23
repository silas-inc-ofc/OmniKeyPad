import tkinter as tk
from tkinter import font as tkfont
import pyperclip

# ── Character groups ──────────────────────────────────────────────────────────
math_chrs = ["±", "×", "÷", "≠", "≈", "≤", "≥", "∞", "√", "∑", "∏", "∂", "∫", "°", "‰", "μ",]
math_chrs.extend(list("⁰³⁶⁹⁺⅟¹⁴⁷ⁿ⁻↉²⁵⁸ⁱ⁼₀₃₆₉₊₁₄₇₍₋₌₎₈₅₂∆∈∋∍∊√∝∛∜∟∠∵∴≅≡≤≥△○□≈"))
CHAR_GROUPS = [
    ("Math",       math_chrs ),
    ("Arrows",      ["←", "→", "↑", "↓", "↔", "↕", "⇐", "⇒", "⇑", "⇓", "⇔", "↩", "↪", "↗", "↘", "↖"]),
    ("Currency",    ["€", "£", "¥", "¢", "₹", "₿", "₩", "₽", "₺", "₦", "₴", "₪", "₫", "฿", "₡", "₲"]),
    ("Punctuation", ["…", "—", "–", "«", "»", "‹", "›", "\u2018", "\u2019", "\u201C", "\u201D", "†", "‡", "•", "·", "§"]),
    ("Symbols",     ["©", "®", "™", "℃", "℉", "№", "℗", "☎", "✉", "✔", "✘", "★", "☆", "♠", "♥", "♦"]),
    ("Technical",   ["⌘", "⌥", "⌃", "⇧", "⌫", "⌦", "⏎", "⏏", "⌨", "🖥", "⚙", "🔒", "🔓", "📋", "💾", "🔍"]),
    ("A",list("ĀāǍǎĂăÁáÂâÃãÀàÄäÅåĄą"))
    
]

COLS = 8   # buttons per row

# ── Palette ───────────────────────────────────────────────────────────────────
BG        = "#0f0f13"
PANEL     = "#17171f"
ACCENT    = "#6c63ff"
ACCENT2   = "#ff6584"
BTN_BG    = "#1e1e2e"
BTN_FG    = "#e0e0f5"
BTN_HOV   = "#2e2e45"
TAB_ACT   = "#6c63ff"
TAB_INACT = "#1e1e2e"
TOAST_BG  = "#6c63ff"
LABEL_FG  = "#888899"


class KeypadApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Special Character Keypad")
        self.configure(bg=BG)
        self.resizable(False, False)

        # fonts
        self.mono   = tkfont.Font(family="Consolas",  size=16)
        self.label_f= tkfont.Font(family="Consolas",  size=9)
        self.tab_f  = tkfont.Font(family="Consolas",  size=10, weight="bold")
        self.toast_f= tkfont.Font(family="Consolas",  size=11, weight="bold")

        self._active_tab = 0
        self._toast_id   = None

        self._build_ui()
        self._switch_tab(0)

        # centre window
        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth()  - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"+{x}+{y}")

    # ── UI construction ───────────────────────────────────────────────────────
    def _build_ui(self):
        outer = tk.Frame(self, bg=BG, padx=2, pady=2)
        outer.pack(fill="both", expand=True)

        # header
        hdr = tk.Frame(outer, bg=BG, pady=10)
        hdr.pack(fill="x")
        tk.Label(hdr, text="⌨  Special Character Keypad",
                 bg=BG, fg="#c8c8ff",
                 font=tkfont.Font(family="Consolas", size=13, weight="bold")
                 ).pack(side="left", padx=16)

        # tabs
        self._tab_btns = []
        tab_bar = tk.Frame(outer, bg=BG, padx=8)
        tab_bar.pack(fill="x")
        for i, (name, _) in enumerate(CHAR_GROUPS):
            btn = tk.Button(tab_bar, text=name, font=self.tab_f,
                            bg=TAB_INACT, fg=BTN_FG, relief="flat",
                            padx=12, pady=5, cursor="hand2",
                            activebackground=TAB_ACT, activeforeground="#fff",
                            command=lambda i=i: self._switch_tab(i))
            btn.pack(side="left", padx=3, pady=(0, 6))
            self._tab_btns.append(btn)

        # grid panel
        self._grid_frame = tk.Frame(outer, bg=PANEL,
                                    padx=14, pady=14,
                                    highlightbackground="#2a2a3a",
                                    highlightthickness=1)
        self._grid_frame.pack(fill="both", expand=True, padx=10, pady=(0, 6))
        self._btn_widgets = []   # (btn, char_var) per slot

        n_chars = max(len(chars) for _, chars in CHAR_GROUPS)
        rows = (n_chars + COLS - 1) // COLS

        for r in range(rows):
            for c in range(COLS):
                idx = r * COLS + c
                char_var = tk.StringVar(value=" ")
                btn = tk.Button(self._grid_frame,
                                textvariable=char_var,
                                font=self.mono,
                                width=3, height=1,
                                bg=BTN_BG, fg=BTN_FG,
                                relief="flat", cursor="hand2",
                                activebackground=ACCENT,
                                activeforeground="#fff",
                                command=lambda cv=char_var: self._copy(cv.get()))
                btn.grid(row=r, column=c, padx=4, pady=4, ipadx=4, ipady=4)
                self._add_hover(btn)
                self._btn_widgets.append((btn, char_var))

        # status bar
        status = tk.Frame(outer, bg=BG, pady=6, padx=16)
        status.pack(fill="x")
        self._status_lbl = tk.Label(status,
                                    text="Click any character to copy it to your clipboard",
                                    bg=BG, fg=LABEL_FG, font=self.label_f)
        self._status_lbl.pack(side="left")

        # toast overlay (hidden initially)
        self._toast = tk.Label(self, text="", bg=TOAST_BG, fg="#fff",
                               font=self.toast_f,
                               padx=18, pady=8, relief="flat")

    # ── Tab switching ─────────────────────────────────────────────────────────
    def _switch_tab(self, idx):
        self._active_tab = idx
        _, chars = CHAR_GROUPS[idx]

        for i, (btn, char_var) in enumerate(self._btn_widgets):
            if i < len(chars):
                char_var.set(chars[i])
                btn.configure(state="normal", bg=BTN_BG)
            else:
                char_var.set(" ")
                btn.configure(state="disabled", bg=PANEL)

        for j, tb in enumerate(self._tab_btns):
            if j == idx:
                tb.configure(bg=TAB_ACT, fg="#fff",
                             relief="flat",
                             font=tkfont.Font(family="Consolas", size=10, weight="bold"))
            else:
                tb.configure(bg=TAB_INACT, fg=BTN_FG, relief="flat",
                             font=self.tab_f)

    # ── Copy & toast ──────────────────────────────────────────────────────────
    def _copy(self, ch):
        if ch.strip() == "":
            return
        pyperclip.copy(ch)
        self._show_toast(f"Copied  {ch}  to clipboard")

    def _show_toast(self, msg):
        self._toast.configure(text=msg)
        # position toast at bottom-centre of window
        self.update_idletasks()
        tw = self._toast.winfo_reqwidth()
        ww = self.winfo_width()
        wh = self.winfo_height()
        self._toast.place(x=(ww - tw) // 2, y=wh - 54)
        self._toast.lift()

        if self._toast_id:
            self.after_cancel(self._toast_id)
        self._toast_id = self.after(1800, self._hide_toast)

    def _hide_toast(self):
        self._toast.place_forget()

    # ── Hover effect ─────────────────────────────────────────────────────────
    def _add_hover(self, btn):
        btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=BTN_HOV))
        btn.bind("<Leave>", lambda e, b=btn: b.configure(
            bg=BTN_BG if b["state"] == "normal" else PANEL))


if __name__ == "__main__":
    app = KeypadApp()
    app.mainloop()
