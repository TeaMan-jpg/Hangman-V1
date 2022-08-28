import pygame
import ptext12 as ptext
import random

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('hangman')
screen = pygame.display.set_mode((1000,600),0,32)
clicking = False
clicking2 = False
right_clicking = False
middle_clicking = False
drawn = False
list1 = []
chosen_word = ''
font = pygame.font.Font(None, 32)
with open('words_to_use.txt','r') as f:
    mylist = [line.rstrip() for line in f]
    chosen_word = random.choice(mylist)

click2 = False
text = ''
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 40)
myfont1 = pygame.font.SysFont('Comic Sans MS', 20)
lives = 10
display = []
guess = ''
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
letter_set = set(chosen_word)

class Word_button():
    displaystr = ''
    def __init__(self,surface,display_word):
        self.surface = surface
        self.display = display_word
        self.display_str = ''

    def create_word_button(self):
        button_1 = pygame.Rect(400,460,200,50)
        return button_1
        
    def draw_empty_word(self):
        
        for i in self.display:
            self.display_str += i
            self.display_str += ' '

        Word_button.displaystr = self.display_str
        textsurface = myfont.render(Word_button.displaystr, False, (0,0,0))
        screen.blit(textsurface,(370,350))


        return True

class CreateButton():
    def __init__(self, surface,display_word):
        self.surface = surface
        self.btn = None
        self.clicked = False
        self.btntexts = None
        self.display = display_word
        self.letters = None
        self.color = color

    def drawButton(self,letter, posX,posY, btn_W, btn_H, color, radius):
       pos = pygame.mouse.get_pos() 
       action = False
       self.btn = pygame.draw.rect(self.surface,color,(posX,posY, btn_W, btn_H),border_radius=radius)
       self.letters = letter
       
       if self.btn.collidepoint(pos) and self.clicked == False:
            if clicking:
                action = True
                self.clicked = True
        

    def textButton(self,btntext,tcolor,font,size,shadow=(0,0),scolor='grey'):

        self.btntexts = btntext
        ptext.draw(btntext,center=self.btn.center,color=tcolor,sysfontname=font,fontsize=size,shadow=shadow,scolor=scolor)
        
    def comparison_word(self):
        letter_click = self.btntexts
        if self.clicked:
            for index,letter in enumerate(chosen_word):
                if letter == letter_click:
                    self.display[index] = letter
                    screen.fill((255,255,255))

                    
    def comparison_word2(self):
        pos = pygame.mouse.get_pos()
        if self.btn.collidepoint(pos):
            letter_clicks = self.letters
            if letter_clicks not in [*chosen_word]:
                screen.fill((255,255,255))
                
                return False
    
lives11 = 1
posX = 220
posY = 35
posY1 = 235
letter_btnH = 40
letter_btnW = 40
color = 'lightskyblue3'



def removes(string):
    return string.replace(" ", "")

