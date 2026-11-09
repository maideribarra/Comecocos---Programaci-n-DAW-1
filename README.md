# COMECOCOS

## 1. Descripción de la práctica

¿Quién no conoce el Comecocos? En esta práctica vas a trabajar sobre una versión simplificada de este clásico videojuego.

Dispondrás de una plantilla de código que contiene parte de la estructura del juego, pero todavía no está terminada. Tu trabajo consistirá en implementar las funcionalidades necesarias para que el juego pueda ejecutarse correctamente.

El juego funcionará exclusivamente en consola. Para controlar al personaje tendrás que utilizar las teclas W, A, S y D.

Tu objetivo será recoger todos los puntos del tablero sin que el fantasma consiga atraparte.

## 2. Funcionamiento del juego

El tablero está representado mediante una matriz bidimensional y utiliza los siguientes símbolos:

| **Símbolo** | **Significado** |
|:---:|---|
| `#` | Pared |
| `.` | Punto que recoger |
| `C` | Personaje |
| `F` | Fantasma |
| Espacio | Casilla vacía |

- El jugador comienza con 3 vidas. Cada punto recogido suma 10 puntos a la puntuación.
- El fantasma se mueve automáticamente después de cada movimiento válido del jugador e intenta acercarse a él.
- Si el fantasma alcanza al jugador, este pierde una vida y ambos personajes vuelven a sus posiciones iniciales.
- La partida termina cuando se recogen todos los puntos, el jugador se queda sin vidas o decide salir.

## 3. Funcionalidades que debes implementar

A partir de la plantilla proporcionada, tendrás que desarrollar las siguientes funcionalidades.

### 1. Visualización del tablero

Implementa la función encargada de representar el estado actual del juego en consola.

El jugador y el fantasma deben aparecer en sus posiciones correspondientes. También deben mostrarse la puntuación y las vidas restantes.

Ten en cuenta que las posiciones de los personajes se almacenan en el estado de la partida, mientras que el resto de elementos se encuentran en la matriz.

No hace falta que modifiques el tablero (añadiendo al personaje y a los fantasmas), solo debes imprimir el carácter correcto en cada momento.

### 2. Movimiento del jugador

Implementa el sistema de movimiento del Comecocos.

El usuario podrá introducir las siguientes teclas:

- `W`: arriba.
- `A`: izquierda.
- `S`: abajo.
- `D`: derecha.

El personaje no podrá atravesar las paredes ni salir del tablero.

Cuando entre en una casilla que contenga un punto, deberá recogerlo, aumentar la puntuación y dejar la casilla vacía.

La función deberá actualizar la información necesaria y devolver los resultados para que el resto del programa pueda continuar la partida.

**Requisitos:**

1. Obtener la posición actual del jugador.
2. Calcular la nueva posición dependiendo de la dirección (`W`, `A`, `S`, `D`).
3. Comprobar que la nueva posición no contiene una pared (`#`).
4. Si hay una pared, el jugador debe permanecer en su posición.
5. Si el movimiento es posible, actualizar la posición del jugador.
6. Si la nueva casilla contiene un punto (`.`):
   - Sumar 10 puntos a la puntuación.
   - Sustituir el punto por un espacio en el tablero.

### 3. Comprobación de la victoria

Implementa una función que permita determinar si el jugador ha conseguido recoger todos los puntos del tablero.

La función deberá indicar mediante un valor booleano si la partida se ha ganado o si todavía quedan puntos pendientes.

### 4. Menú inicial

- Diseña un menú de bienvenida para el juego.
- Debe incluir el nombre del videojuego, las instrucciones básicas y la posibilidad de comenzar la partida o salir.
- Puedes organizar esta funcionalidad como consideres más adecuado, siempre que esté implementada mediante una función.

### 5. Programa principal

Desarrolla el programa principal que coordinará todas las funcionalidades del juego.

Deberás organizar el flujo de ejecución de manera que el usuario pueda jugar hasta que se cumpla alguna de las condiciones de finalización.

El programa principal debe gestionar las entradas del usuario, actualizar el estado de la partida y determinar cuándo debe finalizar.

Al terminar, deberá mostrar el resultado de la partida y la puntuación conseguida.

El programa principal debe:

1. Mostrar el menú.
2. Inicializar la variable que controla el final de la partida.
3. Crear un bucle que se ejecute mientras la partida no haya terminado.
4. Limpiar la consola antes de mostrar el tablero.
5. Mostrar el tablero actualizado.
6. Solicitar al usuario una dirección.
7. Si el usuario introduce `Q`, finalizar la partida.
8. Si introduce una dirección válida:
   - Mover al jugador.
   - Mover al fantasma.
   - Comprobar si se ha producido una colisión.
   - Comprobar si el jugador ha ganado.
   - Comprobar si se ha quedado sin vidas.
9. Al terminar, mostrar la puntuación final y un mensaje de despedida.

## 4. Comprobación del funcionamiento

Antes de entregar, asegúrate de que tu juego contempla las siguientes situaciones:

- El personaje puede moverse en las cuatro direcciones.
- No puede atravesar paredes.
- Los puntos se recogen correctamente y no se contabilizan dos veces.
- El fantasma se mueve durante la partida.
- Las colisiones se gestionan correctamente.
- Las vidas disminuyen cuando corresponde.
- Se detecta correctamente cuándo se han recogido todos los puntos.
- La partida puede finalizar tanto por victoria como por derrota o decisión del usuario.

## 5. Evaluación

| **Apartado** | **Puntuación** |
|---|:---:|
| Visualización del tablero | 2 puntos |
| Movimiento del jugador | 2,5 puntos |
| Comprobación de la victoria | 1 punto |
| Menú inicial | 1 punto |
| Programa principal | 2,5 puntos |
| Organización, uso de parámetros y valores de retorno | 1 punto |
| **TOTAL** | **10 puntos** |
