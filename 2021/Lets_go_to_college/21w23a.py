import csv
import time
import random
import pygame
from pygame.locals import *

ver = "21w23a"

with open('data_package.csv') as file:
    csv_data = []
    for line in file.readlines():
        csv_data.append(line.split(','))

with open('login_data.csv') as file:
    login_data = []
    for line in file.readlines():
        login_data.append(line.split(','))


class select:
    def __init__(self, plag, name, value_1, value_2, value_3):
        self.plag = plag
        self.name = name
        self.value_1 = value_1
        self.value_2 = value_2
        self.value_3 = value_3


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (15, 15, 112)
sky_blue = (51, 179, 255)
beige = (220, 218, 178)
gray = (102, 102, 102)

image = pygame.image.load("1024.png")
image_1 = pygame.transform.scale(image, (420, 420))
image_2 = pygame.transform.scale(image, (200, 200))

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

font_input_L = pygame.font.Font('BinggraeTaom-Bold.ttf', 50)
font_input_M = pygame.font.Font('BinggraeTaom-Bold.ttf', 35)
font_input_S = pygame.font.Font('BinggraeTaom-Bold.ttf', 25)
font_input_subscript = pygame.font.Font('BinggraeTaom-Bold.ttf', 15)
font_input_login_1 = pygame.font.Font('BinggraeTaom-Bold.ttf', 100)
font_input_login_2 = pygame.font.Font('BinggraeTaom-Bold.ttf', 30)
font_input_login_3 = pygame.font.Font('BinggraeTaom-Bold.ttf', 50)
font_input_login_4 = pygame.font.Font('BinggraeTaom-Bold.ttf', 20)
font_input_login_5 = pygame.font.Font('BinggraeTaom-Bold.ttf', 15)
font_input_login_6 = pygame.font.Font('BinggraeTaom-Bold.ttf', 30)
font_input_logging_in = pygame.font.Font('BinggraeTaom-Bold.ttf', 35)
font_input_signup_1 = pygame.font.Font('BinggraeTaom-Bold.ttf', 80)
font_input_signup_2 = pygame.font.Font('BinggraeTaom-Bold.ttf', 20)
font_input_signup_3 = pygame.font.Font('BinggraeTaom-Bold.ttf', 30)
font_input_signup_4 = pygame.font.Font('BinggraeTaom-Bold.ttf', 20)
font_input_signup_5 = pygame.font.Font('BinggraeTaom-Bold.ttf', 15)
font_input_signup_6 = pygame.font.Font('BinggraeTaom-Bold.ttf', 20)
font_input_signup_7 = pygame.font.Font('BinggraeTaom-Bold.ttf', 25)

pygame.display.set_caption("Let's_go_to_college")

clock = pygame.time.Clock()

input_log = select(0, '-', 0.1, 0, 0)


def search(input):
    '''
    input_result = input.split()

    input_log.value_1, input_log.value_2, input_log.value_3 = 0, 0, 0

    search_plag = 0
    while search_plag < 3:
        i = 0
        while True:
            i += 1
            j = 0
            try:
                while True:
                    if input_result[j] == csv_data[i][search_plag]:
                        if search_plag == 0:
                            input_log.value_1 = i
                        elif search_plag == 1:
                            input_log.value_2 = i
                        elif search_plag == 2:
                            input_log.value_3 = i
                    j += 1
            except:
                break

        if search_plag == 0 and input_log.value_1 == 0:
            search_plag += 1

        search_plag += 1
    '''


