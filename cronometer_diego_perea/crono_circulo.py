import pygame
import time
import sys



# Inicializar pygame
pygame.init()

# Crear la ventana con las dimensiones especificadas
ventana = pygame.display.set_mode((400, 400))

# Establecer el título de la ventana
pygame.display.set_caption("cronometro_diego_perea")

# Crear una fuente para mostrar el texto
fuente = pygame.font.Font(None, 70)

# Inicializar el contador en 5 segundos
#contador = 5

# Variables para el tamaño del círculo y el color
x, y = 200, 200
yellow = (255, 255, 0)
red = (255, 0, 0)
color = (0, 0, 255)
radius = 150
width = 1

# Inicializar el reloj
print("Cronometro_diego_perea".center(50, "-"))
print(f'Introducir segundos de 0 a 60 y minutos de 0 a 9')
print("".center(50, "-"))


try:
    segundos_in=input("Introduzca Segundos(Seconds) : ") # en segundos
    if not segundos_in.isnumeric():
        raise ValueError("El valor ingresado no es un número entero")
    segundos_in=int(segundos_in) # en segundos
    if segundos_in < 0 or segundos_in > 60:
        raise ValueError("El valor de segundos debe estar entre 0 y 60")
        
    minutos_in=input("Introduzca Minutos(Minutes) : ") # en minutos
    if not minutos_in.isnumeric():
        raise ValueError("El valor ingresado no es un número entero")
    minutos_in=int(minutos_in) # en minutos
    if minutos_in < 0 or minutos_in > 9:
        raise ValueError("El valor de minutos debe estar entre 0 y 9")
except ValueError as e:
    print(e)

duration = minutos_in*60 + segundos_in

# Obtener tiempo de inicio
start_time = time.time()
# Bucle principal del juepo
while True:
    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range(150):
        # Calcular tiempo transcurrido
        elapsed_time = time.time() - start_time

        # Calcular el tiempo restante
        contador = duration - int(elapsed_time)

        # Convertir el contador a string
        #texto = str(contador)
        minutos, segundos = divmod(contador, 60)
        texto = "{:02}:{:02}".format(minutos, segundos)

    

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
        
        # Bucle para dibujar el círculo       
        pygame.draw.circle(ventana, color, (x, y), radius, width)    
        
        width += 1
        # esperar si es necesario para que la animación dure exactamente el tiempo deseado
        if elapsed_time < (i + 1) * (duration / 150):
            time.sleep((i + 1) * (duration / 150) - elapsed_time)
        # Verificar si ha transcurrido 5 segundos
    if elapsed_time >= duration:
            
            pygame.mixer.init()
            white_noise = pygame.mixer.Sound("./alarm.mp3")
            white_noise.play()
             
            for cambio_color in range(10):
                if color==yellow:
                    color=red
                else:
                    color=yellow
                pygame.draw.circle(ventana, color, (x, y), 150, 150)  
                pygame.display.update()
                pygame.time.wait(500)
             # delay de 5 segundos
            #pygame.time.wait(5000) 
               
            break

