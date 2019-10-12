'''
Be kind to yourself and others.... please. 

First step is to stop thinking, talking about and looking at violent images.  
Violent films are mislabeded 'action' films.
Stop supporting them by not watching about them and not talking about them to others.  
STOP IT!! please. for your own sake.


Many people misinterpret the spiritual state of the upside down person (here represented by tarot card images.)  
Please reference Elizabeth Haich's book on "The Wisdom of The Tarot"  The true meaning of the upside down person 
is when we make progress and see the culture we are in as being 'wrong' and 'harmful' to us physically, mentally, 
emotionally and spiritually.  So up seems down and what we thought of as good now seems bad etc. So the upside down 
person is happy to see the truth but sad to see how wrong they had been before and how they can't talk about their 
new found perspective to most people because they will see it as 'wrong' or 'upside down'.

I hope you enjoy the game and I hope it will help you make some spiritual progress.

This project moved forward with the help of github https://github.com/electronicmag16/pythonHangMan 

'''



import sys
import random
import pygame
from tkinter import messagebox
from time import sleep

#CONSTANTS
MIN_ASCII_VALUE = 97 
MAX_ASCII_VALUE = 122
lineThickness=7
linethickness=4
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

BACKGROUND_COLOR=(90,30,90)
FOREGROUND_COLOR=(0,255,255)

gameDisplay = pygame.display.set_mode((0, 0))
pygame.font.init()               
myfont = pygame.font.SysFont('arial', 36, 'Comic Sans MS', 40)
myfont_big = pygame.font.SysFont('arial', 40, 'Comic Sans', 54)


nouns = [
    'people',
    'history',
    'way',
    'wand',
    'cart',
    'harp'
    'sharp'
    'art',
    'world',
    'information',
    'map',
    'two',
    'family',
    'government',
    'health',
    'system',
    'computer',
    'meat',
    'year',
    'thanks',
    'music',
    'person',
    'reading',
    'method',
    'data',
    'food',
    'understanding',
    'theory',
    'law',
    'bird',
    'literature',
    'problem',
    'software',
    'control',
    'knowledge',
    'power',
    'ability',
    'economics',
    'love',
    'internet',
    'television',
    'science',
    'library',
    'nature',
    'fact',
    'product',
    'idea',
    'temperature',
    'viable',
    'kind',
    'compassion',
    'wonderful',
    'love',
    'generousity',
    'investment',
    'area',
    'society',
    'activity',
    'story',
    'industry',
    'media',
    'thing',
    'oven',
    'community',
    'definition',
    'safety',
    'quality',
    'development',
    'invisible',
    'language',
    'management',
    'player',
    'variety',
    'video',
    'week',
    'security',
    'country',
    'exam',
    'movie',
    'organization',
    'equipment',
    'physics',
    'analysis',
    'policy',
    'series',
    'thought',
    'basis',
    'boyfriend',
    'direction',
    'strategy',
    'technology',
    'peace',
    'camera',
    'freedom',
    'paper',
    'environment',
    'child',
    'instance',
    'month',
    'truth',
    'marketing',
    'university',
    'writing',
    'article',
    'department',
    'difference',
    'goal',
    'news',
    'audience',
    'fishing',
    'growth',
    'income',
    'marriage',
    'user',
    'combination',
    'failure',
    'meaning',
    'medicine',
    'philosophy',
    'teacher',
    'communication',
    'night',
    'chemistry',
    'disease',
    'disk',
    'energy',
    'nation',
    'road',
    'role',
    'soup',
    'advertising',
    'location',
    'success',
    'addition',
    'apartment',
    'education',
    'math',
    'moment',
    'painting',
    'politics',
    'attention',
    'decision',
    'event',
    'property',
    'shopping',
    'student',
    'wood',
    'competition',
    'distribution',
    'entertainment',
    'office',
    'population',
    'president',
    'unit',
    'category',
    'natto',
    'miso',
    'sauerkraut',
    'mulching',
    'sheet',
    'coppicing',
    'landscape',
    'context',
    'introduction',
    'democracy',
    'liberty',
    'sustainability',
    'opportunity',
    'permaculture',
    'indigenous',
    'farming',
    'equality',
    'yikes',
    'awesome',
    'outrageous',
    'stupendous',
    'performance',
    'driver',
    'flight',
    'length',
    'magazine',
    'newspaper',
    'relationship',
    'teaching',
    'cell',
    'dealer',
    'debate',
    'finding',
    'lake',
    'member',
    'message',
    'phone',
    'scene',
    'appearance',
    'association',
    'concept',
    'customer',
    'death',
    'discussion',
    'housing',
    'inflation',
    'insurance',
    'cooperative',
    'cooperation',
    'co-housing',
    'community',
    'mood']

