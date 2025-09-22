import pygame
import sys
import math
import random
import time

# Pygame initialization
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Saud Games - ألعاب سعود")

# Colors
GREEN = (0, 100, 0)
DARK_GREEN = (0, 75, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
VERY_DARK_GRAY = (30, 30, 30)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
DARK_BROWN = (101, 67, 33)

# Fonts
try:
    font = pygame.font.Font('arial.ttf', 24)
except FileNotFoundError:
    font = pygame.font.Font(None, 24)

# Load images
image_size = (200, 200)
try:
    billiard_image = pygame.image.load('1.png')
    billiard_image = pygame.transform.scale(billiard_image, image_size)
    snake_image = pygame.image.load('2.png')
    snake_image = pygame.transform.scale(snake_image, image_size)
    sudoku_image = pygame.image.load('3.png')
    sudoku_image = pygame.transform.scale(sudoku_image, image_size)
    chess_image = pygame.image.load('4.png')
    chess_image = pygame.transform.scale(chess_image, image_size)
    crossword_image = pygame.image.load('5.png')
    crossword_image = pygame.transform.scale(crossword_image, image_size)
except pygame.error as e:
    print(f"Error loading images: {e}")
    sys.exit()

# --------------------------------------------------------------------------------------------------
## Game Menu
# --------------------------------------------------------------------------------------------------

def game_menu():
    screen.fill(BLACK)
    
    title_text_full = font.render("Saud Games - ألعاب سعود", True, WHITE)
    screen.blit(title_text_full, (50, 20))
    
    billiard_rect = pygame.Rect(50, 100, 200, 200)
    screen.blit(billiard_image, billiard_rect)
    text = font.render("Billiards", True, WHITE)
    text_rect = text.get_rect(center=(billiard_rect.centerx, billiard_rect.bottom + 15))
    screen.blit(text, text_rect)

    snake_rect = pygame.Rect(300, 100, 200, 200)
    screen.blit(snake_image, snake_rect)
    text = font.render("Snake", True, WHITE)
    text_rect = text.get_rect(center=(snake_rect.centerx, snake_rect.bottom + 15))
    screen.blit(text, text_rect)
    
    sudoku_rect = pygame.Rect(550, 100, 200, 200)
    screen.blit(sudoku_image, sudoku_rect)
    text = font.render("Sudoku", True, WHITE)
    text_rect = text.get_rect(center=(sudoku_rect.centerx, sudoku_rect.bottom + 15))
    screen.blit(text, text_rect)
    
    chess_rect = pygame.Rect(50, 350, 200, 200)
    screen.blit(chess_image, chess_rect)
    text = font.render("Chess", True, WHITE)
    text_rect = text.get_rect(center=(chess_rect.centerx, chess_rect.bottom + 15))
    screen.blit(text, text_rect)
    
    crossword_rect = pygame.Rect(300, 350, 200, 200)
    screen.blit(crossword_image, crossword_rect)
    text = font.render("Crossword", True, WHITE)
    text_rect = text.get_rect(center=(crossword_rect.centerx, crossword_rect.bottom + 15))
    screen.blit(text, text_rect)
    
    return {"billiard": billiard_rect, "crossword": crossword_rect, "snake": snake_rect, "sudoku": sudoku_rect, "chess": chess_rect}

# --------------------------------------------------------------------------------------------------
## Snake Game
# --------------------------------------------------------------------------------------------------

def snake_game():
    clock = pygame.time.Clock()
    start_time = time.time()
    
    grid_size = 20
    grid_width = SCREEN_WIDTH // grid_size
    grid_height = SCREEN_HEIGHT // grid_size
    
    snake = [(grid_width // 2, grid_height // 2)]
    snake_direction = (1, 0)
    
    apple_pos = (random.randint(1, grid_width-2), random.randint(1, grid_height-2))
    
    score = 0
    
    back_button_rect = pygame.Rect(10, 10, 100, 40)
    
    arrow_size = 40
    arrow_pos_x = 100
    arrow_pos_y = SCREEN_HEIGHT - 100
    up_arrow_rect = pygame.Rect(arrow_pos_x, arrow_pos_y - arrow_size, arrow_size, arrow_size)
    down_arrow_rect = pygame.Rect(arrow_pos_x, arrow_pos_y + arrow_size, arrow_size, arrow_size)
    left_arrow_rect = pygame.Rect(arrow_pos_x - arrow_size, arrow_pos_y, arrow_size, arrow_size)
    right_arrow_rect = pygame.Rect(arrow_pos_x + arrow_size, arrow_pos_y, arrow_size, arrow_size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos): return "menu"
                if up_arrow_rect.collidepoint(event.pos) and snake_direction != (0, 1): snake_direction = (0, -1)
                elif down_arrow_rect.collidepoint(event.pos) and snake_direction != (0, -1): snake_direction = (0, 1)
                elif left_arrow_rect.collidepoint(event.pos) and snake_direction != (1, 0): snake_direction = (-1, 0)
                elif right_arrow_rect.collidepoint(event.pos) and snake_direction != (-1, 0): snake_direction = (1, 0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1): snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1): snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0): snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0): snake_direction = (1, 0)
        
        snake_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, snake_head)
        
        if snake_head == apple_pos:
            score += 1
            apple_pos = (random.randint(1, grid_width-2), random.randint(0, grid_height-2))
        else: snake.pop()
        
        if snake_head[0] < 0 or snake_head[0] >= grid_width or snake_head[1] < 0 or snake_head[1] >= grid_height:
            return "menu"
        if snake_head in snake[1:]: return "menu"
            
        screen.fill(BLACK)
        
        for x in range(0, SCREEN_WIDTH, grid_size):
            pygame.draw.line(screen, VERY_DARK_GRAY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, grid_size):
            pygame.draw.line(screen, VERY_DARK_GRAY, (0, y), (SCREEN_WIDTH, y))

        pygame.draw.rect(screen, RED, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)
        
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0]*grid_size, segment[1]*grid_size, grid_size, grid_size))
            
        pygame.draw.circle(screen, RED, (apple_pos[0]*grid_size + grid_size//2, apple_pos[1]*grid_size + grid_size//2), grid_size//2)
        
        pygame.draw.rect(screen, LIGHT_GRAY, back_button_rect, border_radius=10)
        back_text = font.render("Back", True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)
        
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH - 200, 10))

        elapsed_time = int(time.time() - start_time)
        time_text = font.render(f"Time: {elapsed_time}", True, WHITE)
        screen.blit(time_text, (SCREEN_WIDTH - 200, 40))
        
        arrow_font = pygame.font.Font(None, 30)
        pygame.draw.rect(screen, WHITE, up_arrow_rect, border_radius=10)
        up_text = arrow_font.render('^', True, BLACK)
        up_text_rect = up_text.get_rect(center=up_arrow_rect.center)
        screen.blit(up_text, up_text_rect)

        pygame.draw.rect(screen, WHITE, down_arrow_rect, border_radius=10)
        down_text = arrow_font.render('v', True, BLACK)
        down_text_rect = down_text.get_rect(center=down_arrow_rect.center)
        screen.blit(down_text, down_text_rect)
        
        pygame.draw.rect(screen, WHITE, left_arrow_rect, border_radius=10)
        left_text = arrow_font.render('<', True, BLACK)
        left_text_rect = left_text.get_rect(center=left_arrow_rect.center)
        screen.blit(left_text, left_text_rect)

        pygame.draw.rect(screen, WHITE, right_arrow_rect, border_radius=10)
        right_text = arrow_font.render('>', True, BLACK)
        right_text_rect = right_text.get_rect(center=right_arrow_rect.center)
        screen.blit(right_text, right_text_rect)
        
        pygame.display.flip()
        clock.tick(8)

