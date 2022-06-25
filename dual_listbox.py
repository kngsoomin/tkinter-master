import tkinter as tk


def move_to_basket():
    selection = lbb_top.curselection()
    for i in selection[::-1]:
        val = lbb_top.get(i)
        lbb_top.delete(i)
        lbb_bottom.insert(tk.END, val)

        
def remove_from_basket():
    selection = lbb_bottom.curselection()
    for i in selection[::-1]:
        val = lbb_bottom.get(i)
        lbb_bottom.delete(i)
        lbb_top.insert(tk.END, val)
    
    unsorted = lbb_top.get(0, tk.END)
    lbb_top.delete(0, tk.END)
    for j in sorted(unsorted):
        lbb_top.insert(tk.END, j)


root = tk.Tk()            # New window
root.geometry('330x300')  # Window size
root.title('Supermarket')

# Item list for supermarket listbox
item_list = ['apple', 'banana','durian', 'grapefruit', 'orange',
             'pear', 'pineapple','raspberry','strawberry','tomato']

# Define supermarket label, listbox, scrollbar
cvs_top = tk.Canvas(root, bd=0, highlightthickness=0) # Create top canvas
lbl_market = tk.Label(cvs_top, text='Supermarket')    # Create a label
lbl_market.pack(side='top')
lbb_top = tk.Listbox(cvs_top, 
                     width=40, height=5, selectmode='extended')
lbb_top.pack(fill='both', side='left')

scb_top = tk.Scrollbar(cvs_top, orient='vertical')  # Create scrollbar widget
scb_top.config(command=lbb_top.yview)               # Connect to listbox
scb_top.pack(fill='y', side='right')
lbb_top.config(yscrollcommand=scb_top.set)

# Insert fruits to supermarket listbox
for item in item_list:
    lbb_top.insert(tk.END, item)
    
# Define basket label, listbox, scrollbar
cvs_bottom = tk.Canvas(root, bd=0, highlightthickness=0) # Create bottom canvas
lbl_basket = tk.Label(cvs_bottom, text='Basket')         # Create a label
lbl_basket.pack(side='top')
lbb_bottom = tk.Listbox(cvs_bottom, 
                       width=40, height=5, selectmode='extended')
lbb_bottom.pack(fill='both', side='left')
scb_bottom = tk.Scrollbar(cvs_bottom,               # Create scrollbar widget
                          orient='vertical') 
scb_bottom.config(command=lbb_bottom.yview)         # Connect to listbox
scb_bottom.pack(fill='y', side='right')
lbb_bottom.config(yscrollcommand=scb_bottom.set)

cvs_top.pack(side='top')
cvs_bottom.pack(side='top')

# Button 1: remove from basket
btn_remove_basket = tk.Button(root, 
                              text='Remove from Basket',
                              command=remove_from_basket)
btn_remove_basket.pack(side='left', padx=15)

# Button 2: move to basket
btn_move_to_basket = tk.Button(root, 
                               text='Move to Basket',
                               command=move_to_basket)
btn_move_to_basket.pack(side='right', padx=15)

root.mainloop()






















