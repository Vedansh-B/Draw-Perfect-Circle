"""
Perfect Circle Game!
Author: Vedansh Bhatt
Last Modified: 2023-11-26
Changes Made: Circle drawn with many points rather than a continuous line. 
Next Steps: Put the drawing commands into the draw function.
"""
import sys, pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw Perfect Circle!")

point_colour = (255, 255, 255)
line_colour = point_colour
line_width = 2

def draw():
    start_pos, end_pos = None, None
    if pygame.mouse.get_pressed()[0]:
        start_pos = event.pos
        end_pos = event.pos
        
    if start_pos is not None and end_pos is not None:
        pygame.draw.line(screen, line_colour, start_pos, end_pos, line_width)

confirm = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # for detecting first instance - user commits here
            if event.button == 1:
                confirm = True
        elif event.type == pygame.MOUSEMOTION: # can only fire after the go-ahead from mousebuttondown
            if confirm == True:
                draw()
                # line_start = (width // 2, height // 2)
                # line_end = (width // 2, height // 2)
                # line_color = (255, 0, 0)
                # line_width = 2
                # mouse_x, mouse_y = pygame.mouse.get_pos()
                # line_end = (mouse_x, mouse_y)
                # pygame.draw.line(screen, line_colour, line_start, line_end, 2)
                        
        pygame.draw.circle(screen, point_colour, (width / 2, height / 2), 5)
        
    pygame.display.flip()