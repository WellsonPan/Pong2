class Settings:
    def __init__(self):
        #screen settings
        self.screenWidth = 1200
        self.screenHeight = 800
        self.backgroundColor = (0, 0, 0)

        # paddle settings
        self.padLength = 10
        self.padWidth = 125
        self.padColor = (255, 255, 255)
        self.padSpeed = 1

        # ball settings
        self.ballColor = (255, 0, 0)
        self.ballWidth = self.ballHeight = 10
        self.ballSpeed = 1
        self.ballDirections = [-1, 1]

        # divider settings
        self.dividerHeight = self.screenHeight
        self.dividerWidth = 6
        self.dividerColor = (255, 255, 255)

        # scaling
        self.speedUpScale = 1.01
        self.ballSpeedUp = 1.05

        # game state
        self.gameActive = False
        self.playerScore = 0
        self.AIScore = 0
        self.msg = " "

    def playerScored(self):
        self.playerScore += 1

    def AIScored(self):
        self.AIScore += 1

    def speedUp(self):
        self.padSpeed *= self.speedUpScale
        self.ballSpeed *= self.ballSpeedUp

    def reset(self):
        self.padSpeed = 2
        self.ballSpeed = 1

    def reset_score(self):
        self.playerScore = 0
        self.AIScore = 0
