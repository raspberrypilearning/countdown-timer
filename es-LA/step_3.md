## Cuenta regresiva de texto

Primero, hagamos una cuenta regresiva de 5 a 0 mostrando números y usando la pantalla de píxeles de Sense HAT.

+ Abre el Temporizador de cuenta regresiva inicial en Trinket: <a href="http://jumpto.cc/timer-go" target="_blank">jumpto.cc/timer-go</a>
    
    **El código para configurar Sense HAT ha sido incluído para ti.**

+ Vas a contar hasta 5 primero porque es más fácil de hacer. Agrega el código resaltado a la parte inferior de tu script:
    
    ![captura de pantalla](images/timer-count.png)
    
    El comando ` sense.show_letter () ` muestra una sola letra en Sense HAT. No permite números, por lo que debes usar ` str () ` para cambiar el número a un formato que se pueda mostrar.
    
    `sleep(1)` espera un segundo antes de que el código pase al siguiente paso.

+ En Python, ` rango (1, 6) ` regresa los números del 1 al 5. No tienes que contar en unos:
    
    + range (1, 10, 2) se contaría de dos en dos, así: 1, 3, 5, 7 y 9
    + range (5, 0, -1) cuenta regresiva quitando -1, así: 5, 4, 3, 2, 1
    
    Cambia el rango en tu código para que cuente hasta 0:
    
    ![captura de pantalla](images/timer-numbers.png)

+ El número en los LED no tiene que ser blanco: Sense HAT puede mostrar muchos colores. Se usan colores RGB (rojo, verde y azul).
    
    Intenta usar el color verde:
    
    ![captura de pantalla](images/timer-green.png)