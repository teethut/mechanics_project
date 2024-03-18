
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
text_position=(100,200)
def create_txt(text,font,color,coor):
    text_img=font.render(text,False,color)
    screen.blit(text_img,(coor[0],coor[1]-50))

platform_length=int(input("enter platform length:"))

person_height=80
person_width=30

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        else:
            running=True

    create_txt(display_text,text_style,text_color,text_position)
    rec1=pygame.draw.rect(screen,(255,0,0),(250,400,platform_length,50),width=0)

    for i in range(0,len(selected_people)):   #placing people on the platform
        if len(selected_people)==1:
            pygame.draw.rect(screen,(255,255,0),(250+platform_length/2,320,person_width,person_height),width=0)
        if len(selected_people)==2:
            pygame.draw.rect(screen,(255,255,0),(250+i*(platform_length-person_width),320,person_width,person_height),width=0)
        if len(selected_people)==3:
            pygame.draw.rect(screen,(255,255,0),(250+i*(platform_length-person_width)/2,320,person_width,person_height),width=0)


    pygame.display.update()
    pygame.time.delay(100)

