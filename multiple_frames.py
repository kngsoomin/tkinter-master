import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)             # Create the main window
        self.resizable(False, False)     # Set the window unresizable
        
        container = tk.Frame(self)       # Create the main frame to store frames
        container.pack(fill='both', expand=True)
        
        self.frames = {}                 # Initialize dict to store frames
        self.framesize = {}              # Initialize dict to store frame sizes
        
        # Loop to initialize all frames 
        for F in (PageA, PageB, PageC):
            page_name = F.__name__
						# New frames will be created in container frame in controller window
            frame = F(parent=container, controller=self) 
            self.frames[page_name] = frame
            self.framesize[page_name] = frame.size
            frame.grid(row=0, column=0, sticky='nsew')
            frame.grid_propagate(0)
            
        self.show_frame('PageA')          # Show PageA as the first page
 
    def show_frame(self, page_name):
        # Get the size of frame to display
        frame_size = self.framesize[page_name]
        
        # Change the window size to the frame size
        self.geometry(frame_size)
       
        # Show the frame
        frame = self.frames[page_name]      
        frame.tkraise()
                


class PageA(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='grey', width=200, height=200)
        self.size = '200x200'
        lbl = tk.Label(self, text='PageA', bg='grey')
        lbl.grid(row=0, column=0)
        btn = tk.Button(self, 
                        text='>> PageB', 
                        command=lambda: controller.show_frame('PageB'))
        btn.grid(row=1, column=0)
        
        
        
class PageB(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#ccccff', width=150, height=150)
        self.size = '150x150'
        lbl = tk.Label(self, text='PageB', bg='#ccccff')
        lbl.grid(row=0, column=0)
        btn = tk.Button(self, 
                        text='>> PageC', 
                        command=lambda: controller.show_frame('PageC'))
        btn.grid(row=1, column=0)
        
        
        
class PageC(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#ffcc99', width=300, height=150)
        self.size = '300x150'
        lbl = tk.Label(self, text='PageC', bg='#ffcc99')
        lbl.grid(row=0, column=0)
        btn = tk.Button(self, 
                        text='>> PageA', 
                        command=lambda: controller.show_frame('PageA'))
        btn.grid(row=1, column=0)


root = App()
root.mainloop()