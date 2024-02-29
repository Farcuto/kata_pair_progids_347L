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
i = 0
        #0123456789012345678901234567890123456789012345678901234   
string = "...ant...ant..na..t.ant.t..ant...ant..ant..ant.anant..t"
length_string = len(string)
string = list(string)

while i < length_string:
    if i < length_string - 4:
        #for j in range(4):
           # if string [i+j] == " ":
            #    del string
        if string[i] == " ":
            del string[i]
            string.append(".")

        if string[i+1] == " ":
            del string[i+1]
            string.append(".")

        if string[i+2] == " ":
            del string[i+2]
            string.append(".")
        
        if string[i+3] == " ":
            del string[i+3]
            string.append(".")

    if i < length_string:
        if string == "a"


if count_a > count_n and count_a > count_t:
    dead_ants = count_a
if count_n > count_a and count_n > count_t:
    dead_ants = count_n
if count_t > count_a and count_t > count_n:
    dead_ants = count_t
