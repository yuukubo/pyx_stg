import pyxel
import pdb
#pdb.set_trace()

class App:
    def __init__(self):
        self.title = "pyx_stg c5_48"
        pyxel.init(254, 254, caption=self.title, fps=60)

        self.game_board = GameBoard()
        self.text_area = TextArea(self.title)
        self.stg_area = StgArea(self.text_area)
        self.jiki = Jiki(self.stg_area)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.game_board.update()
        self.text_area.update()
        self.stg_area.update()
        self.jiki.update()

    def draw(self):
        pyxel.cls(0)
        self.game_board.draw()
        self.text_area.draw(self.jiki)
        self.stg_area.draw()
        self.jiki.draw()

class Sprite:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

class   Shooter(Sprite):
    def __init__(self):
        super().__init__()
        pass

class     Enemy(Shooter):
    def __init__(self):
        super().__init__()
        pass

class       Mob(Enemy):
    def __init__(self):
        super().__init__()
        pass

class         Fairy01(Mob):
    def __init__(self):
        super().__init__()
        pass

class         Fairy02(Mob):
    def __init__(self):
        super().__init__()
        pass

class       Boss(Enemy):
    def __init__(self):
        super().__init__()
        pass

class         BigFairy01(Boss):
    def __init__(self):
        super().__init__()
        pass

class     Jiki(Shooter):
    def __init__(self, stg_area):
#        super().__init__()
        self.stg_area = stg_area
        self.x = (self.stg_area.w + self.stg_area.x) / 2
        self.y = (self.stg_area.h + self.stg_area.y) * 9 / 10
        self.w = 4
        self.h = 4
        self.spd = 2

    def update(self):
        self.move()
        self.chkLimit()

    def   move(self):
        if pyxel.btnp(pyxel.KEY_LEFT, 1, 1):
            self.x = self.x - 1 * self.spd
        if pyxel.btnp(pyxel.KEY_UP, 1, 1):
            self.y = self.y - 1 * self.spd
        if pyxel.btnp(pyxel.KEY_RIGHT, 1, 1):
            self.x = self.x + 1 * self.spd
        if pyxel.btnp(pyxel.KEY_DOWN, 1, 1):
            self.y = self.y + 1 * self.spd

    def   chkLimit(self):
        if self.x < self.stg_area.x:
            self.x = self.stg_area.x
        if (self.stg_area.w + self.stg_area.x) < (self.x + self.w):
            self.x = self.stg_area.w + self.stg_area.x - self.w
        if self.y < self.stg_area.y:
            self.y = self.stg_area.y
        if (self.stg_area.h + self.stg_area.y) < (self.y + self.h):
            self.y = self.stg_area.h + self.stg_area.y - self.h

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 8)

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

class       NormalBulletOfEnemy(BulletOfEnemy):
    def __init__(self):
        super().__init__()
        pass

class         MiniBulletOfEnemy(NormalBulletOfEnemy):
    def __init__(self):
        super().__init__()
        pass

class         BigBulletOfEnemy(NormalBulletOfEnemy):
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

class       NomalBulletOfJiki(BulletOfJiki):
    def __init__(self):
        super().__init__()
        pass

class         NeedleBulletOfJiki(NomalBulletOfJiki):
    def __init__(self):
        super().__init__()
        pass

class         HomingBulletOfJiki(NomalBulletOfJiki):
    def __init__(self):
        super().__init__()
        pass

class       LaserBulletOfJiki(BulletOfJiki):
    def __init__(self):
        super().__init__()
        pass

class         LaserBulletOfJiki01(BulletOfJiki):
    def __init__(self):
        super().__init__()
        pass

class       SpellBulletOfJiki(BulletOfJiki):
    def __init__(self):
        super().__init__()
        pass

class         SpellBulletOfJiki01(BulletOfJiki):
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

class   HighScoreScene(GameScene):
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
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pyxel.rect(0, 0, pyxel.width, pyxel.height, 2)

class   TextArea(GameBoard):
    def __init__(self, title):
        self.w = 60
        self.title = title

    def update(self):
        pass

    def draw(self, jiki):
        self.jiki = jiki
        pyxel.text(pyxel.width - self.w, 10, self.title, 10)
        pyxel.text(pyxel.width - self.w, 10 * 3, "x : " + str(self.jiki.x), 10)
        pyxel.text(pyxel.width - self.w, 10 * 4, "y : " + str(self.jiki.y), 10)

class   StgArea(GameBoard):
    def __init__(self, text_area):
        self.x = 10
        self.y = 10
        self.w = pyxel.width - (text_area.w + self.x * 2)
        self.h = pyxel.height - (self.y * 2)

    def update(self):
        pass

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 0)


App()