def registration(name, identification, password_1, password_2):
    input_log.plag = 3

    identification_list = list(identification)
    password_1_lsit = list(password_1)
    password_2_lsit = list(password_2)

    if password_1 != password_2:
        input_log.plag = 14

    i = 0
    try:
        while True:
            if 'a' <= password_1_lsit[i] <= 'z':
                pass
            elif 'A' <= password_1_lsit[i] <= 'Z':
                pass
            elif '0' <= password_1_lsit[i] <= '9':
                pass
            else:
                input_log.plag = 13
            i += 1
    except:
        pass

    i = 0
    try:
        while True:
            if 'a' <= password_2_lsit[i] <= 'z':
                pass
            elif 'A' <= password_2_lsit[i] <= 'Z':
                pass
            elif 0 <= password_2_lsit[i] <= 9:
                pass
            else:
                input_log.plag = 13
            i += 1
    except:
        pass

    if 8 <= len(password_1) <= 16 and  8 <= len(password_2) <= 16:
        pass
    else:
        input_log.plag = 12

    count = 0
    i = 0
    try:
        while True:
            if identification_list[i] == '@':
                if count == 0:
                    count = 1
                else:
                    count = -1
            i += 1
    except:
        pass

    try:
        if identification_list[-4] == '.' and identification_list[-3] == 'c' and \
                identification_list[-2] == 'o' and identification_list[-1] == 'm':
            if count == 1:
                count = 2
    except:
        pass

    if count != 2:
        input_log.plag = 11

    i = 0
    try:
        while True:
            i += 1
            if identification == login_data[i][1]:
                input_log.plag = 10
    except:
        pass

    i = 0
    try:
        while True:
            i += 1
            if name == login_data[i][0]:
                input_log.plag = 9
    except:
        pass

    if name == 'ADMIN':
        input_log.plag = 8

    if input_log.plag == 3:
        f = open('login_data.csv', 'a', newline = '')
        wr = csv.writer(f)
        wr.writerow([name, identification, password_1, ''])
        f.close()

        login_data.append([name, identification, password_1, ''])


