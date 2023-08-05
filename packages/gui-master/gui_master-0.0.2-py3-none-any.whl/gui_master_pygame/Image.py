import pygame.image

class Image:
    def __init__(self, x, y, path, alpha):
        self.x = x
        self.y = y
        self.alpha = alpha

        if self.alpha:
            self.img = pygame.image.load(path).convert_alpha()
        elif not self.alpha:
            self.img = pygame.image.load(path).convert()

        self.rect = self.img.get_rect(topleft=(self.x, self.y))
        self.bordered = False
        self.border_width = 3
        self.border_color = 'Black'

    def draw(self, screen):
        if self.bordered:
            pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)
            screen.blit(self.img, self.rect)
        else:
            screen.blit(self.img, self.rect)
