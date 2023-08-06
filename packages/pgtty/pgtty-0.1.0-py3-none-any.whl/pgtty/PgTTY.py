from pkg_resources import resource_stream

class PgTTY:
    def __init__(self) -> None:
        print("Loading PgTTY...")
        import pygame
        self.pygame = pygame
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.screen.fill((0, 0, 0))
        pygame.display.update()
        self.font = pygame.font.Font(resource_stream("pgtty", "font.ttf"), 16)
        self.foreground = (170, 170, 170)
        self.background = (0, 0, 0)
        self.data = []
        self.pointer = (0, 0)
        self.screen_w = 80
        self.screen_h = 30
        for i in range(self.screen_h):
            tmp_list = []
            for j in range(self.screen_w):
                tmp_list.append((" ", self.foreground, self.background))
            self.data.append(tmp_list)
        pygame.event.get()
    def update(self):
        for y in range(0, len(self.data)):
            for x in range(0, len(self.data[y])):
                char = self.font.render(self.data[y][x][0], False, self.data[y][x][1])
                self.pygame.draw.rect(self.screen, self.data[y][x][2], (x*8, y*16, 8, 16))
                self.screen.blit(char, (x*8, y*16))
        self.pygame.display.update()
    def set(self, yx: tuple[int], char: str, foreground: tuple[int] = 0, background: tuple[int] = 0):
        y, x = yx
        if foreground == 0:
            foreground = self.foreground
        if background == 0:
            background = self.background
        self.data[y][x] = (char, foreground, background)
        char = self.font.render(char, False, foreground)
        self.pygame.draw.rect(self.screen, background, (x*8, y*16, 8, 16))
        self.screen.blit(char, (x*8, y*16))
    def print(self, text: str, foreground: tuple[int] = 0, background: tuple[int] = 0):
        if foreground == 0:
            foreground = self.foreground
        if background == 0:
            background = self.background
        for i in text:
            if i != "\n":
                self.set(self.pointer, i, foreground, background)
                self.pointer = (self.pointer[0], self.pointer[1]+1)
                if self.pointer[1] > self.screen_w-1:
                    if self.pointer[0]+1 >= self.screen_h:
                        self.scroll()
                    else:
                        self.pointer = (self.pointer[0]+1, 0)
            elif i == "\n":
                if self.pointer[0]+1 >= self.screen_h:
                    self.scroll()
                else:
                    self.pointer = (self.pointer[0]+1, 0)
        self.pygame.display.update()
    def scroll(self):
        for y in range(0, len(self.data)):
            for x in range(0, len(self.data[y])):
                if y == 0:
                    continue
                self.data[y-1][x] = self.data[y][x]
                if y == self.screen_h-1:
                    self.data[y][x] = (" ", self.foreground, self.background)
                    continue
        self.pointer = (self.pointer[0], 0)
        self.update()
