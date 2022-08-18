
#Python program to make a Text Editor.....
#add calm music feature also 

# Date 16-04-2020     

# Here i'm going to import all the libraries and function that i need to make my Text Editor Application
import tkinter as tk

#from tkinter import *      # I'm not going to import all function because of size issue.
import  os 
from tkinter import colorchooser
from tkinter import ttk   #ttk is a built module of tkinter 
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog

main_app = tk.Tk()    # it create the overall tk window
main_app.geometry('1200x800')    #here we 
main_app.title('Paradox Text Editor')   # it will hold our application title

#-------------------------Main Menu------------------------------
main_menu = tk.Menu()

#FILE
file = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file) #cascade

#EDIT
edit = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Edit", menu=edit)

#VIEW
view = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="View", menu=view)

#theme
light_default_icon = tk.PhotoImage(file='icons/theme_icons/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons/theme_icons/light_plus.png')
dark_icon = tk.PhotoImage(file='icons/theme_icons/dark.png')
red_icon = tk.PhotoImage(file='icons/theme_icons/red.png')
monokai_icon = tk.PhotoImage(file='icons/theme_icons/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons/theme_icons/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue':('#ededed', '#6b9dc2')
}


main_menu.add_cascade(label="Theme", menu=color_theme)

#about
about = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="About", menu=about)
#__________________________________________________________________________________________________________________________________

#-------------------------ToolBar--------------------------------
tool_bar = ttk.Label(main_app)
# FontBox
font_text=ttk.Label(tool_bar, text="Font :")
font_text.grid(row=0, column=0)

tool_bar.pack(side=tk.TOP, fill=tk.X)
font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width= 25,height=30, textvariable=font_family, state="readonly")
font_box["values"]=font_tuples
font_box.current(font_tuples.index("Arial"))
font_box.grid(row=0, column=1, padx=5)

# SizeBox
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable= size_var, state="readonly")
font_size["values"] = tuple(range(8,88,2))
font_size.current(2)
font_size.grid(row=0,column=2, padx=5)

# Bold Button
bold_icon = tk.PhotoImage(file="icons/tool_bar/bold.png")
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=3, padx=5)

# Italic Button
italic_icon = tk.PhotoImage(file="icons/tool_bar/italic.png")
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=4, padx=5)

# Underline Button
underline_icon = tk.PhotoImage(file="icons/tool_bar/underline.png")
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=5, padx=5)

# Overstrike Button
overstrike_icon = tk.PhotoImage(file="icons/tool_bar/overstrike.png")
overstrike_btn = ttk.Button(tool_bar, image=overstrike_icon )
overstrike_btn.grid(row=0, column=6, padx=5)

# Font color button
fontcolor_icon = tk.PhotoImage(file="icons/tool_bar/font_color.png")
fontcolor_btn = ttk.Button(tool_bar, image=fontcolor_icon)
fontcolor_btn.grid(row=0, column=7, padx=6)

# Left_align button
left_align_icon = tk.PhotoImage(file="icons/tool_bar/align_left.png")
left_align_btn = ttk.Button(tool_bar, image=left_align_icon)
left_align_btn.grid(row=0, column=8, padx=5)

# Center_align button
center_align_icon = tk.PhotoImage(file="icons/tool_bar/align_center.png")
center_align_btn = ttk.Button(tool_bar, image=center_align_icon)
center_align_btn.grid(row=0, column=9, padx=5)

# Right_align button
right_align_icon = tk.PhotoImage(file="icons/tool_bar/align_right.png")
right_align_btn = ttk.Button(tool_bar, image=right_align_icon)
right_align_btn.grid(row=0, column=10, padx=5)
#__________________________________________________________________________________________________________________________________



#-------------------------Editor----------------------------------
text_editor = tk.Text(main_app)
text_editor.config(wrap="word", relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_app)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font and size Functionality 
current_font = "Arial"
current_font_size = 12

def change_font(main_app):
    global current_font
    current_font = font_family.get()
    text_editor.configure(font=(current_font, current_font_size))

def change_font_size(main_app):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_font_size)

# Button Functionality
# BOLD
def change_bold():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["weight"] == "normal":
        text_editor.configure(font=(current_font, current_font_size, "bold"))
    if text_property.actual()["weight"] == "bold":
        text_editor.configure(font=(current_font, current_font_size, "normal"))

