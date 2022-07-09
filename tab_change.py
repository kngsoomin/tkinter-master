import tkinter as tk
import tkinter.ttk as ttk
import random


def update_label_and_change_bg(event):
    '''Define action for tab change'''
    
    global idx_tab1, idx_tab2
    tabname = event.widget.tab('current')['text']  # Get current tab name
    
    if tabname == 'tab1':
        idx_tab1 += 1
        label = tk.Label(tab1, text=f'You selected tab1 for \'{idx_tab1}\' times')
        label.pack()
                
    if tabname == 'tab2':
        idx_tab2 += 1
        label = tk.Label(tab2, text=f'You selected tab2 for \'{idx_tab2}\' times')
        label.pack()

    # Get random color hex 
    color = '#%06x' % random.randint(0, 0xFFFFFF)
    # Change label background
    label.config(bg=color)
       
       
# Create root window
root = tk.Tk()
root.geometry('300x300')
root.title('tkinter - Tabs')

# Create tab controller
tabControl = ttk.Notebook(root)

# Create tabs and add to controller
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='tab1')
tabControl.add(tab2, text='tab2')

# Initalize index
idx_tab1 = 0
idx_tab2 = 0

# Pack tabs
tabControl.pack(expand=1, fill='both')

# Bind function to tab change
tabControl.bind('<<NotebookTabChanged>>', update_label_and_change_bg)

root.mainloop()
