#Codigo para saber si te certificaras

calificacion = input("Introduce tu calificacion de AZ-900: " )

calificacion = int(calificacion)

if calificacion < 700 :   #Pregunta si sacas menor a 700 aparecera el mensaje de la siguiente linea
    print("VEEES, POR NO ESTUDIUAR")
elif calificacion == 700 :
    print("PAANZAZZOOO")
elif calificacion > 1000 : #Dice que si calificacion es mayor a 1000 imprimira el siguiente linea y el comando elif es otro if es como uno secundario
    print("MENTIRA NO PUEDES SACAR MAS DE 1000")
else : #Si no es ninguna de las anteriores condiciones imprimira la siguiente linea
    print("FELICIDADES PASASTE")

#Verificador de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Pasale al Mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del espacio y el tiempo")
else :
    print("No te puedes llevar esos cigarros")

#EN PYTHON NO HAY SWITCH CASE
