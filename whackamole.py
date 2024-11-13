import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        molex, moley = 0,0
  
        mole_width, mole_height = mole_image.get_size()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    mole_rect = mole_image.get_rect(topleft=(molex, moley))
            
                    if mole_rect.collidepoint(mousepos):

                        molex = random.randrange(0, 640 - mole_width, 32)  
                        moley = random.randrange(0, 512 - mole_height, 32) 
            screen.fill("light green")
            # Draw verticlal lines:
            for i in range(20):
                pygame.draw.line(screen, 'black', (32*i, 0), (32*i, 512))
            #Horizontal:
            for i in range(16):
                pygame.draw.line(screen, 'black', (0, 32*i), (640, 32*i))
            
            screen.blit(mole_image, (molex,moley))

            pygame.display.flip()
            clock.tick(60)
            
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
