import pygame.display

from board import Board

class Tetris:
    def __init__(self):
        self._screen = pygame.display.set_mode((720, 920))
        self._board = Board(self._screen) 
        self._running = True
        self._speed = 10 
        self._clock = pygame.time.Clock()
        pygame.font.init()
        self._score_font = pygame.font.SysFont("Arial", 30)
        self.run()

    def run(self):
        counter = 0
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                if event.type == pygame.KEYDOWN:
                    pass
            self._board.update()
            self._screen.fill("black")
            self._board.draw()
            pygame.display.flip()   
            self._clock.tick(40)
            text_surface = self._score_font.render("Score: " + str(self._board._score), False, (255,255,255))
            self._screen.blit(text_surface, (500, 150))         
        pygame.quit()

