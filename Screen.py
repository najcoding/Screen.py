import pygame
import sys

def main():
   
    pygame.init()

    
    WIDTH, HEIGHT = 800, 600

    
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    try:
        
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pygame Rectangle & Text Example")

       
        font = pygame.font.SysFont("Arial", 36, bold=True)

       
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            
            screen.fill(WHITE)

            
            pygame.draw.rect(screen, BLUE, (150, 200, 500, 200))

            
            text_surface = font.render("Hello, Pygame!", True, BLACK)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_surface, text_rect)

           
            pygame.display.flip()

        
        pygame.quit()
        sys.exit()

    except pygame.error as e:
        print(f"Pygame error: {e}")
        pygame.quit()
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        pygame.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