# --------------------------------------------------------------------------------------------------
## Sudoku Game
# --------------------------------------------------------------------------------------------------

def sudoku_game():
    original_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    board = [row[:] for row in original_board]
    cell_size = 50
    board_x = (SCREEN_WIDTH - cell_size * 9) // 2
    board_y = (SCREEN_HEIGHT - cell_size * 9) // 2
    back_button_rect = pygame.Rect(10, 10, 100, 40)
    selected_cell = None
    
    keypad_y_start = board_y + 9 * cell_size + 20
    keypad_rects = {}
    for i in range(1, 10):
        rect = pygame.Rect(board_x + (i-1) * cell_size, keypad_y_start, cell_size, cell_size)
        keypad_rects[i] = rect

    def is_valid(board, num, pos):
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i: return False
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i: return False
        box_x, box_y = pos[1] // 3, pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos: return False
        return True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos): return "menu"
                
                pos = pygame.mouse.get_pos()
                col = (pos[0] - board_x) // cell_size
                row = (pos[1] - board_y) // cell_size
                
                if 0 <= row < 9 and 0 <= col < 9 and original_board[row][col] == 0: selected_cell = (row, col)
                else: selected_cell = None
                
                for num, rect in keypad_rects.items():
                    if rect.collidepoint(pos) and selected_cell:
                        board[selected_cell[0]][selected_cell[1]] = num

        screen.fill(BLACK)
        
        for i in range(9):
            for j in range(9):
                rect = pygame.Rect(board_x + j * cell_size, board_y + i * cell_size, cell_size, cell_size)
                if selected_cell and selected_cell == (i, j): pygame.draw.rect(screen, BLUE, rect, 3)
                else: pygame.draw.rect(screen, WHITE, rect, 1)
                
                if board[i][j] != 0:
                    color = WHITE
                    if not is_valid(board, board[i][j], (i, j)): color = RED
                    text_surface = font.render(str(board[i][j]), True, color)
                    text_rect = text_surface.get_rect(center=rect.center)
                    screen.blit(text_surface, text_rect)
        
        for i in range(4):
            pygame.draw.line(screen, WHITE, (board_x + i * 3 * cell_size, board_y), (board_x + i * 3 * cell_size, board_y + 9 * cell_size), 3)
            pygame.draw.line(screen, WHITE, (board_x, board_y + i * 3 * cell_size), (board_x + 9 * cell_size, board_y + i * 3 * cell_size), 3)

        for num, rect in keypad_rects.items():
            pygame.draw.rect(screen, LIGHT_GRAY, rect, border_radius=10)
            text_surf = font.render(str(num), True, BLACK)
            text_rect = text_surf.get_rect(center=rect.center)
            screen.blit(text_surf, text_rect)

        pygame.draw.rect(screen, LIGHT_GRAY, back_button_rect, border_radius=10)
        back_text = font.render("Back", True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)
        
        pygame.display.flip()

