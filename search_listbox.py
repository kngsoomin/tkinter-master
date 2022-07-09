import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

# Create labels
label1 = tk.Label(root, text='Control a listbox with keyboard events', bg='lightgrey')
label1.pack()
label2 = tk.Label(root, text='Keyword input :')
label2.pack()

# Create listbox
items = ['Bear', 'Bee', 'Camel', 'Chicken', 'Chimpanzee', 'Coyote', 'Crab', 'Deer', 'Dog', 'Duck', 'Elephant', 'Elk', 'Fish', 'Fox', 'Giraffe', 'Goat', 'Gorilla', 'Hedgehog', 'Hippopotamus', 'Horse', 'Kangaroo', 'Koala', 'Leopard', 'Lion', 'Lizard', 'Mole', 'Monkey', 'Otter', 'Owl', 'Panda', 'Pig', 'Rabbit', 'Red panda', 'Reindeer', 'Squirrel', 'Tiger', 'Wombat', 'Woodpecker', 'Zebra']
vars = tk.StringVar(value=sorted(items))
lbox = tk.Listbox(root, listvariable=vars, height=9)
lbox.pack()


def search(event):
    '''Function to search and select a listbox item with keyword events'''
    var = event.char # Get keyboard input
    
    for item in items:
        if item.lower().startswith(var):
            idx = items.index(item)         # Get list item index
            lbox.see(idx)                   # Show selected item
            lbox.selection_clear(0, tk.END) # Clear current selection
            lbox.select_set(idx)            # Select item
            break
    
    # Change text in label to show keyword input 
    label2.config(text=f'Keyword input : {event.char}')


# Bind function to listbox
lbox.bind('<Key>', search)

root.mainloop()