import random, pygame, sys
from pygame.locals import *
#ygvtcf
FPS = 15
WINDOWWIDTH = 840
WINDOWHEIGHT = 680

WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
DARKGREEN   = (  0, 155,   0)
DARKGRAY    = ( 40,  40,  40)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

object1_selected = False
object2_selected = False
object3_selected = False
object4_selected = False
object5_selected = False
object6_selected = False
object7_selected = False
object8_selected = False
object9_selected = False

room = 0

inventory = []

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Final Game')
    
    pygame.mixer.music.load('soundtrack.wav')
    pygame.mixer.music.play(-1)
    
    showStartScreen()
    
    while True:
        runGame()
        showGameOverScreen()
        
    


def runGame():
   global object1_selected
   global object2_selected
   global object3_selected
   global object4_selected
   global object5_selected
   global object6_selected
   global object7_selected
   global object8_selected
   global object9_selected
   global  room
   
   while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()                          
        
        if room == 0:                        
            
            potion = "potion.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            object1_pos_x = 500
            object1_pos_y = 550
            
            door_pos_x = 740
            door_pos_y = 0
            
            object1_size_x = 40
            object1_size_y = 40

            door_size_x = 100
            door_size_y = 680
            
            
            DISPLAYSURF.blit(pygame.image.load("room1.png"), (0,0))
            DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,100))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 150)
            roomNameSurf = roomNameFont.render('Bar', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 180)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
            
            if object1_pos_x < mouse[0] <  object1_pos_x + object1_size_x and object1_pos_y < mouse[1] < object1_pos_y + object1_size_y:
                if click[0] == 1:  
                    inventory.append(potion)
                    object1_selected = True
                    print("Object 1")
                    print(inventory[0])
                    
            
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Kathleen’s Room", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 1
            
                
            if object1_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(potion), (object1_size_x, object1_size_y)), (object1_pos_x, object1_pos_y))
            elif object1_selected == True:
                None            
        
            if len(inventory) != 0:
                pos = 115
                for item in inventory:
                    DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                    pos += 35
        
        
        elif room == 1:                        
            

            paper = "paper.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            object2_pos_x = 300
            object2_pos_y = 530

            object2_size_x = 40
            object2_size_y = 40
            
            DISPLAYSURF.blit(pygame.image.load("room2.png"), (0,0))
            DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,100))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 150)
            roomNameSurf = roomNameFont.render('Kathleen’s Room', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 180)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
 
            if object2_pos_x < mouse[0] <  object2_pos_x + object2_size_x and object2_pos_y < mouse[1] < object2_pos_y + object2_size_y:
                if click[0] == 1:  
                    inventory.append(paper)
                    object2_selected = True
                    print("Object 2")
                    print(inventory[0])
                    
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Mia’s Room", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 2
          
          
            if object2_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(paper), (object2_size_x, object2_size_y)), (object2_pos_x, object2_pos_y))
            elif object2_selected == True:
                None
        
            if len(inventory) != 0:
                pos = 115
                for item in inventory:
                    DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                    pos += 35
        
        elif room == 2:                        
            

            paper = "paper.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            object3_pos_x = 300
            object3_pos_y = 530

            object3_size_x = 40
            object3_size_y = 40
            
            DISPLAYSURF.blit(pygame.image.load("room2.png"), (0,0))
            DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,100))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 150)
            roomNameSurf = roomNameFont.render('Mia’s Room', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 180)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
 
            if object3_pos_x < mouse[0] <  object3_pos_x + object3_size_x and object3_pos_y < mouse[1] < object3_pos_y + object3_size_y:
                if click[0] == 1:  
                    inventory.append(paper)
                    object3_selected = True
                    print("Object 3")
                    print(inventory[0])
                    
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Ubel’s Room", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 3
          
          
            if object3_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(paper), (object2_size_x, object2_size_y)), (object2_pos_x, object2_pos_y))
            elif object3_selected == True:
                None
        
            if len(inventory) != 0:
                pos = 115
                for item in inventory:
                    DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                    pos += 35
           
        
        elif room == 3:                        
            
            potion = "potion.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            object4_pos_x = 500
            object4_pos_y = 550
            
            door_pos_x = 740
            door_pos_y = 0
            
            object4_size_x = 40
            object4_size_y = 40

            door_size_x = 100
            door_size_y = 680
            
            DISPLAYSURF.blit(pygame.image.load("room1.png"), (0,0))
            DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,100))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 150)
            roomNameSurf = roomNameFont.render('Ubel’s Room', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 180)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
            
            if object4_pos_x < mouse[0] <  object4_pos_x + object4_size_x and object4_pos_y < mouse[1] < object4_pos_y + object4_size_y:
                if click[0] == 1:  
                    inventory.append(potion)
                    object4_selected = True
                    print("Object 4")
                    print(inventory[0])
                    
            
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Kitchen", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 4
            
                
            if object4_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(potion), (object1_size_x, object1_size_y)), (object1_pos_x, object1_pos_y))
            elif object4_selected == True:
                None            
        
            if len(inventory) != 0:
                pos = 115
                for item in inventory:
                    DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                    pos += 35
        
        
        elif room == 4:                        
            

            paper = "paper.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            object5_pos_x = 300
            object5_pos_y = 530

            object5_size_x = 40
            object5_size_y = 40
            
            DISPLAYSURF.blit(pygame.image.load("room2.png"), (0,0))
            DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,100))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 150)
            roomNameSurf = roomNameFont.render('Kitchen', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 180)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
 
            if object5_pos_x < mouse[0] <  object5_pos_x + object5_size_x and object5_pos_y < mouse[1] < object5_pos_y + object5_size_y:
                if click[0] == 1:  
                    inventory.append(paper)
                    object5_selected = True
                    print("Object 5")
                    print(inventory[0])
                    
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Bathroom", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 5
          
          
            if object5_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(paper), (object2_size_x, object2_size_y)), (object2_pos_x, object2_pos_y))
            elif object5_selected == True:
                None
        
            if len(inventory) != 0:
                pos = 115
                for item in inventory:
                    DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                    pos += 35
        
        elif room == 5:                        
            

            paper = "paper.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            object6_pos_x = 300
            object6_pos_y = 530

            object6_size_x = 40
            object6_size_y = 40
            
            DISPLAYSURF.blit(pygame.image.load("room2.png"), (0,0))
            DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,100))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 150)
            roomNameSurf = roomNameFont.render('Bathroom', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 180)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
 
            if object6_pos_x < mouse[0] <  object6_pos_x + object6_size_x and object6_pos_y < mouse[1] < object6_pos_y + object6_size_y:
                if click[0] == 1:  
                    inventory.append(paper)
                    object6_selected = True
                    print("Object 6")
                    print(inventory[0])
                    
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Wine Cellar", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 6
          
          
            if object6_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(paper), (object2_size_x, object2_size_y)), (object2_pos_x, object2_pos_y))
            elif object6_selected == True:
                None
        
            if len(inventory) != 0:
                pos = 115
                for item in inventory:
                    DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                    pos += 35
        
        
        elif room == 6:                        
            

            paper = "paper.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            object7_pos_x = 300
            object7_pos_y = 530

            object7_size_x = 40
            object7_size_y = 40
            
            DISPLAYSURF.blit(pygame.image.load("room2.png"), (0,0))
            DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,100))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 150)
            roomNameSurf = roomNameFont.render('Wine Cellar', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 180)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
 
            if object7_pos_x < mouse[0] <  object7_pos_x + object7_size_x and object7_pos_y < mouse[1] < object7_pos_y + object7_size_y:
                if click[0] == 1:  
                    inventory.append(paper)
                    object7_selected = True
                    print("Object 7")
                    print(inventory[0])
                    
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Lobby", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 7
          
          
            if object7_selected == False:
                DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(paper), (object2_size_x, object2_size_y)), (object2_pos_x, object2_pos_y))
            elif object7_selected == True:
                None
        
            if len(inventory) != 0:
                pos = 115
                for item in inventory:
                    DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                    pos += 35
        
        
        elif room == 7:                        
            

            paper = "paper.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            object8_pos_x = 300
            object8_pos_y = 530

            object8_size_x = 40
            object8_size_y = 40
            
            DISPLAYSURF.blit(pygame.image.load("room2.png"), (0,0))
            DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,100))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 150)
            roomNameSurf = roomNameFont.render('Lobby', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 180)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
 
            if object8_pos_x < mouse[0] <  object8_pos_x + object8_size_x and object8_pos_y < mouse[1] < object8_pos_y + object8_size_y:
                if click[0] == 1:  
                    inventory.append(paper)
                    object8_selected = True
                    print("Object 8")
                    print(inventory[0])
                    
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Basement", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 8
                
            if len(inventory) != 0:
                pos = 115
                for item in inventory:
                    DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                    pos += 35
        
        
        elif room == 8:                        
            

            paper = "paper.png"
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            object9_pos_x = 300
            object9_pos_y = 530

            object9_size_x = 40
            object9_size_y = 40
            
            DISPLAYSURF.blit(pygame.image.load("room2.png"), (0,0))
            DISPLAYSURF.blit(pygame.image.load("inventory.png"), (0,100))
            
            roomNameFont = pygame.font.Font('freesansbold.ttf', 150)
            roomNameSurf = roomNameFont.render('Basement', True, WHITE)
            roomNameRect = roomNameSurf.get_rect()
            roomNameRect.midtop = (WINDOWWIDTH / 2, 180)
            
            DISPLAYSURF.blit(roomNameSurf, roomNameRect)  
 
            if object9_pos_x < mouse[0] <  object9_pos_x + object9_size_x and object9_pos_y < mouse[1] < object9_pos_y + object9_size_y:
                if click[0] == 1:  
                    inventory.append(paper)
                    object9_selected = True
                    print("Object 9")
                    print(inventory[0])
                    
            elif door_pos_x < mouse[0] <  door_pos_x + door_size_x and door_pos_y < mouse[1] < door_pos_y + door_size_y:
                doorSurf = BASICFONT.render("Bar", True, WHITE)
                doorRect = doorSurf.get_rect()
                doorRect.topleft = (700, 340)
                DISPLAYSURF.blit(doorSurf, doorRect)
                if click[0] == 1: 
                    room = 0
           
            if len(inventory) != 0:
                pos = 115
                for item in inventory:
                    DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load(item), (25,25)), (10, pos))
                    pos += 35
        
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        

    
def terminate():
    pygame.quit()
    sys.exit()



