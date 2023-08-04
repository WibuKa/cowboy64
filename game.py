import pygame
class Game:
    def __init__(self):
        
        pygame.init()
        self.ml_size = 7
        self.running = False
        self.px_size_scene = 64*self.ml_size

        icon = pygame.image.load('art\icon_game.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Cowboy 64")
        self.screen = pygame.display.set_mode((self.px_size_scene,self.px_size_scene))

    def loading_scene(self):
        clock = pygame.time.Clock()

        white = (255, 255, 255)
        #mành hình loading
        font = pygame.font.Font('font\TeenyTinyPixls.ttf', 5 * self.ml_size)
        running = True
        timeloadingscene = 60
        text_input = "loading | "
        text_output = ""
        while running:
            clock.tick(10)
            self.screen.fill((0,0,0))

            timeloadingscene -= 1
            if text_input == "loading | ":
                text_output = "loading / "
            elif text_input == "loading / ":
                text_output = "loading - "   
            elif text_input == "loading - ":
                text_output = "loading \ "
            elif text_input == "loading \ ":
                text_output = "loading | "
        
            print(text_input, text_output)

            text = font.render(text_output, True, white)
            self.screen.blit(text, (self.ml_size * 2,self.px_size_scene - self.ml_size * 7))
            text_input = text_output
            

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False
            pygame.display.update()
            pass
    
    def RUN(self):
        cowboy_load = pygame.image.load('art\cowboy.png')
        BG_load = pygame.image.load('art\BG.png')
        cowboy = pygame.transform.scale_by(cowboy_load,self.ml_size)
        Background = pygame.transform.scale_by(BG_load,self.ml_size)

        cowboy_x,cowboy_y = 24*self.ml_size,49*self.ml_size

        #chạy game
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running = False
            BG_obj = self.screen.blit(Background,(0,0))
            cowboy_obj = self.screen.blit(cowboy,(cowboy_x,cowboy_y))
            pygame.display.update()

Game().loading_scene()
Game().RUN()