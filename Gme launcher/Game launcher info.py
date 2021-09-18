import tkinter as tk
from tkinter import ttk
from tkinter import *
import PIL
from PIL import ImageTk, Image 

FULL_fortnite_DESC = 'Fortnite is an online video game developed by Epic Games \n  and released in 2017.  \n  It is available in three distinct game mode versions that\n   otherwise share the same general gameplay and game engine: \n  Fortnite: Save The world - battle royale  \n   Battle royale: 100 players get deployed in a small map \n  where they can collect guns-materials and fight\n last man wins!! ' 
fortnite_FACT = 'My opinion: Og fortnite is the best game in gaming History no cap . \n It got destroyed by the toxic-childish community ;() '

FULL_pubg_DESC = ' Battlegrounds is a player versus player shooter game in which\n  up to one hundred players fight in a battle royale,\n  a type of large-scale last man standing\n   deathmatch where players fight to remain the last alive\n.      Players can choose to enter the match \n      solo, duo, or with a small team of up to four people.\n The last person or team alive wins the match.'
pubg_FACT = ' My opinion: If u want a realistic battle royale game WITHOUT HACKERS-BUGS!\n   PUBG is waiting for you ;)'

FULL_rocket_DESC = 'The legendary FIFA series has been produced  \n by EA SPORTS for over 20 years, and is now the largest \nsports video game  franchise on the planet. \n \n  FIFA brings The World’s Game to life, letting you play with  \nthe biggest leagues, clubs,  \n    and players in world football, \n all with incredible detail and realism.'
rocket_FACT = ' My opinion : Back in the days it was insane, fifa 14-15-16 were legendary but ea chose money over the quility of game '

FULL_fifa_DESC = '  Rocket League is a fantastical sport-based video game\n,  developed by Psyonix (it’s “soccer with cars”). \n   It features a competitive game mode based on teamwork and outmaneuvering opponents. \n  Rocket League is rated E for Everyone.'
fifa_FACT = 'My opiniion: Tbh its really great and creative game but i suck in it LOL'

FULL_gta_DESC = 'Grand Theft Auto V is an action-adventure game\n   played from either a third-person or first-person perspective\n    Players complete missions—linear scenarios with set\n   objectives—to progress through the story.\n     Outside of the missions, players may freely \n roam the open world.'
gta_FACT = 'My opinio: One of the best games i have played in my life.\n    The story mode is legendary same as the online mode but i bought every thing in the game LOL'



HEIGHT = 700
WIDTH = 900

root = tk.Tk()
root.title('Welcome to Games info ')

def planet(event):
    planet_type = clicked.get()

    if planet_type == option[0]:                                            # EARTH
        image = Image.open("fn.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()


        earth_label = tk.Label(desc_frame, text=FULL_fortnite_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=fortnite_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        fifp= tk.Label(desc_frame, text='Rating   :   9',font=('Monotype Corsiva', 16), bg='light blue')
        fifp.place(relx=0.2, rely= 0.5, relwidth= 0.5, relheight=0.1)

        item4.pack()




    if planet_type == option[1]:                                            # Jupiter
        image = Image.open("battlegrounds-png-20.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        planet_label = tk.Label(desc_frame, text=FULL_pubg_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        planet_label.pack()

        planet_fact = tk.Label(fact_frame, text=pubg_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        planet_fact.pack(side='left')

        fifp= tk.Label(desc_frame, text='Rating   :   8.19',font=('Monotype Corsiva', 16),bg='light blue')
        fifp.place(relx=0.2, rely= 0.5, relwidth= 0.5, relheight=0.1)



        item4.pack()

    if planet_type == option[2]:                                            # Neptune
        image = Image.open("Ra11964f0eb34dfa7ae9b7fc7fd0add34.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        planet_label = tk.Label(desc_frame, text=FULL_rocket_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        planet_label.pack()

        planet_fact = tk.Label(fact_frame, text=rocket_FACT,font=('Monotype Corsiva', 13), bg='#121212', fg='white')
        planet_fact.pack(side='left')


        fifp= tk.Label(desc_frame, text='Rating   :  7',font=('Monotype Corsiva', 16),bg='light blue')
        fifp.place(relx=0.2, rely= 0.5, relwidth= 0.5, relheight=0.1)

        item4.pack()

    if planet_type == option[3]:                                            # Mars
        image = Image.open("rckt.jpg")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        planet_label = tk.Label(desc_frame, text=FULL_fifa_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        planet_label.pack()

        planet_fact = tk.Label(fact_frame, text=fifa_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        planet_fact.pack(side='left')



        fifp= tk.Label(desc_frame, text='Rating   :   7.5',font=('Monotype Corsiva', 16),bg='light blue')
        fifp.place(relx=0.2, rely= 0.5, relwidth= 0.5, relheight=0.1)

        item4.pack()

    if planet_type == option[4]:                                            # Saturn
        image = Image.open("gta 57.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        earth_label = tk.Label(desc_frame, text=FULL_gta_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=gta_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')


        fifp= tk.Label(desc_frame, text='Rating   :   9.8',font=('Monotype Corsiva', 16),bg='light blue')
        fifp.place(relx=0.2, rely= 0.5, relwidth= 0.5, relheight=0.1)

        item4.pack()

   
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#171717')
canvas.pack()

desc_frame = tk.Frame(root, bg='#121212')              # This should have sliding bar for information
desc_frame.place(relx=0.6, rely=0.1, relheight=0.6, relwidth=0.35)

fact_frame = tk.Frame(root, bg='#121212')
fact_frame.place(relx=0.05, rely=0.72, relheight=0.2, relwidth=0.9)

option = ['Fortnite','Pubg','fifa','Rocket league','GTA V'] # dropdown menu options
clicked = StringVar()
clicked.set(option[0])
drop = OptionMenu(root, clicked, *option)
drop.place(relx=0.1, rely=0.01, relheight=0.05, relwidth=0.3)




button = tk.Button(canvas, text='Get Info')
button.bind('<Button-1>', planet)
button.place(relx=0.4, rely=0.01, relheight=0.05, relwidth=0.1)

text = 'Welcome to the Games App!\n \n \n Choose a games to get started...\n\n\n Project by Its boi ahmad'
text2 = ' my opinions on these games will show up in this box here!'

initial_label2 = tk.Label(fact_frame, text=text2, font=('Monotype Corsiva', 18), bg='#121212', fg='white')
initial_label2.pack(side='left')

initial_label = tk.Label(desc_frame, text=text, font=('Gadugi', 12), bg='#121212', fg='white')
initial_label.pack()

root.mainloop()
