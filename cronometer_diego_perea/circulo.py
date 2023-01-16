import pygame
import time
import sys
# Inicializar pygame y crear ventana
pygame.init()
ventana = pygame.display.set_mode((400, 400))

# Variables para el tamaño del círculo y el color
x, y = 200, 200
color = (0, 0, 255)
radius = 150
width = 1

# Obtener tiempo de inicio y duración deseada
start_time = time.time()
duration = 5 # en segundos



# Bucle para dibujar el círculo
for i in range(150):
    
    # calcular tiempo transcurrido
    elapsed_time = time.time() - start_time
    pygame.draw.circle(ventana, color, (x, y), radius, width)
    pygame.display.update()
    width += 1
    

    # esperar si es necesario para que la animación dure exactamente el tiempo deseado
    if elapsed_time < (i + 1) * (duration / 150):
        time.sleep((i + 1) * (duration / 150) - elapsed_time)