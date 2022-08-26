import pygame

pygame.init()
pygame.display.set_caption('Tic tac toe')

r = 1

bg = pygame.image.load('bg.png')
x = pygame.image.load('x.png')
o = pygame.image.load('o.png')
w1 = pygame.image.load('w1.png')
w2 = pygame.image.load('w2.png')
w3 = pygame.image.load('w3.png')
w4 = pygame.image.load('w4.png')


size = [600, 600]
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
screen.blit(bg, (50, 50))
pygame.display.flip()


mat = [0, 0, 0, 0, 0, 0, 0, 0, 0]
l = [[50, 50], [220, 50], [390, 50], [50, 220], [220, 220], [390, 220], [50, 390], [220, 390], [390, 390]]


running = True

while running:

    
    
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] >= 50 and mouse[0] <= 210 and mouse[1] >= 50 and mouse[1] <= 210:
                if mat[0] == 0:
                    mat[0] = r
                    if r == 1:
                        r = 2
                    else:
                        r = 1
            if mouse[0] >= 220 and mouse[0] <= 380 and mouse[1] >= 50 and mouse[1] <= 210:
                if mat[1] == 0:
                    mat[1] = r
                    if r == 1:
                        r = 2
                    else:
                        r = 1
            if mouse[0] >= 390 and mouse[0] <= 550 and mouse[1] >= 50 and mouse[1] <= 210:
                if mat[2] == 0:
                    mat[2] = r
                    if r == 1:
                        r = 2
                    else:
                        r = 1

            if mouse[0] >= 50 and mouse[0] <= 210 and mouse[1] >= 220 and mouse[1] <= 380:
                if mat[3] == 0:
                    mat[3] = r
                    if r == 1:
                        r = 2
                    else:
                        r = 1
            if mouse[0] >= 220 and mouse[0] <= 380 and mouse[1] >= 220 and mouse[1] <= 380:
                if mat[4] == 0:
                    mat[4] = r
                    if r == 1:
                        r = 2
                    else:
                        r = 1
            if mouse[0] >= 390 and mouse[0] <= 550 and mouse[1] >= 220 and mouse[1] <= 380:
                if mat[5] == 0:
                    mat[5] = r
                    if r == 1:
                        r = 2
                    else:
                        r = 1
                    
            if mouse[0] >= 50 and mouse[0] <= 210 and mouse[1] >= 390 and mouse[1] <= 550:
                if mat[6] == 0:
                    mat[6] = r
                    if r == 1:
                        r = 2
                    else:
                        r = 1
            if mouse[0] >= 220 and mouse[0] <= 380 and mouse[1] >= 390 and mouse[1] <= 550:
                if mat[7] == 0:
                    mat[7] = r
                    if r == 1:
                        r = 2
                    else:
                        r = 1
            if mouse[0] >= 390 and mouse[0] <= 550 and mouse[1] >= 390 and mouse[1] <= 550:
                if mat[8] == 0:
                    mat[8] = r
                    if r == 1:
                        r = 2
                    else:
                        r = 1
                        
        for i in range(9):
            if mat[i] == 1:
                screen.blit(x, l[i])
            elif mat[i] == 2:
                screen.blit(o, l[i])
            pygame.display.flip()
            
        ##win
        if mat[0] == mat[1] == mat[2] and mat[0] != 0:
            print(mat[0])
            running = False
            screen.blit(w1, (50, 50))
        if mat[3] == mat[4] == mat[5] and mat[3] != 0:
            print(mat[3])
            running = False
            screen.blit(w1, (50, 220))
        if mat[6] == mat[7] == mat[8] and mat[6] != 0:
            print(mat[6])
            running = False
            screen.blit(w1, (50, 390))

        if mat[0] == mat[3] == mat[6] and mat[0] != 0:
            print(mat[0])
            running = False
            screen.blit(w2, (50, 50))
        if mat[1] == mat[4] == mat[7] and mat[1] != 0:
            print(mat[1])
            running = False
            screen.blit(w2, (220, 50))
        if mat[2] == mat[5] == mat[8] and mat[2] != 0:
            print(mat[2])
            running = False
            screen.blit(w3, (390, 50))

        if mat[0] == mat[4] == mat[8] and mat[0] != 0:
            print(mat[0])
            running = False
            screen.blit(w3, (50, 50))
        if mat[6] == mat[4] == mat[2] and mat[6] != 0:
            print(mat[6])
            running = False
            screen.blit(w4, (50, 50))
        pygame.display.flip()
        
        #print(mouse)
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()        
    