def signup():
    sigup_plag = 0
    name = ""
    identification = ""
    password_1 = ""
    password_2 = ""
    while 3 <= input_log.plag <= 7:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                input_log.plag = 3
                if 200 <= pos[0] <= 800:
                    if 255 <= pos[1] <= 305:
                        input_log.plag = 4
                    elif 335 <= pos[1] <= 385:
                        input_log.plag = 5
                    elif 415 <= pos[1] <= 465:
                        input_log.plag = 6
                    elif 495 <= pos[1] <= 545:
                        input_log.plag = 7
                    elif 580 <= pos[1] <= 650:
                        registration(name, identification, password_1, password_2)
                        sigup_plag = 0
                        if input_log.plag != 3:
                            sigup_plag = input_log.plag - 7
                            input_log.plag = 3
                        else:
                            input_log.plag = 0
                            login('signup')
                    elif 660 <= pos[1] <= 700:
                        input_log.plag = 0
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if input_log.plag == 4:
                        name = name[:-1]
                    elif input_log.plag == 5:
                        identification = identification[:-1]
                    elif input_log.plag == 6:
                        password_1 = password_1[:-1]
                    elif input_log.plag == 7:
                        password_2 = password_2[:-1]
                elif event.key == K_RETURN:
                    registration(name, identification, password_1, password_2)
                    sigup_plag = 0
                    if input_log.plag != 3:
                        sigup_plag = input_log.plag - 7
                        input_log.plag = 3
                    else:
                        input_log.plag = 0
                        login('signup')
                else:
                    if input_log.plag == 4:
                        if len(name) <= 42:
                            name += event.unicode
                    elif input_log.plag == 5:
                        if len(identification) <= 42:
                            identification += event.unicode
                    elif input_log.plag == 6:
                        if len(password_1) <= 40:
                            password_1 += event.unicode
                    elif input_log.plag == 7:
                        if len(password_2) <= 40:
                            password_2 += event.unicode
            if event.type == QUIT:
                return

        screen.fill(white)

        screen.blit(image_2, [245, 30])
        pygame.draw.polygon(screen, blue, [[0, 0], [0, 250], [250, 0]], 0)
        pygame.draw.rect(screen, gray, [0, 760, 1000, 40], 0)
        pygame.draw.rect(screen, blue, [200, 255, 600, 50], 2)
        pygame.draw.rect(screen, blue, [200, 335, 600, 50], 2)
        pygame.draw.rect(screen, blue, [200, 415, 600, 50], 2)
        pygame.draw.rect(screen, blue, [200, 495, 600, 50], 2)
        pygame.draw.rect(screen, blue, [200, 580, 600, 70], 0)
        pygame.draw.rect(screen, black, [200, 660, 600, 40], 1)
        pygame.draw.line(screen, black, [0, 757], [1000, 757], 3)

        signup_identification_text = font_input_signup_7.render(name, True, blue)
        screen.blit(signup_identification_text, [215, 265])

        signup_identification_text = font_input_signup_7.render(identification, True, blue)
        screen.blit(signup_identification_text, [215, 345])

        signup_password_text = font_input_signup_7.render(len(password_1) * '*', True, blue)
        screen.blit(signup_password_text, [215, 425])

        signup_password_text = font_input_signup_7.render(len(password_2) * '*', True, blue)
        screen.blit(signup_password_text, [215, 505])

        text_1 = font_input_subscript.render("POWERED BY PYTHON3.6 | MADE BY JG IN SEOUL", True, sky_blue)
        screen.blit(text_1, [10, 770])

        text_2 = font_input_subscript.render("ver." + ver, True, sky_blue)
        rect_text_2 = text_2.get_rect()
        rect_text_2.topright = (990, 770)
        screen.blit(text_2, rect_text_2)

        signup_text_1 = font_input_signup_1.render("SIGNUP", True, black)
        screen.blit(signup_text_1, [460, 80])

        signup_text_2 = font_input_signup_2.render("Your name", True, black)
        screen.blit(signup_text_2, [200, 230])

        signup_text_3 = font_input_signup_2.render("Email", True, black)
        screen.blit(signup_text_3, [200, 310])

        signup_text_4 = font_input_signup_2.render("Password", True, black)
        screen.blit(signup_text_4, [200, 390])

        signup_text_4 = font_input_signup_2.render("Re-enter password", True, black)
        screen.blit(signup_text_4, [200, 470])

        signup_text_5 = font_input_signup_3.render("SIGNUP", True, white)
        rect_signup_text_5 = signup_text_5.get_rect()
        rect_signup_text_5.center = (screen_width / 2, 615)
        screen.blit(signup_text_5, rect_signup_text_5)

        signup_text_6 = font_input_signup_4.render("LOGIN", True, gray)
        rect_signup_text_6 = signup_text_6.get_rect()
        rect_signup_text_6.center = (screen_width / 2, 680)
        screen.blit(signup_text_6, rect_signup_text_6)

        if len(name) == 0:
            signup_text_7 = font_input_signup_6.render("Enter your name...", True, gray)
            screen.blit(signup_text_7, [215, 268])

        if len(identification) == 0:
            signup_text_8 = font_input_signup_6.render("Enter email...", True, gray)
            screen.blit(signup_text_8, [215, 348])

        if len(password_1) == 0:
            signup_text_9 = font_input_signup_6.render("Enter password...", True, gray)
            screen.blit(signup_text_9, [215, 428])

        if len(password_2) == 0:
            signup_text_10 = font_input_signup_6.render("Enter re-enter password...", True, gray)
            screen.blit(signup_text_10, [215, 508])

        if sigup_plag == 1:
            signup_error_text_1 = font_input_signup_5.render("'ADMIN'은 사용자 이름으로 사용할 수 없습니다.", True, gray)
            rect_signup_error_text_1 = signup_error_text_1.get_rect()
            rect_signup_error_text_1.center = (screen_width / 2, 555)
            screen.blit(signup_error_text_1, rect_signup_error_text_1)

        if sigup_plag == 2:
            signup_error_text_2 = font_input_signup_5.render("이미 사용중인 사용자 이름 입니다.", True, gray)
            rect_signup_error_text_2 = signup_error_text_2.get_rect()
            rect_signup_error_text_2.center = (screen_width / 2, 555)
            screen.blit(signup_error_text_2, rect_signup_error_text_2)

        if sigup_plag == 3:
            signup_error_text_3 = font_input_signup_5.render("이미 사용중인 사용자 이메일 입니다.", True, gray)
            rect_signup_error_text_3 = signup_error_text_3.get_rect()
            rect_signup_error_text_3.center = (screen_width / 2, 555)
            screen.blit(signup_error_text_3, rect_signup_error_text_3)

        if sigup_plag == 4:
            signup_error_text_4 = font_input_signup_5.render("올바른 이메일을 입력하여주십시오.", True, gray)
            rect_signup_error_text_4 = signup_error_text_4.get_rect()
            rect_signup_error_text_4.center = (screen_width / 2, 555)
            screen.blit(signup_error_text_4, rect_signup_error_text_4)

        if sigup_plag == 5:
            signup_error_text_5 = font_input_signup_5.render("비밀번호는 8~16자로 구성하여 주십시오.", True, gray)
            rect_signup_error_text_5 = signup_error_text_5.get_rect()
            rect_signup_error_text_5.center = (screen_width / 2, 555)
            screen.blit(signup_error_text_5, rect_signup_error_text_5)

        if sigup_plag == 6:
            signup_error_text_6 = font_input_signup_5.render("비밀번호는 영문 대,소문자 혹은 숫자로 구성하여 주십시오.", True, gray)
            rect_signup_error_text_6 = signup_error_text_6.get_rect()
            rect_signup_error_text_6.center = (screen_width / 2, 555)
            screen.blit(signup_error_text_6, rect_signup_error_text_6)

        if sigup_plag == 7:
            signup_error_text_7 = font_input_signup_5.render("비밀번호가 서로 일치하지 않습니다.", True, gray)
            rect_signup_error_text_7 = signup_error_text_7.get_rect()
            rect_signup_error_text_7.center = (screen_width / 2, 555)
            screen.blit(signup_error_text_7, rect_signup_error_text_7)

        pygame.display.update()


