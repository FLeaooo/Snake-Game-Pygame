import pygame, sys, random
from pygame.math import Vector2
import os


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
        path_graphic = r"C:\FernandoLeao\Programacao\Projetos\snake-game\dist\data"
        
        # Head
        self.head_up = pygame.image.load(path_graphic + "/head_up.png").convert_alpha()
        self.head_down = pygame.image.load(path_graphic + "/head_down.png").convert_alpha()
        self.head_right = pygame.image.load(path_graphic + "/head_right.png").convert_alpha()
        self.head_left = pygame.image.load(path_graphic + "/head_left.png").convert_alpha()
        
        # Tail
        self.tail_up = pygame.image.load(path_graphic + "/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load(path_graphic + "/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load(path_graphic + "/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load(path_graphic + "/tail_left.png").convert_alpha()
        
        # Body
        self.body_horizontal = pygame.image.load(path_graphic + "/body_horizontal.png").convert_alpha()
        self.body_vertical = pygame.image.load(path_graphic + "/body_vertical.png").convert_alpha()
        
        # Virando
        self.body_tr = pygame.image.load(path_graphic + "/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load(path_graphic + "/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load(path_graphic + "/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load(path_graphic + "/body_bl.png").convert_alpha()
        
        self.crunch_sound = pygame.mixer.Sound(path_graphic + "/Sound/crunch.wav")
        
    def draw_snake(self):
        self.update_head_graphics()
        self.updade_tail_graphics()
        
        # Cada block é uma parte do corpo da cobra o Vector 2
        for index, block in enumerate(self.body):
            # Pegando a posicao (x,y) e multiplicando pelo valor da celula por conta do grid 
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            # crio o retangulo, com base nas posicoe
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                
                if previous_block.x == next_block.x:
                    screen.blit(self.body_horizontal, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_vertical, block_rect) 
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)           
        
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
        
    def updade_tail_graphics(self):
        tam_body = len(self.body) - 1
        tail_relation = self.body[tam_body - 1] - self.body[tam_body]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down
                    
    def move_snake(self):
        if self.new_block == True:
            # Cria a copia da do corpo da cobra sem a ultima parte
            body_copy = self.body[:]
            # Inserindo na pos 0 a posicao da cabeca + a direcao
            body_copy.insert(0, body_copy[0] + self.direction)
            # Passando a copia pro corpo 
            self.body = body_copy[:]
            self.new_block = False
        else:
            # Cria a copia da do corpo da cobra sem a ultima parte
            body_copy = self.body[:-1]
            # Inserindo na pos 0 a posicao da cabeca + a direcao
            body_copy.insert(0, body_copy[0] + self.direction)
            # Passando a copia pro corpo 
            self.body = body_copy[:]
        
    def add_block(self):
        self.new_block = True
        self.play_crunch_sound()

    def play_crunch_sound(self):
        self.crunch_sound.play()
            
    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
            
class FRUIT:
    def __init__(self):
        self.randomize_fruit()

    def draw_fruit(self):
        # Aqui eu coloco a posicao * o tamanho da celula, o que vai dar a impressao de criar um grid
        # Depois eu coloco o damanho da fruta que e o tamanho da celula do grid
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        # Desenhando na tela(screen) passar a cor e o objeto
        #pygame.draw.rect(screen, (200,50,100), fruit_rect)
        screen.blit(apple, fruit_rect)
        
    def randomize_fruit(self):
        # Esta vai ser a posicao da fruta
        self.x = random.randint(5, cell_number - 6)
        self.y = self.x = random.randint(5, cell_number - 6)
        # O uso do Vector2 do pygame facilita as operacoes
        self.pos = Vector2(self.x, self.y)
        
        
class MAIN:
    def __init__(self):
        # Cria o objeto snake da classe snake
        self.cobra = SNAKE()
        self.fruta = FRUIT()

    def update(self):
        self.cobra.move_snake()
        self.check_colision()
        self.check_fail()
     
    def draw_elements(self):
        self.draw_grass()
        self.fruta.draw_fruit()
        self.cobra.draw_snake()
        self.draw_score()
            
    def check_colision(self):
        if self.cobra.body[0] == self.fruta.pos:
            self.fruta.randomize_fruit()
            self.cobra.add_block()
        
        for block in self.cobra.body[1:]:
            if block == self.fruta.pos:
                self.fruta.randomize_fruit()
            
    def check_fail(self):
        if not (0 <= self.cobra.body[0].x < cell_number) or not (0 <= self.cobra.body[0].y < cell_number):
            self.game_over()
        for body in self.cobra.body[1:]:
            if body == self.cobra.body[0]:
                self.game_over()
            
    def game_over(self):
        last_record = self.last_record()
        if int(last_record) < len(self.cobra.body) - 3:
            self.save_record(str(len(self.cobra.body) - 3))
            print(f"Parabens conseguiu bater o record. Pontos {str(len(self.cobra.body) - 3)}")
        else:
            print(f"Nao conseguiu bater o record: Record atual de {last_record}")
        self.cobra.reset() 
      
    def draw_grass(self):
        grass_color = (170,180,100)
        
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
                    
    def draw_score(self):
        score_text = str(len(self.cobra.body) - 3)
        score_surface = game_font.render(score_text, True, (255,255,30))
        score_x = 60
        score_y = 40
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + 30, apple_rect.height)
        
        pygame.draw.rect(screen, (170,180,100), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (0,0,0), bg_rect, 2)
        
    def last_record(self):
        with open(r"C:\FernandoLeao\Programacao\Projetos\snake-game\dist\data\record.txt", "r") as file:
            record = file.read()
            return record
        
    def save_record(self, new_record):
        with open(r"C:\FernandoLeao\Programacao\Projetos\snake-game\dist\data\record.txt", "w") as file:
            file.write(new_record)
    

# Iniciando o pygame
pygame.init()

# Tamanho da celula do grid da tela
cell_size = 30
cell_number = 20

#Constantes
width = cell_size * cell_number
height = cell_size * cell_number

# Desenhar e setar o tamanho da tela
screen = pygame.display.set_mode((width, height))



# Obtém o caminho absoluto para o diretório do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto para a imagem
# Pegando as imagens
path_apple = r"C:\FernandoLeao\Programacao\Projetos\snake-game\dist\data\apple.png"
apple = pygame.image.load(path_apple).convert_alpha()
# Font para o score
path_font = r"C:\FernandoLeao\Programacao\Projetos\snake-game\dist\data\Font\PoetsenOne-Regular.ttf"
game_font = pygame.font.Font(path_font, 25)




# Criei um objeto relogio (clock)
clock = pygame.time.Clock()

# Criei um evento do pygame
SCREEN_UPDATE = pygame.USEREVENT
# Atualiza o evento a cada 150 milisegundos
pygame.time.set_timer(SCREEN_UPDATE, 150)

main = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main.update()
        # Caso qualquer tecla do teclado seja pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if main.cobra.direction.y != 1:
                    main.cobra.direction = Vector2(0,-1)
            if event.key == pygame.K_a:
                if main.cobra.direction.x != 1:
                    main.cobra.direction = Vector2(-1,0)
            if event.key == pygame.K_s:
                if main.cobra.direction.y != -1:
                    main.cobra.direction = Vector2(0,1)
            if event.key == pygame.K_d:
                if main.cobra.direction.x != -1:
                    main.cobra.direction = Vector2(1,0)
    
    # Pintando o fundo da tela cinza meio verde
    screen.fill((200,200,110))
    
    main.draw_elements()
    
    pygame.display.update()
    # Vai executar o loop no maximo 60 vezes por segundo
    clock.tick(60)
