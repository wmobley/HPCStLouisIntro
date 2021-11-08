import time

import pygame

from spritesheet import Spritesheet

################################# LOAD UP A BASIC WINDOW #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 960, 540
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
running = True
###########################################################################################

my_spritesheet = Spritesheet('images/Donatello.png')
mikey_spritesheet = Spritesheet('images/Michelangelo.png')
ralph_spritesheet = Spritesheet('images/Raphael.png')
text_idx = []
start_sprite =pygame.image.load("images/floodofCode.PNG").convert()
intro_sprite = pygame.image.load("images/intro.PNG").convert()
techno_sprite = pygame.image.load("images/technodrone.png").convert()
donny = [my_spritesheet.parse_sprite(frame) for frame in (my_spritesheet.data['frames'])]

text_idx.append(len(donny))
mikey = [mikey_spritesheet.parse_sprite(frame) for frame in (mikey_spritesheet.data['frames'])]
text_idx.append(len(mikey))
ralph = [ralph_spritesheet.parse_sprite(frame) for frame in (ralph_spritesheet.data['frames'])]
text_idx.append(len(mikey))

print("leng",len(mikey), len(donny))
font = pygame.font.Font('sound/Pixel_NES.otf', 26)

# create a text surface object,
# on which text is drawn on it.
green = (0, 255, 0)
blue = (0, 0, 128)


# create a rectangular object for the
imagelist = [
    {"character": donny, "name": "Ana Olvers", "title": "Production Developer", "spritesheet": my_spritesheet,
              "names": list(my_spritesheet.data['frames']),
     "headshots":pygame.image.load("images/Ana.png").convert()},
             {"character": mikey, "name": "Charles Gaffney", "title": "Geospatial Datascience",
              "spritesheet": mikey_spritesheet, "names": list(mikey_spritesheet.data['frames']),
              "headshots":pygame.image.load("images/charles.png").convert()},
             {"character": ralph, "name": "Tyler Jackson", "title": "Writer & Designer",
              "spritesheet": ralph_spritesheet, "names": list(ralph_spritesheet.data['frames']),
            "headshots":pygame.image.load("images/tyler.png").convert()
              }]
index = -1
character = 0
pygame.mixer.init()
pygame.mixer.music.load('sound/TMNT_Title.wav')
pygame.mixer.music.play(-1)
def text(text, x, y ):
    text = font.render(text, True, (255,255,255), (0,0,0))
    textRect = text.get_rect()
    textRect.center = (x, y)
    canvas.blit(text, textRect)
    window.blit(canvas, (0, 0))
    pygame.display.update()

