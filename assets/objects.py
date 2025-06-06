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
    "track":[(4768.211920529801, 'x'), (5165.562913907284, 'x'), (5562.913907284767, 'cx'), (5960.2649006622505, 'x'), (6357.615894039734, 'x'), (6754.966887417217, 'cx'), (7152.3178807947, 'x'), (7549.668874172183, 'x'), (7947.019867549666, 'cx'), (9536.4238410596, 'x'), (9933.774834437085, 'z'), (10331.125827814569, 'cx'), (10728.476821192053, 'z'), (11125.827814569537, 'x'), (11523.17880794702, 'cz'), (11920.529801324505, 'x'), (12317.880794701989, 'z'), (12715.231788079473, 'cx'), (14304.635761589409, 'x'), (14701.986754966892, 'z'), (15099.337748344376, 'cx'), (15496.68874172186, 'z'), (15894.039735099344, 'x'), (16291.390728476828, 'cz'), (16688.741721854312, 'x'), (17086.092715231796, 'z'), (17483.44370860928, 'cx')]
    },
    "tutorial":{
        "path":"assets\music\_tinikling.mp3",
        "track":[(4768.211920529801, 'x'), (5960.2649006622505, 'x'), (7152.3178807947, 'x'), (8344.370860927149, 'x'), (10728.476821192053, 'z'), (11920.529801324505, 'z'), (13112.582781456957, 'z'), (14304.635761589409, 'z'), (17483.44370860928, 'cx'), (18675.496688741732, 'cx'), (19867.549668874184, 'cx'), (21059.602649006636, 'cx'), (23443.70860927154, 'cz'), (24635.761589403992, 'cz'), (25827.814569536444, 'cz'), (27019.867549668896, 'cz'), (28609.27152317883, 'x'), (29006.622516556316, 'z'), (29403.9735099338, 'cx'), (29801.324503311283, 'z'), (30198.675496688767, 'x'), (30596.02649006625, 'cz'), (30993.377483443735, 'x'), (31390.72847682122, 'z'), (31788.079470198703, 'cx'), (33377.48344370864, 'z'), (33774.83443708612, 'x'), (34172.18543046361, 'cz'), (34569.53642384109, 'x'), (34966.887417218575, 'z'), (35364.23841059606, 'cx'), (35761.58940397354, 'z'), (36158.94039735103, 'x'), (36556.29139072851, 'cz'), (46490.06622516561, 'x')]
    }
}

class beat:
    def __init__(self,place,color): # "place" can only be "up" or "down"
        self.surface = pygame.transform.scale_by(feet[color],4/5).convert_alpha()
        self.rect = self.surface.get_rect(midleft=coords[place])
        self.color=color

class receiver:
    def __init__(self,place):
        dir = {"up":(30,20),"down":(80,643)}
        x=100
        if place == "long":
            x=1280
        self.surface = pygame.Surface((x,115))
        
        self.surface.fill("White")
        self.surface.set_alpha(100)
        self.rect=self.surface.get_rect(topleft=(30,20))

bamboo = pygame.image.load("assets\images\_bamboo.png")



