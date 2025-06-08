import pygame
import assets.objects as objects

temp=[]
#important shit
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption("Indak")

#==========================initializing assets
objects.init()

colors = {"z":"blue","x":"red","cz":"purple","cx":"orange"}


#===========================init
state=["titlescreen"]
#==========================global stuff
sounds = {"hit":pygame.mixer.Sound(objects.sounds["hit"]),"clap":pygame.mixer.Sound(objects.sounds["clap"])}
sounds["hit"].set_volume(0.6)
sounds["clap"].set_volume(0.8)
settings={
    "beat_speed":10,
    "volume":10
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
last_time=[0]

last_level=["tutorial"]
diag_center=[640,670]
#==========================global stuff
#=====================================================#
#=====================================================#
#=====================================================#
#=========== initializing levels =============#


def init_tutorial():
    state[0]="tutorial"
    last_level[0]="tutorial"
    start[0]=pygame.time.get_ticks()-160

    #clear
    objects.beats.clear()
    track.clear()
    animtrack.clear()
    tuttrack.clear()
    dialoguetrack.clear()

    for i in objects.songs["tutorial"]['track']:
        track.append(i)
    pygame.mixer.music.load(objects.songs["tutorial"]["path"])
    pygame.mixer.music.play()   
    percent[0],percent[1],percent[2]=0,1,1
    currsong[0]="Tinikling"
    for i in objects.tutorial["track"]:
        animtrack.append(i)
    for i in objects.tutorial["helpdiag"]:
        tuttrack.append(i)
    for i in objects.tutorial["dialogue"]:
        dialoguetrack.append(i)


def init_final():
    state[0]="final"
    last_level[0]="final"

    #clear
    objects.beats.clear()
    track.clear()
    animtrack.clear()
    dialoguetrack.clear()


    pygame.mixer.music.load(objects.songs["final"]["path"])
    pygame.mixer.music.play()
    for x in objects.songs["final"]["track"]:
        track.append(x)
    print(track)
    start[0]=pygame.time.get_ticks()-321
    currsong[0]="Les Parapluies de Cherbourg"
    percent[0],percent[1],percent[2]=0,1,1


#=============================================#
#=====================================================#
#=====================================================#
#=====================================================#
#============= EFFECTS ============#

def success():
    combo[0]+=1
    objects.beats.pop(0)
    sounds["hit"].play()
    percent[1]+=1
    percent[2]+=1

def fail():
    percent[2]+=1
    percent[0]=percent[1]/percent[2]
    if percent[0]<.7:
        state[0]="game_over"

#============= EFFECTS ============#
#=====================================================#
#=====================================================#
#=====================================================#
#===============updates================#
def update_beat():
    dt = (pygame.time.get_ticks()-last_time[0])*0.06

    if len(objects.beats)>0:
        for beat in objects.beats:
            beat.rect.x-=settings["beat_speed"]*dt
            screen.blit(beat.surface,beat.rect)
        if objects.beats[0].rect.right<=0:
            objects.beats.pop(0)
            fail()

def update_ui():
    percent[0]=percent[1]/percent[2]
    screen.blit(objects.fonts["maragsa"].render("%"+f'{percent[0]*100:.2f}',True,(255,255,255)),(1100,140))
    screen.blit(objects.ui["threefourths"],(0,0))
    
def update_dialogue():
    lim =pygame.time.get_ticks()-start[0]
    if len(dialoguetrack)>1 and lim<dialoguetrack[1][0]:
        pass
    elif len(dialoguetrack)>1:
        dialoguetrack.pop(0)
    font = objects.fonts["maragsa"].render(dialoguetrack[0][1],True,(255,255,255))
    rect= font.get_rect(center=(diag_center[0],diag_center[1]))
    screen.blit(font,rect)
    
def update_anim(folder,x,y): # folder = list[frames] ,x ,y
    lim = pygame.time.get_ticks()-start[0]
    if len(animtrack)>1 and lim>=animtrack[1][0]:
        animtrack.pop(0)
    screen.blit( folder[animtrack[0][1]-1] , (x,y))

def update_volume(l): # +-1
    settings["volume"]+=l
    pygame.mixer.music.set_volume(settings['volume']/10)
    sounds["hit"].set_volume(0.6*(settings['volume']/10))
    sounds["clap"].set_volume(0.8*(settings['volume']/10))

def update_speed(l): # +-1
    settings["beat_speed"]+=l
    delay[0]=1000*(1200/settings["beat_speed"])/60

#=====================================================#
#=====================================================#
#=====================================================#
#=====================================================#
#=====================================================#
#======================== WINDOWS ====================#
def titlescreen():
    screen.blit(objects.ui["background"], (0, 0))
    objects.ui["play_button"].draw(screen)
    objects.ui["settings_button"].draw(screen)
    objects.ui["exit_button"].draw(screen)

def Settings():
    background = pygame.image.load("assets/Settings Panel/SETTINGS_Layout.png").convert_alpha()
    screen.blit(background, (0, 0))
    objects.ui["exit_button2"].draw(screen)
    objects.ui["volume_up"].draw(screen)
    objects.ui["volume_down"].draw(screen)
    pangtakip = pygame.Surface((50,50))
    pangtakip.fill((212, 191, 144))
    screen.blit(pangtakip,(917,378))
    screen.blit(pangtakip,(915,560))

    txt = objects.fonts["bantayoglight"].render(str(settings["volume"]),True,(0,0,0))
    screen.blit(txt,(920,378))
    txt1 = objects.fonts["bantayoglight"].render(str(settings["beat_speed"]),True,(0,0,0))
    screen.blit(txt1,(915,560))

def scene1():
    pass    
    
def tutorial():
    #bacgkround
    lim=pygame.time.get_ticks()-start[0]
    tim=lim+delay[0]
    if lim<47682.06:
        bg=objects.bg["tutorial"]
    else:
        bg=objects.bg["tutorial"]
    screen.blit(bg,(0,0))
    #background
    #track
    screen.blit(objects.bamboo[0],(0,17))
    screen.blit(receiver[0].surface,receiver[0].rect)
    #screen.blit(objects.ui["boton"],receiver[0].rect.topleft)
    #track
    
    #new beat
    if len(track)>0 and tim>track[0][0]: 
        objects.beats.append(objects.beat(place="up",color=colors[track[0][1]]))
        track.pop(0)

    #new frame
    if lim<47682:
        bro=objects.tutorial["frames"]
        y=236
    else:
        y=136
        bro=objects.tutorial["frames2"]

    update_anim(bro,0,y)

    #new tutdig
    if lim < 27000:
        if len(tuttrack)>1 and lim>=tuttrack[1][0]:
            tuttrack.pop(0)
        objects.ui["help"]=objects.fonts["bantayog"].render(tuttrack[0][1],True,(255,255,255))
        screen.blit(objects.ui["help"],(30,150))    

    update_ui()
    update_beat()
    update_dialogue()

    if lim>104008.609271522:
        state[0]="scene2"
        sounds["clap"].play(fade_ms=4000)
        start[0]=pygame.time.get_ticks()
        pygame.mixer.music.load(objects.songs["atincupongsingsing"]["path"])
        pygame.mixer.music.play()



def scene2():
    time = (pygame.time.get_ticks()-start[0])*0.001
    if time<10: #hooray
        bg = pygame.Surface((1280,720)) #pose
        bg.fill("Black")
        screen.blit(bg,(0,0))
    elif time>10:
        pass
    elif time>20:
        pass
    else:
        state[0]="talk_before_final"



#start[0]=pygame.time.get_ticks()
def talk_before_final():
    time = (pygame.time.get_ticks()-start[0])/1000
    bg = pygame.Surface((1280,720))
    bg.fill("Black")
    screen.blit(bg,(0,0))
    l=objects.fonts["maragsasmall"]
    j1 = l.render("Josefina: Mama, bukas na po ang sayaw ko sa fiesta!",True,(255,255,255))
    j2 = l.render("Ilang buwan ko na ito inaabangan at ngayon parating na.",True,(255,255,255))
    c1 = l.render("Carmela:  Haha, handa ka na anak?",True,(255,255,255))
    j3 = l.render("Josefina: Opo ma, pero... ma, ika'y hindi talaga makapupunta?",True,(255,255,255))
    c2 = l.render("Carmela: 'Di, hindi maganda ang aking pakiramdam.",True,(255,255,255))
    c3 = l.render("Ako'y mananatili nalang muna rito sa ating tahanan.",True,(255,255,255))
    j4 = l.render("Josefina: Sige po...",True,(255,255,255))
    d1 = l.render("Ang hindi alam ni Josefina ay bukas na rin ihahatid si Carmela",True,(255,255,255))
    d2 = l.render("patungong ",True,(255,255,255))
    d3 = l.render("Impyerno.",True,(255,0,0))

    a1 = l.render("Carmela: O, matulog na at may fiesta ka pa bukas!",True,(255,255,255))
    a2 = l.render("Josefina: Sige, mama.",True,(255,255,255))

    a3 = l.render("Carmela: Paano ko ba sasabihin sa kaniya.",True,(255,255,255))
    a4 = l.render("Paano?",True,(255,0,0))

    if time<43:
        if time>3:
            screen.blit(j1,(30,30))
        if time>6:
            screen.blit(j2,(140,70))
        if time>10:
            screen.blit(c1,(30,120))
        if time>13:
            screen.blit(j3,(30,170))
        if time>20:
            screen.blit(c2,(30,220))
        if time>25:
            screen.blit(c3,(140,260))
        if time>30:
            screen.blit(j4,(30,310))    
        if time>35:
            screen.blit(d1,(30,410))
        if time>40:
            screen.blit(bg,(0,0))
            screen.blit(d2,(30,450))
        if time>40.5:
            screen.blit(d3,(170,450))
    elif time<60:
        if time>43:
            screen.blit(a1,(30,30))
        if time>48:
            screen.blit(a2,(30,80))
        if time>53:
            screen.blit(a3,(30,180))
        if time>57:
            screen.blit(a4,(140,220))
    elif True:
        frame=()
        if time>=57:
            pass
        if time>=64:
            pass




    if time>70:
        init_final()

def final():
    bg = pygame.Surface((1280,720))
    bg.fill("Black")
    screen.blit(bg,(0,0))
    
    lim=pygame.time.get_ticks()-start[0]
    tim=lim+delay[0]

    screen.blit(bg,(0,0))
    #background
    #track
    screen.blit(objects.bamboo[0],(0,17))
    screen.blit(receiver[0].surface,receiver[0].rect)
    #track
    
    #new beat
    if len(track)>0 and tim>track[0][0]: 
        objects.beats.append(objects.beat(place="up",color=colors[track[0][1]]))
        track.pop(0)

    update_anim(objects.ui["final_frames"],0,0)
    update_ui()
    update_beat()
    update_dialogue()

    if lim>166_000:
        state[0]="ty"

def mechanics():
    screen.blit(objects.ui["mech"],(0,0))

def game_over():
    bg = objects.ui["fail"]
    screen.blit(bg,(0,0))
    pygame.mixer.music.stop()

def ty():
    #img = something
    #screen.blit(img,(0,0))
    pass

#====================================================#
#=====================================================#
#=====================================================#
#=====================================================#

def changemech():
    state[0]="mechanics"

def main():
    l = False
    states = {"titlescreen":titlescreen,"tutorial":tutorial,"Settings":Settings,"scene2":scene2,"scene1":scene1,"talk_before_final":talk_before_final,"final":final,"mechanics":mechanics,"game_over":game_over,"ty":ty}
    inits = {"tutorial":changemech,"final":init_final}
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
            
            if event.type == pygame.KEYDOWN:
                if event.key==32: #space
                    if state[0]=="mechanics":
                        init_tutorial()

                    if state[0]=="menu":
                        pass

                    if state[0]=="game_over":
                        inits[last_level[0]]()
                
                if event.key==99: #c
                    if len(objects.beats)>0:
                        pressed[2]=1
                        if objects.beats[0].rect.colliderect(receiver[0].rect):
                            if objects.beats[0].color=="orange" and pressed[1]==1:
                                success()
                            elif objects.beats[0].color=="purple" and pressed[0]==1:
                                success()
                            elif objects.beats[0].color in ["blue","red"]:
                                objects.beats.pop(0)
                                fail()
                        else:
                            fail()

                if event.key==122: #z
                    if len(objects.beats)>0:
                        pressed[0]=1
                        if objects.beats[0].rect.colliderect(receiver[0].rect):
                            if objects.beats[0].color=="blue":
                                success()
                            elif objects.beats[0].color=="purple" and pressed[2]==1:
                                success()
                        else:
                            fail()

                if event.key==120: #x
                    if len(objects.beats)>0:
                        pressed[1]=1
                        if objects.beats[0].rect.colliderect(receiver[0].rect):
                            if objects.beats[0].color=="red":
                                success()
                            elif objects.beats[0].color=="orange" and pressed[2]==1:
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
            
            if state[0]=="titlescreen":
                if objects.ui["play_button"].is_pressed(event):
                    state[0]="mechanics"
                elif objects.ui["settings_button"].is_pressed(event):
                    state[0]="Settings"
                elif objects.ui["exit_button"].is_pressed(event):
                    return True
            elif state[0]=="Settings":
                if objects.ui["exit_button2"].is_pressed(event):
                    state[0]="titlescreen"
                if objects.ui["volume_up"].is_pressed(event) and settings["volume"]<10:
                    update_volume(1)
                if objects.ui["volume_down"].is_pressed(event) and settings["volume"]>0:
                    update_volume(-1)
                if objects.ui["speed_up"].is_pressed(event) and settings["beat_speed"]<15:
                    update_speed(1)
                if objects.ui["speed_down"].is_pressed(event) and settings['beat_speed']>8:
                    update_speed(-1)

        if l:
            pygame.mixer.music.load(objects.songs["final"]["path"])
            pygame.mixer.music.play()
            for x in [(4361, 'z'), (6312, 'x'), (7609, 'z'), (8056, 'x'), (9759, 'z'), (11491, 'x'), (12821, 'z'), (13208, 'x'), (14594, 'z'), (15043, 'x'), (16386, 'z'), (16836, 'x'), (18341, 'z'), (18825, 'x'), (19791, 'z'), (20673, 'x'), (21556, 'z'), (21986, 'x'), (22463, 'z'), (24261, 'x'), (25950, 'z'), (26435, 'x'), (26887, 'z'), (27936, 'x'), (32564, 'z'), (34966, 'x'), (35885, 'z'), (36852, 'x'), (37751, 'z'), (38612, 'x'), (39554, 'z'), (40453, 'x'), (42286, 'z'), (43182, 'x'), (44129, 'z'), (45924, 'x'), (46867, 'z'), (47777, 'x'), (48206, 'z'), (48819, 'x'), (49319, 'z'), (49751, 'x'), (50729, 'z'), (51593, 'x'), (52537, 'z'), (52999, 'x'), (53459, 'z'), (54326, 'x'), (55242, 'z'), (56155, 'x'), (57088, 'z'), (57555, 'x'), (58036, 'z'), (58983, 'x'), (60112, 'z'), (63614, 'x'), (66729, 'z'), (67196, 'x'), (67674, 'z'), (68087, 'x'), (68548, 'z'), (68962, 'x'), (69404, 'z'), (69851, 'x'), (70315, 'z'), (70745, 'x'), (71126, 'z'), (72069, 'x'), (72531, 'z'), (72989, 'x'), (73469, 'z'), (73846, 'x'), (74326, 'z'), (74745, 'x'), (75173, 'z'), (75598, 'x'), (76471, 'z'), (77264, 'x'), (78093, 'z'), (79118, 'x'), (79554, 'z'), (79997, 'x'), (80460, 'z'), (80896, 'x'), (81360, 'z'), (81742, 'x'), (82208, 'z'), (82672, 'x'), (83464, 'z'), (84416, 'x'), (86168, 'z'), (86997, 'x'), (87846, 'z'), (88662, 'x'), (89665, 'z'), (90578, 'x'), (94674, 'z'), (95510, 'x'), (96445, 'z'), (97384, 'x'), (97795, 'z'), (98190, 'x'), (98606, 'z'), (99100, 'x'), (99508, 'z'), (99935, 'x'), (100424, 'z'), (100889, 'x'), (101787, 'z'), (102733, 'x'), (103610, 'z'), (104576, 'x'), (104961, 'z'), (105441, 'x'), (105835, 'z'), (106299, 'x'), (106726, 'z'), (107142, 'x'), (108189, 'z'), (109052, 'x'), (109924, 'z'), (110832, 'x'), (111764, 'z'), (112659, 'x'), (113509, 'z'), (114449, 'x'), (114849, 'z'), (115030, 'x'), (115330, 'z'), (116132, 'x'), (116993, 'z'), (117827, 'x'), (118780, 'z'), (119779, 'x'), (124985, 'z'), (125867, 'x'), (126797, 'z'), (127661, 'x'), (128528, 'z'), (129437, 'x'), (130341, 'z'), (131199, 'x'), (132048, 'z'), (132962, 'x'), (133866, 'z'), (134733, 'x'), (135685, 'z'), (136619, 'x'), (137553, 'z'), (138677, 'x'), (139496, 'z'), (140432, 'x'), (141336, 'z'), (142309, 'x'), (142709, 'z'), (143175, 'x'), (144074, 'z'), (144957, 'x'), (145942, 'z'), (146345, 'x'), (146828, 'z'), (147311, 'x'), (147777, 'z'), (148758, 'x'), (149386, 'z'), (149521, 'x'), (149690, 'z'), (151133, 'x'), (154343, 'z')]:
                track.append(x)
            print(track)
            start[0]=pygame.time.get_ticks()-321
            l=False
            currsong[0]="Les Parapluies de Cherbourg"
            percent[0],percent[1],percent[2]=0,1,1

        states[state[0]]()
        last_time[0]=pygame.time.get_ticks()    

        pygame.display.update()
        clock.tick(60)

        

main()
print(temp)
pygame.quit()