while running:

    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            ############### UPDATE SPRITE IF SPACE IS PRESSED #################################
            if event.key == pygame.K_SPACE:
                pass


    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.fill((0, 0, 0))
    if index == -1:
        index+=1
        start_sprite= pygame.transform.rotozoom(start_sprite, 0,.3)
        start_rect = start_sprite.get_rect()
        start_rect.center =(DISPLAY_W/2,DISPLAY_H*.3)
        canvas.blit(start_sprite,start_rect )

        ##start text
        text("start", DISPLAY_W * .5, DISPLAY_H * .66)


        time.sleep(2)
        canvas.fill((0, 0, 0))
        text("Three turtles living in the sewers of St. Louis", DISPLAY_W * .5, DISPLAY_H * .2)
        text("were exposed to radioactive programming", DISPLAY_W * .5, DISPLAY_H * .4)
        text("and became mutant coders over night...", DISPLAY_W * .5, DISPLAY_H * .6)
        time.sleep(4)
        canvas.fill((0, 0, 0))
        text("These mutant coders noticed", DISPLAY_W * .5, DISPLAY_H * .2)
        text("the rising water in their sewers and streets", DISPLAY_W * .5, DISPLAY_H * .3)
        text("And the dangers it posed...", DISPLAY_W * .5, DISPLAY_H * .45)

        text("But they knew they could protect ", DISPLAY_W * .5, DISPLAY_H * .65)
        text("all those who traveled the city...", DISPLAY_W * .5, DISPLAY_H * .75)
        time.sleep(6)
        canvas.fill((0, 0, 0))
        text("With their new powers they tracked the floods", DISPLAY_W * .5, DISPLAY_H * .2)
        text("to warn where the waters were highest...", DISPLAY_W * .5, DISPLAY_H * .4)
        time.sleep(4)
        canvas.fill((0, 0, 0))
        text("The adventure of ", DISPLAY_W * .5, DISPLAY_H * .2)
        text("the Teenage Mutant Flood Coders", DISPLAY_W * .5, DISPLAY_H * .4)
        text(" starts now...", DISPLAY_W * .5, DISPLAY_H * .6)
        time.sleep(4)



    else:
        index = (index + 1)
        canvas.blit(imagelist[character]['character'][index], (

        imagelist[character]["spritesheet"].data['frames'][imagelist[character]['names'][index]]['location']['x'],
        imagelist[character]["spritesheet"].data['frames'][imagelist[character]['names'][index]]['location']['y']))
        name = []

        if index ==len(imagelist[character]["character"])-1:

            job = font.render(imagelist[character]['title'], True, green, blue)
            # text surface object
            screen_text = font.render(imagelist[character]['name'], True, green, blue)
            textRect = screen_text.get_rect()

            # set the center of the rectangular object.
            textRect.center = (DISPLAY_W * .66, DISPLAY_H * .33)
            jobRect = job.get_rect()

            # set the center of the rectangular object.
            jobRect.center = (DISPLAY_W * .66, DISPLAY_H * .45)

            canvas.blit(screen_text, textRect)
            canvas.blit(job, jobRect)



            index = 0
            window.blit(canvas, (0, 0))
            pygame.display.update()
            time.sleep(2)

            image = pygame.transform.scale(imagelist[character]['headshots'], (200,400))
            canvas.blit(image, (200,80))

            window.blit(canvas, (0, 0))
            pygame.display.update()
            time.sleep(2)
            character += 1
        else:
            # index += 1
            window.blit(canvas, (0, 0))
            pygame.display.update()
            time.sleep(.3)
        if character ==3:
            canvas.fill((0, 0, 0))
            techno_sprite = pygame.transform.rotozoom(techno_sprite, 0, 1.5)
            techno_rect = techno_sprite.get_rect()
            techno_rect.center = (DISPLAY_W *.85, DISPLAY_H * .25)

            intro_sprite = pygame.transform.rotozoom(intro_sprite, 0, 2)
            intro_rect = intro_sprite.get_rect()
            intro_rect.center = (85, DISPLAY_H * .85)
            canvas.blit(intro_sprite, intro_rect)

            window.blit(canvas, (0, 0))
            pygame.display.update()
            canvas.blit(techno_sprite, techno_rect)
            screen_text = font.render("Mentors", True, green, blue)
            textRect = screen_text.get_rect()

            # set the center of the rectangular object.
            textRect.update((250, DISPLAY_H*.65, 250, 250))
            canvas.blit(screen_text, textRect)
            screen_text = font.render("Will Mobley", True, green, blue)
            textRect = screen_text.get_rect()

            # set the center of the rectangular object.
            textRect.update((250, DISPLAY_H*.75, 250, 250))
            canvas.blit(screen_text, textRect)
            screen_text = font.render("Virginia Trueheart", True, green, blue)
            textRect = screen_text.get_rect()

            # set the center of the rectangular object.
            textRect.update((250, DISPLAY_H*.85, 250, 250))
            canvas.blit(screen_text, textRect)
            window.blit(canvas, (0, 0))
            pygame.display.update()
            time.sleep(5)
            canvas.fill((0, 0, 0))
            text("You guys are great! ", DISPLAY_W * .5, DISPLAY_H * .2)
            text("Let's celebrate with a pizza!", DISPLAY_W * .5, DISPLAY_H * .4)
            time.sleep(3)
            running=False



