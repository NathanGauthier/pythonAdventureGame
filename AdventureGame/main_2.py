import pygame, sys
from sprite import Sprite
import math
from sprite_controlled import SpriteControlled

def main():
    #Load
    pygame.init()
    
    screen = pygame.display.set_mode((800,600))
    font = pygame.font.Font(None,24)
    hero = SpriteControlled(100,435,"Sprite.png",2)
                                                    #OOP SPRITE
    copain = Sprite(500,435,"copain.png")

    #spr_surface=pygame.image.load("Sprite.png").convert()
    background = pygame.image.load("background.png").convert()
    ground = pygame.image.load("ground.png").convert()


    #copain

    #copain_x, copain_y = 500, 435
    #copain_surface=pygame.image.load("copain.png").convert()
    collision_text = font.render("Oops, sorry Mamen",False, (0, 0, 0))



    


    cursor = Sprite(0,0,"cursor.jpg")

    spr_is_moving = False
    
    spr_x, spr_y = 100, 435
    spr_speed = 1
    goal_x = 0
  
    #cursor = pygame.image.load("D:\\Nathan_Gauthier\\Exercices\\AdventureGame\\cursor.jpg").convert_alpha()
    pygame.mouse.set_visible(False)
  
    quit = False

    while not(quit):
        #Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True 
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                player.move_to(mouse_click[0])

                
                
                # mouse_click_pos=pygame.mouse.get_pos()
                #hero.set_position(mouse_click)
               
                
                    
                    


        #Update

        cursor_pos = pygame.mouse.get_pos()
        cursor.set_position(cursor_pos)

        

        if(spr_is_moving):
            #spr_pos = mouse_click

            if(spr_x < goal_x): 
                spr_x = spr_x + spr_speed 
            if(spr_x > goal_x): 
                spr_x = spr_x - spr_speed 
            if(math.fabs(goal_x - spr_x) < spr_speed): 
                spr_is_moving = False 
            
            
            
           
            
            #spr_x = mouse_click[0]

      


         #Draw
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(ground, (0,500))
        screen.blit(spr_surface, (spr_x, spr_y))
        
        copain.draw(screen)
        hero.draw(screen)
        if(hero.intersects(copain)):                                           #OOP
            screen.blit(collision_text, (spr_x, spr_y - 100)) 



        
        #x1, y1, w1, h1 = spr_x, spr_y, spr_surface.get_width(), spr_surface.get_height() 
        #x2, y2, w2, h2 = copain_x, copain_y, copain_surface.get_width(), copain_surface.get_height() 
       # if(not(x1+ w1<x2 or x2 + w2<x1 or y1 + 61 < y2 or y2 + 2 < y1)): 
            #screen.blit(collision_text, (spr_x, spr_y - 100)) 

        #screen.blit(copain_surface, ( copain_x, copain_y))
        cursor.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()