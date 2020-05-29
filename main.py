import sys, pygame
from pygame.locals import *
from llama import *
from person import *

pygame.init()

screen_info = pygame.display.Info()
screen_size = (screen_info.current_w, screen_info.current_h)

SIGN_image = pygame.image.load("SIGN.png")
SIGN_image = pygame.transform.smoothscale(SIGN_image, (80, 80))
SIGN_rect = SIGN_image.get_rect()
SIGN_rect.center = (screen_info.current_w // 2, screen_info.current_h // 2) 

size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

color = (0, 127, 255)
textColor=(50,254,30)
txtBackgroundColor=(94,0,4)
fishes = pygame.sprite.Group()

Person=Person((150,150))
EVIL_LLAMAS=pygame.sprite.Group()


font=pygame.font.Font('freesansbold.ttf', 32) 
text=font.render("HEEELP!!",True,textColor,txtBackgroundColor)
textRect = text.get_rect() 
textRect.center = (width // 2, height // 2) 


def main():
    for i in range(10):
        EVIL_LLAMAS.add(Llama((width / 2, height / 2)))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                EVIL_LLAMAS.add(llama(event.pos))
            if event.type == KEYUP:
                if event.key == K_UP:
                  Person.speed[1]=0 
                if event.key == K_DOWN:
                  Person.speed[1]=0  
                if event.key==K_LEFT:
                  Person.speed[0]=0
                if event.key==K_RIGHT:
                  Person.speed[0]=0
            if event.type == KEYDOWN:
                if event.key == K_UP:
                  Person.speed[1]=-10 
                if event.key == K_DOWN:
                  Person.speed[1]=10  
                if event.key==K_LEFT:
                  Person.speed[0]=-10
                if event.key==K_RIGHT:
                  Person.speed[0]=10
                
                
                if event.key == K_d:
                    for i in range(len(llamas) // 2):
                        llamas.pop(0)
                if event.key == K_f:
                    pygame.display.set_mode(screen_size, FULLSCREEN)
                if event.key == K_ESCAPE:
                    pygame.display.set_mode(size)

       
        
        screen.fill(color)
        for llama in EVIL_LLAMAS:
            llama.update()
        for llama in EVIL_LLAMAS:
            llama.draw(screen)
        Person.update()
        get_hit=pygame.sprite.spritecollide(Person,EVIL_LLAMAS,False)
        screen.blit(Person.image,Person.rect)
        screen.blit(SIGN_image, SIGN_rect)
        if get_hit:
          screen.blit(text,textRect)
        pygame.display.flip()


if __name__ == '__main__':
    main()