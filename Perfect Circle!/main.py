"""
Perfect Circle Game!
Author: Vedansh Bhatt
Last Modified: 2023-11-24
Next Steps: Put the drawing commands into the draw function.
"""
import sys, pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Perfect Circle!")

point_colour = (255, 255, 255)
line_colour = point_colour
start_pos, end_pos = None, None
line_width = 2

def draw():
    pass

confirm = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # for detecting first instance - user commits here
            if event.button == 1:
                confirm = True
                start_pos = event.pos
                end_pos = event.pos
        elif event.type == pygame.MOUSEMOTION: # can only fire after the go-ahead from mousebuttondown
            if confirm == True:
                draw()
            if pygame.mouse.get_pressed()[0]:
                end_pos = event.pos
                
        if start_pos is not None and end_pos is not None:
            pygame.draw.line(screen, line_colour, start_pos, end_pos, line_width)
        
        pygame.draw.circle(screen, point_colour, (width / 2, height / 2), 5)
        
    pygame.display.flip()