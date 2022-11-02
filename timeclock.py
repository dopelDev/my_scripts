#!/usr/bin/python3.10
from tkinter import Tk, Label, Button, Frame
from tkinter import BOTTOM, LEFT, RIGHT, TOP
from typing import List
from datetime import datetime

class my_time_controller():
    def __init__(self) -> None:
        self.FONT = 'DaddyTimeMono Nerd Font'
        self.BACKGROUND = 'black'
        self.FOREGROUND = 'white' 
        self.tracker_list : List[str] = []

        self.app = Tk(className='Time Control')
        self.app.geometry('450x800')
        self.app.configure(bg='black')

# Labels
    def title_label(self):
        title = Label(self.top_frame, text='Time Control', font=(self.FONT, 25))
        title.configure(bg=self.BACKGROUND, fg=self.FOREGROUND)
        title.pack(side=TOP)

    def tracker_label(self, text):
        tracker_clock = Label(self.mid_frame, text=text)
        tracker_clock.configure(bg=self.BACKGROUND, fg=self.FOREGROUND, font=(self.FONT,20))
        tracker_clock.pack()

    def main_clock_label(self):
        time = datetime.now()
        clock = Label(self.top_frame, text=time.strftime('%I %M %S'))
        clock.configure(bg=self.BACKGROUND, fg=self.FOREGROUND, pady=20, font=(self.FONT, 20)) 
        clock.pack()
        clock.after(1002, lambda : clock.destroy())
        self.app.after(1000, self.main_clock_label)

# Frames
    def overhead_frame(self):
        self.top_frame = Frame(self.app, bg=self.BACKGROUND)
        self.top_frame.pack(side=TOP, fill='x')
    # call witgets
        self.title_label()
        self.main_clock_label()


    def middle_frame(self):
        self.mid_frame = Frame(self.app, bg=self.BACKGROUND)
        self.mid_frame.pack(side=TOP, fill='x')
        self.mid_frame.pack()


    def bottom_frame(self):
        self.btm_frame = Frame(self.app, bg=self.BACKGROUND)
        self.btm_frame.pack(side=BOTTOM, fill='x')
    # call witgets
        self.add_tracker_button()
        self.remove_tracker_button()

# Buttons
    def add_tracker_button(self):
        btm = Button(self.btm_frame, text='Add', command=self.mtd_add) 
        btm.configure(bg=self.BACKGROUND, fg=self.FOREGROUND, padx=10, pady=10, font=(self.FONT, 18))
        btm.pack(side=RIGHT)  
 
    def remove_tracker_button(self):
        btm = Button(self.btm_frame, text='Remove', command=self.mtd_remove) 
        btm.configure(bg=self.BACKGROUND, fg=self.FOREGROUND, padx=10, pady=10, font=(self.FONT, 18))
        btm.pack(side=LEFT)
# commands
    def mtd_add(self):
        time = datetime.now()
        text = time.strftime('%I %M %S')
        self.tracker_list.append(text)
        self.tracker_label(text)

    def mtd_remove(self):
        # remove the last label
        self.mid_frame.destroy()
        self.tracker_list = self.tracker_list[:-1]
        self.middle_frame()
        for label in self.tracker_list:
            self.tracker_label(label)

    def run(self):
        self.overhead_frame()
        self.middle_frame()
        self.bottom_frame()
        self.app.mainloop()

if __name__ == '__main__':
    app = my_time_controller()
    app.run()
