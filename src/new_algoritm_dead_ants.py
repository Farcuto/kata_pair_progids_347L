'''
cont_a
cont_n 
cont_t

problema: ...ant...ant..na..t.ant.t..ant...ant..ant..ant.anant..t

Donde se identifique "ant" sera reemplazada y en caso de que se encuentre 
una letra "a","n" o "t" se va sumar en el contador.

El contador con el valor superior se tomara como la cantidad de hormigas muertas

'''

count_a = 0
count_n = 0
count_t = 0
dead_ants = 0




if count_a > count_n and count_a > count_t:
    dead_ants = count_a
if count_n > count_a and count_n > count_t:
    dead_ants = count_n
if count_t > count_a and count_t > count_n:
    dead_ants = count_t