run = True
screen.fill((255,255,255))   
mouseOver = False
victory = False
defeat = False
while run:
    mx,my = pygame.mouse.get_pos()
    button_set = Word_button(screen,display)
    button_set_1 = button_set.create_word_button()
    if button_set_1.collidepoint((mx,my)):
        if clicking:
            screen.fill((255,255,255))
            drawn = True
    if drawn:
        button_set.draw_empty_word()              
        
    pygame.draw.rect(screen, (255,0,0), button_set_1)

  
    a_button = CreateButton(screen,display)
    a_button.drawButton('a',posX,posY,letter_btnW,letter_btnH,color,5)
    a_button.textButton('a', 'black', 'Comic Sans MS', 20, (0,0))
    a_button.comparison_word()
    

    b_button = CreateButton(screen,display)
    b_button.drawButton('b',posX+100,posY,letter_btnW,letter_btnH,color,5)
    b_button.textButton('b', 'black', 'Comic Sans MS', 20, (0,0))
    b_button.comparison_word()
        

    c_button = CreateButton(screen,display)
    c_button.drawButton('c',posX+200,posY,letter_btnW,letter_btnH,color,10)
    c_button.textButton('c', 'black', 'Comic Sans MS', 20, (0,0))
    c_button.comparison_word()
        
    
    d_button = CreateButton(screen,display)
    d_button.drawButton('d',posX+300,posY,letter_btnW,letter_btnH,color,10)
    d_button.textButton('d', 'black', 'Comic Sans MS', 20, (0,0))
    d_button.comparison_word()
        

    e_button = CreateButton(screen,display)
    e_button.drawButton('e',posX+400,posY,letter_btnW,letter_btnH,color,10)
    e_button.textButton('e', 'black', 'Comic Sans MS', 20, (0,0))
    e_button.comparison_word()
        

    f_button = CreateButton(screen,display)
    f_button.drawButton('f',posX+500,posY,letter_btnW,letter_btnH,color,10)
    f_button.textButton('f', 'black', 'Comic Sans MS', 20, (0,0))
    f_button.comparison_word()
        

    g_button = CreateButton(screen,display)
    g_button.drawButton('g',posX,posY+50,letter_btnW,letter_btnH,color,10)
    g_button.textButton('g', 'black', 'Comic Sans MS', 20, (0,0))
    g_button.comparison_word()
        

    h_button = CreateButton(screen,display)
    h_button.drawButton('h',posX+100,posY+50,letter_btnW,letter_btnH,color,10)
    h_button.textButton('h', 'black', 'Comic Sans MS', 20, (0,0))
    h_button.comparison_word()
        

    i_button = CreateButton(screen,display)
    i_button.drawButton('i',posX+200,posY+50,letter_btnW,letter_btnH,color,10)
    i_button.textButton('i', 'black', 'Comic Sans MS', 20, (0,0))
    i_button.comparison_word()
        

    j_button = CreateButton(screen,display)
    j_button.drawButton('j',posX+300,posY+50,letter_btnW,letter_btnH,color,10)
    j_button.textButton('j', 'black', 'Comic Sans MS', 20, (0,0))
    j_button.comparison_word()
        

    k_button = CreateButton(screen,display)
    k_button.drawButton('k',posX+400,posY+50,letter_btnW,letter_btnH,color,10)
    k_button.textButton('k', 'black', 'Comic Sans MS', 20, (0,0))
    k_button.comparison_word()
        

    l_button = CreateButton(screen,display)
    l_button.drawButton('l',posX+500,posY+50,letter_btnW,letter_btnH,color,10)
    l_button.textButton('l', 'black', 'Comic Sans MS', 20, (0,0))
    l_button.comparison_word()
        

    m_button = CreateButton(screen,display)
    m_button.drawButton('m',posX,posY+100,letter_btnW,letter_btnH,color,10)
    m_button.textButton('m', 'black', 'Comic Sans MS', 20, (0,0))
    m_button.comparison_word()
    

    n_button = CreateButton(screen,display)
    n_button.drawButton('n',posX+100,posY+100,letter_btnW,letter_btnH,color,10)
    n_button.textButton('n', 'black', 'Comic Sans MS', 20, (0,0))
    n_button.comparison_word()
        

    o_button = CreateButton(screen,display)
    o_button.drawButton('o',posX+200,posY+100,letter_btnW,letter_btnH,color,10)
    o_button.textButton('o', 'black', 'Comic Sans MS', 20, (0,0))
    o_button.comparison_word()
        

    p_button = CreateButton(screen,display)
    p_button.drawButton('p',posX+300,posY+100,yes_btnW,yes_btnH,color,10)
    p_button.textButton('p', 'black', 'Comic Sans MS', 20, (0,0))
    p_button.comparison_word()
    
        
    q_button = CreateButton(screen,display)
    q_button.drawButton('q',posX+400,posY+100,letter_btnW,letter_btnH,color,10)
    q_button.textButton('q', 'black', 'Comic Sans MS', 20, (0,0))
    q_button.comparison_word()
        

    r_button = CreateButton(screen,display)
    r_button.drawButton('r',posX+500,posY+100,letter_btnW,letter_btnH,color,10)
    r_button.textButton('r', 'black', 'Comic Sans MS', 20, (0,0))
    r_button.comparison_word()
    

    s_button = CreateButton(screen,display)
    s_button.drawButton('s',posX,posY+150,letter_btnW,letter_btnH,color,10)
    s_button.textButton('s', 'black', 'Comic Sans MS', 20, (0,0))
    s_button.comparison_word()
        

    t_button = CreateButton(screen,display)
    t_button.drawButton('t',posX+100,posY+150,letter_btnW,letter_btnH,color,10)
    t_button.textButton('t', 'black', 'Comic Sans MS', 20, (0,0))
    t_button.comparison_word()
        

    u_button = CreateButton(screen,display)
    u_button.drawButton('u',posX+200,posY+150,letter_btnW,letter_btnH,color,10)
    u_button.textButton('u', 'black', 'Comic Sans MS', 20, (0,0))
    u_button.comparison_word()
        

    v_button = CreateButton(screen,display)
    v_button.drawButton('v',posX+300,posY+150,letter_btnW,letter_btnH,color,10)
    v_button.textButton('v', 'black', 'Comic Sans MS', 20, (0,0))
    v_button.comparison_word()
        

    w_button = CreateButton(screen,display)
    w_button.drawButton('w', posX+400,posY+150,letter_btnW,letter_btnH,color,10)
    w_button.textButton('w', 'black', 'Comic Sans MS', 20, (0,0))
    w_button.comparison_word()
        

    x_button = CreateButton(screen,display)
    x_button.drawButton('x', posX+500,posY+150,letter_btnW,letter_btnH,color,10)
    x_button.textButton('x', 'black', 'Comic Sans MS', 20, (0,0))
    x_button.comparison_word()
        

    y_button = CreateButton(screen,display)
    y_button.drawButton('y',posX,posY+200,letter_btnW,letter_btnH,color,10)
    y_button.textButton('y', 'black', 'Comic Sans MS', 20, (0,0))
    y_button.comparison_word()
        

    z_button = CreateButton(screen,display)
    z_button.drawButton('z',posX+100,posY+200,letter_btnW,letter_btnH,color,10)
    z_button.textButton('z', 'black', 'Comic Sans MS', 20, (0,0))
    z_button.comparison_word()


    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
                if drawn == True:
                    clicking2 = True
                    
                if a_button.comparison_word2() == False:
                     lives -= 1

                elif b_button.comparison_word2() == False:
                     lives -= 1

                elif c_button.comparison_word2() == False:
                     lives -= 1

                elif d_button.comparison_word2() == False:
                     lives -= 1
     
                elif e_button.comparison_word2() == False:
                     lives -= 1
             
                elif f_button.comparison_word2() == False:
                     lives -= 1
                    
                elif g_button.comparison_word2() == False:
                     lives -= 1
                 
                elif h_button.comparison_word2() == False:
                     lives -= 1
                   
                elif i_button.comparison_word2() == False:
                     lives -= 1
                   
                elif j_button.comparison_word2() == False:
                     lives -= 1
                
                elif k_button.comparison_word2() == False:
                    lives -= 1
                 
                elif l_button.comparison_word2() == False:
                     lives -= 1
                    
                elif m_button.comparison_word2() == False:
                      lives -= 1
                      
                elif n_button.comparison_word2() == False:
                    lives -= 1
                 
                elif o_button.comparison_word2() == False:
                     lives -= 1
                 
                elif p_button.comparison_word2() == False:
                     lives -= 1
                   
                elif q_button.comparison_word2() == False:
                     lives -= 1
                
                elif r_button.comparison_word2() == False:
                     lives -= 1
                   
                elif s_button.comparison_word2() == False:
                     lives -= 1
                    
                elif t_button.comparison_word2() == False:
                     lives -= 1
                 
                elif u_button.comparison_word2() == False:
                     lives -= 1
               
                elif v_button.comparison_word2() == False:
                     lives -= 1
                  
                elif w_button.comparison_word2() == False:
                     lives -= 1
               
                elif x_button.comparison_word2() == False:
                     lives -= 1
                  
                elif y_button.comparison_word2() == False:
                     lives -= 1
                  
                elif z_button.comparison_word2() == False:
                     lives -= 1
          
            if event.button == 2:
                middle_clicking = True
            if event.button == 3:
                right_clicking = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False
                clicking2 = False
            if event.button == 2:
                middle_clicking = False
            if event.button == 3:
                right_clicking = False
       

    lives_str = str(lives)
    live_surface = myfont.render(f'Lives: {lives_str}',False,(0,0,0))
    screen.blit(live_surface,(30,100))
    

    displaystrs = removes(Word_button.displaystr)
    if displaystrs == chosen_word:
            clicking = False
            screen.fill((255,255,255))
            drawn = False
            victory = True
            victory_text = myfont.render('You win', False, (0,0,0))
            screen.blit(victory_text,(430,300))
            lives = 10
            display = []
            displaystrs = ''
            with open('words_to_use.txt','r') as f:
                mylist = [line.rstrip() for line in f]
                chosen_word = random.choice(mylist)
            word_length = len(chosen_word)
            for _ in range(word_length):
                display += '_'
 
    elif lives == 0:
            clicking = False
            screen.fill((255,255,255))
            drawn = False
            defeat = True
            defeat_text = myfont.render('You lose', False, (0,0,0))
            screen.blit(defeat_text,(430,300))
            lives = 10
            display = []
            displaystrs = ''
            with open('words_to_use.txt','r') as f:
                mylist = [line.rstrip() for line in f]
                chosen_word = random.choice(mylist)
            word_length = len(chosen_word)
            for _ in range(word_length):
                display += '_'
    
    pygame.display.update()

    mainClock.tick(60)
