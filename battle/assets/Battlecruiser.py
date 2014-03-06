import pygame, os, sys
from pygame.locals import *

class Battlecruiser(pygame.sprite.Sprite):
    """The space ship"""
    
    def load_image(self, image_name):
        """The proper way to load an image"""
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()
        
    def __init__(self, screen, img_filename, init_x, init_y, init_x_speed, init_y_speed):
        """initializes the battlecruiser"""
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.screen = screen
		
		# Load the image
        self.image = self.load_image(img_filename)
        self.rect = self.image.get_rect() # Set the rect attribute for the sprite (absolutely necessary for collision detection)

		# Get the image's width and height
        self.image_w, self.image_h = self.image.get_size()
			
        # Create a moving collision box
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        
        #set the laser group
        self.lasers = pygame.sprite.Group()
        
		# Set the (x, y)
        self.x = init_x
        self.y = init_y
		
		# Set the default speed (dx, dy)
        self.dx = init_x_speed
        self.dy = init_y_speed
				
    def update(self, dir):
        """update the battlecruiser with movement"""
        if dir == "UP":
            self.y = self.y - 3
        elif dir == "DOWN":
            self.y = self.y + 3
        elif dir == "LEFT":
			self.x = self.x - 3
        elif dir == "RIGHT":
            self.x = self.x + 3
        elif dir == "SPACE":
            self.fire_laser()
        elif dir == "UP_VEL":
            self.y = self.y - 3
        elif dir == "DOWN_VEL":
            self.y = self.y + 3
        elif dir == "LEFT_VEL":
			self.x = self.x - 3
        elif dir == "RIGHT_VEL":
            self.x = self.x + 3
            
        self.x = self.x + self.dx
        self.y = self.y + self.dy
			
		# Move the bounding box too!
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x, self.y)
        self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)	
        
    def draw(self):
        """Draws the battlecruiser on the screen"""
        self.lasers.update()
        self.lasers.draw(self.screen)
        self.screen.blit(self.image, (self.x, self.y))
        
    def fire_laser(self):
        self.lasers.add(Laser(self.screen, "laser.gif", self.x + 50, self.y, 0, -5))

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
    """The main part of moving the cruiser"""
    #Check if sound and font are supported
    if not pygame.font:
        print "Warning, fonts disabled"
    if not pygame.mixer:
        print "Warning, sound disabled"
    
    #Constants
    FPS = 50
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BACKGROUND_COLOR = (0, 0, 0)
    SPRITE_IMAGE = "battlecruiser.gif"
    
    # Initialize Pygame, the clock (for FPS), and a simple counter
    pygame.init()
    clock = pygame.time.Clock()
    
    #Set the display settings
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('BattleCruiser Demo')
    
    # Keep track of which arrow key was pressed
    pressed = None
    
    bc_hero = Battlecruiser(screen, SPRITE_IMAGE, 300, 400, 0, 0,)
    laser_flag = 0;
    decompi = None
    #The game loop
    while True:
        clock.tick(FPS)
        laser_flag = laser_flag - 1
        cool_down = False
        if ( laser_flag >= 0):
            cool_down = True
        keys = pygame.key.get_pressed()
        screen.fill(BACKGROUND_COLOR)
        bc_hero.draw()
        
        #decompi = None
        
    
        #Update the entire drawing surface
        pygame.display.flip()
        
        # Process events via input function
        #print(len(pygame.event.get()))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                elif event.key == K_UP:
                    pressed = "UP"
                    bc_hero.update(pressed)
                elif event.key == K_DOWN:
                    pressed = "DOWN"
                    bc_hero.update(pressed)
                elif event.key == K_LEFT:
                    pressed = "LEFT"
                    bc_hero.update(pressed)
                elif event.key == K_RIGHT:
                    pressed = "RIGHT"
                    bc_hero.update(pressed)
                elif event.key == K_SPACE:
                    if (cool_down != True):
                        pressed = "SPACE"
                        laser_flag = 10;
                        bc_hero.update(pressed)
            
                
        if pressed != None:
            if keys[K_ESCAPE]:
                quit()
            elif keys[K_UP]:
                pressed = "UP_VEL"
                bc_hero.update(pressed)
            elif keys[K_DOWN]:
                pressed = "DOWN_VEL"
                bc_hero.update(pressed)
            elif keys[K_LEFT]:
                pressed = "LEFT_VEL"
                bc_hero.update(pressed)
            elif keys[K_RIGHT]:
                pressed = "RIGHT_VEL"
                bc_hero.update(pressed)
            if keys[K_SPACE]:
                if (cool_down != True):
                    pressed = "SPACE"
                    laser_flag = 10;
                    bc_hero.update(pressed)
    
        
    
    


        
        
        
        
        
        
        
        
        



