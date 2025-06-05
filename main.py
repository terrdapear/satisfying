import pygame


#important shit
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption("TITLE")



def main():
    state = "Menu"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        pygame.display.update()
        clock.tick(60)
    


main()
pygame.quit()