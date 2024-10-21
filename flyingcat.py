import pygame
pygame.init()
pygame.display.set_caption("Flying Cat!")
width = 500
height = 400
screen = pygame.display.set_mode((width, height))
class movinganimals(pygame.sprite.Sprite):
    def __init__(self, img, speed = 5):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.speed = speed
    #moving the cat when keys are pressed
    def update(self, key):
        if key[pygame.K_w]:
            self.rect.move_ip(0,- self.speed)
        if key[pygame.K_a]:
            self.rect.move_ip(- self.speed,0)
        if key[pygame.K_d]:
            self.rect.move_ip(+ self.speed,0)
        if key[pygame.K_s]:
            self.rect.move_ip(0,+ self.speed)
        #keeping player in the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 500:
            self.rect.right = 500
        if self.rect.bottom > 400:
            self.rect.bottom = 400
        if self.rect.top < 0:
            self.rect.top = 0
Spritesg = pygame.sprite.Group()
def startup():
    obj1 = movinganimals("cat.png", 3) 
    obj2 = movinganimals("dog.png", 2)
    Spritesg.add(obj1)
    Spritesg.add(obj2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        obj1.update(keys)
        obj2.update(keys)
        screen.blit(pygame.image.load("background.jpg"), (0,0))
        Spritesg.draw(screen)
        pygame.display.update()
startup()
