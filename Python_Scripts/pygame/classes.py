import random
from constantes import *
import pygame

class Button:
    def __init__(self, setting, pos):
        self.text = ""
        self.is_hover = False
        self.is_clicked = False
        self.default_color = WHITE
        self.hover_color = GREEN
        self.clicked_color = YELLOW
        self.bomb_color = RED
        self.font_color = BLACK
        self.obj = None
        self.setup = setting
        self.has_bomb = False
        self.position = pos

    def label(self):
        font = pygame.font.Font(None, 20)
        return font.render(self.text, 1, self.font_color)

    def color(self):
        if self.is_hover:
            return self.hover_color
        elif self.is_clicked:
            return self.clicked_color
        else:
            if DEBUG and self.has_bomb:
                return self.bomb_color
            else:
                return self.default_color

    def click(self):
        self.is_clicked = True

    def draw(self, screen, mouse, labelcoord=None):
        '''create rect obj, draw, and change color based on input'''
        self.obj  = pygame.draw.rect(screen, self.color(), self.setup)
        if self.is_clicked:
            screen.blit(self.label(), [self.setup[0]+5,self.setup[1]+2])
        #change color if mouse over button
        self.check_hover(mouse)

    def check_hover(self, mouse):
        '''adjust is_hover value based on mouse over button - to change hover color'''
        if self.obj.collidepoint(mouse):
            self.is_hover = True
        else:
            self.is_hover = False

class Grid():
    def __init__(self, number_x, number_y, qte_mines):
        self.x = number_x
        self.y = number_y
        self.mines = qte_mines
        self.generate_array()
        self.obj_list = []
        self.obj_per_coord = {}
        #self.add_text()
        #self.show()

    def generate_array(self):
        self.grille = [["." for x in range(self.x)] for y in range(self.y)]

    def show(self):
        for y in range(self.y):
            print(self.grille[y])

    def place_bomb(self, start_x, start_y):
        #on pose aleatoirement n bombe en verifiant qu'on ne soit pas sur la position de depart
        self.position_bomb=[]
        while len(self.position_bomb) < self.mines+1:
            new_pos = (random.randrange(0,self.x-1,1), random.randrange(0,self.y-1,1))
            if new_pos not in self.position_bomb and new_pos != [start_x, start_y]:
                self.position_bomb.append(new_pos)
                self.grille[new_pos[0]][new_pos[1]] = "*"
                self.obj_per_coord[(new_pos[0],new_pos[1])].has_bomb= True
        self.add_text()
        self.show()

    def add_text(self):
        #pour tous les boutons de la grille
        for each_button in self.obj_list:
            #si le boutton est sur la position d'une bombe on met une *
            if each_button.position in self.position_bomb:
                each_button.text="*"
            else: #sinon on compte les bombe voisines
                voisin = 0
                for each_bomb in self.position_bomb:
                    if abs(each_bomb[0]-each_button.position[0])<2 and abs(each_bomb[1]-each_button.position[1])<2:
                        voisin +=1
                each_button.text=str(voisin)

    def expand_from(self, start_x, start_y):
        #print("expand on " + pos_str(x,y))
        if self.grille[start_x][start_y] == ".":
            voisin = 0
            for each_bomb in self.position_bomb:
                if abs(each_bomb[0]-start_x) < 2 and abs(each_bomb[1]-start_y) < 2:
                    voisin +=1
            self.grille[start_x][start_y]=voisin

            #if x+1 != old_x and x+1 <= l-1 and pos_str(x+1,y) not in visited.keys():
            #    visited[pos_str(x+1,y)]=1
            #    count += expand(x+1, y, x, y)
            #if x-1 != old_x and x-1 >= 0 and pos_str(x-1,y) not in visited.keys():
            #    visited[pos_str(x-1,y)]=1
            #    count += expand(x-1, y, x, y)
            #if y+1 != old_y and y+1 <= h-1 and pos_str(x,y+1) not in visited.keys():
            #    visited[pos_str(x,y+1)]=1
            #    count += expand(x, y+1, x, y)
            #if y-1 != old_y and y-1 >= 0 and pos_str(x,y-1) not in visited.keys():
            #    visited[pos_str(x,y-1)]=1
            #    count += expand(x, y-1, x, y)
        #return count

    def create_display(self, window):
        #Creation des boutons en 2 layer (bordure et contenu)
        for y in range(self.y):
            for x in range(self.x):
                #generate rectangle with border
                outer_case = pygame.draw.rect(window, BLACK, [(x+1)*(WIDTH_CELL+GAP_VERTICAL), (y+1)*(HEIGHT_CELL+GAP_HORIZONTAL), WIDTH_CELL, HEIGHT_CELL], CASE_THK)
                inner_case = Button([(y+1)*(HEIGHT_CELL+GAP_HORIZONTAL)+CASE_THK, (x+1)*(WIDTH_CELL+GAP_VERTICAL)+CASE_THK, WIDTH_CELL-(2*CASE_THK), HEIGHT_CELL-(2*CASE_THK)], (x,y))
                self.obj_list.append(inner_case)
                self.obj_per_coord[(x,y)] = inner_case
        return self.obj_list


    def click(self, window, position, bool_first_click):
        #pour tous les boutons de la grille
        for each_case in self.obj_list:
            if each_case.obj.collidepoint(position): #si le clic bouton hit le rectangle
                each_case.is_clicked = True
                if not bool_first_click: #si on n'a pas fait le 1er coup
                    self.place_bomb(position[0], position[1]) #on pose les bombes (pour eviter de demarrer directement sur une bombe)
                    bool_first_click = True
        return bool_first_click #on retourne que le 1er clic est fait ou non (si on clic a coté d'une case par ex)