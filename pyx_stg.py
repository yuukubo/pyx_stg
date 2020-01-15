import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="pyx_stg")

        self.x = 50
        self.y = 100
        self.w = 4
        self.h = 4
        self.spd = 2
        self.title = "pyx_stg c1"

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.x = self.x - 1 * self.spd
        elif pyxel.btnp(pyxel.KEY_UP, 1, 1):
            self.y = self.y - 1 * self.spd
        elif pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.x = self.x + 1 * self.spd
        elif pyxel.btnp(pyxel.KEY_DOWN, 1, 1):
            self.y = self.y + 1 * self.spd
        elif pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, pyxel.width, pyxel.height, 2)
        pyxel.rect(10, 10, 90, 100, 0)
        pyxel.text(pyxel.width - 50, 10, self.title, 10)

        pyxel.rect(self.x, self.y, self.w, self.h, 8)

App()
