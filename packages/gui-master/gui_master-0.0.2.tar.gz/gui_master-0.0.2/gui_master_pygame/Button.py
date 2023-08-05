import pygame


class Button:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.text_color = 'Black'
		self.color = 'White'
		self.border_color = 'Black'
		self.border_width = 3
		self.x_offset = 30 # offset of the btn txt x pos
		self.y_offset = 15 # offset of the btn txt y pos
		self.bg_rect = pygame.Rect(self.x, self.y, self.width, self.height)
		
	def draw(self, screen, text, font):
		btn_txt = font.render(text, True, self.text_color)
		btn_rect = btn_txt.get_rect(topleft=(self.x + self.x_offset, self.y + self.y_offset))
		
		pygame.draw.rect(screen, self.color, self.bg_rect)
		pygame.draw.rect(screen, self.border_color, self.bg_rect, self.border_width)
		screen.blit(btn_txt, btn_rect)
	
	def clicked(self, event):
		if self.bg_rect.collidepoint(event.pos):
			return True
		else:
			return False