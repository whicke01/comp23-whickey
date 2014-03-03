import pygame, os, sys
from pygame.locals import *
from random import randint

class Laser(pygame.sprite.Sprite):
    """A simple vertically moving laser"""
    
    def load_image(self, image_name):
        ''' The proper way to load an image '''
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()
    
    def __init__(self, screen, img_filename, init_x, init_y, init_x_speed, init_y_speed):
        """initializes lazer sprite"""
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.screen = screen
        
        #Load the image
        self.image = self.load_image(img_filename)
        self.rect = self.image.get_rect() # Set the rect attribute for the sprite (absolutely necessary for collision detection)

		# Get the image's width and height
        self.image_w, self.image_h = self.image.get_size()
        
        # Create a moving collision box
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
				
		# Set the (x, y)
        self.x = init_x
        self.y = init_y
		
		# Set the default speed (dx, dy)
        self.dx = init_x_speed
        self.dy = init_y_speed
        
        #set the active bool to true
        self.active = True
        
    def update(self):
        """Move the laser up the screen"""
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.y += self.dy
        self.rect.move(self.rect.x, self.rect.y)
        
        if self.rect.y <= ((-1) * self.image_h):
            self.active = False 
        
    def draw(self):
        """draw the laser on the screen"""
        if self.active == True:
            self.screen.blit(self.image, (self.x, self.y))
        
if __name__ == "__main__":
    #Check if sound and font are supported
    if not pygame.font:
        print "Warning, fonts disabled"
    if not pygame.mixer:
        print "Warning, sound disabled"
		
	# Constants
    FPS = 50
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    MAX_SPEED = 3
    BACKGROUND_COLOR = (0, 0, 0)
    SPRITE_IMAGES = 'laser.gif'
    #NUM_SPRITES = 1
    #COUNTER_LOCATION = (10, 10)
	
	# Initialize Pygame, the clock (for FPS), and a simple counter
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	
	# For fullscreen mode...
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN, 32)
    pygame.display.set_caption('Laser Sprite Demo')
    
    counter = 0
	
	# Create the sprites; choose random sprite image, starting location, and starting speed for each sprite
    sprites = []
    #for i in range(NUM_SPRITES):
        #sprites.append(Laser(screen, SPRITE_IMAGES, randint(1, SCREEN_WIDTH), 0, 0, randint(1, MAX_SPEED)))
	
	# Game loop
    while True:
        sprites.append(Laser(screen, SPRITE_IMAGES, randint(1, SCREEN_WIDTH), SCREEN_HEIGHT, 0, (-1) * randint(1, MAX_SPEED)))
        
		# Event handling here (to quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()					
		
		# Redraw the background
        screen.fill(BACKGROUND_COLOR)
		
		# Update and redraw all sprites
        for sprite in sprites:
            sprite.update()
            sprite.draw()
		
		# Draw the counter on surface
        #screen.blit(text, COUNTER_LOCATION)
		
		# Update the counter
        counter+=1
		
		# Draw the sprites
        pygame.display.flip()
        
        