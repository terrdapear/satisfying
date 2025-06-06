import pygame
import assets.objects as objects
import time


#important shit
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption("TITLE")

colors = {"z":"blue","x":"red"}

#==========================global stuff
state=["menu"]
settings={
    "beat_speed":10
}
receiver = [objects.receiver("up")]
track = []
start = [0]
delay=[1000*(1200/settings["beat_speed"])/60]

combo=[0]
#==========================global stuff

def update_beat():
    if len(objects.beats)>0:
        for beat in objects.beats:
            beat.rect.x-=settings["beat_speed"]
            screen.blit(beat.surface,beat.rect)
        if objects.beats[0].rect.right<=0:
            objects.beats.pop(0)
    
#========== WINDOWS ===========#
def menu():
    pass

def play():
    bg = pygame.Surface((1280,720))
    bg.fill("Black")

    screen.blit(bg,(0,0))
    screen.blit(receiver[0].surface,receiver[0].rect)

    if len(track)>0 and pygame.time.get_ticks()-start[0]+delay[0]>track[0][0]:
        objects.beats.append(objects.beat(place="up",color=colors[track[0][1]]))
        track.pop(0)
    update_beat()

    
def tutorial():
    pass

def settings_menu():
    pass

def explode():
    pass

#============= EFFECTS ============#

def success():
    combo[0]+=1
    print("let's go")
    pass

def fail():
    combo[0]=0
    print("bruh")
    pass

# astig 25
# mahusay 50
# lodi 100
def astig():
    pass

def mahusay():
    pass

def lodi():
    pass

#============= EFFECTS ============#

def main():
    states = {"menu":menu,"tutorial":tutorial,"settings_menu":settings_menu,"play":play}
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key==32: #space
                    state[0]="play"
                    start[0]=pygame.time.get_ticks()
                    for i in objects.songs["tinikling"]['track']:
                        track.append(i)
                    pygame.mixer.music.load(objects.songs["tinikling"]["path"])
                    pygame.mixer.music.play()

                if event.key==122:
                    if len(objects.beats)>0:
                        if objects.beats[0].rect.colliderect(receiver[0].rect):
                            if objects.beats[0].color=="blue":
                                success()
                            else:
                                fail()
                            objects.beats.pop(0)
                        else:
                            fail()
                if event.key==120   :
                    if len(objects.beats)>0:
                        if objects.beats[0].rect.colliderect(receiver[0].rect):
                            if objects.beats[0].color=="red":
                                success()
                            else:
                                fail()
                            objects.beats.pop(0)
                        else:
                            fail()
                    
                print("key:",event.key)
                
            
        states[state[0]]()

        pygame.display.update()
        clock.tick(60)

        

main()
pygame.quit()