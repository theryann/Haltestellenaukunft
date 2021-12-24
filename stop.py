import dvb
from tkinter import *

class Haltestelle:

    def __init__(self, haltestelle='Alberplatz'):
        self.stop = haltestelle

    def show(self):
        time_offset = 0
        num_results = 10
        city = 'Dresden'

        departures = dvb.monitor(self.stop, time_offset, num_results, city)

        # zur abschätzung wie weit die namen eingerückt sein müssen
        max_line_width = 0
        for dep in departures:
            if len(dep['line']) > max_line_width:
                max_line_width = len(dep['line'])


        # Window
        bg_color ="#101010"     #Globale Hintergrundfarbe

        root = Tk()
        root.title("Rubik's Cube")
        root.geometry("500x507+600+200")
        root.configure(background=bg_color)

        # Attriblutes
        font_face = "Arial"
        line_text_size = 20
        top_margin = 60
        margin_line = 10
        margin_direction = margin_line + max_line_width * line_text_size / 2.0  + 20
        margin_min = 400

        # Pivot Haltestelle
        haltestelle_text = Label(text = self.stop, fg = "Yellow", bg=bg_color, font=(font_face, 30))
        haltestelle_text.pack()

        # Abfahrten
        for line in departures:

            line_label = Label(text = line['line'], fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
            line_label.pack()
            line_label.place(x=margin_line, y=top_margin)

            direction_label = Label(text = line['direction'], fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
            direction_label.pack()
            direction_label.place(x=margin_direction, y=top_margin)


            if line['arrival'] <= 60:
                min_text = str(line['arrival'])
                x_offset = 0
            else:
                min_text = str(line['arrival'] // 60) + 'h ' + str(line['arrival'] % 60) + 'm'
                x_offset = len(min_text) * line_text_size * (-1 / 2)

            min_label = Label(text = min_text, fg = "Yellow", bg=bg_color, font=(font_face, line_text_size))
            min_label.pack()
            min_label.place(x=margin_min + x_offset, y=top_margin)

            top_margin += line_text_size * 2

        # Mainloop
        root.mainloop()


hs2 = Haltestelle('Albertplatz')
hs2.show()
hs = Haltestelle('Tronitzer Straße')
hs.show()