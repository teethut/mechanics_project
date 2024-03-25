
import pygame
import random

pygame.init()

platform_limit=random.randint(450,800)
print('limit',platform_limit)
people_weight_list=[45,55,60,65,70,75,80,85,90,100]
peopleTOpick=random.randint(1,3)
print('peopleTOpick',peopleTOpick)
selected_people=random.sample(people_weight_list, peopleTOpick)
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
platform_height=platform_max_height*(sum(selected_people)/platform_limit)
platform_length=500
recPlatform=pygame.Rect(250,600-platform_height,platform_length,platform_height)


person_height=80
person_width=30
recP=pygame.Rect(0,0,person_width,person_height)

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        else:
            running=True
    
    create_txt("Platform Weight Limit: "+str(platform_limit),text_style,text_color,text_position)
    create_txt("Person's Weight: "+str(selected_people),text_style,text_color,(100,200))
    create_txt("Current Weight: "+str(sum(selected_people)),text_style,(255,255-255*(sum(selected_people)/platform_limit),255-255*(sum(selected_people)/platform_limit)),(100,250)) #red if max load, whight if no load

    pos= pygame.mouse.get_pos()
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

    for i in range(0,len(selected_people)):   #placing people on the platform
        if len(selected_people)==1:
            recP.center=(250+person_width/2+platform_length/2,600-platform_height-40)
            pygame.draw.rect(screen,(255,255,0),recP,width=0)
        if len(selected_people)==2:
            recP.center=(250+person_width/2+i*(platform_length-person_width),600-platform_height-40)
            pygame.draw.rect(screen,(255,255,0),recP,width=0)
        if len(selected_people)==3:
            recP.center=(250+person_width/2+i*(platform_length-person_width)/2,600-platform_height-40)
            pygame.draw.rect(screen,(255,255,0),recP,width=0)   
        
    pygame.display.update()
    pygame.time.delay(100)