def showStartScreen():
    back = pygame.image.load("back.png")
    DISPLAYSURF.blit(back, (0,0))
    i = 0
    while True:         
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button1_pos_x = 340
        button1_pos_y = 320
        
        button2_pos_x = 340
        button2_pos_y = 420
        
        button3_pos_x = 340
        button3_pos_y = 520
        
        size_x = 200
        size_y = 80
        
        bt1 = pygame.image.load("button1.png")
        bt1p = pygame.image.load("button1p.png")    
        bt2 = pygame.image.load("button2.png")
        bt2p = pygame.image.load("button2p.png")
        bt3 = pygame.image.load("button3.png")
        bt3p = pygame.image.load("button3p.png") 
        
        if button1_pos_x < mouse[0] <  button1_pos_x + size_x and button1_pos_y < mouse[1] < button1_pos_y + size_y:
            if click[0] == 1:
                DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
                DISPLAYSURF.blit(bt2p, (button2_pos_x, button2_pos_y))
                DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
                print("Button 1")
                i = 0
                #return
        elif button2_pos_x < mouse[0] <  button2_pos_x + size_x and button2_pos_y < mouse[1] < button2_pos_y + size_y:
            if click[0] == 1:
                DISPLAYSURF.blit(bt1p, (button1_pos_x, button1_pos_y))
                DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
                DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
                print("Button 2")
                i = 1
                #return
        elif button3_pos_x < mouse[0] <  button3_pos_x + size_x and button3_pos_y < mouse[1] < button3_pos_y + size_y:
            if click[0] == 1:
                DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
                DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
                DISPLAYSURF.blit(bt3p, (button3_pos_x, button3_pos_y))
                print("Button 3")
                i = 2
                #return
            
           
        if i == 0:
            DISPLAYSURF.blit(bt1p, (button1_pos_x, button1_pos_y))
            DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
            DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
        elif i == 1:
            DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
            DISPLAYSURF.blit(bt2p, (button2_pos_x, button2_pos_y))
            DISPLAYSURF.blit(bt3, (button3_pos_x, button3_pos_y))
        elif i == 2:
            DISPLAYSURF.blit(bt1, (button1_pos_x, button1_pos_y))
            DISPLAYSURF.blit(bt2, (button2_pos_x, button2_pos_y))
            DISPLAYSURF.blit(bt3p, (button3_pos_x, button3_pos_y))
           
        for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                if event.type == KEYDOWN:        
                         if (event.key == K_DOWN):
                           if i == 2:
                               i = 0
                           else: 
                               i += 1
                         if (event.key == K_UP):
                                   if i == 0:
                                       i = 2
                                   else: 
                                       i -= 1
                                 
                         if (event.key == K_RETURN) and i == 0:  
                             return 
                         elif (event.key == K_RETURN) and i == 1:
                                return
                         elif (event.key == K_RETURN) and i == 2:
                                terminate()
                       
        
        
        FPSCLOCK.tick(FPS)
        pygame.display.update() 
        
def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate
            else:
                return True



def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render("Press any key to play...", True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect() 
    pressKeyRect.bottomright = (WINDOWWIDTH - 10, WINDOWHEIGHT - 10)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

if __name__ == '__main__':
    main()
