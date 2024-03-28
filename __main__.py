
import pygame
import random

pygame.init()

platform_limit=random.randint(450,800) #random platform weight limit
print('limit',platform_limit)
people_weight_list=[45,55,60,65,70,75,80,85,90,100] #list of weights of the people
peopleTOpick=random.randint(1,3) #randomise how many person is spawn
print('peopleTOpick',peopleTOpick)
selected_people=random.sample(people_weight_list, peopleTOpick) #randomly select which persons to spawn
print(selected_people)

screen=pygame.display.set_mode((1024,720)) 
running=True

display_text="Test"
text_style=pygame.font.SysFont("Arial",30,bold=True)
text_color=(255,255,255)
text_position=(100,100)
def create_txt(text,font,color,coor):
    text_img=font.render(text,False,color)
    screen.blit(text_img,(coor[0],coor[1]-50))

#platform_length=int(input("enter platform length:"))

platform_max_height=300
platform_height=platform_max_height*(1-((sum(selected_people))/platform_limit))
platform_length=500



person_height=80
person_width=30


recCreate=pygame.Rect(560,100,60,40) #adding people button
rectb=pygame.Rect(450,100,100,40)

font = pygame.font.SysFont("Arial",40 ,bold=True)
text = ""
input_active = False
tbcol=(50,50,50)
enteredNew=False
recNew=pygame.Rect(0,0,person_width,person_height)
drawNew=False
sticking=False
placed=False
addedPerson=0

while running:
    
    screen.fill(0)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                tbcol=(50,50,50)
                text = ""
                #enteredNew=True
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode
    
    if enteredNew==True:
        drawNew=True
        enteredNew=False

    if drawNew:
        recNew.center=pygame.mouse.get_pos()
        pygame.draw.rect(screen,(255,255,0),recNew)
        sticking=True

    if sticking&pygame.mouse.get_pressed()[0]:
        drawNew=False
        placed=True
        addedPerson=int(text)
        platform_height=platform_max_height*(1-((sum(selected_people)+addedPerson)/platform_limit))
        recNew.center=(pygame.mouse.get_pos()[0],700-platform_height-40)
        pygame.draw.rect(screen,(255,255,0),recNew)
        text = ""
        
    if placed:
        sticking=False
        pygame.draw.rect(screen,(255,255,0),recNew)
    
    recPlatform=pygame.Rect(250,700-platform_height,platform_length,platform_height) #creating the platform

    recP=pygame.Rect(0,0,person_width,person_height) #creating people
    pos=pygame.mouse.get_pos()
    if recPlatform.collidepoint(pos)&pygame.mouse.get_pressed()[0]: #hold the mouse left-click to expand the platform
        col=(0,255,0)
        #platform_length=300
        recPlatform.inflate_ip(5, 0)
        #recPlatform.update(250,400,platform_length,50)
        #platform_length=300
        #recPlatform=pygame.Rect(250,400,350,50)
        
        #pygame.draw.rect(screen,col,recPlatform)
    elif recPlatform.collidepoint(pos)&pygame.mouse.get_pressed()[2]: #hold the mouse right-click to shrink the platform
        col=(255,0,0)
        recPlatform.inflate_ip(-5, 0)    
    else:
        col=(0,0,255)
        #platform_length=400
        #pygame.draw.rect(screen,col,recPlatform)


    pygame.draw.rect(screen,col,recPlatform)

    ccol=(255,0,0)
    
    if recCreate.collidepoint(pos)&pygame.mouse.get_pressed()[0]:
        try:
            int(text)
        except:
            text = ""
        else:
            drawNew=True
            pygame.time.delay(50)
        ccol=(0,255,0)
        tbcol=(50,50,50)

    elif recCreate.collidepoint(pos)!=True &pygame.mouse.get_pressed()[0]:
        tbcol=(50,50,50)
        input_active = False
    elif recCreate.collidepoint(pos):
        text = ""
        ccol=(160,0,0)
    else:
        ccol=(255,0,0)    
    
    if rectb.collidepoint(pos)&pygame.mouse.get_pressed()[0]:
        input_active = True
        tbcol=(20,20,20)

    

    pygame.draw.rect(screen,tbcol,rectb)
    text_surf = font.render(text, True, (255, 0, 0))
    #print(text)
    screen.blit(text_surf, (460,95))

    
    pygame.draw.rect(screen,ccol,recCreate)
    create_txt("ADD",text_style,text_color,(562,150))

    for i in range(0,len(selected_people)):   #placing people on the platform
        if len(selected_people)==1:
            recP.center=(250+person_width/2+platform_length/2,700-platform_height-40)
            pygame.draw.rect(screen,(255,255,0),recP,width=0)
        if len(selected_people)==2:
            recP.center=(250+person_width/2+i*(platform_length-person_width),700-platform_height-40)
            pygame.draw.rect(screen,(255,255,0),recP,width=0)
        if len(selected_people)==3:
            recP.center=(250+person_width/2+i*(platform_length-person_width)/2,700-platform_height-40)
            pygame.draw.rect(screen,(255,255,0),recP,width=0)   
    
    
    
    create_txt("Platform Weight Limit: "+str(platform_limit),text_style,text_color,text_position)
    create_txt("Person's Weight: "+str(selected_people)+"+"+str(addedPerson),text_style,text_color,(100,200))
    WeightColor=255-255*((sum(selected_people)+addedPerson)/platform_limit) if (sum(selected_people)+addedPerson)<=1 else 1
    create_txt("Current Weight: "+str(sum(selected_people)+addedPerson),text_style,(255,WeightColor,WeightColor),(100,250)) #red if max load, whight if no load
    create_txt("Enter a new person's weight: ",text_style,text_color,(100,150))
    
    pygame.display.update()
    pygame.time.delay(50)

