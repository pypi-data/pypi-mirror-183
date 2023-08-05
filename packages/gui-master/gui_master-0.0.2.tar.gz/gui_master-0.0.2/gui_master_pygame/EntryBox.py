import pygame
from py_game_gui.Text import Text

class EntryBox:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.active = False
		self.bordered = False
		self.color = 'Gray'
		self.border_color = 'Black'
		self.border_width = 3
		self.active_color = 'White'
		self.passive_color = 'Gray'
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.text = Text(self.rect.x + 5, self.rect.y + 5)
	
	def activated(self, event):
		if self.rect.collidepoint(event.pos):	
			return True
		else:
			return False
			
	def draw(self, screen, text, font):
		if self.active:
			self.color = self.active_color
			if self.bordered:
				pygame.draw.rect(screen, self.color, self.rect)
				pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)
				self.text.draw(screen, text, font)
				self.rect.w = max(300, self.text.width+10)
			else:
			    pygame.draw.rect(screen, self.color, self.rect)
			    self.text.draw(screen, text, font)
			    self.rect.w = max(300, self.text.width+10)
		else:
			self.color = self.passive_color
			if self.bordered:
				pygame.draw.rect(screen, self.color, self.rect)
				pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)
				self.text.draw(screen, text, font)
				self.rect.w = max(300, self.text.width+10)
			else:
			    pygame.draw.rect(screen, self.color, self.rect)
			    self.text.draw(screen, text, font)
			    self.rect.w = max(300, self.text.width+10)
        	
        		