bold_btn.configure(command=change_bold)

# ITALIC
def change_italic():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["slant"] == "roman":
        text_editor.configure(font=(current_font, current_font_size, "italic"))
    if text_property.actual()["slant"] == "italic":
        text_editor.configure(font=(current_font, current_font_size, "roman"))

italic_btn.configure(command=change_italic)

# UNDERLINE
def change_underline():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["underline"] == 0:
        text_editor.configure(font=(current_font, current_font_size, "underline"))
    if text_property.actual()["underline"] == 1:
        text_editor.configure(font=(current_font, current_font_size, "normal"))

underline_btn.configure(command=change_underline)

# Overstrike
def change_overstrike():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["overstrike"] == 0:
        text_editor.configure(font=(current_font, current_font_size, "overstrike"))
    if text_property.actual()["overstrike"] == 1:
        text_editor.configure(font=(current_font, current_font_size, "normal"))

overstrike_btn.configure(command=change_overstrike)

# Font Color Functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

fontcolor_btn.configure(command=change_font_color)

# Align Functionality
# Left Align
def align_left():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "left")
left_align_btn.configure(command=align_left)

# Center Align
def align_center():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "center")
center_align_btn.configure(command=align_center)

# Right Align
def align_right():
    text_content = text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "right")
right_align_btn.configure(command=align_right)

text_editor.configure(font=("Arial", 12))

#

#__________________________________________________________________________________________________________________________________

#-------------------------Status Bar------------------------------
status_bar = ttk.Label(main_app, text= "Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event=None):
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, "end-1c").split())
        characters = len(text_editor.get(1.0, "end-1c").replace(" ",""))
        status_bar.config(text=f"Characters :{characters} words : {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>", changed)        
    

#__________________________________________________________________________________________________________________________________


#-------------------------Main Menu tools-------------------------


########################################### File Command 
# variable
url = ''

# new Functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)
file.add_command(label= "New", accelerator="command+N", command=new_file)

# open Functionality
def open_file(event=None):
    global url
    
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=[("Text File", "*.txt"), ("All Files", "*.*")])
    try:
        with open(url, 'r')as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))
file.add_command(label= "Open",  accelerator="command+O", command=open_file)

# save Functionality
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, "w", encoding="utf-8")as fw:
                fw.write(content) 
        else:
            url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text File", "*.txt"), ("All Files", "*.*")])
            content2 = text_editor(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label= "Save",  accelerator="command+S", command=save_file)

# Save as Functionality
def save_as(event=None):
    global url
    try:
        content = str(text_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text File", "*.txt"), 
                                                                                     ("All Files", "*.*")])
        url.write(content)
        url.close
    except:
        return

file.add_command(label= "Save as",  accelerator="command+Shift+S", command=save_as)

# Close Window Functionality
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ? ')
            if mbox is True:
                save_file()
                main_app.destroy()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return


file.add_command(label='Exit', accelerator='command+Q', command=exit_func)


##########################################      Edit Commands
# Cut Functionality
edit.add_command(label= "Cut", accelerator="command+X", command=lambda:text_editor.event_generate("<Control x>"))

# Copy Functionality
edit.add_command(label= "Copy",  accelerator="command+C", command=lambda:text_editor.event_generate("<Control c>"))

# Paste Functionality
edit.add_command(label= "Paste",  accelerator="command+V", command=lambda:text_editor.event_generate("<Control v>"))

# Clear All Functionality
edit.add_command(label= "Clear All",  accelerator="command+Shift+X", command=lambda:text_editor.delete(1.0, tk.END))

# Find Functionality
def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches+=1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    ## entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    ## label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()
    
edit.add_command(label= "Find",  accelerator="command+F", command=find_func)


# view check button
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
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


view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0, variable=show_toolbar, 
                     compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False, variable=show_statusbar, 
                     compound=tk.LEFT, command=hide_statusbar)

# color theme


def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1



#--------------- End main menue functionality ------------#

main_app.config(menu=main_menu)

# bind shortcut keys
main_app.bind("<Command-n>", new_file)
main_app.bind("<Command-o>", open_file)
main_app.bind("<Command-s>", save_file)
main_app.bind("<Command-s>", save_as)
main_app.bind("<Command-q>", exit_func)
main_app.bind("<Command-f>", find_func)

main_app.mainloop()


