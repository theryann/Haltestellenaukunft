import dvb
from tkinter import *

class Haltestelle:

    def __init__(self, haltestelle='Alberplatz'):
        self.stop = haltestelle
        self.departures = dvb.monitor(self.stop, 0, 10, 'Dresden')

    def on_after(self):

        self.departures = dvb.monitor(self.stop, 0, 10, 'Dresden')
        self.show()


    def show(self):
        


        # Window
        bg_color ="#101010"     #Globale Hintergrundfarbe

        root = Tk()
        root.title("Abfahrten")
        root.geometry("500x507+600+200")
        root.configure(background=bg_color)

        # Attriblutes
        font_face = "Courier New"
        line_text_size = 20
        top_margin = 60
        

        # Pivot Haltestelle
        haltestelle_text = Label(text = self.stop, fg = "Yellow", bg=bg_color, font=(font_face, 30))
        haltestelle_text.pack()

        ''' Labels anbringen '''

        # 1
        line_label_1 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_1.pack()
        line_label_1.place(x=10, y=top_margin)
        direction_label_1 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_1.pack()
        direction_label_1.place(x=10, y=top_margin)
        min_label_1 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_1.pack()
        min_label_1.place(x=10, y=top_margin)
        # 2
        line_label_2 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_2.pack()
        line_label_2.place(x=10, y=top_margin)
        direction_label_2 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_2.pack()
        direction_label_2.place(x=10, y=top_margin)
        min_label_2 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_2.pack()
        min_label_2.place(x=10, y=top_margin)
        # 3
        line_label_3 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_3.pack()
        line_label_3.place(x=10, y=top_margin)
        direction_label_3 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_3.pack()
        direction_label_3.place(x=10, y=top_margin)
        min_label_3 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_3.pack()
        min_label_3.place(x=10, y=top_margin)
        # 4
        line_label_4 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_4.pack()
        line_label_4.place(x=10, y=top_margin)
        direction_label_4 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_4.pack()
        direction_label_4.place(x=10, y=top_margin)
        min_label_4 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_4.pack()
        min_label_4.place(x=10, y=top_margin)
        # 5
        line_label_5 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_5.pack()
        line_label_5.place(x=10, y=top_margin)
        direction_label_5 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_5.pack()
        direction_label_5.place(x=10, y=top_margin)
        min_label_5 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_5.pack()
        min_label_5.place(x=10, y=top_margin)
        # 6
        line_label_6 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_6.pack()
        line_label_6.place(x=10, y=top_margin)
        direction_label_6 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_6.pack()
        direction_label_6.place(x=10, y=top_margin)
        min_label_6 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_6.pack()
        min_label_6.place(x=10, y=top_margin)
        # 7
        line_label_7 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_7.pack()
        line_label_7.place(x=10, y=top_margin)
        direction_label_7 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_7.pack()
        direction_label_7.place(x=10, y=top_margin)
        min_label_7 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_7.pack()
        min_label_7.place(x=10, y=top_margin)
        # 8
        line_label_8 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_8.pack()
        line_label_8.place(x=10, y=top_margin)
        direction_label_8 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_8.pack()
        direction_label_8.place(x=10, y=top_margin)
        min_label_8 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_8.pack()
        min_label_8.place(x=10, y=top_margin)
        # 9
        line_label_9 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_9.pack()
        line_label_9.place(x=10, y=top_margin)
        direction_label_9 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_9.pack()
        direction_label_9.place(x=10, y=top_margin)
        min_label_9 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_9.pack()
        min_label_9.place(x=10, y=top_margin)
        # 10
        line_label_10 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        line_label_10.pack()
        line_label_10.place(x=10, y=top_margin)
        direction_label_10 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        direction_label_10.pack()
        direction_label_10.place(x=10, y=top_margin)
        min_label_10 = Label(text = '', fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
        min_label_10.pack()
        min_label_10.place(x=10, y=top_margin)


        line_label_list = [line_label_1, line_label_2, line_label_3, line_label_4, line_label_5, line_label_6, line_label_7, line_label_8, line_label_9, line_label_10]
        direction_label_list = [direction_label_1, direction_label_2, direction_label_3, direction_label_4, direction_label_5, direction_label_6, direction_label_7, direction_label_8, direction_label_9, direction_label_10]
        min_label_list = [min_label_1, min_label_2, min_label_3, min_label_4, min_label_5, min_label_6, min_label_7, min_label_8, min_label_9, min_label_10]

        
        ''' Data einfüllen'''
        
        # zur abschätzung wie weit die namen eingerückt sein müssen
        max_line_width = 0
        for dep in self.departures:
            if len(dep['line']) > max_line_width:
                max_line_width = len(dep['line'])

        margin_line = 10
        margin_direction = margin_line + (max_line_width * line_text_size / 1.5)  + 30
        margin_min = 400

        i = 0
        for dep in self.departures:
            line_text = ' ' * (max_line_width - len(dep['line'])) + dep['line']
            line_label_list[i].configure(text=line_text)
            line_label_list[i].place(x=margin_line, y=top_margin + i * line_text_size * 2)
            
            direction_label_list[i].configure(text=dep['direction'])
            direction_label_list[i].place(x=margin_direction, y=top_margin + i * line_text_size * 2)

            if dep['arrival'] <= 60:
                min_text = str(dep['arrival'])
                x_offset = 0
            else:
                min_text = str(dep['arrival'] // 60) + 'h ' + str(dep['arrival'] % 60) + 'm'
                x_offset = len(min_text) * line_text_size * (-1 / 2)

            min_label_list[i].configure(text=min_text)
            min_label_list[i].place(x=margin_min + x_offset, y=top_margin + i * line_text_size * 2)


            i += 1


        # Mainloop
        root.mainloop()


# hs2 = Haltestelle('Albertplatz')
# hs2.show()
hs = Haltestelle('Tronitzer Straße')
hs.show()