import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser, filedialog, messagebox
import os

main_win = tk.Tk()
main_win.geometry('1200x800')
main_win.title('Coolest text editior')
main_win.wm_iconbitmap('icon.ico')

#--------------------------------------------------------main menu-------------------------------------------------------------------
main_menu = tk.Menu()
# file--------------------------------------------------------------------
# File icon
new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
save_as_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")

File = tk.Menu(main_menu, tearoff=False)

# Edit ---------------------------------------------------------------
# edit icons

copy_icon = tk.PhotoImage(file="icons2/copy.png")
paste_icon = tk.PhotoImage(file="icons2/paste.png")
cut_icon = tk.PhotoImage(file="icons2/cut.png")
clear_all_icon = tk.PhotoImage(file="icons2/clear_all.png")
find_icon = tk.PhotoImage(file="icons2/find.png")

Edit = tk.Menu(main_menu, tearoff=False)

# View-----------------------------------------------------------------
# view icons
tool_bar_icon = tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon = tk.PhotoImage(file="icons2/status_bar.png")

View = tk.Menu(main_menu, tearoff=False)

# Colout themes-----------------------------------------------------------
# Color icons
light_default_icon = tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon = tk.PhotoImage(file="icons2/light_plus.png")
monokai_icon = tk.PhotoImage(file="icons2/monokai.png")
dark_icon = tk.PhotoImage(file="icons2/dark.png")
night_blue_icon = tk.PhotoImage(file="icons2/night_blue.png")
red_icon = tk.PhotoImage(file="icons2/red.png")

Color_theme = tk.Menu(main_menu, tearoff=False)
theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, monokai_icon, dark_icon, night_blue_icon, red_icon)

color_dict = {
    'Light Default' : ('#000000', '#ffffff'),
    'Light Plus+' : ('#474747','#e0e0e0'),
    'Monokai' : ('#d3b774','#474747'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Night Blue' : ('#ededed','#6b9dc2'),
    'Red' : ('#2d2d2d','#ffe8e8')
}

# cascade
main_menu.add_cascade(label='File', menu=File)
main_menu.add_cascade(label='Edit', menu=Edit)
main_menu.add_cascade(label='View', menu=View)
main_menu.add_cascade(label='Color-Theme', menu=Color_theme)

# *******************************************************End Main menu***************************************************************

#--------------------------------------------------------toolbar-------------------------------------------------------------------

tool_label = ttk.Label(main_win)
tool_label.pack(side=tk.TOP, fill=tk.X)

# fonts families 
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_label, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)


# font size

font_size = tk.IntVar()
font_size_box = ttk.Combobox(tool_label, width=20, textvariable=font_size, state='readonly')
font_size_box['values'] = tuple(range(8,88,2))
font_size_box.current(4)
font_size_box.grid(row=0, column=1, padx=5)


# bold button
bold_icon = tk.PhotoImage(file="icons2/bold.png")
bold_btn = ttk.Button(tool_label, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# italic button
italic_icon = tk.PhotoImage(file="icons2/italic.png")
italic_btn = ttk.Button(tool_label, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

#underline button
underline_icon = tk.PhotoImage(file="icons2/underline.png")
underline_btn = ttk.Button(tool_label, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# font_color_button
font_color_icon = tk.PhotoImage(file="icons2/font_color.png")
font_btn = ttk.Button(tool_label, image=font_color_icon)
font_btn.grid(row=0, column=5, padx=5)

# align left button
align_left_icon = tk.PhotoImage(file="icons2/align_left.png")
align_left_btn = ttk.Button(tool_label, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# align center button
align_center_icon = tk.PhotoImage(file="icons2/align_center.png")
align_center_btn = ttk.Button(tool_label, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

# align right button
align_right_icon = tk.PhotoImage(file="icons2/align_right.png")
align_right_btn = ttk.Button(tool_label, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

# *******************************************************End toolbar***************************************************************

#--------------------------------------------------------text editior-------------------------------------------------------------------


text_editor = tk.Text(main_win)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_win)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality
current_font_family = 'Arial'
current_font_size = 16

def Change_font(main_win):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def Change_font_size(main_win):
    global current_font_size
    current_font_size = font_size.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", Change_font)
font_size_box.bind("<<ComboboxSelected>>", Change_font_size)



# #############################button facanility
# ----------------- Bold button functionality
def Change_bold():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=Change_bold)

# italic button functionality
def Change_italic():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command=Change_italic)


# Underline button functionality
def Change_underline():
    text_property= tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=Change_underline)

# Font color button functionality
def Change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_btn.configure(command=Change_font_color)


# align button functionality
def Change_align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=Change_align_left)

#align center button functionality
def Change_align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=Change_align_center)
 
