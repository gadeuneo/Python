#This game is written by Siang and Nikko
#Runs three levels of Brick Breaker game

import pygame

class BrickBreaker: 
   
    def __init__(self, winWidth, winHeight):
        """Constructor of game
            Inputs
            1)Window width and height"""
        
        #Set window width and height
        self.winWidth = winWidth
        self.winHeight = winHeight
        
        #Create game window
        self.win = pygame.display.set_mode((self.winWidth, self.winHeight))
        pygame.display.set_caption("Brick Breaker")
        
        #Set background color to white
        self.bgcolor = (255,255,255)
        self.win.fill(self.bgcolor)
        
        #Create paddle and ball objects in game, create paddleGroup
        self.paddle = Paddle(self.winWidth, self.winHeight)
        self.paddleGroup = pygame.sprite.Group()
        self.paddleGroup.add(self.paddle)
        self.ball = Ball(self.winWidth, self.winHeight)
        
        #Create a list of all bricks and allSprites
        self.bricksLevel1 = pygame.sprite.Group()
        self.bricksLevel2 = pygame.sprite.Group()
        self.bricksLevel3 = pygame.sprite.Group()
        self.ballAndPaddle = pygame.sprite.Group()
        
        #Add paddle and ball to list of allSprites
        self.ballAndPaddle.add(self.paddle)
        self.ballAndPaddle.add(self.ball)
    
        #Add bricks to levels:
        self.addBricks(self.bricksLevel1, 3)
        self.addBricks(self.bricksLevel2, 4)
        self.addBricks(self.bricksLevel3, 5)
        
        #Sets state: None if still playing, "Win" if won, and "Loss" if lost
        self.state = None
        
        #Sets quit to False, if quit is True, exit window
        self.quit = False
        
        #Set end text:
        self.endText = None
        
        #Set sound for the paddle
        self.paddleSound = pygame.mixer.Sound("switch10.wav")
        
        #Set sound for the brick
        self.brickSound = pygame.mixer.Sound("switch38.wav")
        
        #Set to true if user reaches last level
        self.lastLevel = False
        
        #Set to true if user is on first level
        self.font = pygame.font.SysFont("tahoma", 22)
        self.startText = self.font.render("Hold down and move left mouse button to move paddle", 1, (0, 0, 0))
        
    def addBricks(self, brickGroup, rows):
        """Adds bricks to brickGroup in a rows X 5 matrix formation"""
        for y in range(rows):
            for x in range(5):
                #Position bricks in correct locations to form self.row X 5 grid
                xpos = self.winWidth // 10 + x * self.winWidth // 5
                ypos = self.winHeight // 24 + y * self.winHeight // 12
                newBrick = Brick(xpos, ypos)
                
                #Append brick to list of bricks and allSprites
                brickGroup.add(newBrick)
    
    def draw(self, brickGroup):
        """Draws all objects in window"""
        
        #Erase all objects in window
        self.win.fill((255,255,255))
        
        #Draws all objects
        for sprt in brickGroup:
            self.win.blit(sprt.image, sprt.rect)
        for sprt in self.ballAndPaddle:
            self.win.blit(sprt.image, sprt.rect)
        
        #Draw end text:
        if self.endText:
            self.win.blit(self.endText, (0, 2*self.winHeight//3))
            
        #Draws start text:
        if self.startText:
            self.win.blit(self.startText, (0, 2*self.winHeight//3))
        
        #Update the window 
        pygame.display.flip()
        
    def play(self):
        """ Loops through game in three stages
            1) Start screen
            2) Gameplay
            3) End screen"""
        
        #Gameloops and Endscreen
        self.gameLoop(self.bricksLevel1)
        self.gameLoop(self.bricksLevel2)
        self.gameLoop(self.bricksLevel3, True)
        
        
    def gameLoop(self, brickGroup, lastLevel = False):
        """Runs gameloop for one level of the game
        Input a group of bricks"""
        
        #Sets up clock for timing
        clock = pygame.time.Clock()
        
        #Set self.lastLevel to correct value
        self.lastLevel = lastLevel
        
        #Reset ball and paddle
        self.ball.reset()
        self.paddle.reset()
        
        #Start loop
        start = False
        while not self.quit and not start:
            for event in pygame.event.get():
                #Start game on left-click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.paddle.moving = True
                        self.ball.speed = [3,3]
                        start = True
                        
                #Allows user to exit window
                if event.type == pygame.QUIT:
                    if self.quit == False:
                        self.quit = True
            
            #Draws all objects in window
            self.draw(brickGroup)
        
        #Removes start text
        self.startText = False
        
        #Gameplay loop
        while brickGroup and not self.quit and not self.state:
            for event in pygame.event.get():

                #If the user clicks the left button, the paddle will begin moving
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.paddle.moving = True

                #If the user clicks the right button, the paddle will stop moving
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.paddle.moving = False

                #If the user moves the mouse left and right, the paddle follows
                if event.type == pygame.MOUSEMOTION and self.paddle.moving:
                    self.paddle.updatePos(event.pos)

                #Allows the user to exit window
                if event.type == pygame.QUIT:
                    if self.quit == False:
                        self.quit = True

            #Moves ball
            self.ball.moveStep()

            #Checks the collisions
            self.collision(brickGroup)
            
            #Checks if game is won or lost
            self.checkState(brickGroup)

            #Draws all objects in window
            self.draw(brickGroup)

            #Sets frame/second 
            clock.tick(80)

        #Display loss message if lost
        if self.state == "Loss":
            #Find number of bricks hit
            numBricksLeft = 0
            for brick in self.bricksLevel1:
                numBricksLeft += 1
            for brick in self.bricksLevel2:
                numBricksLeft += 1
            for brick in self.bricksLevel3:
                numBricksLeft += 1
            numBricksHit = 60 - numBricksLeft
            numBricksHit = str(numBricksHit)

            self.endText = self.font.render("Game Over. Score: " + numBricksHit, 1, (0, 0, 0)) 

        #Display win message if won
        elif self.state == "Win":
            self.endText = self.font.render("You Win!", 1, (0, 0, 0))
            
        #End screen loop
        while not self.quit and self.state:
            #Allows user to exit the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.quit == False:
                        self.quit = True

            #Draws all objects in window
            self.draw(brickGroup)
    
    def collision(self, brickGroup):
        """Checks if ball collides with bricks or paddle"""
        
        #Creates list of bricks that were collided with
        bricksHit = pygame.sprite.spritecollide(self.ball, brickGroup, False)
        
        #If any bricks were collided with, change direction of ball and remove brick from 
        #window
        if bricksHit:
            
            self.brickSound.play()
            
            for brick in bricksHit:
                
                #6 is needed to account for the ball moving slightly inside the brick
                #Change y-direction
                if (brick.rect.left < (self.ball.rect.right -6)< brick.rect.right) or (brick.rect.left < (self.ball.rect.left + 6) < brick.rect.right):
                    self.ball.speed[1] *= -1
                    brick.kill()
                    
                #3 is needed to account for the ball moving slightly inside the brick
                #Change x-direction
                elif (brick.rect.top < (self.ball.rect.top - 3)< brick.rect.bottom) or (brick.rect.top < (self.ball.rect.bottom + 3) < brick.rect.bottom):
                    self.ball.speed[0] *= -1
                    brick.kill()
                
        #Creates list containing paddle if paddle is collided with        
        paddleHit = pygame.sprite.spritecollide(self.ball, self.paddleGroup, False)
        
        #If the paddle is collided with, change the direction of the ball
        if paddleHit:
            
            self.paddleSound.play()

            
            #6 is needed to account for the ball moving slightly inside the paddle
            #Change y-direction
            if ((paddleHit[0].rect.left < (self.ball.rect.right-6)< paddleHit[0].rect.right) or (paddleHit[0].rect.left < (self.ball.rect.left+6) < paddleHit[0].rect.right)) and self.ball.speed[1] >= 0 and self.ball.rect.bottom-3 < self.paddle.rect.top:
                self.ball.speed[1] *= -1
                
                #Check where ball hits the paddle
                xChanged = False
                for i in range(6):
                    if self.ball.rect.centerx < self.paddle.rect.left + self.paddle.sec * (i+1) and not xChanged:
                        #Change x-direction according to location of collision
                        self.ball.speed[0] += i - 3
                        xChanged = True
                        
                if not xChanged:
                    self.ball.speed[0] += 3
                    xChanged = True

                    
                #Set maximum speed
                if self.ball.speed[0] > 6:
                    self.ball.speed[0] = 6
                    
                #Set minimum speed
                elif self.ball.speed[0] < -6:
                    self.ball.speed[0] = -6
                
            #3 is needed to account for the ball moving slightly inside the paddle
            #Change x-direction
            elif (paddleHit[0].rect.top < (self.ball.rect.top - 3)< paddleHit[0].rect.bottom) or (paddleHit[0].rect.top < (self.ball.rect.bottom + 3) < paddleHit[0].rect.bottom):
                self.ball.speed[0] *= -1
        
    def checkState(self, brickGroup):
        """Checks whether game is won or lost"""
        
        #Checks if player lost because the ball went off screen
        if self.ball.rect.top >= self.winHeight:
            self.state = "Loss"
        
        #Checks if player won because all bricks were gone
        if not brickGroup and self.lastLevel:
            self.state = "Win"
            
        
class Brick(pygame.sprite.Sprite):
    
    def __init__(self, xpos, ypos):
        """Constructor for Brick 
            Inputs:
            1)x position of brick center
            2)y position of brick center"""
        
        #Calls the Sprite init function 
        super().__init__()
        
        #Import brick image
        self.image = pygame.image.load("brick.png").convert()
        
        
        #Set all white pixels in self.image to transparent
        self.image.set_colorkey((255,255,255))
        
        #Set brick initial position
        self.rect = self.image.get_rect(center = (xpos, ypos))
             
class Paddle(pygame.sprite.Sprite):
    
    def __init__(self, winWidth, winHeight):
        """Constructor for Paddle class
            Inputs:
            1) Window's width 
            2) Window's height"""
        
        #Calls the Sprite init function 
        super().__init__()
        
        #Set window width and height
        self.winWidth = winWidth
        self.winHeight = winHeight
        
        #Import paddle image
        self.image = pygame.image.load("paddle1.png").convert()
        
        
        #Set all white pixels in self.image to transparent
        self.image.set_colorkey((0,0,0))
        
        #Set paddle initial position
        self.rect = self.image.get_rect() 
        self.rect.centerx = self.winWidth // 2
        self.rect.centery = self.winHeight - self.rect.height // 2
        
        #Set paddle movement to False
        self.moving = False
        
        #Length of one section of paddle
        self.sec = (self.rect.right - self.rect.left) // 7
        
    def updatePos(self, mouse):
        """Change the position of paddle based on mouse position"""
        
        #Move paddle if the mouse moves in the window, but do not move the paddle off screen
        if mouse[0] > self.rect.width // 2 and mouse[0] < (self.winWidth - self.rect.width // 2):
            self.rect.centerx = mouse[0]
    
    def reset(self):
        #Set paddle initial position
        self.rect.centerx = self.winWidth // 2
        self.rect.centery = self.winHeight - self.rect.height // 2
        
        #Set paddle movement to False
        self.moving = False
        
class Ball(pygame.sprite.Sprite):
    
    def __init__(self, winWidth, winHeight):
        """Constructor of Ball class
            Inputs:
            1) Window's width 
            2) Window's height"""
        
        #Calls the Sprite init function 
        super().__init__()
        
        #Set sound for the wall
        self.wallSound = pygame.mixer.Sound("switch36.wav")
        
        #Set window width and height
        self.winWidth = winWidth
        self.winHeight = winHeight
        
        #Set ball's speed and direction
        self.speed = [0, 0]
        
        #Import ball image
        self.image = pygame.image.load("ball.png").convert()
        
        #Set all white pixels in self.image to transparent
        self.image.set_colorkey((0,0,0))
        
        #Set ball initial position
        self.rect = self.image.get_rect() 
        self.rect.centerx = self.rect.width // 2
        self.rect.centery = self.winHeight // 2
        
    def moveStep(self):
        """Moves ball and change direction if it collides with top or sides of window"""
        
        #Check for collision with sides of window
        if (self.rect.left <= 0 and self.speed[0] <= 0) or (self.rect.right >= self.winWidth and self.speed[0] >= 0):
            
            #Switch x-component of direction
            self.speed[0] *= -1
            
            #Plays wall sound
            self.wallSound.play()
        
        #Check for collision with top of window
        if self.rect.top <= 0 and self.speed[1] <= 0:
            
            #Switch y-component of direction
            self.speed[1] *= -1
            
            #Plays wall sound
            self.wallSound.play()
            
        #Change position    
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]

    def reset(self):
        #Set ball initial position
        self.rect.centerx = self.rect.width // 2
        self.rect.centery = self.winHeight // 2
        
        #Set ball speed to zero
        self.speed = [0,0]
        
def main():
    
    #Sets up pygame module
    pygame.init()
    
    #Create BrickBreaker object
    game = BrickBreaker(600, 400)
    
    #Play the game
    game.play()
        
if __name__=="__main__":
    main()