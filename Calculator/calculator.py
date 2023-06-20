# Imports
import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Images
logo = pygame.image.load("logo.png")

# Set up the window
width, height = 400, 670
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Calculator")
pygame.display.set_icon(logo)

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DGRAY = (44, 44, 44)

# Set up fonts
font_small = pygame.font.Font(None, 40)
font_large = pygame.font.Font(None, 60)

# Set up buttons
buttons = [
    ["(", ")", "√", "^"],
    ["sin", "cos", "tan", "π"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Set up input box
input_box = pygame.Rect(50, 100, 300, 50)
input_text = ""

# Main loop
running = True
while running:
    screen.fill(DGRAY)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(len(buttons)):
                    for j in range(len(buttons[i])):
                        button_x = 50 + j * 75
                        button_y = 200 + i * 75
                        button_rect = pygame.Rect(button_x, button_y, 70, 70)
                        if button_rect.collidepoint(mouse_pos):
                            button = buttons[i][j]
                            if button == "C":
                                input_text = ""
                            elif button == "=":
                                try:
                                    result = eval(input_text)
                                    input_text = str(result)
                                except:
                                    input_text = "Error"
                            elif button == "√":
                                try:
                                    result = math.sqrt(eval(input_text))
                                    input_text = str(result)
                                except:
                                    input_text = "Error"
                            elif button in ["sin", "cos", "tan"]:
                                try:
                                    radians = math.radians(eval(input_text))
                                    result = None
                                    if button == "sin":
                                        result = math.sin(radians)
                                    elif button == "cos":
                                        result = math.cos(radians)
                                    elif button == "tan":
                                        result = math.tan(radians)
                                    input_text = str(result)
                                except:
                                    input_text = "Error"
                            elif button == "π":
                                input_text += str(math.pi)
                            elif button == "^":
                                input_text += "**"
                            else:
                                input_text += button

    pygame.draw.rect(screen, GRAY, input_box, border_radius=10)
    pygame.draw.rect(screen, BLACK, input_box, 3)

    input_surface = font_large.render(input_text, True, BLACK)
    screen.blit(input_surface, (input_box.x + 10, input_box.y + 10))

    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            button_x = 50 + j * 75
            button_y = 200 + i * 75
            pygame.draw.rect(
                screen, GRAY, (button_x, button_y, 70, 70), border_radius=10)
            pygame.draw.rect(screen, BLACK, (button_x, button_y, 70, 70), 3)
            button_surface = font_small.render(buttons[i][j], True, BLACK)
            button_rect = button_surface.get_rect(
                center=(button_x + 35, button_y + 35))
            screen.blit(button_surface, button_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()