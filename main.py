import pygame
import assets.objects as objects

temp=[]
#important shit
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption("TITLE")

for i in range(5):
    objects.tutorial["frames"][i] = objects.tutorial["frames"][i].convert_alpha()

colors = {"z":"blue","x":"red","cz":"purple","cx":"orange"}

#==========================global stuff
sounds = {"hit":pygame.mixer.Sound(objects.sounds["hit"])}
state=["titlescreen"]
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
def titlescreen():
    pass

def scene1():
    pass
    
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
    tim=pygame.time.get_ticks()-start[0]+delay[0]

    if len(track)>0 and tim>track[0][0]:
        objects.beats.append(objects.beat(place="up",color=colors[track[0][1]]))
        track.pop(0)
    if len(objects.tutorial["track"])>1 and tim-delay[0]<objects.tutorial["track"][1][0]:
        screen.blit(objects.tutorial["frames"][objects.tutorial["track"][0][1]-1],(0,136))
    elif len(objects.tutorial["track"])>1:
        objects.tutorial["track"].pop(0)
    screen.blit(objects.tutorial["frames"][objects.tutorial["track"][0][1]-1],(0,136))    
    
    update_beat()
    if tim>106_000:
        state[0]="scene2"

def scene2():
    pass

def settings_menu():
    pass

def explode():
    pass

#============= EFFECTS ============#

def success():
    combo[0]+=1
    objects.beats.pop(0)
    sounds["hit"].play()
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
    states = {"titlescreen":titlescreen,"tutorial":tutorial,"settings_menu":settings_menu,"scene2":scene2,"scene1":scene1}
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
            
            if event.type == pygame.KEYDOWN:
                if event.key==32: #space
                    state[0]="tutorial"
                    start[0]=pygame.time.get_ticks()-100
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
                    
                if event.key==112:
                    temp.append(pygame.time.get_ticks()-start[0])
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
#print(temp)
pygame.quit()