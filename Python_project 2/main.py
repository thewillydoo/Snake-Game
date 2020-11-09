import pygame
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
 
# Set the width and height of each snake block
block_width = 15
block_height = 15
# Margin between each block
block_margin = 3
 
# Set initial speed
change_x = block_width + block_margin
change_y = 0
 
 
class Block(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([block_width, block_height])
        self.image.fill(RED)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Snake Game')
 
allspriteslist = pygame.sprite.Group()
 
# Create an initial snake
snake_blocks = []
for i in range(15):
    x = 250 - (block_width + block_margin) * i
    y = 30
    block = Block(x, y)
    snake_blocks.append(block)
    allspriteslist.add(block)
 
 
clock = pygame.time.Clock()
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Set the speed 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = (block_width + block_margin) * -1
                change_y = 0
            if event.key == pygame.K_RIGHT:
                change_x = (block_width + block_margin)
                change_y = 0
            if event.key == pygame.K_UP:
                change_x = 0
                change_y = (block_height + block_margin) * -1
            if event.key == pygame.K_DOWN:
                change_x = 0
                change_y = (block_height + block_margin)
 
    # Get rid of last block of the snake
    old_block = snake_blocks.pop()
    allspriteslist.remove(old_block)
 
    # Figure out where new block will be
    x = snake_blocks[0].rect.x + change_x
    y = snake_blocks[0].rect.y + change_y
    block = Block(x, y)
 
    # Insert new block into the list
    snake_blocks.insert(0, block)
    allspriteslist.add(block)
 
    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)
 
    allspriteslist.draw(screen)
 
    # Flip screen
    pygame.display.flip()
 
   
    clock.tick(10)
 
pygame.quit()