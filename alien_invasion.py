import sys

import pygame

class AlienInvasion:
	"""A generic class that controls game resources and behavior."""

	def __init__(self):
		"""Initialize game, create game resources."""
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 650))
		pygame.display.set_caption("Alien Invasion")


	def run_game(self):
		"""Start the main cycle of the game."""
		while True:

			# Monitor mouse and keyboard events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

		# Show the last normal screen.
		pygame.display.flip()


if __name__ == '__main__':
	# Create an instance of the game and run the game.
	ai = AlienInvasion()
	ai.run_game()