class stick_person:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color

    def draw_head(self):
        pygame.draw.circle(self.screen, self.color, (200, 230), 20, 3)
    
    def draw_body(self):
        pygame.draw.line(self.screen, self.color ,(200, 210), (200, 100), linethickness)
        
    def draw_left_arm(self):
        pygame.draw.line(self.screen, self.color ,(200, 180), (170, 120), linethickness)

    def draw_right_arm(self):
        pygame.draw.line(self.screen, self.color ,(200, 180), (230, 120), linethickness)

    def draw_left_leg(self):
        pygame.draw.line(self.screen, self.color ,(200, 110), (230, 50), linethickness)

    def draw_right_leg(self):
        pygame.draw.line(self.screen, self.color ,(200, 110), (170, 50), linethickness)

    def draw_left_foot(self):
        pygame.draw.line(self.screen, self.color ,(170, 50), (150, 50), linethickness)

    def draw_right_foot(self):
        pygame.draw.line(self.screen, self.color ,(230, 50), (250, 50), linethickness)


def draw_base(screen, FOREGROUND_COLOR):
    #lineThickness = 5
    pygame.draw.line(screen, FOREGROUND_COLOR, (20,20), (20,300), lineThickness)
    pygame.draw.line(screen, FOREGROUND_COLOR,(20,300),(200,300), lineThickness)
    pygame.draw.line(screen, FOREGROUND_COLOR,(20,20),(170,20), lineThickness)
    pygame.draw.line(screen, FOREGROUND_COLOR,(170,20),(170,50), lineThickness)



