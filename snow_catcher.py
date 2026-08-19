# ============================================================
# Intro
# Snow Catcher.
# Inspired by a comment on the Cave Bear Games Discord
# Similar idea to Kaboom
# https://en.wikipedia.org/wiki/Kaboom!_(video_game)
# ============================================================

import pygame
import random
import math
import sys

# ============================================================
# Configuration
# ============================================================

WIDTH = 900
HEIGHT = 600
GROUND_Y = 520
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 70
BUCKET_WIDTH = 70
BUCKET_HEIGHT = 25
SNOWFLAKE_RADIUS = 8
ICE_WIDTH = 70
ICE_HEIGHT = 12
TARGET_CATCHES = 20
FPS = 60

# ============================================================
# Colors
# ============================================================

SKY = (135, 200, 235)
GROUND = (235, 245, 250)
PLAYER_COLOR = (50, 80, 180)
BUCKET_COLOR = (120, 160, 210)
SNOW_COLOR = (255, 255, 255)
ICE_COLOR = (150, 220, 255)
TEXT_COLOR = (30, 40, 60)

# ============================================================
# Player
# ============================================================

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = GROUND_Y - PLAYER_HEIGHT
        self.speed = 5

        # -1 = left
        #  0 = stopped
        #  1 = right
        self.direction = 0

        # Direction becomes locked while on ice.
        self.ice_direction = None

    @property
    def rect(self):
        return pygame.Rect(
            int(self.x),
            int(self.y),
            PLAYER_WIDTH,
            PLAYER_HEIGHT
        )

    @property
    def bucket_rect(self):
        return pygame.Rect(
            int(
                self.x -
                (BUCKET_WIDTH - PLAYER_WIDTH) / 2
            ),
            int(self.y + 10),
            BUCKET_WIDTH,
            BUCKET_HEIGHT
        )

    def update(self, keys, ice_patches):
        requested_direction = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            requested_direction = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            requested_direction = 1
        on_ice = self.is_on_ice(ice_patches)

        # ----------------------------------------------------
        # Ice behavior
        # ----------------------------------------------------

        if on_ice:
            if self.ice_direction is None:
                if requested_direction != 0:
                    self.ice_direction = requested_direction
                elif self.direction != 0:
                    self.ice_direction = self.direction
            if self.ice_direction is not None:
                self.direction = self.ice_direction
        else:
            self.ice_direction = None
            self.direction = requested_direction
        # Move the player.

        self.x += self.direction * self.speed

        # No edge clamping.
        #
        # The player is allowed to leave the screen.
        # Game.update() detects this and ends the game.

    def is_on_ice(self, ice_patches):
        player_rect = self.rect
        # Only the player's feet interact with the ice.
        feet = pygame.Rect(
            player_rect.left + 5,
            player_rect.bottom - 5,
            player_rect.width - 10,
            10
        )

        for patch in ice_patches:
            if feet.colliderect(patch):
                return True
        return False

    def draw(self, screen):
        # ----------------------------------------------------
        # Body
        # ----------------------------------------------------
        pygame.draw.rect(
            screen,
            PLAYER_COLOR,
            self.rect,
            border_radius=8
        )

        # ----------------------------------------------------
        # Head
        # ----------------------------------------------------

        pygame.draw.circle(
            screen,
            (245, 205, 170),
            (
                int(self.x + PLAYER_WIDTH // 2),
                int(self.y - 12)
            ),
            18
        )

        # ----------------------------------------------------
        # Bucket
        # ----------------------------------------------------

        pygame.draw.rect(
            screen,
            BUCKET_COLOR,
            self.bucket_rect,
            border_radius=5
        )

        # Bucket rim

        pygame.draw.line(
            screen,
            (60, 90, 120),
            (
                self.bucket_rect.left,
                self.bucket_rect.top
            ),
            (
                self.bucket_rect.right,
                self.bucket_rect.top
            ),
            4
        )

        # Bucket handle

        pygame.draw.arc(
            screen,
            (60, 90, 120),
            (
                self.bucket_rect.left + 8,
                self.bucket_rect.top - 12,
                self.bucket_rect.width - 16,
                25
            ),
            math.pi,
            2 * math.pi,
            3
        )


# ============================================================
# Snowflake
# ============================================================

class Snowflake:
    def __init__(self, speed):
        self.x = random.randint(
            SNOWFLAKE_RADIUS,
            WIDTH - SNOWFLAKE_RADIUS
        )
        self.y = -20
        self.speed = speed
    def update(self):
        self.y += self.speed

    @property
    def rect(self):
        return pygame.Rect(
            int(self.x - SNOWFLAKE_RADIUS),
            int(self.y - SNOWFLAKE_RADIUS),
            SNOWFLAKE_RADIUS * 2,
            SNOWFLAKE_RADIUS * 2
        )

    def draw(self, screen):
        x = int(self.x)
        y = int(self.y)
        # Simple six-arm snowflake.
        for angle in range(0, 180, 30):
            radians = math.radians(angle)
            dx = math.cos(radians) * 10
            dy = math.sin(radians) * 10
            pygame.draw.line(
                screen,
                SNOW_COLOR,
                (x - dx, y - dy),
                (x + dx, y + dy),
                2
            )
        pygame.draw.circle(
            screen,
            SNOW_COLOR,
            (x, y),
            3
        )

# ============================================================
# Game
# ============================================================

class Game:
    def __init__(self):
        self.player = Player()
        self.level = 1
        self.caught = 0
        self.snowflakes = []
        # Ice patches persist for the entire game.
        self.ice_patches = []
        self.spawn_timer = 0
        self.running = True
        self.game_over = False
        self.font = pygame.font.Font(
            None,
            36
        )
        self.big_font = pygame.font.Font(
            None,
            64
        )

    # ========================================================
    # Spawn snowflake
    # ========================================================

    def spawn_snowflake(self):
        # Snow gets faster every level.
        speed = (
            2.5 +
            (self.level - 1) * 0.7
        )
        self.snowflakes.append(
            Snowflake(speed)
        )

    # ========================================================
    # Create ice patch
    # ========================================================

    def create_ice_patch(self, x):
        patch_x = int(
            x - ICE_WIDTH / 2
        )
        # Keep the ice patch on the playing surface.
        patch_x = max(
            0,
            min(
                WIDTH - ICE_WIDTH,
                patch_x
            )
        )
        patch = pygame.Rect(
            patch_x,
            GROUND_Y - ICE_HEIGHT,
            ICE_WIDTH,
            ICE_HEIGHT
        )
        # Don't create overlapping patches.
        for existing in self.ice_patches:
            if existing.colliderect(patch):
                return
        self.ice_patches.append(patch)

    # ========================================================
    # Snowflake collision
    # ========================================================

    def check_snowflake(self, snowflake):
        if snowflake.rect.colliderect(
            self.player.bucket_rect
        ):
            self.caught += 1
            return True
        return False

    # ========================================================
    # Advance level
    # ========================================================

    def next_level(self):
        self.level += 1
        self.caught = 0
        # Remove currently falling snowflakes.
        self.snowflakes.clear()
        # Ice patches are intentionally NOT cleared.
        self.player.x = WIDTH // 2
        self.player.direction = 0
        self.player.ice_direction = None
        # Brief transition pause.
        pygame.time.delay(700)

    # ========================================================
    # Update game
    # ========================================================

    def update(self):
        # Don't update after game over.
        if self.game_over:
            return
        keys = pygame.key.get_pressed()

        # ----------------------------------------------------
        # Update player
        # ----------------------------------------------------

        self.player.update(
            keys,
            self.ice_patches
        )

        # ----------------------------------------------------
        # Check whether player fell off the edge.
        # ----------------------------------------------------

        if (
            self.player.x + PLAYER_WIDTH < 0
            or self.player.x > WIDTH
        ):
            self.game_over = True
            return

        # ----------------------------------------------------
        # Spawn snowflakes
        # ----------------------------------------------------

        spawn_interval = max(
            18,
            55 - self.level * 3
        )
        self.spawn_timer += 1
        if self.spawn_timer >= spawn_interval:
            self.spawn_timer = 0
            self.spawn_snowflake()

        # ----------------------------------------------------
        # Update snowflakes
        # ----------------------------------------------------

        for snowflake in self.snowflakes[:]:
            snowflake.update()

            # ------------------------------------------------
            # Did the player catch it?
            # ------------------------------------------------

            if self.check_snowflake(
                snowflake
            ):
                self.snowflakes.remove(
                    snowflake
                )
                # Level complete?
                if self.caught >= TARGET_CATCHES:
                    self.next_level()
                continue

            # ------------------------------------------------
            # Did we miss it?
            # ------------------------------------------------

            if (
                snowflake.y -
                SNOWFLAKE_RADIUS
                >= GROUND_Y
            ):

                self.create_ice_patch(
                    snowflake.x
                )

                self.snowflakes.remove(
                    snowflake
                )

    # ========================================================
    # Draw game
    # ========================================================

    def draw(self, screen):
        screen.fill(SKY)

        # ----------------------------------------------------
        # Ground
        # ----------------------------------------------------

        pygame.draw.rect(
            screen,
            GROUND,
            (
                0,
                GROUND_Y,
                WIDTH,
                HEIGHT - GROUND_Y
            )
        )

        # ----------------------------------------------------
        # Ice patches
        # ----------------------------------------------------

        for patch in self.ice_patches:
            pygame.draw.ellipse(
                screen,
                ICE_COLOR,
                patch
            )
            # Small highlight.
            pygame.draw.line(
                screen,
                (210, 245, 255),
                (
                    patch.left + 10,
                    patch.centery
                ),
                (
                    patch.right - 10,
                    patch.centery
                ),
                2
            )

        # ----------------------------------------------------
        # Snowflakes
        # ----------------------------------------------------

        for snowflake in self.snowflakes:
            snowflake.draw(screen)

        # ----------------------------------------------------
        # Player
        # ----------------------------------------------------

        self.player.draw(screen)

        # ----------------------------------------------------
        # HUD
        # ----------------------------------------------------

        level_text = self.font.render(
            f"LEVEL {self.level}",
            True,
            TEXT_COLOR
        )

        bucket_text = self.font.render(
            f"SNOWFLAKES: "
            f"{self.caught}/{TARGET_CATCHES}",
            True,
            TEXT_COLOR
        )

        screen.blit(
            level_text,
            (20, 20)
        )

        screen.blit(
            bucket_text,
            (20, 55)
        )

        # ----------------------------------------------------
        # Ice status
        # ----------------------------------------------------

        if self.player.ice_direction is not None:
            ice_text = self.font.render(
                "ON ICE!",
                True,
                TEXT_COLOR
            )

            screen.blit(
                ice_text,
                (
                    WIDTH -
                    ice_text.get_width() -
                    20,
                    20
                )
            )

        # ----------------------------------------------------
        # Controls
        # ----------------------------------------------------

        controls = self.font.render(
            "<- ->  or  A / D",
            True,
            TEXT_COLOR
        )

        screen.blit(
            controls,
            (
                WIDTH -
                controls.get_width() -
                20,
                HEIGHT - 40
            )
        )

        # ----------------------------------------------------
        # Game over screen
        # ----------------------------------------------------

        if self.game_over:

            overlay = pygame.Surface(
                (WIDTH, HEIGHT),
                pygame.SRCALPHA
            )

            overlay.fill(
                (0, 0, 0, 150)
            )

            screen.blit(
                overlay,
                (0, 0)
            )

            game_over_text = self.big_font.render(
                "GAME OVER",
                True,
                (255, 255, 255)
            )

            restart_text = self.font.render(
                "R = Restart    ESC = Quit",
                True,
                (255, 255, 255)
            )

            screen.blit(
                game_over_text,
                (
                    WIDTH // 2 -
                    game_over_text.get_width() // 2,
                    HEIGHT // 2 - 60
                )
            )

            screen.blit(
                restart_text,
                (
                    WIDTH // 2 -
                    restart_text.get_width() // 2,
                    HEIGHT // 2 + 10
                )
            )

        pygame.display.flip()


# ============================================================
# Main
# ============================================================

def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )
    pygame.display.set_caption(
        "Snow Catcher"
    )
    clock = pygame.time.Clock()
    game = Game()
    while game.running:
        # ----------------------------------------------------
        # Events
        # ----------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.KEYDOWN:
                # ESC always quits.
                if event.key == pygame.K_ESCAPE:
                    game.running = False
                # R only restarts from game-over.
                elif (
                    event.key == pygame.K_r
                    and game.game_over
                ):
                    game = Game()

        # ----------------------------------------------------
        # Update
        # ----------------------------------------------------

        game.update()

        # ----------------------------------------------------
        # Draw
        # ----------------------------------------------------

        game.draw(screen)
        clock.tick(FPS)
    pygame.quit()
    sys.exit()


# ============================================================
# Entry point
# ============================================================

if __name__ == "__main__":
    main()
