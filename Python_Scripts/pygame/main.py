import pygame
from pygame.locals import *
from constantes import *
import classes
import time

def main():
    pygame.init()

    #Ouverture de la fenêtre Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLUE)
    screen.blit(background, (0, 0))

    #generation de la grille
    ma_grille=classes.Grid(NUMBER_PER_LINE, NUMBER_OF_LINE, NUMBER_OF_BOMB)

    #on génère les x*y boutons
    list_button = ma_grille.create_display(screen)

    #Rafraîchissement de l'écran
    pygame.display.flip()

    #Loop until the user clicks the close button.
    done = False
    first_click_done = False

    #on charge une horloge
    #clock = pygame.time.Clock()

    #BOUCLE INFINIE
    while not done:
        #toutes les 10 ms
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                #on envoi dans la grille la position du clique et on signale si c'est le 1er clic
                loop_start_time = time.time()
                first_click_done = ma_grille.click(screen, event.pos, first_click_done)
                print("Loop time = ", loop_start_time - time.time())

        #a chaque tour on recup la position souris pour faire de on_hover
        position = pygame.mouse.get_pos()
        for each in list_button:
            each.draw(screen, position)

        pygame.display.flip()




if __name__ == '__main__':
    main()