from dvb import monitor
from tkinter import *
import os
from datetime import datetime, time

class Haltestelle:

    def __init__(self, haltestelle='Alberplatz'):
        self.stop = haltestelle
        self.departures = monitor(self.stop, 0, 10, 'Dresden')
        
        # Window
        bg_color ="#101010"     #Globale Hintergrundfarbe

        self.root = Tk()
        self.root.title("Fahrten")
        #self.root.iconbitmap(os.getcwd() + '/logo.png')
        self.root.geometry("700x707")
        # self.root.overrideredirect(1)
        self.root.configure(background=bg_color)

        # Attriblutes
        self.font_face = "Courier"
        self.line_text_size = 30
        self.top_margin = 60
        

        # Pivot Haltestelle
        self.haltestelle_text = Label(text = self.stop, fg = "Yellow", bg=bg_color, font=(self.font_face, 30))
        self.haltestelle_text.pack()

        # Uhrzeit
        now = datetime.now()
        self.uhrzeit_text = now.strftime('%H:%M')
        self.uhrzeit = Label(text = self.uhrzeit_text, fg =bg_color, bg='Yellow', font=(self.font_face, self.line_text_size))
        self.uhrzeit.pack()
        self.uhrzeit.place(x=400, y=5)

        ''' Labels anbringen '''

        # 1
        self.line_label_1 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_1.pack()
        self.line_label_1.place(x=10, y=self.top_margin)
        self.direction_label_1 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_1.pack()
        self.direction_label_1.place(x=10, y=self.top_margin)
        self.min_label_1 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_1.pack()
        self.min_label_1.place(x=10, y=self.top_margin)
        # 2
        self.line_label_2 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_2.pack()
        self.line_label_2.place(x=10, y=self.top_margin)
        self.direction_label_2 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_2.pack()
        self.direction_label_2.place(x=10, y=self.top_margin)
        self.min_label_2 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_2.pack()
        self.min_label_2.place(x=10, y=self.top_margin)
        # 3
        self.line_label_3 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_3.pack()
        self.line_label_3.place(x=10, y=self.top_margin)
        self.direction_label_3 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_3.pack()
        self.direction_label_3.place(x=10, y=self.top_margin)
        self.min_label_3 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_3.pack()
        self.min_label_3.place(x=10, y=self.top_margin)
        # 4
        self.line_label_4 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_4.pack()
        self.line_label_4.place(x=10, y=self.top_margin)
        self.direction_label_4 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_4.pack()
        self.direction_label_4.place(x=10, y=self.top_margin)
        self.min_label_4 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_4.pack()
        self.min_label_4.place(x=10, y=self.top_margin)
        # 5
        self.line_label_5 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_5.pack()
        self.line_label_5.place(x=10, y=self.top_margin)
        self.direction_label_5 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_5.pack()
        self.direction_label_5.place(x=10, y=self.top_margin)
        self.min_label_5 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_5.pack()
        self.min_label_5.place(x=10, y=self.top_margin)
        # 6
        self.line_label_6 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_6.pack()
        self.line_label_6.place(x=10, y=self.top_margin)
        self.direction_label_6 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_6.pack()
        self.direction_label_6.place(x=10, y=self.top_margin)
        self.min_label_6 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_6.pack()
        self.min_label_6.place(x=10, y=self.top_margin)
        # 7
        self.line_label_7 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_7.pack()
        self.line_label_7.place(x=10, y=self.top_margin)
        self.direction_label_7 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_7.pack()
        self.direction_label_7.place(x=10, y=self.top_margin)
        self.min_label_7 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_7.pack()
        self.min_label_7.place(x=10, y=self.top_margin)
        # 8
        self.line_label_8 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_8.pack()
        self.line_label_8.place(x=10, y=self.top_margin)
        self.direction_label_8 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_8.pack()
        self.direction_label_8.place(x=10, y=self.top_margin)
        self.min_label_8 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_8.pack()
        self.min_label_8.place(x=10, y=self.top_margin)
        # 9
        self.line_label_9 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_9.pack()
        self.line_label_9.place(x=10, y=self.top_margin)
        self.direction_label_9 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_9.pack()
        self.direction_label_9.place(x=10, y=self.top_margin)
        self.min_label_9 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_9.pack()
        self.min_label_9.place(x=10, y=self.top_margin)
        # 10
        self.line_label_10 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.line_label_10.pack()
        self.line_label_10.place(x=10, y=self.top_margin)
        self.direction_label_10 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.direction_label_10.pack()
        self.direction_label_10.place(x=10, y=self.top_margin)
        self.min_label_10 = Label(text = '', fg = "Yellow", bg=bg_color, font=(self.font_face, self.line_text_size))
        self.min_label_10.pack()
        self.min_label_10.place(x=10, y=self.top_margin)


        self.line_label_list = [self.line_label_1, self.line_label_2, self.line_label_3, self.line_label_4, self.line_label_5, self.line_label_6, self.line_label_7, self.line_label_8, self.line_label_9, self.line_label_10]
        self.direction_label_list = [self.direction_label_1, self.direction_label_2, self.direction_label_3, self.direction_label_4, self.direction_label_5, self.direction_label_6, self.direction_label_7, self.direction_label_8, self.direction_label_9, self.direction_label_10]
        self.min_label_list = [self.min_label_1, self.min_label_2, self.min_label_3, self.min_label_4, self.min_label_5, self.min_label_6, self.min_label_7, self.min_label_8, self.min_label_9, self.min_label_10]


        # mainloop
        self.error_label = None
        self.on_after()
        self.root.after(30*1000, self.on_after)
        # self.departures = monitor('Tronitzer Straße', 0, 10, 'Dresden')
        self.root.mainloop()


    def on_after(self):
        try:
            self.departures = monitor(self.stop, 0, 10, 'Dresden')
            if not self.departures == {}:
                self.update()
                self.root.after(30*1000, self.on_after)
            if self.error_label != None:
                self.error_label.destroy()
                self.error_label = None
        except:
            if self.error_label != None:
                self.error_label.destroy()
                self.error_label = None
            self.error_label = Label(text='NETWORK ERROR', fg='Red')
            self.error_label.pack()
            self.error_label.place(x=200,y=200)
            self.root.after(60*1000, self.on_after)



    ''' Data einfüllen'''
    def update(self):      

        # Uhrzeit ändern
        now = datetime.now()
        self.uhrzeit_text = now.strftime('%H:%M')   
        self.uhrzeit.configure(text=self.uhrzeit_text)
        
        # zur abschätzung wie weit die namen eingerückt sein müssen
        max_line_width = 0
        for dep in self.departures:
            if len(dep['line']) > max_line_width:
                max_line_width = len(dep['line'])

        margin_line = 10
        margin_direction = margin_line + (max_line_width * self.line_text_size / 1.5)  + 30
        margin_min = 400


        i = 0
        for dep in self.departures:
            line_text = ' ' * (max_line_width - len(dep['line'])) + dep['line']
            self.line_label_list[i].configure(text=line_text)
            self.line_label_list[i].place(x=margin_line, y=self.top_margin + i * self.line_text_size * 2)
            
            max_dir = int((margin_min - margin_direction) / self.line_text_size )
            if len(dep['direction']) > max_dir:
                direction_text = dep['direction'][:max_dir] + '…'
            else:
                direction_text = dep['direction']

            self.direction_label_list[i].configure(text=direction_text)
            self.direction_label_list[i].place(x=margin_direction, y=self.top_margin + i * self.line_text_size * 2)

            if dep['arrival'] <= 60:
                min_text = str(dep['arrival'])
                x_offset = 0
            else:
                min_text = str(dep['arrival'] // 60) + 'h ' + str(dep['arrival'] % 60) + 'm'
                x_offset = len(min_text) * self.line_text_size * (-1 / 2)

            self.min_label_list[i].configure(text=min_text)
            self.min_label_list[i].place(x=margin_min + x_offset, y=self.top_margin + i * self.line_text_size * 2)

            i += 1
        
        for j in range(i, 10):
            self.line_label_list[j].configure(text='')
            self.direction_label_list[j].configure(text='')                        
            self.min_label_list[j].configure(text='')





hs = Haltestelle('Albertplatz')
