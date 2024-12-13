from tkinter import*
def main():
    print('--> start <--')
    mainwin = Tk()
    wcan = Canvas (mainwin, bg='white',
    width = 600, height = 800)

    wcan.create_oval(100, 100, 500, 500,
    fill = 'white', outline = 'green', width = 5)

    points = [400, 450, 200, 450, 300, 550]
    wcan.create_polygon(points, outline = 'black',
    fill = 'white', width = 10)
    wcan.pack()
    wcan.create_line(400, 330, 200, 330, width = 30, fill = 'yellow')
    wcan.create_oval(325, 170, 430, 270,
    fill = 'blue', outline = 'black', width = 5)
    wcan.create_oval(270, 270, 170, 170,
    fill = 'red', outline = 'black', width = 5)
    mainwin.mainloop()
main()
