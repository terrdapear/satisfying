import pygame

beats = []

coords = {"up":(1280,77),"down":(1280,643),"center":(640,360)}
feet = {
    "blue":pygame.image.load("assets\images\_feet\_bluefeet.png"),
    "red":pygame.image.load("assets\images\_feet\_redfeet.png"),
    "orange":pygame.image.load("assets\images\_feet\orangefeet.png"),
    "purple":pygame.image.load("assets\images\_feet\purplefeet.png")
        }

songs = {
    "tinikling":{
    "path":"assets\music\_tinikling.mp3",
    "track":[(4768.211920529801, 'x'), (5165.562913907284, 'x'), (5562.913907284767, 'x'), (5960.2649006622505, 'x'), (6357.615894039734, 'x'), (6754.966887417217, 'x'), (7152.3178807947, 'x'), (7549.668874172183, 'x'), (7947.019867549666, 'x'), (9536.4238410596, 'x'), (9933.774834437085, 'z'), (10331.125827814569, 'x'), (10728.476821192053, 'z'), (11125.827814569537, 'x'), (11523.17880794702, 'z'), (11920.529801324505, 'x'), (12317.880794701989, 'z'), (12715.231788079473, 'x'), (14304.635761589409, 'x'), (14701.986754966892, 'z'), (15099.337748344376, 'x'), (15496.68874172186, 'z'), (15894.039735099344, 'x'), (16291.390728476828, 'z'), (16688.741721854312, 'x'), (17086.092715231796, 'z'), (17483.44370860928, 'x')]
    }
}

class beat:
    def __init__(self,place,color): # "place" can only be "up" or "down"
        self.surface = pygame.transform.scale_by(feet[color],4/5).convert_alpha()
        self.rect = self.surface.get_rect(midleft=coords[place])
        self.color=color

class receiver:
    def __init__(self,place):
        dir = {"up":(80,77),"down":(80,643)}
        self.surface = pygame.Surface((100,115))
        self.surface.fill("White")
        self.surface.set_alpha(100)
        self.rect=self.surface.get_rect(center=dir[place])



