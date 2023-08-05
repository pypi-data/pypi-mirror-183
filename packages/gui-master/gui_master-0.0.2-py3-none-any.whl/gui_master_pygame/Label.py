import pygame

class Label:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.bordered = False
		self.color = 'White'
		self.border_color = 'Black'
		self.border_width = 3
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
	
	def draw(self, screen):
		if self.bordered:
			pygame.draw.rect(screen, self.color, self.rect)
			pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)
		else:
			pygame.draw.rect(screen, self.color, self.rect)
