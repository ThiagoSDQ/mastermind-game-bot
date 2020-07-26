import random
from InputField import InputField

class Level:
    def __init__(self, passwordSize, numberOfAttempts):
        """Create a level with certain password size and max number of attempts."""
        self.passwordSize = passwordSize
        
        self.password = ""
        for i in range(passwordSize):
            x = str(random.randint(0, 9))
            while x in self.password:
                x = str(random.randint(0, 9))
            
            self.password += x

        self.attempts = [InputField(passwordSize) for i in range(numberOfAttempts)]

        self.currentAttempt = 0

        self.solved = False

    def __str__(self):
        ret = ""

        for x in self.password:
            ret += (x if self.solved == True else "░") + " "
        ret += "\n"

        for i in range(self.passwordSize):
            ret += "--"
        ret += "\n"
        
        for attempt in self.attempts:
            ret += str(attempt) + "\n"

        return ret

    def tryAnswer(self, attempt):
        try:
            self.attempts[self.currentAttempt].fill(attempt, self.password)
        except Exception as exc:
            raise exc

        self.solved = self.attempts[self.currentAttempt].solved()
        self.currentAttempt += 1
    
    