def logging_in():
    count = 0
    while input_log.plag == 15 and count <= 1000:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        count += random.randint(5, 8)

        time.sleep(0.1)

        screen.fill(white)

        screen.blit(image_2, [400, 200])
        pygame.draw.polygon(screen, blue, [[0, 0], [0, 250], [250, 0]], 0)
        pygame.draw.rect(screen, gray, [0, 760, 1000, 40], 0)
        pygame.draw.line(screen, black, [0, 757], [1000, 757], 3)

        pygame.draw.rect(screen, blue, [200, 550, 600, 50], 0)
        pygame.draw.rect(screen, white, [200 + count, 550, 600, 50], 0)
        pygame.draw.rect(screen, black, [200, 550, 600, 50], 2)

        text_1 = font_input_subscript.render("POWERED BY PYTHON3.6 | MADE BY JG IN SEOUL", True, sky_blue)
        screen.blit(text_1, [10, 770])

        text_2 = font_input_subscript.render("ver." + ver, True, sky_blue)
        rect_text_2 = text_2.get_rect()
        rect_text_2.topright = (990, 770)
        screen.blit(text_2, rect_text_2)

        if count < 600:
            logging_in_text_1 = font_input_logging_in.render("로그인중...", True, gray)
        elif count > 650:
            logging_in_text_1 = font_input_logging_in.render("환영합니다. " + input_log.name + " 님", True, gray)
        else:
            logging_in_text_1 = font_input_logging_in.render("", True, gray)
        rect_logging_in_text_1 = logging_in_text_1.get_rect()
        rect_logging_in_text_1.center = (screen_width / 2, 450)
        screen.blit(logging_in_text_1, rect_logging_in_text_1)

        pygame.display.update()

    if input_log.plag == 15:
        input_log.plag = 16


