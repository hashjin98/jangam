import pygame
from random import *


# 레벨에 맞게 설정
def setup(level):
    number_count = (level // 3 ) +5
    number_count = min(number_count, 20) # 만약 20을 초과하면 20으로 처리


    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)


# 숫자 섞기(이 프로젝트에서 가장 중요)
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130 # 각 grid cell 별 가로, 세로 크기
    button_size = 110 # 각 grid cell 내에 실제로 그려질 버튼 크기
    screen_left_margin = 55 #여백
    screen_top_margin = 20

    grid =  [[0 for col in range(columns)] for row in range(rows)] # 5 * 9

    number = 1 # 시작 숫자 1부터 number_count 까지, 만약 5라면 5까지 숫자를 랜덤으로 배치
    while number <= number_count:
        row_idx = randrange(0, rows) # 0,1,2,3,4 중에서 랜덤으로 뽑기
        col_idx = randrange(0, columns) # 0 ~ 8 중에서 랜덤으로 뽑기

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            #현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + ( cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + ( cell_size / 2)

            #숫자 버튼
            button  = pygame.Rect(0, 0, button_size, button_size)
            button.center = ( center_x, center_y)

            number_buttons.append(button)
    
    print(grid)


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    #흰색 원 중심좌표 =start button 반지름 60, 두께 5

# 게임 화면 보여주기
def display_game_screen():
    for idx, rect in enumerate(number_buttons, start = 1 ):
        pygame.draw.rect(screen, GRAY, rect)

        # 실제 숫자 텍스트
        cell_text = game_font.render(str(idx), True, WHITE)
        text_rect = cell_text.get_rect(center = rect.center)
        screen.blit(cell_text, text_rect)



def check_buttons(pos): # pos에 해당하는 버튼 확인
    global start
    if start_button.collidepoint(pos):
        start = True

def check_box_button(pos) :
    pass
    

pygame.init()
screen_width = 1280
screen_height = 720

screen =pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120) #폰트 정의

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)


# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)
number_buttons = []

#게임 시작 여부
start =False

# 게임 시작 전에 게임 설정 함수 수행
setup(1)


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

