from tkinter import *
from PIL import ImageTk, Image
import normalChampPage


def create_auto_button(c, w, gui):
    """
    :param c: the canvas
    :param w: width of the canvas
    :param gui: the actually gui overall
    :return: creates button that leads to auto page
    """
    auto_button = Button(gui, text='Auto Game Starter')
    auto_button.configure(fg='#D4AF37', bg='black', activebackground='white', cursor='trek')
    auto_button_window = c.create_window(w/2, 100, window=auto_button)


def create_normal_button(c, w, gui):
    """
    :param c: the canvas
    :param w: width of the canvas
    :param gui: the actually gui overall
    :return: creates button that leads to normal page
    """

    def open_new_window():
        gui.destroy()
        normalChampPage.normal_champ_window()

    normal_button = Button(gui, text='Does same stuff as all other league apps', command=open_new_window)
    normal_button.configure(fg='#D4AF37', bg='black', activebackground='white', cursor='trek')
    normal_button_window = c.create_window(w/2, 170, window=normal_button)


def create_title(c, w):
    """
    :param c: the canvas
    :param w: width of the canvas
    :return: creates title returns none
    """

    title_text = 'Look Its Blitz With No Ads Please Use Me I Have No Ads'
    title = c.create_text(w / 2, 30, text=title_text, font="50", fill='#D4AF37')
    title_bbox = c.bbox(title)
    rect_item = c.create_rectangle(title_bbox, outline="red", fill="black")
    c.tag_raise(title, rect_item)


def main():

    gui = Tk(className='League Is Garbage')
    gui.iconbitmap("../icons/dota.ico")

    # set canvas and create background images
    bg_img = ImageTk.PhotoImage(Image.open("../Images/backgrounds/guiMainBg.png"))
    w = bg_img.width()
    h = bg_img.height()
    c = Canvas(gui, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
    c.pack()
    c.create_image(int(w/2), int(h/2), image=bg_img)

    # code that adds features to the canvas
    create_title(c, w)
    create_auto_button(c, w, gui)
    create_normal_button(c, w, gui)

    gui.mainloop()


if __name__ == '__main__':
    main()