# --------------------------------------------------------------------------------------------------
## دالة لعبة الشطرنج (Chess Game)
# --------------------------------------------------------------------------------------------------

def chess_game():
    cell_size = 70
    board_x = (SCREEN_WIDTH - cell_size * 8) // 2
    board_y = (SCREEN_HEIGHT - cell_size * 8) // 2
    
    piece_font = pygame.font.Font(None, 60)
    pieces = {'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟︎',
              'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'}
    
    board = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    ]
    
    selected_piece_pos = None
    
    back_button_rect = pygame.Rect(10, 10, 100, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return "menu"
                
                pos = pygame.mouse.get_pos()
                col = (pos[0] - board_x) // cell_size
                row = (pos[1] - board_y) // cell_size
                
                if 0 <= row < 8 and 0 <= col < 8:
                    if selected_piece_pos:
                        old_row, old_col = selected_piece_pos
                        if board[row][col] == ' ' or board[row][col].islower() != board[old_row][old_col].islower():
                            board[row][col] = board[old_row][old_col]
                            board[old_row][old_col] = ' '
                            selected_piece_pos = None
                    elif board[row][col] != ' ':
                        selected_piece_pos = (row, col)

        screen.fill(BLACK)
        
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK
                pygame.draw.rect(screen, color, (board_x + j * cell_size, board_y + i * cell_size, cell_size, cell_size))
                
                if selected_piece_pos and selected_piece_pos == (i, j):
                    pygame.draw.rect(screen, BLUE, (board_x + j * cell_size, board_y + i * cell_size, cell_size, cell_size), 4)

                piece = board[i][j]
                if piece != ' ':
                    piece_color = BLACK if piece.islower() else WHITE
                    piece_text = piece_font.render(pieces[piece], True, piece_color)
                    piece_rect = piece_text.get_rect(center=(board_x + j * cell_size + cell_size // 2, board_y + i * cell_size + cell_size // 2))
                    screen.blit(piece_text, piece_rect)
        
        pygame.draw.rect(screen, LIGHT_GRAY, back_button_rect, border_radius=10)
        back_text = font.render("Back", True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)
        
        pygame.display.flip()
# --------------------------------------------------------------------------------------------------
## دالة لعبة البلياردو (Billiards Game)
# --------------------------------------------------------------------------------------------------
def billiards_game():
    ball_radius = 12
    table_rect = pygame.Rect(50, 50, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100)
    pockets = [(table_rect.left, table_rect.top), (table_rect.centerx, table_rect.top), (table_rect.right, table_rect.top), (table_rect.left, table_rect.bottom), (table_rect.centerx, table_rect.bottom), (table_rect.right, table_rect.bottom)]
    
    class Ball:
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.color = color
            self.radius = ball_radius
            self.vel = [0, 0]
            self.is_moving = False
        def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
            if self.color != WHITE: pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius, 1)
        def move(self):
            self.x += self.vel[0]
            self.y += self.vel[1]
            self.vel[0] *= 0.98
            self.vel[1] *= 0.98
            if abs(self.vel[0]) < 0.1 and abs(self.vel[1]) < 0.1: self.vel = [0, 0]; self.is_moving = False
            else: self.is_moving = True
        def check_collisions(self):
            if self.x - self.radius < table_rect.left or self.x + self.radius > table_rect.right:
                self.vel[0] *= -1
                self.x = max(self.x, table_rect.left + self.radius)
                self.x = min(self.x, table_rect.right - self.radius)
            if self.y - self.radius < table_rect.top or self.y + self.radius > table_rect.bottom:
                self.vel[1] *= -1
                self.y = max(self.y, table_rect.top + self.radius)
                self.y = min(self.y, table_rect.bottom - self.radius)
            for pocket in pockets:
                if math.hypot(self.x - pocket[0], self.y - pocket[1]) < ball_radius + 10:
                    return True
            return False
    def setup_balls():
        balls = []
        white_ball = Ball(table_rect.left + 100, table_rect.centery, WHITE)
        balls.append(white_ball)
        start_x = table_rect.centerx + 150
        start_y = table_rect.centery
        row_count = 5
        ball_spacing = ball_radius * 2 + 2
        for row in range(row_count):
            for col in range(row + 1):
                x = start_x + row * (ball_spacing * math.sqrt(3) / 2)
                y = start_y - (row * ball_spacing / 2) + col * ball_spacing
                balls.append(Ball(x, y, RED))
        return balls
    def draw_table():
        pygame.draw.rect(screen, DARK_GREEN, table_rect)
        pygame.draw.rect(screen, BLACK, table_rect, 5)
        for pocket in pockets: pygame.draw.circle(screen, BLACK, pocket, ball_radius + 5)
    
    all_balls = setup_balls()
    white_ball = all_balls[0]
    billiards_score = 0
    start_time = time.time()
    
    is_shooting = False
    
    back_button_rect = pygame.Rect(10, 10, 100, 40)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button_rect.collidepoint(event.pos): return "menu"
                    is_shooting = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and is_shooting:
                    is_shooting = False
                    shot_end_pos = pygame.mouse.get_pos()
                    
                    dx = white_ball.x - shot_end_pos[0]
                    dy = white_ball.y - shot_end_pos[1]
                    distance = math.hypot(dx, dy)
                    
                    speed = min(distance / 15, 15)
                    white_ball.vel[0] = dx / distance * speed
                    white_ball.vel[1] = dy / distance * speed
        for ball in all_balls:
            ball.move()
            
        balls_to_remove = []
        for ball in all_balls:
            if ball.check_collisions():
                if ball.color == WHITE:
                    ball.x = table_rect.left + 100
                    ball.y = table_rect.centery
                    ball.vel = [0, 0]
                else: 
                    billiards_score += 1
                    balls_to_remove.append(ball)
        for ball in balls_to_remove: all_balls.remove(ball)
        
        screen.fill(GREEN)
        draw_table()
        for ball in all_balls: ball.draw(screen)
        if is_shooting:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, WHITE, (white_ball.x, white_ball.y), mouse_pos, 2)
        
        pygame.draw.rect(screen, LIGHT_GRAY, back_button_rect, border_radius=10)
        back_text = font.render("Back", True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)
        
        elapsed_time = int(time.time() - start_time)
        score_text = font.render(f"Score: {billiards_score}", True, WHITE)
        time_text = font.render(f"Time: {elapsed_time}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH - 200, 10))
        screen.blit(time_text, (SCREEN_WIDTH - 200, 40))
        
        pygame.display.flip()

# --------------------------------------------------------------------------------------------------
## دالة لعبة الكلمات المتقاطعة (Crossword Game)
# --------------------------------------------------------------------------------------------------
CROSSWORD_DATA = [
    {
        "difficulty": "Easy",
        "words": [("ORANGE", "A citrus fruit"), ("BANANA", "A yellow fruit")],
        "layout": {
            (1, 1): "O", (1, 2): "R", (1, 3): "A", (1, 4): "N", (1, 5): "G", (1, 6): "E",
            (2, 6): " ",
            (3, 2): "B", (4, 2): "A", (5, 2): "N", (6, 2): "A", (7, 2): "N", (8, 2): "A",
        }
    },
    {
        "difficulty": "Medium",
        "words": [("TIGER", "A striped wild cat"), ("LION", "King of the jungle")],
        "layout": {
            (1, 1): "T", (1, 2): "I", (1, 3): "G", (1, 4): "E", (1, 5): "R",
            (3, 1): " ",
            (3, 2): "L", (4, 2): "I", (5, 2): "O", (6, 2): "N",
        }
    }
]
def crossword_game():
    current_level = 0
    back_button_rect = pygame.Rect(10, 10, 100, 40)
    prev_button_rect = pygame.Rect(SCREEN_WIDTH - 220, 10, 100, 40)
    next_button_rect = pygame.Rect(SCREEN_WIDTH - 110, 10, 100, 40)
    cell_size = 40
    grid_start_x = (SCREEN_WIDTH - 9*cell_size) // 2
    grid_start_y = 100
    
    user_input = {pos: '' for pos, word in CROSSWORD_DATA[current_level]['layout'].items() if word != ' '}
    selected_cell = None

    while True:
        level_data = CROSSWORD_DATA[current_level]
        puzzle = level_data["words"]
        layout = level_data["layout"]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos): return "menu"
                if prev_button_rect.collidepoint(event.pos) and current_level > 0:
                    current_level -= 1
                    user_input = {pos: '' for pos, word in CROSSWORD_DATA[current_level]['layout'].items() if word != ' '}
                    selected_cell = None
                if next_button_rect.collidepoint(event.pos) and current_level < len(CROSSWORD_DATA) - 1:
                    current_level += 1
                    user_input = {pos: '' for pos, word in CROSSWORD_DATA[current_level]['layout'].items() if word != ' '}
                    selected_cell = None
                
                pos = pygame.mouse.get_pos()
                col = (pos[0] - grid_start_x) // cell_size
                row = (pos[1] - grid_start_y) // cell_size
                
                if (row, col) in layout and layout[(row, col)] != ' ':
                    selected_cell = (row, col)
                else: selected_cell = None
                
            if event.type == pygame.KEYDOWN and selected_cell:
                if event.key in range(pygame.K_a, pygame.K_z + 1):
                    user_input[selected_cell] = event.unicode.upper()
        
        screen.fill(BLACK)
        
        pygame.draw.rect(screen, LIGHT_GRAY, back_button_rect, border_radius=10)
        back_text = font.render("Back", True, BLACK)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        screen.blit(back_text, back_text_rect)

        pygame.draw.rect(screen, LIGHT_GRAY, prev_button_rect, border_radius=10)
        prev_text = font.render("Prev", True, BLACK)
        prev_text_rect = prev_text.get_rect(center=prev_button_rect.center)
        screen.blit(prev_text, prev_text_rect)
        
        pygame.draw.rect(screen, LIGHT_GRAY, next_button_rect, border_radius=10)
        next_text = font.render("Next", True, BLACK)
        next_text_rect = next_text.get_rect(center=next_button_rect.center)
        screen.blit(next_text, next_text_rect)

        # Draw puzzle grid and words
        for pos, word in layout.items():
            row, col = pos
            if word != " ":
                rect = pygame.Rect(grid_start_x + col * cell_size, grid_start_y + row * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, WHITE, rect, 1)
                text = font.render(user_input.get(pos, ''), True, WHITE)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
        
        # Draw clues
        clue_font = pygame.font.Font(None, 20)
        clue_x = grid_start_x + 9 * cell_size + 20
        clue_y = grid_start_y
        for word_data in puzzle:
            clue = word_data[1]
            clue_text = clue_font.render(clue, True, WHITE)
            screen.blit(clue_text, (clue_x, clue_y))
            clue_y += 30
        
        pygame.display.flip()
# --------------------------------------------------------------------------------------------------
## إدارة حالة اللعبة (Game State Manager)
# --------------------------------------------------------------------------------------------------

current_state = "menu"

running = True
while running:
    if current_state == "menu":
        button_rects = game_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rects["billiard"].collidepoint(event.pos): current_state = "billiards"
                if button_rects["crossword"].collidepoint(event.pos): current_state = "crossword"
                if button_rects["snake"].collidepoint(event.pos): current_state = "snake"
                if button_rects["sudoku"].collidepoint(event.pos): current_state = "sudoku"
                if button_rects["chess"].collidepoint(event.pos): current_state = "chess"
    elif current_state == "billiards":
        result = billiards_game()
        if result == "menu": current_state = "menu"
        elif result == "quit": running = False
    elif current_state == "crossword":
        result = crossword_game()
        if result == "menu": current_state = "menu"
        elif result == "quit": running = False
    elif current_state == "snake":
        result = snake_game()
        if result == "menu": current_state = "menu"
        elif result == "quit": running = False
    elif current_state == "sudoku":
        result = sudoku_game()
        if result == "menu": current_state = "menu"
        elif result == "quit": running = False
    elif current_state == "chess":
        result = chess_game()
        if result == "menu": current_state = "menu"
        elif result == "quit": running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
