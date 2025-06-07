import pygame
import assets.objects as objects

temp=[]
#important shit
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption("TITLE")

#==========================initializing assets
objects.init()

for i in range(5):
    objects.tutorial["frames"][i] = objects.tutorial["frames"][i].convert_alpha()

colors = {"z":"blue","x":"red","cz":"purple","cx":"orange"}


#===========================init
#==========================global stuff
sounds = {"hit":pygame.mixer.Sound(objects.sounds["hit"])}
state=["titlescreen"]
settings={
    "beat_speed":10
}
receiver = [objects.receiver("up"),objects.receiver("long")]
track = []
animtrack=[]
dialoguetrack = []
#for tutorial only
tuttrack=[]

start = [0]
delay=[1000*(1200/settings["beat_speed"])/60]
currsong=["None"]
percent=[0,1,1] #0 -> percent, 1->number of hit, 2->number of total notes
combo=[0]
pressed = [0,0,0]
#==========================global stuff
#==========================more init



#============================init

def update_beat():
    if len(objects.beats)>0:
        for beat in objects.beats:
            beat.rect.x-=settings["beat_speed"]
            screen.blit(beat.surface,beat.rect)
        if objects.beats[0].rect.right<=0:
            objects.beats.pop(0)
            percent[2]+=1

def update_ui():
    percent[0]=percent[1]/percent[2]
    objects.ui["percent"]=objects.fonts["maragsa"].render("%"+f'{percent[0]*100:.2f}',True,(255,255,255))
    objects.ui["currplay"]=objects.fonts["maragsa"].render("Currently Playing: "+currsong[0],True,(255,255,255))

    screen.blit(objects.ui["currplay"],(30,650))
    screen.blit(objects.ui["percent"],(1100,140))
    

    
#========== WINDOWS ===========#
def titlescreen():
    pass

def scene1():
    pass
    
def tutorial():
    #bacgkround

    lim=pygame.time.get_ticks()-start[0]
    tim=lim+delay[0]

    if lim>46490.06:
        bg=objects.bg["tutorial"]
        
    screen.blit(bg,(0,0))
    #background
    #track
    screen.blit(objects.bamboo.convert_alpha(),(0,17))
    screen.blit(receiver[0].surface,receiver[0].rect)
    #track
    
        

    #new beat
    if len(track)>0 and tim>track[0][0]: 
        objects.beats.append(objects.beat(place="up",color=colors[track[0][1]]))
        track.pop(0)

    #new frame
    
    if len(animtrack)>1 and lim<animtrack[1][0]: 
        pass
    elif len(animtrack)>1:
        animtrack.pop(0)
    screen.blit(objects.tutorial["frames"][animtrack[0][1]-1],(0,136))  

    #new tutdig
    if lim < 27000:
        if len(tuttrack)>1 and lim<tuttrack[1][0]:
            pass
        elif len(tuttrack)>1:
            tuttrack.pop(0)
        objects.ui["help"]=objects.fonts["bantayog"].render(tuttrack[0][1],True,(255,255,255))
        screen.blit(objects.ui["help"],(30,170))    


    
    update_ui()
    update_beat()

    if tim>106_000:
        state[0]="scene2"


def scene2():
    bg = pygame.Surface((1280,720))
    bg.fill("Black")
    screen.blit(bg,(0,0))
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
    percent[1]+=1
    percent[2]+=1
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
                if state[0]=="titlescreen":
                    if event.key==32: #space
                        state[0]="tutorial"
                        start[0]=pygame.time.get_ticks()-100
                        for i in objects.songs["tutorial"]['track']:
                            track.append(i)
                        pygame.mixer.music.load(objects.songs["tutorial"]["path"])
                        pygame.mixer.music.play()   
                        percent=[0,1,1]
                        currsong[0]="Tinikling"
                        for i in objects.tutorial["track"]:
                            animtrack.append(i)
                        for i in objects.tutorial["helpdiag"]:
                            tuttrack.append(i)

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
print(temp)
pygame.quit()