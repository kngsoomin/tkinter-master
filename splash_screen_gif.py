import tkinter as tk
from tkinter import PhotoImage
from urllib.request import urlopen
import base64


def get_position(root):

    ws = root.winfo_screenwidth()   # Width of the screen
    hs = root.winfo_screenheight()  # Height of the screen       

    # Calculate x and y coordinates for the TK root window
    w = root.size[0]
    h = root.size[1]
    
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    
    return w, h, x, y



class SplashWindow(tk.Tk):

    def __init__(self):
        no_frame = 0

        tk.Tk.__init__(self)
        
        self.size = (300, 200)

        w, h, x, y = get_position(self)
        
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.configure(bg='#ffffff')
        
        # Hide the title bar
        self.overrideredirect(True)
        
        # Read gif from URL        
        image_url = 'https://media.giphy.com/media/S5AM8D4X5u8P6/giphy.gif'
        self.gif = self.get_gif(image_url)

        # Read gif from local directory
        # self.gif = PhotoImage(file='moving.gif', format = 'gif -index 0')
        
        # Label to insert the gif
        self.lbl_gif = tk.Label(self, borderwidth=0, highlightthickness=0)
        self.lbl_gif.place(x=20,y=0)
        
        # Label 'Splash screen'
        self.lbl_sscreen = tk.Label(self, text='This is splash screen')
        self.lbl_sscreen.place(x=170, y=170)
        
        self.animate(no_frame)

    def animate(self, no_frame):
        try:
            if no_frame == 50:
                no_frame = 0
            else:
                self.gif['format'] = 'gif -index ' + str(no_frame)
                self.lbl_gif['image'] = self.gif 
                no_frame += 1

            self.after(30, lambda: self.animate(no_frame)) # Recursive function

        except:
            pass
        
    def get_gif(self, image_url):
        
        image_byt = urlopen(image_url).read()
        image_b64 = base64.encodebytes(image_byt)
        image = PhotoImage(data=image_b64, format = 'gif -index 0')
        
        return image    



class MainWindow(tk.Tk):

    def __init__(self):
        
        splash_root.destroy()
        
        tk.Tk.__init__(self)
        
        self.title('Main window')
        self.size = (360, 360)
        
        w, h, x, y = get_position(self)
        
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        tk.Label(self, text='This is main screen').pack()


   
splash_root = SplashWindow()
splash_root.after(2500, lambda: MainWindow())
tk.mainloop()