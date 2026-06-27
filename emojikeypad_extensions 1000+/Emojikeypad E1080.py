
import tkinter as tk
from tkinter import font as tkfont
import pyperclip
from itertools import *

mouths = ['O','o','0','.','_','u','U','x','X','w','W','3','__']+list('▢▭▯◊▫▱◁▷△◅▻▵◃▹◇◌▽○◯◻□') + list('¤ÒÓÔÕÖ×ØÙÚÛÜñòóôõöøùúûüńņňŉŊŋŌōŎŏŐőŨũŪūŬŭŮůŰűŲųǑǒǓǔǕǖǗǘǙǚǛǜǝǪǫǬǭǷǾǿȌȍȎȏȔȕȖȗȪȫȬȭȮȯȰȱϘϙϪϫѺѻՄՈՌծ')

mouths + list('⁔‿ϖ∆∇∏∐∩∪∧∨∸∻∾≁∼∿≂∽≍⊌⊍⊎⊓⊔⋀⋁⊳⊲⋂⋃⋒⋓⋄⨃⨆⨄⨅⨿⩂⩅⩃⩀⩂⩅⩄⩁⩇⩈⩋⩎⩑⩔⩗⩉⩌⩏⩒⩕⩘⩊⩍⩐⩓⩖⩙⩚⩝⩛⩟⪦⪧⫏⫐⪤')
mouths += list('ǮǯɄДЏШЛɯɰɜɛɝωӅӆҖҗшъԒԓӼӽӾӿաӜӝӠӡ')

eyes= list("""¤ÒÓÔÕÖ×ØÙÚÛÜàáâäãåðñòóôõöøùúûüĨĩĪīĬĭĮįİıĺļľŀłńņňŉŊŋŌōŎŏŐőŨũŪūŬŭŮůŰűŲųƍƏƔƖƗƬƯưƱƲƿǀǁǂǃǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǪǫǬǭǷǾǿȈȉȊȋȌȍȎȏȔȕȖȗȢȣȪȫȬȭȮȯȰȱɊɋɑɒɓɘəɚɞɣɤɲɳɵɷʘʚͲͳͼͽΊΌ
           ΏΐΘΩαδθιπρσϔϓϒϘϙϪϫϬϭϱϮϯϴϾϿбѦѧѲѳѺѻҨҩҼҽҾҿӚӛӪӫӬӭԮԯԱԸԹԺԾՃՄՈՌծկժգզդճմնվռև֍֎""")
