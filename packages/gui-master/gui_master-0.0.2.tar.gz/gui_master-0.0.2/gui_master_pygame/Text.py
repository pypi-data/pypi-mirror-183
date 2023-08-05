import pygame

class Text:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		#self.txt_surf = font.render("", True, self.color)
		self.width = 0
		self.height = 0
		self.color = 'Black'
		
	def draw(self, screen, txt, font):
		txt_surf = font.render(txt, True, self.color)
		txt_rect = txt_surf.get_rect(topleft=(self.x, self.y))
		
		self.width = txt_surf.get_width()
		self.height = txt_surf.get_height()
		
		screen.blit(txt_surf, txt_rect)