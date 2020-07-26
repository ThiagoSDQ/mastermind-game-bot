class InvalidInput(Exception):
    def __init__(self, message):
        self.message = message

class InputField:
    def __init__(self, digits):
        """Creates a InputField for a password with the given number of digits."""
        self.size = digits
        self.password = [" " for i in range(digits)]
        self.rightNumberAndPosition = 0
        self.rightNumber = 0

    def __str__(self):
        ret = ""
        for x in self.password:
            ret += x + " "
        
        ret += ": "

        for i in range(self.rightNumberAndPosition):
            ret += "■ "
        for i in range(self.rightNumber):
            ret += "# "
        for i in range(self.size - self.rightNumber - self.rightNumberAndPosition):
            ret += "_ "

        return ret

    def fill(self, playerAnswer, correctAnswer):
        """Put the player answer in the pasword field."""
        if len(playerAnswer) != self.size:
            raise InvalidInput("Given password is invalid")

        for digit in playerAnswer:
            if not digit.isnumeric():
                raise InvalidInput("Given password is invalid")
        
        if len(set(playerAnswer)) != len(playerAnswer):
            raise InvalidInput("Given password is invalid")

        for i in range(self.size):
            self.password[i] = playerAnswer[i]

        self.checkAnswer(correctAnswer) 

    def checkAnswer(self, correctAnswer):
        """Check how many digits are present in the answer and how many are in correct positions."""
        for i in range(self.size):
            if correctAnswer[i] in self.password:
                if correctAnswer[i] == self.password[i]:
                    self.rightNumberAndPosition += 1
                else:
                    self.rightNumber += 1

    def solved(self):
        return self.rightNumberAndPosition == self.size