def identify(identification, password):
    i = 0
    try:
        while True:
            print(identification, login_data[i][1])
            print(identification == login_data[i][1])
            print(password, login_data[i][2])
            print(password == login_data[i][2])
            if identification == login_data[i][1]:
                if password == login_data[i][2]:
                    input_log.name = login_data[i][0]
                    if input_log.name == 'ADMIN':
                        input_log.name = '개발자'
                    input_log.plag = 15
            i += 1
    except:
        pass


def login(access):
    login_plag = 0
    identification = ""
    password = ""
    while 0 <= input_log.plag <= 2:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                input_log.plag = 0
                if 200 <= pos[0] <= 800:
                    if 320 <= pos[1] <= 390:
                        input_log.plag = 1
                    elif 450 <= pos[1] <= 520:
                        input_log.plag = 2
                    elif 580 <= pos[1] <= 650:
                        identify(identification, password)
                        if input_log.plag != 15:
                            login_plag = 1
                    elif 660 <= pos[1] <= 700:
                        input_log.plag = 3
                        login_plag = 2
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if input_log.plag == 1:
                        identification = identification[:-1]
                    elif input_log.plag == 2:
                        password = password[:-1]
                elif event.key == K_RETURN:
                    identify(identification, password)
                    if input_log.plag != 15:
                        login_plag = 1
                else:
                    if input_log.plag == 1:
                        if len(identification) <= 28:
                            identification += event.unicode
                    elif input_log.plag == 2:
                        if len(password) <= 28:
                            password += event.unicode
            elif event.type == QUIT:
                return

        screen.fill(white)

        screen.blit(image_2, [235, 70])
        pygame.draw.polygon(screen, blue, [[0, 0], [0, 250], [250, 0]], 0)
        pygame.draw.rect(screen, gray, [0, 760, 1000, 40], 0)
        pygame.draw.rect(screen, blue, [200, 320, 600, 70], 2)
        pygame.draw.rect(screen, blue, [200, 450, 600, 70], 2)
        pygame.draw.rect(screen, blue, [200, 580, 600, 70], 0)
        pygame.draw.rect(screen, black, [200, 660, 600, 40], 1)
        pygame.draw.line(screen, black, [0, 757], [1000, 757], 3)

        identification_text = font_input_M.render(identification, True, blue)
        screen.blit(identification_text, [215, 330])

        password_text = font_input_M.render(len(password) * '*', True, blue)
        screen.blit(password_text, [215, 465])

        text_1 = font_input_subscript.render("POWERED BY PYTHON3.6 | MADE BY JG IN SEOUL", True, sky_blue)
        screen.blit(text_1, [10, 770])

        text_2 = font_input_subscript.render("ver." + ver, True, sky_blue)
        rect_text_2 = text_2.get_rect()
        rect_text_2.topright = (990, 770)
        screen.blit(text_2, rect_text_2)

        login_text_1 = font_input_login_1.render("LOGIN", True, black)
        screen.blit(login_text_1, [460, 120])

        login_text_2 = font_input_login_2.render("Email", True, black)
        screen.blit(login_text_2, [200, 280])

        login_text_4 = font_input_login_2.render("Password", True, black)
        screen.blit(login_text_4, [200, 410])

        login_text_5 = font_input_login_2.render("LOGIN", True, white)
        rect_login_text_5 = login_text_5.get_rect()
        rect_login_text_5.center = (screen_width / 2, 615)
        screen.blit(login_text_5, rect_login_text_5)

        login_text_6 = font_input_login_4.render("SIGNUP", True, gray)
        rect_login_text_6 = login_text_6.get_rect()
        rect_login_text_6.center = (screen_width / 2, 680)
        screen.blit(login_text_6, rect_login_text_6)

        if login_plag == 1:
            if access == 'main' or access == 'signup':
                access = '-'
            login_text_7 = font_input_login_5.render("가입하지 않은 아이디이거나, 잘못된 비밀번호입니다.", True, gray)
            rect_login_text_7 = login_text_7.get_rect()
            rect_login_text_7.center = (screen_width / 2, 535)
            screen.blit(login_text_7, rect_login_text_7)

        if len(identification) == 0:
            login_text_8 = font_input_login_6.render("Enter email...", True, gray)
            screen.blit(login_text_8, [215, 335])

        if len(password) == 0:
            login_text_9 = font_input_login_6.render("Enter password...", True, gray)
            screen.blit(login_text_9, [215, 465])

        if access == 'main':
            login_text_10 = font_input_login_5.render("정상적으로 로그아웃 되었습니다.", True, gray)
            rect_login_text_10 = login_text_10.get_rect()
            rect_login_text_10.center = (screen_width / 2, 535)
            screen.blit(login_text_10, rect_login_text_10)

        if access == 'signup':
            login_text_10 = font_input_login_5.render("정상적으로 화원가입 되었습니다.", True, gray)
            rect_login_text_10 = login_text_10.get_rect()
            rect_login_text_10.center = (screen_width / 2, 535)
            screen.blit(login_text_10, rect_login_text_10)

        pygame.display.update()

    if login_plag == 2:
        signup()
        login('return')
    else:
        logging_in()