def main():
    newGame = 0
    screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('Spirtual Hang Person')
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

    

    p = stick_person(screen, FOREGROUND_COLOR)
    global counter
    counter = -1
    global wordsSolved
    wordsSolved = 0
    errors = 0
    line1 = ''
    line2 = 'You are given the first and last letter.  Please select a letter: '
    line3 = ''
    line4 = 'Number of errors: '
    line5 = ''
    line6 = "The letters you have already guessed are: "
    line8 = "You have correctly guessed " + str(wordsSolved) + " words!"
    word = ''
    processed_word = ''
    
    running = True
    letterList = []
    while running:
        
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                 sys.exit()
        screen.fill(BACKGROUND_COLOR)
        draw_base(screen, FOREGROUND_COLOR)
        
        if errors > 0:
            p.draw_head()

        if errors > 1:
            p.draw_body()

        if errors > 2:
            p.draw_left_arm()

        if errors > 3:
            p.draw_right_arm()

        if errors > 4:
            p.draw_left_leg()

        if errors > 5:
            p.draw_right_leg()

        if errors > 6:
            p.draw_left_foot()

        if errors > 7:
            p.draw_right_foot()
            pygame.display.flip()
            screen.fill(BACKGROUND_COLOR)
            pygame.display.flip()
            line9 = "One more lifetime completed!!!"
            line9b = "You are learning"
            line11 = 'The word was %s'  % answer
            line10 = 'Do you want to play again y or n?'
            display_message(screen, line9, FOREGROUND_COLOR, (150, 200))
            display_message(screen, line9b, FOREGROUND_COLOR, (200, 270))
            display_message(screen, line11, FOREGROUND_COLOR, (250, 340))
            display_message(screen, line10, FOREGROUND_COLOR, (300, 410))
            hangerImage = pygame.image.load('victorianfairyhanged140width.jpg')
            gameDisplay.blit(hangerImage, (0, 0))
            hanger2Image = pygame.image.load('victorianfairyhangedupsidedown140width.jpg')
            gameDisplay.blit(hanger2Image, (860,465))
            hangerImage = pygame.image.load('hangingP3.jpg')
            gameDisplay.blit(hangerImage, (860, 0))
            hanger2Image = pygame.image.load('hangingP4.jpg')
            gameDisplay.blit(hanger2Image, (0,454))
            pygame.display.flip()
            stay = True
            decision = ask_player(screen, 80, 400)
            while stay == True:
              if 'y' == decision.lower():
                stay = False
                main()
              elif 'n' == decision.lower():
                stay = False
                sys.exit()
              else:
                show_message_box(screen, '''Do you want to play again y or n? Please''')
                decision = ask_player(screen, 80, 400)
     
            
        else: 
            if processed_word.find('-') == -1:
                word = ''
                
            if word == '':
                word = generate_word()
                if counter >= 0:
                  wordsSolved += 1 
                counter +=1
                letterList = []
                letter = ""
                line8 = "You have correctly guessed " + str(wordsSolved) + " words!"
                line2 = 'Please select a letter '
                display_message(screen, line8, FOREGROUND_COLOR, (50, 620))
                pygame.display.flip()
                answer = word
                count = 0
                processed_word = ""
                processed_word = processed_word + word[0]
                while count <= (len(word)-3):
                    processed_word = processed_word + '-'
                    count +=1
                processed_word = processed_word + word[-1]
                line1 = processed_word
            
            display_message(screen, line1, FOREGROUND_COLOR, (50, 320))
            display_message(screen, line2, FOREGROUND_COLOR, (50, 380))
            display_message(screen, line3, FOREGROUND_COLOR, (50, 400))
            display_message(screen, line4 + str(errors), FOREGROUND_COLOR, (50, 440))
            letterListAlphaBetised = ""
            for n in letterList:
                letterListAlphaBetised = letterListAlphaBetised + n + " "
            display_message(screen, line6, FOREGROUND_COLOR, (50, 500))
            display_message(screen, letterListAlphaBetised, FOREGROUND_COLOR, (50, 560))
            display_message(screen, line8, FOREGROUND_COLOR, (50, 620))
            line8 = "You have correctly guessed " + str(wordsSolved) + " words!"
            line2 = 'Please select a letter '
            pygame.display.flip()
            
            letter = ask_letter(screen, 80, 350) 

            line2 = 'You selected the letter: ' + letter
            letterList.append(letter)
            letterList = sorted(letterList)
            word = list(word)
            word[len(word)-1] = '1'
            word[0] = '1'

            if letter in word:
                letter_pos = [i for i, a in enumerate(word) if a == letter]
                processed_word = list(processed_word)
                for key in letter_pos:
                    processed_word[key] = letter
                    word[key] = '1'
                processed_word = ''.join(processed_word)
                line1 = processed_word
                
            else:
                errors += 1
           
def display_message(screen, message, color, pos = (50, 30)):
    text = myfont.render(message, False, color)
    screen.blit(text, pos)
     
def display_message2(screen, message, color, pos = (50, 30)):
    text = myfont_big.render(message, False, color)
    screen.blit(text, pos)

def show_message_box(screen, message):
    sleep(2)
    screen.fill((90,30,30))
    text = myfont_big.render(message, False, (95, 255, 55))
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    sleep(3)

def detect_pressed_key(screen, key_pressed_ascii):
    key_pressed = ""
    if key_pressed_ascii >= MIN_ASCII_VALUE and key_pressed_ascii <= MAX_ASCII_VALUE: 
        key_pressed = chr(key_pressed_ascii)
        if key_pressed == "":
            pass
        else:
            return key_pressed
    else:
        
        return key_pressed   

def ask_player(screen, cord_x = 50, cord_y = 350):
    runningP = True
    while runningP:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                 sys.exit()
            if events.type == pygame.KEYDOWN:
                decision = detect_pressed_key(screen, events.key)
                runningP = False
    return decision

def ask_letter(screen, cord_x = 50, cord_y = 50):
    running = True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                 sys.exit()
            if events.type == pygame.KEYDOWN:
                letter = detect_pressed_key(screen, events.key)
                running = False
    return letter
               
def generate_word():
    numberBig = random.randint(0, 12345)
    word = nouns[numberBig % len(nouns)]
    return word
    




if __name__=="__main__":
  main()
