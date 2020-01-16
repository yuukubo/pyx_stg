import pyxel

class App:
    def __init__(self):
        pyxel.init(255, 255, caption="pyx_stg")

        self.text_area_w = 60

        self.game_board_x = 10
        self.game_board_y = 10
        self.game_board_w = pyxel.width - (self.text_area_w + self.game_board_x * 2)
        self.game_board_h = pyxel.height - (self.game_board_y * 2)

        self.x = (self.game_board_w + self.game_board_x) / 2
        self.y = self.game_board_h * 9 / 10
        self.w = 4
        self.h = 4
        self.spd = 2
        self.title = "pyx_stg c3_1"

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.x = self.x - 1 * self.spd
        if pyxel.btnp(pyxel.KEY_UP, 1, 1):
            self.y = self.y - 1 * self.spd
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.x = self.x + 1 * self.spd
        if pyxel.btnp(pyxel.KEY_DOWN, 1, 1):
            self.y = self.y + 1 * self.spd
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        if self.x < self.game_board_x:
            self.x = self.game_board_x
        if (self.game_board_w + self.game_board_x) < (self.x + self.w):
            self.x = self.game_board_w + self.game_board_x - self.w
        if self.y < self.game_board_y:
            self.y = self.game_board_y
        if (self.game_board_h + self.game_board_y) < (self.y + self.h):
            self.y = self.game_board_h + self.game_board_y - self.h

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, pyxel.width, pyxel.height, 2)
        pyxel.rect(self.game_board_x, self.game_board_y, self.game_board_w, self.game_board_h, 0)
        pyxel.text(pyxel.width - self.text_area_w, 10, self.title, 10)
        pyxel.text(pyxel.width - self.text_area_w, 10 * 3, "x : " + str(self.x), 10)
        pyxel.text(pyxel.width - self.text_area_w, 10 * 4, "y : " + str(self.y), 10)

        pyxel.rect(self.x, self.y, self.w, self.h, 8)

App()
