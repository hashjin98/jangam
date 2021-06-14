import pygame
from random import *


# 레벨에 맞게 설정
def setup(level):
    # 숫자 보여주는 시간
    global display_time
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)

    # 숫자 갯수
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
    
    # print(grid)


def display_start_screen():
    # start_font = pygame.font.Font(None, 45)
    # start_text = start_font.render("START", True,WHITE)
    # screen.blit(start_text, start_button_text)
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    #흰색 원 중심좌표 =start button 반지름 60, 두께 5

    msg = game_font.render(f" {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center = start_button.center)
    screen.blit(msg , msg_rect)

# 게임 화면 보여주기
def  display_game_screen():
    global hidden

    if not hidden:
        elapsed_time = float(pygame.time.get_ticks() -  start_ticks) / 1000 # ms -> sec
        if elapsed_time > display_time:
            hidden  = True
        
    for idx, rect in enumerate(number_buttons, start = 1 ):
        if hidden:
        # 버튼 사각형 그리기
            pygame.draw.rect(screen, GRAY, rect)
        else:
        # 실제 숫자 텍스트
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)


def check_buttons(pos): # pos에 해당하는 버튼 확인
    global start, start_ticks

    if start:
        check_number_buttons(pos)
    if start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()

def check_number_buttons(pos):
    global start, hidden, curr_level

    for button in number_buttons:
        global hidden
        if button.collidepoint(pos):
            if button == number_buttons[0]: # 올바른 숫자 클릭
                print("Correct")  
                del number_buttons[0]
                if not hidden:
                    hidden = True # 숫자 숨김 처리      
            else: # 잘못된 숫자 클릭
                game_over()
            break
    # LEVEL UP
    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)

# 게임 종료 처리. 메시지도 보여줌
def game_over():

    global running
    running = False
    msg = game_font.render(f"Your Level is {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center = (screen_width/2, screen_height/2))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)


pygame.init()
screen_width = 1280
screen_height = 720

screen =pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120) #폰트 정의

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)
start_button_text = (75, screen_height - 130)


# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)
number_buttons = [] # 플레이어가 눌러야 하는 버튼들
curr_level = 1
display_time = None # 숫자를 보여주는 시간
start_ticks = None # 시간 계산

#게임 시작 여부
start =False

#숫자 숨김 여부
hidden = False

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
        

    # 화면 전체을 까맣게 칠함
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
# 5초 
pygame.time.delay(5000)
pygame.quit()