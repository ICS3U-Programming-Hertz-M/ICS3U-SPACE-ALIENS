# Created by: hertz 
# Created on: Jun 9 ,2022 
# This program is the "Space Aliens" program on the PyBadge
 
 
import ugame 
import stage
import time
import random
import constants
import supervisor

def game_win_scene(final_score):

    # stop sound
    sound = ugame.audio
    sound.stop()

    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    
    # add text objects that will be displayed on the screeen 
    text = []
    text1 = stage.Text(width=29, height=14 , font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final score: {:0>2d}" .format(final_score))
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move (40, 60)
    text2.text("Wow, you won:)")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer= None)
    text3.move(32,110)
    text3.text("PRESS SELECT")
    text.append(text3)

    game = stage.Stage(ugame.display, constants.FPS)
 
    # creating a background  to show on and set the frame rate to 60fp.
    game.layers = text + [background]
   
    # set the layers of all the sprites
    # the items are shown in order. 
    game.render_block()
    
    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()
        game.tick()
 

# for the game over scene 
def game_over_scene(final_score):

    # stop sound
    sound = ugame.audio
    sound.stop()

    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    
    # add text objects that will be displayed on the screeen 
    text = []
    text1 = stage.Text(width=29, height=14 , font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final score: {:0>2d}" .format(final_score))
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move (43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer= None)
    text3.move(32,110)
    text3.text("PRESS SELECT")
    text.append(text3)

    game = stage.Stage(ugame.display, constants.FPS)
 
    # creating a background  to show on and set the frame rate to 60fp.
    game.layers = text + [background]
   
    # set the layers of all the sprites
    # the items are shown in order. 
    game.render_block()
    
    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()
        game.tick()
 

def splash_scene(): 
 
    coin_sound = open ("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)
    # image banks for circuiption
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
 
    # set the background to image 0 in the image back the size
    #(10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X ,constants.SCREEN_GRID_Y)

    text = []
    text1 = stage.Text(width=29, height=14 , font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(40, 100)
    text1.text("SPACE ALIEN")
    text.append(text1)

    # use this image to split the image into titles: the first 2 numbers prisents x any and
    # then the 3rd number specifies  which exctaly titles to use. 
    background.tile(2, 2, 0)  
 
    background.tile(3, 2, 1)
 
    background.tile(4, 2, 2)
 
    background.tile(5, 2, 3)
 
    background.tile(6, 2, 4)
 
    background.tile(7, 2, 0) 
 
 
 
    background.tile(2, 3, 0)  
 
    background.tile(3, 3, 5)
 
    background.tile(4, 3, 6)
 
    background.tile(5, 3, 7)
 
    background.tile(6, 3, 8)
 
    background.tile(7, 3, 0) 
 
 
 
    background.tile(2, 4, 0) 
 
    background.tile(3, 4, 9)
 
    background.tile(4, 4, 10)
 
    background.tile(5, 4, 11)
 
    background.tile(6, 4, 12)
 
    background.tile(7, 4, 0) 
 
 
 
    background.tile(2, 5, 0)  
 
    background.tile(3, 5, 0)
 
    background.tile(4, 5, 13)
 
    background.tile(5, 5, 14)
 
    background.tile(6, 5, 0)
 
    background.tile(7, 5, 0)
 
    # it will be changed every time we update  frame
    game = stage.Stage(ugame.display, constants.FPS)
 
    # creating a background  to show on and set the frame rate to 60fp.
    game.layers = text + [background]
   
    # set the layers of all the sprites
    # the items are shown in order. 
    game.render_block()
 
    # loop 
    # repeats forever game 
    while True:
        
        # you have to wait for 2 seconds. 
        time.sleep(3.0)
        menu_scene1()
 
def menu_scene1(): 
    # image banks for circuiption
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
 
    # creating a list
    text = []
    #creating  the text and adding width and height of the text and the colour of the text
    text1= stage.Text(width=29 , height=12 , font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20,10)
    text1.text("MT Game Studios")
    # add it to the list
    text.append(text1)
 
    text2 = stage.Text(width=29, height = 12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS B")
    text.append(text2)
 
    # set the background to image 0 in the image back the size
    #(10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X ,constants.SCREEN_GRID_Y)
 
    # it will be changed every time we update  frame
    game = stage.Stage(ugame.display, constants.FPS)
 
    # creating a background  to show on and set the frame rate to 60fp.
    game.layers = text + [background]
   
    # set the layers of all the sprites
    # the items are shown in order. 
    game.render_block()
 
    # loop 
    # repeats forever game 
    while True:
        # user input that display how many a specific button is being pressed
        Keys = ugame.buttons.get_pressed()
 
        if Keys & ugame.K_X != 0:
            menu_scene()
 
        # to make sure we have the 60 frame has occurred 
        game.tick()


       
def menu_scene(): 
    # image banks for circuiption
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
 
    # creating a list
    text = []
    #creating  the text and adding width and height of the text and the colour of the text
    text1= stage.Text(width=29 , height=12 , font=None, palette=constants.NEW_PALETTE, buffer=None)
    text1.move(10,10)
    text1.text("HOW FAST ARE YOU ?")
    # add it to the list
    text.append(text1)
 
    text2 = stage.Text(width=29, height = 12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)
 
    text3 = stage.Text(width=29, height= 12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text3.move(1,40)
    text3.text("GET AS MANY AS U CAN")
    text.append(text3)

    text4 = stage.Text(width=28, height= 10, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text4.move(1,60)
    text4.text("Shot 1, WIN 5 POINTS")
    text.append(text4)

    text5 = stage.Text(width=29, height= 12, font=None, palette=constants.NEW_PALETTE, buffer=None)
    text5.move(2,80)
    text5.text("MISS 1,LOSS A POINT")
    text.append(text5)
    # set the background to image 0 in the image back the size
    #(10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X ,constants.SCREEN_GRID_Y)
 
    # it will be changed every time we update  frame
    game = stage.Stage(ugame.display, constants.FPS)
 
    # creating a background  to show on and set the frame rate to 60fp.
    game.layers = text + [background]
   
    # set the layers of all the sprites
    # the items are shown in order. 
    game.render_block()
 
    # loop 
    # repeats forever game 
    while True:
        # user input that display how many a specific button is being pressed
        Keys = ugame.buttons.get_pressed()
 
        if Keys & ugame.K_START != 0:
            game_scene()
 
        # to make sure we have the 60 frame has occurred 
        game.tick()
 
def game_scene(): 

    # showing the score earned. 
    score = 0

    # text showing the score you got.
    score_text = stage.Text(width = 29, height = 14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("sore: {0}". format(score))
 
    def show_alien():
        # This function checks the aliens in the list and if it is less than zero
        # it makes sure it  moves on the screen. 
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                                         constants.SCREEN_X - constants.SPRITE_SIZE),
                                          constants.OFF_TOP_SCREEN)
                break
    # image banks for circuiption
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
 
    # buttons used 
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
 
    #including sound
    pew_sound = open("pew.wav", 'rb')
    boom_sound = open("boom.wav", 'rb')
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
 
    # set the background to image 0 in the image back the size
    #(10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X ,constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)
 
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE ) )
 
    # create list of aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS) :
        a_single_alien = stage.Sprite(image_bank_sprites, 9,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    show_alien()
 
    # creating lasers to come towards us 
    lasers = []
    for lasers_number in range (constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)
 
    # this is a sprite
    # it will be changed every time we update  frame
    game = stage.Stage(ugame.display, constants.FPS)
 
    # all the images that are  shown on the screen.
    game.layers = [score_text] + lasers + [ship] + aliens + [background]
   
    # set the layers of all the sprites
    # the items are shown in order. 
    game.render_block()
 
    # loop 
    # repeats forever game 
    while True:
        # user input that display how many a specific button is being pressed
        Keys = ugame.buttons.get_pressed()
 
        # setting A button when it should make a sound and when it shouldn't. 
        if Keys & ugame.K_O != 0 :
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
 
            elif a_button == constants.button_state["button_just_pressed"]:
                sound.play(pew_sound)
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if Keys & ugame.K_X:
            pass
        if Keys & ugame.K_START:
            pass
        if Keys & ugame.K_SELECT:
            pass
        if Keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1 , ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE , ship.y)
        if Keys & ugame.K_LEFT:
            if ship.x >= 0 : 
               ship.move(ship.x - 2 , ship.y)
            else:
                ship.move(0 , ship.y)
        if Keys & ugame.K_UP: 
           pass
        if Keys & ugame.K_DOWN:
            pass
        # play sound if A was just button _just_pressed       
        if a_button == constants.button_state["button_just_pressed"]:
            # firing the layers. 
            for lasers_number in range(len(lasers)):
                if lasers[lasers_number].x < 0:
                    lasers[lasers_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        # moving the lasers upwards that have been fired up.
        for lasers_number in range(len(lasers)):
            if lasers[lasers_number].x > 0:
                lasers[lasers_number].move(lasers[lasers_number].x,
                                          lasers[lasers_number].y - constants. LASER_SPEED)
                if lasers[lasers_number].y <  constants.OFF_TOP_SCREEN:
                    lasers[lasers_number].move(constants.OFF_SCREEN_X,
                                             constants.OFF_SCREEN_Y)
        # moving the aliens downwards if the aliens are shown  on the screen.
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x,
                                          aliens[alien_number].y +
                                            constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("score {0}" .format(score))

        #checking if  any of the lasers are tounching any of the aliens.
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                         lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                         aliens[alien_number].x +1, aliens[alien_number].y,
                                         aliens[alien_number].x +15, aliens[alien_number].y + 15):
                            # when you hit an allien 
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers [laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 5
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("score:{0}" .format(score))
                            if score > 20:
                                game_win_scene(score)
                                

        # checking if any aliens are touching the space ship
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                 aliens[alien_number].x +15, aliens[alien_number].y + 15 ,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):

                    # if the aliens hit the ship 
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(3.0)
                    game_over_scene(score)

    # turning off the sound 
        # moving the images as programed on the screen 
        game.render_sprites(lasers + [ship] + aliens )
        # to make sure we have the 60 frame has occurred 
        game.tick()
 
if __name__ == "__main__":
    splash_scene()
