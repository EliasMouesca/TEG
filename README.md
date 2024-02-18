# Probabilidades del TEG
Un programa que calcula las probabilidad de un ataque aislado teniendo en cuenta el número de dados con que juega cada jugador. El programa no tiene en cuenta ningún tipo de contexto, por ejemplo, no es lo mismo jugar 3 dados contra 3 dados teniendo 4 ejercitos que teniendo 10. Hay en github otro repo que tiene en cuenta los intentos reiterados de conquista, muy interesante, sugiero chequearlo.

## Uso
./teg.py \<número de dados del atacante\> \<número de dados del defensor\>

./teg.py            \# valores por defecto

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
La puntuación es como una referencia de que tan bueno es el movimiento. Como todo el programa, no tiene en cuenta el contexto, claro; si para ganar solo te falta un país y tenés tropas para tomarlo, atacalo, no importa lo que diga la puntuación, obvio. En general, es una forma de comparar que tan eficaces son los ataques entre sí.

Ahora, la puntuación se calcula con esta formula: 

```
S = (x - N / 2) * P(x) * 100

Siendo:
* S, la puntuación
* x, la cantidad de dados que ganó el atacante
* N, la cantidad de dados que se jugaron
* P(x), la probabilidad de que se ganen esa cantidad de dados (habiendo tirado N en total)

Se escala por 100 para que se vea más fácil
```

Como se ve en la fórmula, la puntuación toma en cuenta la cantidad de dados que se ganó, así como la cantidad de dados que se tiraron _(no es lo mismo ganar 1 habiendo tirado 1, que ganar 1 habiendo tirado 3)_ y la probabilidad de que pase.

Cuanto más negativa es la puntuación, menos le conviene al atacante. Casi todas las puntuaciones de los ataques son negativas, porque no conviene atacar; pero algunas obvias sí tienen una puntuación positiva: 3:1, 3:2 y 2:1.

La puntuación se basa en la idea de que si ambos jugadores pierden la misma cantidad de tropas, es un desenlace neutro. También se puede pensar como que si en un caso hipotético se jugara esa batalla 100 veces, el atacante en promedio debería haber conseguido aventajar al defensor por _\<puntuación\>_ tropas más de las que tenían de diferencia. O si la puntuación es negativa, por ejemplo -20, luego de jugar esa batalla 100 veces, en promedio el atacante debería haber perdido 20 tropas _MÁS_ que el defensor.

Parte del porqué hice este programa es para resolver la pregunta de: si tengo en un caso por ejemplo 4 tropas (sin contar la que se tiene que quedar en el país) contra 4, ¿Cuántas tropas tengo que agregar a ese país para equilibrar la balanza cosa de que sea un enfrentamiento lo más neutro posible? Es decir, si tengo 4 tropas contra 4, la probabilidades no me favorecen porque defender es más fácil que atacar; una tropa defensiva vale más que una tropa atacante, pero, ¿cuánto más? La respuesta es la puntuación de esa batalla. Practicamente no se puede aplicar del todo porque implicaría jugar una batalla de 3 contra 3, aún cuando las tropas en los paises enfrentados no lleguen a 3, pero nos da una buena herramienta para usar en una situación que se dan a menudo sobre el final del juego: que muchas tropas ataquen a muchas tropas. Digamos, 10 tropas contra 8. Que ataquen muchos a muchos, implica que vamos a jugar varias partidas seguidas de 3:3, lo que nos da más pie a usar este tipo de instrumentos estadísticos. La puntuación de la batalla 3:3 es -39.31 =~ -40. Eso implica que por cada batalla que juguemos el defensor le aventaja 0.4 tropas al atacante. Y esa es nuestra respuesta!, el atacante, si quiere un enfrentamiento justo (_justo, no necesariamente favorable_), debería igualar las tropas del defensor y a eso sumarle un 40%. No nos podemos fiar demasiaaado en esto, porque al final, cuando quedan 3 tropas en un país, ya no podemos hacer batalla de 3:3, por lo que la puntuación sería distinta, pero si no es el caso más desfavorable (el 2:3), esas tropas que calculamos con la puntuación de -40 de la 3:3 deberían bastarnos. También, la suerte es la suerte y tampoco jugamos taaantas batallas como para fiarnos de la ley de los grandes números. Peeeero, es una aproximación a la pregunta de cuántas tropas se deberían agregar para equilibrar la balanza.

