import pygame
from pygame.locals import *
import sys

print("\n[프로젝트] 대학가자\n\n")


with open('data_package.csv') as file:
    csv_data = []
    for line in file.readlines():
        csv_data.append(line.split(','))


class select:
    def __init__(self, value_1, value_2, value_3):
        self.value_1 = value_1
        self.value_2 = value_2
        self.value_3 = value_3


pygame.init()

white = (255,255,255)
black = (0,0,0)
blue = (15,15,112)
sky_blue = (51,179,255)
beige = (220,218,178)
gray = (102,102,102)

image_1 = pygame.image.load("1024.png")
image_1 = pygame.transform.scale(image_1, (420, 420))

screen_width = 1000
screen_height = 800
main_screen = pygame.display.set_mode((screen_width, screen_height))

font_input_L = pygame.font.Font('BinggraeTaom-Bold.ttf', 50)
font_input_M = pygame.font.Font('BinggraeTaom-Bold.ttf', 35)
font_input_S = pygame.font.Font('BinggraeTaom-Bold.ttf', 25)
font_input_subscript = pygame.font.Font('BinggraeTaom-Bold.ttf', 15)

pygame.display.set_caption("Let's_go_to_college")

clock = pygame.time.Clock()

input_log = select(0.1, 0, 0)


def search(input):
    input_result = input.split()

    input_log.value_1, input_log.value_2, input_log.value_3 = 0, 0, 0

    plag = 0
    while plag < 3:
        i = 0
        while True:
            i += 1
            j = 0
            try:
                while True:
                    if input_result[j] == csv_data[i][plag]:
                        if plag == 0:
                            input_log.value_1 = i
                        elif plag == 1:
                            input_log.value_2 = i
                        elif plag == 2:
                            input_log.value_3 = i
                    j += 1
            except:
                break

        if plag == 0 and input_log.value_1 == 0:
            plag += 1

        plag += 1


def main():
    input = ""
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    if len(input) <= 30:
                        input += event.unicode
                elif event.key == K_SPACE:
                    if len(input) <= 30:
                        input += " "
                elif event.key == K_BACKSPACE:
                    input = input[:-1]
                elif event.key == K_RETURN:
                    search(input)
                    input = ""
            elif event.type == QUIT:
                return


        main_screen.fill(white)

        main_screen.blit(image_1, [290, 100])
        pygame.draw.polygon(main_screen, blue, [[0, 0], [0, 250], [250, 0]], 0)
        pygame.draw.rect(main_screen, gray, [0, 760, 1000, 40], 0)
        pygame.draw.rect(main_screen, beige, [100, 568, 800, 70], 0)
        pygame.draw.rect(main_screen, blue, [100, 568, 800, 70], 5)
        pygame.draw.line(main_screen, black, [0, 757], [1000, 757], 3)

        if len(input) <= 14:
            input_text = font_input_L.render(input, True, blue)
        elif len(input) <= 22:
            input_text = font_input_M.render(input, True, blue)
        else:
            input_text = font_input_S.render(input, True, blue)
        rect_input_text = input_text.get_rect()
        rect_input_text.center = (screen_width / 2, 600)
        main_screen.blit(input_text, rect_input_text)

        text_1 = font_input_subscript.render("POWERED BY PYTHON3.6 | MADE BY JG IN SEOUL", True, sky_blue)
        main_screen.blit(text_1, [10, 770])

        text_2 = font_input_subscript.render("ver.21w22b", True, sky_blue)
        main_screen.blit(text_2, [900, 770])

        if input_log.value_1 == 0 and input_log.value_2 == 0 and input_log.value_3 == 0:
            error_text = font_input_subscript.render("검색결과가 없습니다.", True, gray)
            rect_error_text = error_text.get_rect()
            rect_error_text.center = (screen_width / 2, 670)
            main_screen.blit(error_text, rect_error_text)

        pygame.display.update()

if __name__ == "__main__":
    main()