from tkinter import *
from PIL import ImageTk, Image
import mainGui


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
    normal_button = Button(gui, text='Does same stuff as all other league apps')
    normal_button.configure(fg='#D4AF37', bg='black', activebackground='white', cursor='trek')
    normal_button_window = c.create_window(w/2, 170, window=normal_button)


def champ_info(c):
    """
    :param c: the canvas
    :return: creates images of hero and its abilities
    """
    global hero_img, ability_q, ability_w, ability_e, ability_r
    hero_img = ImageTk.PhotoImage(Image.open('../Images/Champs/Morgana.png'))
    w_hero = hero_img.width()
    h_hero = hero_img.height()
    x_hero = 75
    y_hero = 160
    c.create_rectangle(x_hero-w_hero/2-3, y_hero-h_hero/2-3, x_hero+w_hero/2+3, y_hero+h_hero/2+3, fill='#D4AF37')
    c.create_image(x_hero, y_hero, image=hero_img)

    # this part needs updating when program figures out what champ ur playing
    ability_q = ImageTk.PhotoImage(Image.open('../Images/Abilites/MorganaQ.png'))
    ability_w = ImageTk.PhotoImage(Image.open('../Images/Abilites/MorganaW.png'))
    ability_e = ImageTk.PhotoImage(Image.open('../Images/Abilites/MorganaE.png'))
    ability_r = ImageTk.PhotoImage(Image.open('../Images/Abilites/MorganaR.png'))
    ability_images = [ability_q, ability_w, ability_e, ability_r]

    w_ability = ability_q.width()
    h_ability = ability_q.height()
    x_ability = 178
    x_ability_spacing = 75
    y_ability = 188
    i = 0
    while i < 4:
        c.create_rectangle(x_ability - w_ability/2 - 3, y_ability - h_ability/2 - 3, x_ability + w_ability/2 + 3,
                           y_ability + h_ability/2 + 3, fill='#D4AF37')
        c.create_image(x_ability, y_ability, image=ability_images[i])
        x_ability += x_ability_spacing
        i += 1


def spell_info(c, gui):
    """
    :param c: the canvas
    :param gui: the actually gui overall
    :return: creates the recommenced spells and build and port it into league
    """

    global smite, flash
    # ability order code
    x = 15
    x_spacing = 64
    y = 270
    i = 0
    ability_order = ['Q', '>', 'W', '>', 'E']  # this part will need to be modified
    while i < 5:
        if i % 2 == 0:
            c.create_rectangle(x, y, x+64, y+64, fill='', outline='#D4AF37')
            c.create_text(x+32, y+32, text=ability_order[i], fill='#D4AF37', font='128')
        else:
            c.create_text(x+32, y+32, text=ability_order[i], fill='#D4AF37', font='128')
        i += 1
        x += x_spacing

    # summoner spell code change the line under it for future
    x += x_spacing*.83
    smite = ImageTk.PhotoImage(Image.open('../Images/Summoner/SummonerSmite.png'))
    flash = ImageTk.PhotoImage(Image.open('../Images/Summoner/SummonerFlash.png'))
    summoner_spells = [smite, flash]

    for i in summoner_spells:
        c.create_rectangle(x-3, y-3, x+67, y+67, fill='#D4AF37')
        c.create_image(x+32, y+32, image=i)
        x += (x_spacing*3)/2

    # Port Button Code
    x += x_spacing/2
    port_button = Button(gui, text='Port Spells')
    port_button.configure(fg='#D4AF37', bg='black', activebackground='white', cursor='trek')
    port_button_window = c.create_window(600, y+32, window=port_button)


def item_info(c, gui):
    """
    :param c: the canvas
    :param gui: the actually gui overall
    :return: creates the recommenced item build and ports it into league
    """
    global item1, item2, item3, item4, item5, item6, item7, item8
    x = 15
    x_spacing = 67
    y = 380
    item1 = ImageTk.PhotoImage(Image.open('../Images/Items/1039.png'))
    item2 = ImageTk.PhotoImage(Image.open('../Images/Items/2031.png'))
    item3 = ImageTk.PhotoImage(Image.open('../Images/Items/1402.png'))
    item4 = ImageTk.PhotoImage(Image.open('../Images/Items/3020.png'))
    item5 = ImageTk.PhotoImage(Image.open('../Images/Items/3151.png'))
    item6 = ImageTk.PhotoImage(Image.open('../Images/Items/3089.png'))
    item7 = ImageTk.PhotoImage(Image.open('../Images/Items/3157.png'))
    item8 = ImageTk.PhotoImage(Image.open('../Images/Items/3135.png'))

    items = [item1, item2, item3, item4, item5, item6, item7, item8]
    for item in items:
        c.create_rectangle(x-3, y-3, x+67, y+67, fill='#D4AF37')
        c.create_image(x+32, y+32, image=item)
        x += x_spacing

    # port button code
    x += x_spacing / 1.5
    port_button = Button(gui, text='Port Items')
    port_button.configure(fg='#D4AF37', bg='black', activebackground='white', cursor='trek')
    port_button_window = c.create_window(600, y + 32, window=port_button)