eyes_batched = list(batched(eyes,len(eyes)//17))



left_cheek = ['[','(','{','|'] + list('∈∉≮≤≰≨≦≲≴≪≺⊆≾⊊⊂≼⊄⊈⊏⊑⋠⋞⋜⋢⋦⋨⩽⪁⪇⪍⪅⪃⪉⪙⪗⪝⪕⪛⪡⪬⪯⪪⪷⪽⫃⪵⪻⫁⪹⪿⫅⫉⫇⫹⫷⩻⩹⩿')
RIGHT_CHEEK = [']',')','}','|'] + list('∋∌≯≥≱≩≧≳≵≫≻⊇≿⊋⊃≽⊅⊉⊐⊒⋡⋟⋝⋣⋧⋩⩾⪂⪈⪎⪆⪄⪊⪚⪘⪞⪖⪜⪢⪭⪰⪫⪸⪾⫄⪶⪼⫂⪺⫀⫆⫊⫈⫺⫸⩼⩺⪀')
eyes0 = eyes_batched[1]
eyes1 = eyes_batched[5]
emoticons_list = []

for e3 in eyes0:
    for e4 in eyes1:
        for m in mouths:

            for c in left_cheek:
                string = f'{c}{e3}{m}{e4}{RIGHT_CHEEK[left_cheek.index(c)]}'
              
                emoticons_list.append(string)


print(len(emoticons_list))
print('task complete')
        








classic_emoticons_list_of_lists = list(batched(emoticons_list,4000))

CHAR_GROUPS = [






















]


for i in classic_emoticons_list_of_lists:
    if classic_emoticons_list_of_lists.index(i) <442:
        CHAR_GROUPS.append((f"E{classic_emoticons_list_of_lists.index(i)+8245}",i))

print(len(classic_emoticons_list_of_lists))  #2481

print(len(CHAR_GROUPS))

print('task completed')
COLS = 8

BG        = "#0f0f13"
PANEL     = "#17171f"
ACCENT    = "#63ff80"
BTN_BG    = "#1e1e2e"
BTN_FG    = "#e0e0f5"
BTN_HOV   = "#2e2e45"
TAB_ACT   = "#63b1ff"
TAB_INACT = "#AD7F29"
TOAST_BG  = "#6c63ff"
LABEL_FG  = "#888899"
SB_TROUGH = "#17171f"
SB_THUMB  = "#3a3a55"


class ScrollableTabBar(tk.Frame):
    """A horizontally scrollable row of tab buttons."""

    def __init__(self, parent, tab_names, on_select, tab_f, **kwargs):
        super().__init__(parent, bg=BG, **kwargs)

        self._canvas = tk.Canvas(self, bg=BG, height=38,
                                 highlightthickness=0, bd=0)
        self._sb = tk.Scrollbar(self, orient="horizontal",
                                command=self._canvas.xview,
                                troughcolor=SB_TROUGH,
                                bg=SB_THUMB, activebackground=ACCENT,
                                highlightthickness=0, bd=0)
        self._canvas.configure(xscrollcommand=self._sb.set)
        self._canvas.pack(side="top", fill="x", expand=True)
        self._sb.pack(side="bottom", fill="x")

        self._inner = tk.Frame(self._canvas, bg=BG)
        self._win_id = self._canvas.create_window((0, 0), window=self._inner, anchor="nw")

        self._inner.bind("<Configure>", self._on_inner_configure)
        self._canvas.bind("<Configure>", self._on_canvas_configure)
        self._canvas.bind("<MouseWheel>", self._on_mousewheel)
        self._canvas.bind("<Button-4>",   lambda e: self._canvas.xview_scroll(-1, "units"))
        self._canvas.bind("<Button-5>",   lambda e: self._canvas.xview_scroll( 1, "units"))

        self._btns  = []
        self._tab_f = tab_f
        self._bold_f = tkfont.Font(family="Consolas", size=10, weight="bold")

        for i, name in enumerate(tab_names):
            btn = tk.Button(
                self._inner, text=name, font=self._tab_f,
                bg=TAB_INACT, fg=BTN_FG, relief="flat",
                padx=12, pady=5, cursor="hand2",
                activebackground=TAB_ACT, activeforeground="#fff",
                command=lambda i=i: on_select(i)
            )
            btn.pack(side="left", padx=3, pady=(2, 4))
            self._btns.append(btn)

    def _on_inner_configure(self, _=None):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self._canvas.itemconfig(self._win_id,
                                width=max(event.width, self._inner.winfo_reqwidth()))

    def _on_mousewheel(self, event):
        self._canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

    def highlight(self, active_idx):
        for j, tb in enumerate(self._btns):
            if j == active_idx:
                tb.configure(bg=TAB_ACT, fg="#fff", font=self._bold_f)
            else:
                tb.configure(bg=TAB_INACT, fg=BTN_FG, font=self._tab_f)


class ScrollableButtonGrid(tk.Frame):
    """A vertically scrollable grid of character buttons."""

    def __init__(self, parent, cols, mono_font, on_copy, **kwargs):
        super().__init__(parent, bg=PANEL, **kwargs)

        self._cols    = cols
        self._mono    = mono_font
        self._on_copy = on_copy
        self._btn_widgets = []

        self._canvas = tk.Canvas(self, bg=PANEL, highlightthickness=0, bd=0)
        self._sb = tk.Scrollbar(self, orient="vertical",
                                command=self._canvas.yview,
                                troughcolor=SB_TROUGH,
                                bg=SB_THUMB, activebackground=ACCENT,
                                highlightthickness=0, bd=0)
        self._canvas.configure(yscrollcommand=self._sb.set)
        self._canvas.pack(side="left", fill="both", expand=True)
        self._sb.pack(side="right", fill="y")

        self._inner = tk.Frame(self._canvas, bg=PANEL)
        self._win_id = self._canvas.create_window((0, 0), window=self._inner, anchor="nw")

        self._inner.bind("<Configure>", self._on_inner_configure)
        self._canvas.bind("<Configure>", self._on_canvas_configure)
        for w in (self._canvas, self._inner):
            w.bind("<MouseWheel>", self._on_mousewheel)
            w.bind("<Button-4>",   lambda e: self._canvas.yview_scroll(-1, "units"))
            w.bind("<Button-5>",   lambda e: self._canvas.yview_scroll( 1, "units"))

    def _on_inner_configure(self, _=None):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self._canvas.itemconfig(self._win_id, width=event.width)

    def _on_mousewheel(self, event):
        self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _add_hover(self, btn):
        btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=BTN_HOV))
        btn.bind("<Leave>", lambda e, b=btn: b.configure(
            bg=BTN_BG if str(b["state"]) == "normal" else PANEL))
        btn.bind("<MouseWheel>", self._on_mousewheel)
        btn.bind("<Button-4>",   lambda e: self._canvas.yview_scroll(-1, "units"))
        btn.bind("<Button-5>",   lambda e: self._canvas.yview_scroll( 1, "units"))

    def load(self, chars):
        needed = len(chars)
        while len(self._btn_widgets) < needed:
            char_var = tk.StringVar(value=" ")
            idx = len(self._btn_widgets)
            r, c = divmod(idx, self._cols)
            btn = tk.Button(
                self._inner,
                textvariable=char_var,
                font=self._mono,
                width=7, height=2,
                bg=BTN_BG, fg=BTN_FG,
                relief="flat", cursor="hand2",
                activebackground=ACCENT,
                activeforeground="#fff",
                command=lambda cv=char_var: self._on_copy(cv.get())
            )
            btn.grid(row=r, column=c, padx=4, pady=4, ipadx=8, ipady=6)
            self._add_hover(btn)
            self._btn_widgets.append((btn, char_var))

        for i, (btn, char_var) in enumerate(self._btn_widgets):
            if i < needed:
                r, c = divmod(i, self._cols)
                char_var.set(chars[i])
                btn.grid(row=r, column=c, padx=4, pady=4, ipadx=8, ipady=6)
                btn.configure(state="normal", bg=BTN_BG)
            else:
                char_var.set(" ")
                btn.grid_remove()

        self._canvas.yview_moveto(0)


class KeypadApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Emojikeypad E1080")
        self.configure(bg=BG)
        self.resizable(True, True)
        self.minsize(520, 340)

        self.mono    = tkfont.Font(family="Consolas", size=10)
        self.label_f = tkfont.Font(family="Consolas", size=9)
        self.tab_f   = tkfont.Font(family="Consolas", size=10, weight="bold")
        self.toast_f = tkfont.Font(family="Consolas", size=11, weight="bold")

        self._toast_id = None
        self._build_ui()
        self._switch_tab(0)

        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth()  - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"+{x}+{y}")

    def _build_ui(self):
        outer = tk.Frame(self, bg=BG, padx=2, pady=2)
        outer.pack(fill="both", expand=True)

        hdr = tk.Frame(outer, bg=BG, pady=10)
        hdr.pack(fill="x")
        tk.Label(hdr, text="⌨  Emojikeypad Extension 1080",
                 bg=BG, fg="#66eee7",
                 font=tkfont.Font(family="Consolas", size=13, weight="bold")
                 ).pack(side="left", padx=16)

        self._tab_bar = ScrollableTabBar(
            outer,
            tab_names=[name for name, _ in CHAR_GROUPS],
            on_select=self._switch_tab,
            tab_f=self.tab_f
        )
        self._tab_bar.pack(fill="x", padx=8, pady=(0, 4))

        self._grid = ScrollableButtonGrid(
            outer, cols=COLS,
            mono_font=self.mono,
            on_copy=self._copy,
            highlightbackground="#dfa024",
            highlightthickness=1
        )
        self._grid.pack(fill="both", expand=True, padx=10, pady=(0, 6))

        status = tk.Frame(outer, bg=BG, pady=6, padx=16)
        status.pack(fill="x")
        tk.Label(status,
                 text="Click any character to copy it to your clipboard",
                 bg=BG, fg=LABEL_FG, font=self.label_f
                 ).pack(side="left")

        self._toast = tk.Label(
            self, text="", bg=TOAST_BG, fg="#fff",
            font=self.toast_f, padx=18, pady=8, relief="flat"
        )

    def _switch_tab(self, idx):
        _, chars = CHAR_GROUPS[idx]
        self._grid.load(chars)
        self._tab_bar.highlight(idx)

    def _copy(self, ch):
        if ch.strip() == "":
            return
        pyperclip.copy(ch)
        self._show_toast(f"Copied  {ch}  to clipboard")

    def _show_toast(self, msg):
        self._toast.configure(text=msg)
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


if __name__ == "__main__":
    app = KeypadApp()
    app.mainloop()
