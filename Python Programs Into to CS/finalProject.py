#This game is written by Siang and Nikko

import pygame
from pygame.locals import * #maybe get rid of later

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
        
        #Set number of rows of bricks to 3
        self.row = 3
        
        #Create a list of all bricks and allSprites
        self.bricks = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()
        
        #Add paddle and ball to list of allSprites
        self.allSprites.add(self.paddle)
        self.allSprites.add(self.ball)
        
        for y in range(self.row):
            for x in range(5):
                #Position bricks in correct locations to form self.row X 5 grid
                xpos = self.winWidth // 10 + x * self.winWidth // 5
                ypos = self.winHeight // 24 + y * self.winHeight // 12
                newBrick = Brick(xpos, ypos)
                
                #Append brick to list of bricks and allSprites
                self.bricks.add(newBrick)
                self.allSprites.add(newBrick)
        
        #Sets state: None if still playing, "Win" if won, and "Loss" if lost
        self.state = None
        
        #Sets quit to False, if quit is True, exit window
        self.quit = False
        
    def draw(self):
        """Draws all objects in window"""
        
        #Erase all objects in window
        self.win.fill((255,255,255))
        
        #Draws all objects
        for sprt in self.allSprites:
            self.win.blit(sprt.image, sprt.rect)
        
        #Update the window 
        pygame.display.flip()
        
    def play(self):
        """ Loops through game in three stages
            1) Start screen
            2) Gameplay
            3) End screen"""
        
        #Sets up clock for timing
        clock = pygame.time.Clock()
        
        #Start screen loop
        start = False
        while not self.quit and not start:
            for event in pygame.event.get():
                #Start game on left-click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.paddle.moving = True
                        start = True
                        
                #Allows user to exit window
                if event.type == pygame.QUIT:
                    if self.quit == False:
                        self.quit = True
            
            #Draws all objects in window
            self.draw()
                    
        #Gameplay loop
        while not self.state and not self.quit:
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
            
            #Checks if game is won or lost
            self.checkState()
            
            #Checks the collisions
            self.collision()
            
            #Draws all objects in window
            self.draw()
            
            #Sets frame/second 
            clock.tick(80)
            
        #End screen loop
        while not self.quit:
            #Allows user to exit the window
            for event in pygame.event.get():       
                if event.type == pygame.QUIT:
                    if self.quit == False:
                        self.quit = True

    def collision(self):
        """Checks if ball collides with bricks or paddle"""
        
        #Creates list of bricks that were collided with
        bricksHit = pygame.sprite.spritecollide(self.ball, self.bricks, False)
        
        #If any bricks were collided with, change direction of ball and remove brick from 
        #window
        if bricksHit:
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
            
            #6 is needed to account for the ball moving slightly inside the brick
            #Change y-direction
            if (paddleHit[0].rect.left < (self.ball.rect.right-6)< paddleHit[0].rect.right) or (paddleHit[0].rect.left < (self.ball.rect.left+6) < paddleHit[0].rect.right):
                self.ball.speed[1] *= -1    
                
            #3 is needed to account for the ball moving slightly inside the brick
            #Change x-direction
            elif (paddleHit[0].rect.top < (self.ball.rect.top - 3)< paddleHit[0].rect.bottom) or (paddleHit[0].rect.top < (self.ball.rect.bottom + 3) < paddleHit[0].rect.bottom):
                self.ball.speed[0] *= -1
        
    def checkState(self):
        """Checks whether game is won or lost"""
        
        #Checks if player lost because the ball went off screen
        if self.ball.rect.top >= self.winHeight:
            self.state = "Loss"
        
        #Checks if player won because all bricks were gone
        if not self.bricks:
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
        #self.image = pygame.image.load("test.png").convert()
        self.image = pygame.Surface((50,30))
        
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
        #self.image = pygame.image.load("test.png").convert()
        self.image = pygame.Surface((300,30))
        
        #Set all white pixels in self.image to transparent
        self.image.set_colorkey((255,255,255))
        
        #Set paddle initial position
        self.rect = self.image.get_rect() 
        self.rect.centerx = self.winWidth // 2
        self.rect.centery = self.winHeight - self.rect.height // 2
        
        #Set paddle movement to False
        self.moving = False
        
    def updatePos(self, mouse):
        """Change the position of paddle based on mouse position"""
        
        #Move paddle if the mouse moves in the window, but do not move the paddle off screen
        if mouse[0] > self.rect.width // 2 and mouse[0] < (self.winWidth - self.rect.width // 2):
            self.rect.centerx = mouse[0]
        
class Ball(pygame.sprite.Sprite):
    
    def __init__(self, winWidth, winHeight):
        """Constructor of Ball class
            Inputs:
            1) Window's width 
            2) Window's height"""
        
        #Calls the Sprite init function 
        super().__init__()
        
        #Set window width and height
        self.winWidth = winWidth
        self.winHeight = winHeight
        
        #Set ball's speed and direction
        self.speed = [3, 3]
        
        #Import ball image
        #self.image = pygame.image.load("test.png").convert()
        self.image = pygame.Surface((30,30))
        
        #Set all white pixels in self.image to transparent
        self.image.set_colorkey((255,255,255))
        
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
        
        #Check for collision with top of window
        if self.rect.top <= 0 and self.speed[1] <= 0:
            
            #Switch y-component of direction
            self.speed[1] *= -1
            
        #Change position    
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]

def main():
    
    #Sets up pygame module
    pygame.init()
    
    #Create BrickBreaker object
    game = BrickBreaker(600, 400)
    
    #Play the game
    game.play()
        
if __name__=="__main__":
    main()