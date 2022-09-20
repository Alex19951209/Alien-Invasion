import sys

import pygame

from settings import Settings

class AlienInvasion:
	"""A generic class that controls game resources and behavior."""

	def __init__(self):
		"""Initialize game, create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")


	def run_game(self):
		"""Start the main cycle of the game."""
		while True:

			# Monitor mouse and keyboard events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				# Redraw the screen on each loop interpretation.
				self.screen.fill(self.settings.bg_color)

				# Show the last normal screen.
				pygame.display.flip()


if __name__ == '__main__':
	# Create an instance of the game and run the game.
	ai = AlienInvasion()
	ai.run_game()