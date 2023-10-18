import pygame, random, math

pygame.init()

screen_width = 1300
screen_height = 650
fps = 60
SPEED = 2.5
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
background_color = (255, 255, 255)  # White color (R, G, B values)
PATH = ([0, 170], [250, 170], [250, 10], [1050, 10], [1050, 530], [-50, 530])

class Monkey(pygame.sprite.Sprite):
    def __init__(self, x, y, firing_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"ball.jpg")
        self.scaled_image = pygame.transform.scale(self.image, (80, 100))
        self.rect = self.scaled_image.get_rect()
        self.rect.center = [x, y]
        self.speed = 50  # Added speed for bullets
        self.time_cooldown = 0  # Added time_cooldown

    def update(self):
        if self.time_cooldown <= 0:
            for balloon in balloon_group:
                distance = math.sqrt((self.rect.x - balloon.rect.x) ** 2 + (self.rect.y - balloon.rect.y) ** 2)
                time = distance / self.speed
                future_x = balloon.rect.x + balloon.velocity[0] * time
                future_y = balloon.rect.y + balloon.velocity[1] * time

                bullet = Bullet(self.rect.x, self.rect.y, future_x + 20, future_y)
                bullet_group.add(bullet)
                self.time_cooldown = 750 
                    
        self.time_cooldown -= clock.get_time()

        for bullet in bullet_group:
            bullet.update()


class Balloon(pygame.sprite.Sprite):
    def __init__(self, x, y, health, ballon_spawn, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"ball.jpg")
        self.scaled_image = pygame.transform.scale(self.image, (80, 100))
        self.rect = self.scaled_image.get_rect()
        self.ballon_spawn = ballon_spawn
        self.healh = health
        self.rect.center = [x, y]
        self.path = PATH
        self.current_waypoint_index = 0
        self.velocity = velocity  # Added velocity
        self.rect = pygame.Rect(PATH[0][0], PATH[0][1], 20, 20)

    def update(self):          
        if self.current_waypoint_index < len(self.path):
            target_x, target_y = self.path[self.current_waypoint_index]
            if self.rect.x < target_x:
                self.rect.x += SPEED
            elif self.rect.x > target_x:
                self.rect.x -= SPEED
            if self.rect.y < target_y:
                self.rect.y += SPEED
            elif self.rect.y > target_y:
                self.rect.y -= SPEED

            if self.rect.x == target_x and self.rect.y == target_y:
                self.current_waypoint_index += 1
                

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((122, 56, 67))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"ball.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 5

    def update(self):
        for balloon in balloon_group:
            if self.rect.x < balloon.rect.x:
                self.rect.x += 10
            elif self.rect.x > balloon.rect.x:
                self.rect.x -= 10
            if self.rect.y < balloon.rect.y:
                self.rect.y += 10
            elif self.rect.x > balloon.rect.y:
                self.rect.y -= 10

        for bullet in bullet_group:
            collisions = pygame.sprite.spritecollide(self, balloon_group, False)
            if collisions:
                bullet.kill()

block_group = pygame.sprite.Group()
block1 = Block(0, 200, 330, 70)
block2 = Block(240, 20, 90, 250)
block3 = Block(240, 20, 900, 70)
block4 = Block(1060, 20, 90, 600)
block5 = Block(0, 550, 1100, 70)

block_group.add(block1, block2, block3, block4, block5)
balloon_group = pygame.sprite.Group()

# Set an initial velocity for the balloon (dx, dy)
initial_velocity = (SPEED, 0)  # You can change this as needed
balloon1 = Balloon(70, 300, 10, 0, initial_velocity)
balloon_group.add(balloon1)

monkey_group = pygame.sprite.Group()
monkey1 = Monkey(400, 300, 10)
monkey_group.add(monkey1)

bullet_group = pygame.sprite.Group()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((30, 0, 0))
    screen.fill(background_color)
    balloon1.update()
    monkey1.update()

    block_group.draw(screen)
    monkey_group.draw(screen)
    bullet_group.draw(screen)
    screen.blit(balloon1.scaled_image, balloon1.rect)

    pygame.display.update()

    clock.tick(fps)

pygame.quit()