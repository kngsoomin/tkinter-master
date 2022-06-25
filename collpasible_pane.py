import tkinter as tk
import tkinter.ttk as ttk


def active_panel():
    if var.get():
        # Expand pane
        root.geometry('600x300')
        btn_expand.configure(text=txt_collapse)
        frame_cllp.pack(side='left')
    
    elif not var.get():
        # Hide pane
        frame_cllp.pack_forget()
        root.geometry('150x300')
        btn_expand.configure(text=txt_expand)


root = tk.Tk()                 # Create new window
root.title('collapsible pane') # Set a title
root.geometry('150x300')       # A size of window when the pane is collpased
root.resizable(False, False)

s = ttk.Style()                # Create style
s.configure('pane.TButton', background='#ffffff', borderwidth=0)

# Main Frame 
frame_main = tk.Frame(root, width=300, height=300, bg='#ffffff')
frame_main.pack(side='left', fill='both', expand=True)

var = tk.IntVar()            # Initialize button for checkbutton
txt_expand = 'Expand'        # Text for button
txt_collapse = 'Collpase'    # Text for button

# Checkbutton returns default value 1 when clicked, otherwise return 0
btn_expand = ttk.Checkbutton(frame_main, style='pane.TButton',
                             text=txt_expand, 
                             command=active_panel,
                             variable=var)
btn_expand.pack(anchor='center')

# Collapsible pane
frame_cllp = tk.Frame(root, width=450, height=300)

# Image file path
path = r'C:\Users\soomi\Desktop\Soo\hiding_spongebob.png'
img = tk.PhotoImage(file=path)

# Create label for image
panel = tk.Label(frame_cllp, image=img)
panel.pack(fill = "both", expand = "yes")

root.mainloop()
