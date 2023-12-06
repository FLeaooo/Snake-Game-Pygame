import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (50,50,200), block_rect)
            
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

            
class FRUIT:
    def __init__(self):
        self.randomize_fruit()

    def draw_fruit(self):
        # Aqui eu coloco a posicao * o tamanho da celula, o que vai dar a impressao de criar um grid
        # Depois eu coloco o damanho da fruta que e o tamanho da celula do grid
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        # Desenhando na tela(screen) passar a cor e o objeto
        pygame.draw.rect(screen, (200,50,100), fruit_rect)
        
    def randomize_fruit(self):
        # Esta vai ser a posicao da fruta
        self.x = random.randint(0, cell_number - 1)
        self.y = self.x = random.randint(0, cell_number - 1)
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
        
    def draw_elements(self):
        self.fruta.draw_fruit()
        self.cobra.draw_snake()
        
    def check_colision(self):
        if self.cobra.body[0] == self.fruta.pos:
            self.fruta.randomize_fruit()
            self.cobra.add_block()
            


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
                main.cobra.direction = Vector2(0,-1)
            if event.key == pygame.K_a:
                main.cobra.direction = Vector2(-1,0)
            if event.key == pygame.K_s:
                main.cobra.direction = Vector2(0,1)
            if event.key == pygame.K_d:
                main.cobra.direction = Vector2(1,0)
    
    # Pintando o fundo da tela cinza meio verde
    screen.fill((200,200,110))
    
    main.draw_elements()
    
    pygame.display.update()
    # Vai executar o loop no maximo 60 vezes por segundo
    clock.tick(60)
