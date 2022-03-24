# imports
import pygame, os, sys

# center pygame window on display
# technique found at https://stackoverflow.com/questions/5814125/how-to-designate-where-pygame-creates-the-game-window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# initialize pygame
pygame.init()

# constants
WIDTH = 250
HEIGHT = 275
FPS = 5

# RGB colors
white = (255, 255, 255)
black = (0, 0, 0)

# variables
image_count = 0 # counter for images
clock = pygame.time.Clock() # clock object
running = True
timer = 0

# load images into pygame
my_images = [
pygame.image.load('./assets/rodriguez_1.png'),
pygame.image.load('./assets/rodriguez_2.png'),
pygame.image.load('./assets/rodriguez_3.png')
]

# changes size of all images to fit screen
for i in range(len(my_images)):
  my_images[i] = pygame.transform.scale(my_images[i], (250, 200))

# set Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tree Animation")
WINDOW.fill(white)

# set up your font
font = pygame.font.Font('./fonts/Lobster-Regular.ttf', 10)

# create your text
text = font.render('Tree Animation', True, black, white)
textRect = text.get_rect()

credits = font.render('Programming by Tyler and Connor Art by Rodriguez', True, black, white)
creditsRect = credits.get_rect()

# position the text
textRect.center = (WIDTH // 2, HEIGHT // 7)

###credtsRect.center = Width

# display text
WINDOW.blit(text, textRect)
pygame.display.flip()

# draw shape function
def drawShape():
  global my_images
  global image_count
  if (image_count == 3):
    image_count = 0
  WINDOW.blit(my_images[image_count], (0, 100))
  pygame.display.flip()
  image_count += 1
  
# main animation Loop that will run for 10 seconds
while running and timer < 50:

  # upadate screen according to FPS value
  clock.tick(FPS)

  # update timer
  timer += 1

  # check if "X" is clicked by user 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      sys.exit()

  # call to drawShape function
  drawShape()