# align right button functionality
def Change_align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=Change_align_right)
 

text_editor.configure(font=('Arial', 16))

# *******************************************************End text editior***************************************************************

#--------------------------------------------------------status bar-------------------------------------------------------------------

status_bar = ttk.Label(main_win, text='Status bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def Changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words=len(text_editor.get(1.0, 'end-1c').split())
        characters=len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", Changed)


# *******************************************************End status bar***************************************************************
#--------------------------------------------------------main functionality-------------------------------------------------------------------


#----------------------------- file commands

# variable
url = ''

# new file functionality

def new_f(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)
File.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_f)

# open functiionlity 

def open_f(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main_win.title(os.path.basename(url))
File.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_f)

# Save file functiionality

def save_f(even=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as wf:
                wf.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return
File.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command=save_f)

# Save as functionality
def save_as_f(even=None):
    global url
    try:
        content = str(text_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return    
File.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+A', command=save_as_f)

# Exit functionality
def exit_fun(event=None):
    global url, text_changed
    try :
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as wf:
                        wf.write(content)
                        main_win.destroy()
                else:
                    content2 = text_editor.get(1.0, tk.END)
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_win.destroy()
            elif mbox is False:
                main_win.destroy()
        else:
            main_win.destroy()
    except:
        return
File.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_fun)


# Edit command

# ___________Find Functionality
def find_fun(event=None):

    def Find():
        word = find_input.get()
        text_editor.tag_remove('match', 1.0, tk.END)
        matches = 0
        if word:
            start_pos = 1.0
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches+=1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def Replace():
        word = find_input.get()
        replace_txt = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_txt)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dailoge = tk.Toplevel()
    find_dailoge.geometry('400x200+500+200')
    find_dailoge.title('Find')

    # frame
    find_frame = ttk.LabelFrame(find_dailoge, text='Find/Replace')
    find_frame.pack(pady=20)

    # label
    text_find_label = ttk.Label(find_frame, text='Find')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    # entry
    find_input = ttk.Entry(find_frame, width=25)
    find_input.focus_set()
    replace_input = ttk.Entry(find_frame, width=25)

    # button
    find_btn = ttk.Button(find_frame, text='Find', command=Find)
    replace_btn = ttk.Button(find_frame, text='Repalce', command=Replace)

    # label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    # entry box grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # button grid
    find_btn.grid(row=2, column=0, padx=8, pady=4)
    replace_btn.grid(row=2, column=1, padx=8, pady=4)


    find_dailoge.mainloop()



Edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
Edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
Edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<Control v>"))
Edit.add_command(label='Clear all', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+A',command=lambda:text_editor.delete(1.0, tk.END))
Edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command=find_fun)

# view command

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_label.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_label.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True    

View.add_checkbutton(label='Tool bar', onvalue=True, offvalue=False, variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
View.add_checkbutton(label='Status bar', onvalue=True, offvalue=False, variable=show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)

# Color theme

def change_theme():
    choosen = theme_choice.get()
    color_tuple = color_dict.get(choosen)
    fg , bg = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg, foreground=fg)
count = 0
for i in color_dict:
    Color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count+=1
# *******************************************************End Main functionality***************************************************************




main_win.config(menu=main_menu)

# bind shortcut keys

main_win.bind("<Control-n>", new_f)
main_win.bind("<Control-o>", open_f)
main_win.bind("<Control-s>", save_f)
main_win.bind("<Control-a>", save_as_f)
main_win.bind("<Control-q>", exit_fun)
main_win.bind("<Control-f>", find_fun)



main_win.mainloop()
