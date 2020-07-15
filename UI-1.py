from tkinter import Frame, Label, Entry , Button , Text


class UI:
    
    def __init__(self, master):
        self.root = master
        self.name_widget = None
        self.join_button = None
        self.enter_text_widget = None


    def initialize_gui(self):
        self.root.tittle('Chat App')
        self.root.resizable(0,0)


    def display_name_section(self):
        frame = Frame()
        Label(frame, text='Chat Box' , font = ("Serif" , 13)).pack(side='top' , anchor = 'w')
        self.name_widget = Text(frame, width=50 , borderwidth = 2)
        self.name_widget.pack(side = 'left' , anchor = 'e')
        self.join_button = Button(frame , text = 'Join' , width = 10 , command = self.on_join).pack(side = 'left')
        frame.pack(side = 'top' , anchor = 'w')


    def chat_entry_box(self):
        frame = Frame()
        Label(frame, text='Enter Message' , font = ("Serif" , 13)).pack(side='top' , anchor = 'w')
        self.enter_text_widget = Text(frame, width=60 , height = 3, font = ("Serif" , 13))
        self.enter_text_widget.pack(side='left', pady=16)
        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)
        frame.pack(side = 'top')