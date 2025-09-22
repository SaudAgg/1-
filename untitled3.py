import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ألعاب سعود")

def draw_game_boxes():
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 200, 200)) # بلياردو
    pygame.draw.rect(screen, (0, 255, 0), (300, 50, 200, 200)) # لعبة الدودة
    pygame.draw.rect(screen, (0, 0, 255), (550, 50, 200, 200)) # الغاز
    pygame.draw.rect(screen, (255, 255, 0), (50, 300, 200, 200)) # لعبة الذاكرة
    pygame.draw.rect(screen, (255, 0, 255), (300, 300, 200, 200)) # أفعى وسلالم
    pygame.draw.rect(screen, (0, 255, 255), (550, 300, 200, 200)) # سودوكو
    pygame.draw.rect(screen, (128, 0, 128), (50, 550, 200, 200)) # شطرنج
    pygame.draw.rect(screen, (0, 128, 0), (300, 550, 200, 200)) # كلمات متقاطعة

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0)) # خلفية سوداء
    draw_game_boxes() # استدعاء الدالة هنا
    pygame.display.flip()

pygame.quit()