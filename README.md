# Probabilidades del TEG
Un programa que calcula las probabilidad de un ataque aislado teniendo en cuenta el número de dados con que juega cada jugador. El programa no tiene en cuenta ningún tipo de contexto, por ejemplo, no es lo mismo jugar 3 dados contra 3 dados teniendo 4 ejercitos que teniendo 10. Hay en github otro repo que tiene en cuenta los intentos reiterados de conquista, muy interesante, sugiero chequearlo.

En el readme y en los comentarios del código si ven que digo 'una batalla 2:3', por ejemplo, me refiero a que un jugador ataca con 2 ejercitos (es decir en su país tiene 3) y el otro defiende con 3. En general, todo el programa está enfocado desde el lado del atacante que es el que controla qué se ataca y cuándo.

## Uso
./teg.py \<número de dados del atacante\> \<número de dados del defensor\>

Se puede quitar o cambiar la advertencia que tira cuando jugás con más de 3 dados, revisar las globales al principio del archivo.

## Output
El output tipicamente se vería así

```
Attack: 1   Defense: 1

Attacker wins 0: 58.33%
Attacker wins 1: 41.67%

Favorable result for attacker: 41.67%
```

'Attacker wins N: P' significa que la probabilidad de que el atacante gane una cantidad de N tiradas de dados es P. En este ejemplo, la probabilidad de que el atacante gane 1 tirada de dado es del 41.67%. Si la probabilidad es 0, no se muestra. Los casos favorables son todos los casos en los que el atacante gana más de lo que perdió. Los casos neutros son en los que el atacante pierde lo mismo que el defensor.

## Algunos datos interesantes
* Si atacás 1 a 1, las probabilidades de ganar son 41.67%... bastaaante lejos del 50%
* Si atacás 3 a 1, _el mejor de los casos en el juego original_, tenés **solo un 65.97%** de probabilidades de ganar.
* Si atacás 3 a 3, la probabilidad de perder los 3, o sea, _el peor de todos los casos_, **es 38.3%**; altísimo para ser el peor caso..

## Score
La puntuación es una referencia de que tan bueno es el movimiento. Al igual que el resto del programa, no tiene en cuenta el contexto; si para ganar solo te falta un país y tenés tropas para tomarlo, atacalo, no importa lo que diga la puntuación, obvio. En general, es una forma de comparar que tan eficaces son los ataques entre sí.

La puntuación se calcula con esta formula: 

```
S = (x - N / 2) * P(x) * 100

Siendo:
- S, la puntuación
- x, la cantidad de dados que ganó el atacante
- N, la cantidad de dados que se jugaron
- P(x), la probabilidad de que se ganen esa cantidad de dados (habiendo tirado N en total)

Se escala por 100 para que se vea más fácil
```

Como se ve en la fórmula, la puntuación toma en cuenta la cantidad de dados que ganó el atacante, así como la cantidad de dados que se jugaron _(no es lo mismo ganar un dado habiendo jugado un dado, que ganar un dado habiendo jugado 3)_ y la probabilidad de que pase.

Cuanto más negativa es la puntuación, menos le conviene al atacante. Casi todas las puntuaciones de los ataques son negativas, porque no conviene atacar; pero algunas obvias sí tienen una puntuación positiva: 3:1, 3:2 y 2:1.

La puntuación se basa en la idea de que si ambos jugadores pierden la misma cantidad de tropas, es un desenlace neutro. También se puede pensar como que si en un caso hipotético se jugara esa batalla 100 veces, el atacante en promedio debería haber conseguido aventajar al defensor por _\<puntuación\>_ tropas más de las que tenían de diferencia. O si la puntuación es negativa, por ejemplo -20, luego de jugar esa batalla 100 veces, en promedio el atacante debería haber perdido 20 tropas _MÁS_ que el defensor.

## Usando la puntuación
Parte del porqué hice este programa es para resolver la pregunta de: si tengo en un caso por ejemplo 4 tropas (sin contar la que se tiene que quedar en el país) contra 4, ¿Cuántas tropas tengo que agregar a ese país para equilibrar la balanza cosa de que sea un enfrentamiento lo más neutro posible? Es decir, si tengo 4 tropas contra 4, la probabilidades no me favorecen porque defender es más fácil que atacar (ganar defendiendo es más probable); una tropa defensiva vale más que una tropa atacante, pero, ¿cuánto más? 

La respuesta es -_mas o menos_- la puntuación de las batallas que se vayan a jugar. Antes de empezar, necesitamos estimar vagamente cuantas y de que tipo, batallas vamos a jugar. Por ejemplo, si quiero atacar un pais defendido por 4 ejercitos (y quiero equilibrar las probabilidades), mínimo voy a poner 4 ejercitos para atacar, ya con eso podemos saber que va a tomar lugar una batalla 3:3. Si ejecutamos el programa con la batalla 3:3 nos va a decir que la perdida de tropas media (para el atacante) en el caso de la 3:3 es de 1.89. Podemos imaginar que luego de esa batalla contaríamos con 2.11 tropas, jugaríamos nosotros con 2 tropas, y el otro, va a perder en promedio un poco menos, pero podemos asumir que juega con el mismo número que nosotros. Entonces con 2.11 tropas jugaríamos una 2:2, con perdida media de 1.22; lo que nos dejaría en 0.89. Finalmente, podríamos decir que jugamos una más 1:1. 

Entonces, tenemos la idea de que quizá jugaríamos una 3:3, una 2:2 y una 1:1. Si sumamos la puntuación de cada una de las batallas que suponemos pelearíamos, y agregamos esa suma a las tropas iniciales que teníamos (la misma cantidad que tiene el país que se defiende), llegamos a un número que suele estar cerca de lo que sería una batalla justa (_justa, no favorable_).

Todo esto tampoco tiene mucha importancia igual porque si uno se molesta en hacer los cálculos, para todos los casos, por lo menos hasta el 10, alcanza con sumarle 1 tropa que ataque más y las probabilidades ya están a nuestro favor. Pero bueno...

