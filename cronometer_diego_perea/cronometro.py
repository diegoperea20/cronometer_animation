import pygame
import time
import sys

pygame.mixer.init()
white_noise = pygame.mixer.Sound("C:/Users/User/Downloads/tinywow_NewJeans (뉴진스) 'Cookie' Official MV_10899114.mp3")
white_noise.play()


# Inicializar pygame
pygame.init()

# Crear la ventana con las dimensiones especificadas
ventana = pygame.display.set_mode((400, 400))

# Establecer el título de la ventana
pygame.display.set_caption("Mi ventana")

# Crear una fuente para mostrar el texto
fuente = pygame.font.Font(None, 70)

# Inicializar el contador en 5 segundos
contador = 5

# Obtener tiempo de inicio
start_time = time.time()
# Bucle principal del juepo
while True:
    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calcular tiempo transcurrido
    elapsed_time = time.time() - start_time

    # Calcular el tiempo restante
    contador = 5 - int(elapsed_time)

    # Convertir el contador a string
    texto = str(contador)

    # Crear el texto a partir de la string
    texto = fuente.render(texto, True, (255, 255, 255))
    # Obtener el rectángulo que contiene el texto
    rect = texto.get_rect()


    # Limpiar la parte superior de la ventana
    ventana.fill((0, 0, 0), (0, 0, ventana.get_width(), rect.height))


    # Establecer la posición del rectángulo en la parte superior de la ventana
    rect.center = (ventana.get_width() // 2, 20)

    # Dibujar el texto en la ventana
    ventana.blit(texto, rect)

    # Actualizar la pantalla
    pygame.display.update()

    # Verificar si ha transcurrido 5 segundos
    if elapsed_time >= 5:
        break

