import pyxel

class App:
    def __init__(self):
        pyxel.init(254, 254, caption="pyx_stg", fps=60)

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
        self.title = "pyx_stg c4_1"

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

class Sprite:
    def __init__(self):
        pass

class   Shooter(Sprite):
    def __init__(self):
        super().__init__()
        pass

class     Enemy(Shooter):
    def __init__(self):
        super().__init__()
        pass

class       Fairy01(Enemy):
    def __init__(self):
        super().__init__()
        pass

class       Fairy02(Enemy):
    def __init__(self):
        super().__init__()
        pass

class       BigFairy01(Enemy):
    def __init__(self):
        super().__init__()
        pass

class     Jiki(Shooter):
    def __init__(self):
        super().__init__()
        pass

class       PowerTypeJiki(Jiki):
    def __init__(self):
        super().__init__()
        pass

class       HomingTypeJiki(Jiki):
    def __init__(self):
        super().__init__()
        pass

class   Bullet(Sprite):
    def __init__(self):
        super().__init__()
        pass

class     BulletOfEnemy(Bullet):
    def __init__(self):
        super().__init__()
        pass

class       MiniBulletOfEnemy(BulletOfEnemy):
    def __init__(self):
        super().__init__()
        pass

class       BigBulletOfEnemy(BulletOfEnemy):
    def __init__(self):
        super().__init__()
        pass

class       SpellOfEnemy(BulletOfEnemy):
    def __init__(self):
        super().__init__()
        pass

class         SpellOfEnemy01Easy(SpellOfEnemy):
    def __init__(self):
        super().__init__()
        pass

class         SpellOfEnemy01Hard(SpellOfEnemy):
    def __init__(self):
        super().__init__()
        pass

class         SpellOfEnemy02Easy(SpellOfEnemy):
    def __init__(self):
        super().__init__()
        pass

class         SpellOfEnemy02Hard(SpellOfEnemy):
    def __init__(self):
        super().__init__()
        pass

class     BulletOfJiki(Bullet):
    def __init__(self):
        super().__init__()
        pass

class       BulletOfJikiNomal(BulletOfJiki):
    def __init__(self):
        super().__init__()
        pass

class       BulletOfJikiLaser(BulletOfJiki):
    def __init__(self):
        super().__init__()
        pass

class       BulletOfJikiSpell(BulletOfJiki):
    def __init__(self):
        super().__init__()
        pass


class GameScene:
    pass

class   LogoScene(GameScene):
    pass

class   TitleScene(GameScene):
    pass

class   ManualScene(GameScene):
    pass

class   StageScene(GameScene):
    pass

class     Stage1Scene(StageScene):
    pass

class     Stage2Scene(StageScene):
    pass

class     PauseScene(StageScene):
    pass

class     ResultScene(StageScene):
    pass

class   GameOverScene(GameScene):
    pass

class   GameClearScene(GameScene):
    pass

class   EndingScene(GameScene):
    pass

class   InterScene(GameScene):
    pass



class StageScenario:
    pass

class   Stage1ScenarioEasy(StageScenario):
    pass

class   Stage1ScenarioHard(StageScenario):
    pass

class   Stage2ScenarioEasy(StageScenario):
    pass

class   Stage2ScenarioHard(StageScenario):
    pass



class GameBoard:
    pass

class   StgArea(GameBoard):
    pass

class   TextArea(GameBoard):
    pass



App()