def rune_info(c, gui):
    """
    :param c: the canvas
    :param gui: the actually gui overall
    :return: creates the recommenced rune page and ports it into league
    """
    global main_tree, main_tree_1_ruin, main_tree_2_ruin, main_tree_3_ruin, main_tree_4_ruin, secondary_tree,\
           secondary_tree_1_ruin, secondary_tree_2_ruin, first_stat, second_stat, third_stat
    x = 32
    y = 520
    x_spacing = 64

    main_tree = ImageTk.PhotoImage(Image.open('../Images/Runes/Styles/7200_Domination.png'))
    main_tree_1_ruin = ImageTk.PhotoImage(Image.open('../Images/Runes/Styles/Domination/DarkHarvest/DarkHarvest.png'))
    main_tree_2_ruin = ImageTk.PhotoImage(Image.open('../Images/Runes/Styles/Domination/CheapShot/CheapShot.png'))
    main_tree_3_ruin = ImageTk.PhotoImage(Image.open('../Images/Runes/Styles/Domination/EyeballCollection/EyeballCollection.png'))
    main_tree_4_ruin = ImageTk.PhotoImage(Image.open('../Images/Runes/Styles/Domination/RavenousHunter/RavenousHunter.png'))
    main_perks = [main_tree, main_tree_1_ruin, main_tree_2_ruin, main_tree_3_ruin, main_tree_4_ruin]

    for perk in main_perks:
        c.create_image(x, y, image=perk)
        x += x_spacing

    x = 32
    y = 600
    secondary_tree = ImageTk.PhotoImage(Image.open('../Images/Runes/Styles/7203_Whimsy.png'))
    secondary_tree_1_ruin = ImageTk.PhotoImage(Image.open('../Images/Runes/Styles/Inspiration/MagicalFootwear/MagicalFootwear.png'))
    secondary_tree_2_ruin = ImageTk.PhotoImage(Image.open('../Images/Runes/Styles/Inspiration/CosmicInsight/CosmicInsight.png'))
    secondary_perks = [secondary_tree, secondary_tree_1_ruin, secondary_tree_2_ruin]

    for perk in secondary_perks:
        c.create_image(x, y, image=perk)
        x += x_spacing

    y += 18
    first_stat = ImageTk.PhotoImage(Image.open('../Images/Runes/StatMods/StatModsAttackSpeedIcon.png'))
    second_stat = ImageTk.PhotoImage(Image.open('../Images/Runes/StatMods/StatModsAdaptiveForceIcon.png'))
    third_stat = ImageTk.PhotoImage(Image.open('../Images/Runes/StatMods/StatModsArmorIcon.png'))
    stats = [first_stat, second_stat, third_stat]

    for stat in stats:
        c.create_image(x, y, image=stat)
        x += x_spacing/2

    # Button Code
    port_button = Button(gui, text='Port Runes')
    port_button.configure(fg='#D4AF37', bg='black', activebackground='white', cursor='trek')
    port_button_window = c.create_window(600, y - 64, window=port_button)


def port_all_button(c, gui):

    port_button = Button(gui, text='Port All')
    port_button.configure(fg='#D4AF37', bg='black', activebackground='white', cursor='trek')
    port_button_window = c.create_window(600, 700, window=port_button)


def return_button(c, gui):

    def back_to_main_menu():
        gui.destroy()
        mainGui.main()

    normal_button = Button(gui, text='Return To Main Menu', command=back_to_main_menu)
    normal_button.configure(fg='#D4AF37', bg='black', activebackground='white', cursor='trek')
    normal_button_window = c.create_window(550, 30, window=normal_button)

def create_title(c, w):
    """
    :param c: the canvas
    :param w: width of the canvas
    :return: creates title returns none
    """

    title_text = 'SnackTime'
    title = c.create_text(183, 50, text=title_text, font=("Helvetica", "50"), fill='#D4AF37')
    title_bbox = c.bbox(title)
    rect_item = c.create_rectangle(title_bbox, outline="red", fill="black")
    c.tag_raise(title, rect_item)


def normal_champ_window():

    gui_normal_champ = Tk(className='League Is Good')
    gui_normal_champ.iconbitmap('../icons/dota.ico')

    # set canvas and create background images
    bg_img = ImageTk.PhotoImage(Image.open('../Images/backgrounds/normalPageBg.jpg'))
    w = bg_img.width()
    h = bg_img.height()
    c = Canvas(gui_normal_champ, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
    c.pack()
    c.create_image(int(w/2), int(h/2), image=bg_img)

    # code that adds features to the canvas
    create_title(c, w)
    champ_info(c)
    spell_info(c, gui_normal_champ)
    item_info(c, gui_normal_champ)
    rune_info(c, gui_normal_champ)
    port_all_button(c, gui_normal_champ)
    return_button(c, gui_normal_champ)

    gui_normal_champ.mainloop()


if __name__ == "__main__":
    normal_champ_window()
