import pygame

class Button:
    def __init__(self, image_path, position, scale = None):
        self.image = pygame.image.load(image_path).convert_alpha()

        if scale:
            self.image = pygame.transform.smoothscale(self.image, scale)
        else:
            self.image = self.image

        self.rect = self.image.get_rect(topleft = position)
        self.pressed = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_pressed(self, event):
        mouse_position = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_position):
            if mouse_pressed and not self.pressed:
                self.pressed = True
                return True
        
        if not mouse_pressed:
            self.pressed = False
        
        return False