def main():
    clock.tick(20)

    login('start')

    main_plag = 0
    input = ""
    while input_log.plag == 16:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 835 <= pos[0] <= 1000:
                    if 0 <= pos[1] <= 35:
                        main_plag = 1
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if len(input) <= 30:
                        input += " "
                elif event.key == K_BACKSPACE:
                    input = input[:-1]
                elif event.key == K_RETURN:
                    search(input)
                    input = ""
                else:
                    if len(input) <= 30:
                        input += event.unicode
            elif event.type == QUIT:
                return

        if input_log.plag == 16:
            screen.fill(white)

            screen.blit(image_1, [290, 100])
            pygame.draw.polygon(screen, blue, [[0, 0], [0, 250], [250, 0]], 0)
            pygame.draw.rect(screen, gray, [0, 760, 1000, 40], 0)
            pygame.draw.rect(screen, beige, [100, 568, 800, 70], 0)
            pygame.draw.rect(screen, blue, [100, 568, 800, 70], 5)
            pygame.draw.line(screen, black, [0, 757], [1000, 757], 3)

            text_1 = font_input_subscript.render("POWERED BY PYTHON3.6 | MADE BY JG IN SEOUL", True, sky_blue)
            screen.blit(text_1, [10, 770])

            text_2 = font_input_subscript.render("ver." + ver, True, sky_blue)
            rect_text_2 = text_2.get_rect()
            rect_text_2.topright = (990, 770)
            screen.blit(text_2, rect_text_2)

            account_text = font_input_subscript.render(input_log.name + " 님 환영합니다.", True, gray)
            rect_account_text = account_text.get_rect()
            rect_account_text.topright = (990, 10)
            screen.blit(account_text, rect_account_text)

            if len(input) <= 14:
                input_text = font_input_L.render(input, True, blue)
            elif len(input) <= 22:
                input_text = font_input_M.render(input, True, blue)
            else:
                input_text = font_input_S.render(input, True, blue)
            rect_input_text = input_text.get_rect()
            rect_input_text.center = (screen_width / 2, 600)
            screen.blit(input_text, rect_input_text)

            main_text_1 = font_input_S.render("검색어를 입력하세요.", True, gray)
            rect_main_text_1 = main_text_1.get_rect()
            rect_main_text_1.center = (screen_width / 2, 545)
            screen.blit(main_text_1, rect_main_text_1)

            if input_log.value_1 == 0 and input_log.value_2 == 0 and input_log.value_3 == 0:
                error_text = font_input_subscript.render("검색결과가 없습니다.", True, gray)
                rect_error_text = error_text.get_rect()
                rect_error_text.center = (screen_width / 2, 670)
                screen.blit(error_text, rect_error_text)

        pygame.display.update()

        if main_plag == 1:
            input_log.plag = 0
            login('main')


if __name__ == "__main__":
    main()