import math
import random
from pathlib import Path

import pygame
from pygame import mixer

BASE_DIR = Path(__file__).resolve().parent
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 2
BULLET_SPEED = 1
ENEMY_COUNT = 6
PLAYER_Y = 500


def asset(name):
    return str(BASE_DIR / name)


def load_font(size):
    font_path = BASE_DIR / "Waffle Story.ttf"
    if font_path.exists():
        return pygame.font.Font(str(font_path), size)
    return pygame.font.Font(None, size)


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    return math.hypot(enemy_x - bullet_x, enemy_y - bullet_y) < 27


def main():
    pygame.init()
    mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invader")
    clock = pygame.time.Clock()

    background = pygame.image.load(asset("bg.jpg")).convert()
    icon = pygame.image.load(asset("ufo.png")).convert_alpha()
    pygame.display.set_icon(icon)

    try:
        mixer.music.load(asset("space_line.wav"))
        mixer.music.play(-1)
    except pygame.error:
        pass

    player_img = pygame.image.load(asset("player 2.png")).convert_alpha()
    enemy_img = pygame.image.load(asset("alien.png")).convert_alpha()
    bullet_img = pygame.image.load(asset("bullets.png")).convert_alpha()

    bullet_sound = collision_sound = game_over_sound = None
    for filename, target in [
        ("arcbsmm.wav", "bullet"),
        ("coll.wav", "collision"),
        ("govdsf.wav", "game_over"),
    ]:
        try:
            sound = mixer.Sound(asset(filename))
            if target == "bullet":
                bullet_sound = sound
            elif target == "collision":
                collision_sound = sound
            else:
                game_over_sound = sound
        except pygame.error:
            pass

    font = load_font(30)
    game_over_font = load_font(65)

    player_x = 370
    player_x_change = 0

    enemies = [
        {
            "x": random.randint(0, WIDTH - 64),
            "y": random.randint(30, 170),
            "speed": 0.5,
        }
        for _ in range(ENEMY_COUNT)
    ]

    bullet_x = 0
    bullet_y = PLAYER_Y
    bullet_state = "ready"
    score_value = 0
    game_over = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -PLAYER_SPEED
                elif event.key == pygame.K_RIGHT:
                    player_x_change = PLAYER_SPEED
                elif event.key == pygame.K_SPACE and bullet_state == "ready" and not game_over:
                    if bullet_sound:
                        bullet_sound.play()
                    bullet_x = player_x
                    bullet_y = PLAYER_Y
                    bullet_state = "fire"

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player_x_change = 0

        if not game_over:
            player_x += player_x_change
            player_x = max(0, min(player_x, WIDTH - player_img.get_width()))

            for enemy in enemies:
                if enemy["y"] > 440:
                    game_over = True
                    if game_over_sound:
                        game_over_sound.play()
                    break

                enemy["x"] += enemy["speed"]

                if enemy["x"] <= 0:
                    enemy["x"] = 0
                    enemy["speed"] = abs(enemy["speed"])
                    enemy["y"] += 20
                elif enemy["x"] >= WIDTH - enemy_img.get_width():
                    enemy["x"] = WIDTH - enemy_img.get_width()
                    enemy["speed"] = -abs(enemy["speed"])
                    enemy["y"] += 20

                if bullet_state == "fire" and is_collision(
                    enemy["x"], enemy["y"], bullet_x, bullet_y
                ):
                    if collision_sound:
                        collision_sound.play()
                    bullet_y = PLAYER_Y
                    bullet_state = "ready"
                    score_value += 1
                    enemy["x"] = random.randint(0, WIDTH - enemy_img.get_width())
                    enemy["y"] = random.randint(30, 170)

            if bullet_state == "fire":
                bullet_y -= BULLET_SPEED
                if bullet_y < 0:
                    bullet_y = PLAYER_Y
                    bullet_state = "ready"

        screen.blit(background, (0, 0))

        for enemy in enemies:
            if enemy["y"] < HEIGHT:
                screen.blit(enemy_img, (enemy["x"], enemy["y"]))

        if bullet_state == "fire" and not game_over:
            screen.blit(bullet_img, (bullet_x + 16, bullet_y + 10))

        screen.blit(player_img, (player_x, PLAYER_Y))

        score_surface = font.render(f"Score: {score_value}", True, (250, 128, 114))
        screen.blit(score_surface, (10, 10))

        if game_over:
            game_over_surface = game_over_font.render("GAME OVER", True, (250, 128, 114))
            rect = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(game_over_surface, rect)

            hint = font.render("Close the window to exit.", True, (255, 255, 255))
            hint_rect = hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
            screen.blit(hint, hint_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
