import pygame
import assets.objects as objects


#important shit
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption("TITLE")

colors = {"z":"blue","x":"red","cz":"purple","cx":"orange"}

#==========================global stuff
state=["menu"]
settings={
    "beat_speed":10
}
receiver = [objects.receiver("up"),objects.receiver("long")]
track = []
start = [0]
delay=[1000*(1200/settings["beat_speed"])/60]

combo=[0]
pressed = [0,0,0]
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

def level1():
    #bacgkround
    bg = pygame.Surface((1280,720))
    bg.fill("Black")

    screen.blit(bg,(0,0))
    #background
    #track
    screen.blit(objects.bamboo.convert_alpha(),(0,17))
    screen.blit(receiver[0].surface,receiver[0].rect)

    #track

    if len(track)>0 and pygame.time.get_ticks()-start[0]+delay[0]>track[0][0]:
        objects.beats.append(objects.beat(place="up",color=colors[track[0][1]]))
        track.pop(0)
    update_beat()

    
def tutorial():
    #bacgkround
    bg = pygame.Surface((1280,720))
    bg.fill("Black")

    screen.blit(bg,(0,0))
    #background
    #track
    screen.blit(objects.bamboo.convert_alpha(),(0,17))
    screen.blit(receiver[0].surface,receiver[0].rect)
    #track

    if len(track)>0 and pygame.time.get_ticks()-start[0]+delay[0]>track[0][0]:
        objects.beats.append(objects.beat(place="up",color=colors[track[0][1]]))
        track.pop(0)
    update_beat()

def settings_menu():
    pass

def explode():
    pass

#============= EFFECTS ============#

def success():
    combo[0]+=1
    objects.beats.pop(0)
    pass

def fail():
    combo[0]=0
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
    states = {"menu":menu,"tutorial":tutorial,"settings_menu":settings_menu,"level1":level1}
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
            
            if event.type == pygame.KEYDOWN:
                if event.key==32: #space
                    state[0]="tutorial"
                    start[0]=pygame.time.get_ticks()
                    for i in objects.songs["tutorial"]['track']:
                        track.append(i)
                    pygame.mixer.music.load(objects.songs["tutorial"]["path"])
                    pygame.mixer.music.play()

                if event.key==122:
                    if len(objects.beats)>0:
                        pressed[0]=1
                        if objects.beats[0].rect.colliderect(receiver[0].rect):
                            if objects.beats[0].color=="blue":
                                success()
                            elif objects.beats[0].color=="purple" and pressed[2]==1:
                                success()
                        else:
                            fail()

                if event.key==120:
                    if len(objects.beats)>0:
                        pressed[1]=1
                        if objects.beats[0].rect.colliderect(receiver[0].rect):
                            if objects.beats[0].color=="red":
                                success()
                            elif objects.beats[0].color=="orange" and pressed[2]==1:
                                success()
                        else:
                            fail()
                
                if event.key==99:
                    if len(objects.beats)>0:
                        pressed[2]=1
                        if objects.beats[0].rect.colliderect(receiver[0].rect):
                            if objects.beats[0].color=="orange" and pressed[1]==1:
                                success()
                            elif objects.beats[0].color=="purple" and pressed[0]==1:
                                success()
                        else:
                            fail()
                    
                #print("key:",event.key)
            
            if event.type == pygame.KEYUP:
                if event.key ==122:
                    pressed[0]=0
                if event.key ==120:
                    pressed[1]=0
                if event.key ==99:
                    pressed[2]=0



        states[state[0]]()

        pygame.display.update()
        clock.tick(60)

        

main()
pygame.quit()