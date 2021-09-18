from ursina import *
import sys


app = Ursina()

camera.orthographic = True
camera.fov = 4
camera.position = (1, 1)
Text.default_resolution *= 2

player = Entity(name='o', color=color.red)
cursor = Tooltip(text="+", color=color.gray, origin=(0,0), scale=4, enabled=True)
cursor.background.color = color.clear
bg = Entity(parent=scene, model='quad', texture='shore', scale=(16,8), z=10, color=color.light_gray)
mouse.visible = False

# create a matrix to store the buttons in. makes it easier to check for victory
board = [[' ' for x in range(3)] for y in range(3)]

for y in range(3):
    for x in range(3):
        b = Button(text=' ',parent=scene, position=(x,y))
        board[x][y] = b

        def on_click(b=b):
            b.text = player.name
            b.color = player.color
            b.collision = False
            check_for_victory()
                

            if player.name == 'o':
                player.name = 'x'
                player.color = color.blue
            else:
                player.name = 'o'
                player.color = color.red

                
            

        b.on_click = on_click



        
        
        

def check_for_victory():
    name = player.name
    draw=(
    (board[0][0].text != " " and board[1][0].text != ' ' and board[2][0].text !=' ') and # across the bottom
    (board[0][1].text != ' ' and board[1][1].text != ' ' and board[2][1].text != ' ') and # across the middle
    (board[0][2].text != ' ' and board[1][2].text != ' ' and board[2][2].text != ' ') and # across the top
    (board[0][0].text != ' ' and board[0][1].text != ' ' and board[0][2].text != ' ') and # down the left side
    (board[1][0].text != ' ' and board[1][1].text != ' ' and board[1][2].text != ' ') and # down the middle
    (board[2][0].text != ' ' and board[2][1].text != ' ' and board[2][2].text != ' ') and # down the right side
    (board[0][0].text != ' ' and board[1][1].text != ' ' and board[2][2].text != ' ') and # diagonal /
    (board[0][2].text != ' ' and board[1][1].text != ' ' and board[2][0].text != ' '))   # diagonal \
    won = (
    (board[0][0].text == name and board[1][0].text == name and board[2][0].text == name) or # across the bottom
    (board[0][1].text == name and board[1][1].text == name and board[2][1].text == name) or # across the middle
    (board[0][2].text == name and board[1][2].text == name and board[2][2].text == name) or # across the top
    (board[0][0].text == name and board[0][1].text == name and board[0][2].text == name) or # down the left side
    (board[1][0].text == name and board[1][1].text == name and board[1][2].text == name) or # down the middle
    (board[2][0].text == name and board[2][1].text == name and board[2][2].text == name) or # down the right side
    (board[0][0].text == name and board[1][1].text == name and board[2][2].text == name) or # diagonal /
    (board[0][2].text == name and board[1][1].text == name and board[2][0].text == name))   # diagonal \

    if won:
        print('winner is:', name)
        destroy(cursor)
        mouse.visible = True
        Panel(z=1, scale=10, model='quad')
        t = Text('draw', scale=3, origin=(0,0), background=True)
        t.create_background(padding=(.5,.25), radius=Text.size/2)
        
        playagn=Button(parent=camera.ui,text='Exit',  scale=.15, text_origin=(0,0),font=4,position=(-.5,.5),color=color.pink)
        playagn.on_click=  application.quit
        destroy(t)
        
        
    elif not won and draw:
        destroy(cursor)
        Panel(z=1, scale=10, model='quad')
        t = Text('draw', scale=3, origin=(0,0), background=True)
        t.create_background(padding=(.5,.25), radius=Text.size/2)
        
        mouse.visible=True
        playagn=Button(parent=camera.ui,text='Exit',  scale=.15, text_origin=(0,0),font=4,position=(-.7,.4),color=color.pink)
        playagn.on_click= application.quit
        destroy(t)
        
        



app.run()