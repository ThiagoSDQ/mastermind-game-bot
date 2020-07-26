from Level import Level

class Game:
    difficulty = [(3, 10), (5, 10), (7, 14)]
    WON = 1
    PLAYING = 0
    LOST = -1

    def __init__(self):
        self.currentDifficulty = 0

        self.status = self.PLAYING
        self.active = True

        self.level = Level(*self.difficulty[0])


    def __str__(self):
        ret = ""

        if self.active == True:
            ret = f"LEVEL {self.currentDifficulty+1}\n"
            ret += str(self.level)

        return ret

    def startNextLevel(self):
        if self.currentDifficulty < 2:
            self.currentDifficulty += 1
            self.status = self.PLAYING
            self.active = True
            self.level = Level(*self.difficulty[self.currentDifficulty])

    def attempt(self, playerAttempt):
        at = playerAttempt.split()
        at = "".join(at)

        try:
            self.level.tryAnswer(at)
        except Exception as exc:
            raise exc    

        if self.level.solved:
            self.status = self.WON
        elif self.level.currentAttempt == self.difficulty[0][1]:
            self.status = self.LOST

        


    

