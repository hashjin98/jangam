from sys import displayhook
import pygame


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    #흰색 원 중심좌표 =start button 반지름 60, 두께 5

# 게임 화면 보여주기
def display_game_screen():
    print("Game Start")


def check_buttons(pos): # pos에 해당하는 버튼 확인
    global start
    if start_button.collidepoint(pos):
        start = True

pygame.init()
screen_width = 1280
screen_height = 720

screen =pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)


# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#게임 시작 여부
start =False


running =True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: #사용자가 마우스를 클릭했을때
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
        

    # 화면 전체르 까맣게 칠함
    screen.fill(BLACK)
    
    if start:
        display_game_screen()
    else:
        display_start_screen()    # 시작 화면 표시

    # 사용자가 클릭한 좌표값이 있다면( 어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)

    #화면 업데이트
    pygame.display.update()


pygame.quit()

