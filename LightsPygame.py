import pygame

pygame.init()

screen = pygame.display.set_mode((300,450))
pygame.display.set_caption("Traffic light simulation")

light = "Red"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    start_time = 5000
    elapsed = pygame.time.get_ticks() - start_time
    screen.fill("black")
    pygame.draw.circle(screen, "grey20", (150,75),50) #red
    pygame.draw.circle(screen, "grey20", (150,225),50) #amber
    pygame.draw.circle(screen, "grey20", (150,375),50) #green
    
    if light == "Red":
        pygame.draw.circle(screen, "red", (150,75),50) 
        light = "rAmber"
        pygame.time.wait(1000)
    elif light == "rAmber":
        pygame.draw.circle(screen, "orange", (150,225),50) 
        light = "Green"
        pygame.time.wait(2000)
    elif light == "Green":
        pygame.draw.circle(screen, "green", (150,375),50) 
        light = "gAmber"
        pygame.time.wait(1000)
    elif light == "gAmber":
        pygame.draw.circle(screen, "orange", (150,225),50) 
        light = "Red"
        pygame.time.wait(2000)

    pygame.display.flip()

pygame.quit()