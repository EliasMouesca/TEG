# Probabilidades del TEG
Un programa que calcula las probabilidad de un ataque aislado teniendo en cuenta el número de dados con que juega cada jugador. El programa no tiene en cuenta ningún tipo de contexto, por ejemplo, no es lo mismo jugar 3 dados contra 3 dados teniendo 4 ejercitos que teniendo 10. Hay en github otro repo que tiene en cuenta los intentos reiterados de conquista, muy interesante, sugiero chequearlo.

## Uso
./teg.py \<número de dados del atacante\> \<número de dados del defensor\>

./teg.py            \# valores por defecto

Se puede quitar o cambiar la advertencia que tira cuando jugás con más de 3 dados, revisar las globales al principio del archivo.

## Output
El output tipicamente se vería así

-------------------------------------

Attack: 1   Defense: 1

Attacker wins 0: 58.33%

Attacker wins 1: 41.67%

Favorable result for attacker: 41.67%

-------------------------------------

'Attacker wins N: P' significa que la probabilidad de que el atacante gane una cantidad de N tiradas de dados es P. En este ejemplo, la probabilidad de que el atacante gane 1 tirada de dado es del 41.67%. Si la probabilidad es 0, no se muestra. Los casos favorables son todos los casos en los que el atacante gana más de lo que perdió.


## Algunos casos interesantes
* Si atacás 1 a 1, las probabilidades de ganar son 41.67%... bastaaante lejos del 50%
* Si atacás 3 a 1, _el mejor de los casos en el juego original_, tenés **solo un 65.97%** de probabilidades de ganar.
* Si atacás 3 a 3, la probabilidad de perder los 3, o sea, _el peor de todos los casos_, **es 38.3%**; altísimo para ser el peor caso..

## Conclusiones
Atacar, es bastante más jugado de lo que uno pensaría, aún cuando se tienen muchos ejercitos. Además, siento que **no** tenemos en la cabeza un valor cercano al real de las probabilidades en el juego (supongo que es parte de la gracia igual, no?). 


