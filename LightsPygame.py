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
    
    elapsed = pygame.time.get_ticks() - start_time
    screen.fill("black")
    pygame.draw.circle(screen, "grey20", (150,75),50) #red
    pygame.draw.circle(screen, "grey20", (150,225),50) #amber
    pygame.draw.circle(screen, "grey20", (150,375),50) #green
    if elapsed >= 5000:
        if light == "Red":
            light = "Green"
        elif light == "Green":
            light = "Amber"
        elif light == "Amber":
            light = "Red"

        start_time = 5000

    if light == "Red":
        pygame.draw.circle(screen, "red", (150,75),50) #red

    elif light == "Amber":
            pygame.draw.circle(screen, "amber", (150,225),50) #red

    else:
            pygame.draw.circle(screen, "green", (150,375),50) #red
    
    pygame.display.flip()

pygame.quit()