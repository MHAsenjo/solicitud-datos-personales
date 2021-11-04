#este es un programa, que pregunta tu nombre, apellido, edad, direccion, fecha de nacimiento
#email, telefono. Además, debe sumar la edad y año de nacimiento
nombre = input("buen dia, estoy completando ti ficha, por favor dime tu nombre: ")
apellido = input("cual es tu apellido: ")
edad = int(input("cual es tu edad: "))
direccion = input("tu direccion: ")
fechaNacimiento = input("fecha de nacimiento: ")
correoElectronico = input("cual es el correo electronico: ")
telefono = input("dame el telefono: ")
year = int(input("dime tu año de nacimiento: "))
#a continuación sumare year y edad
resultado = year + edad
print(f"los datos del formulario son: {nombre, apellido, direccion, fechaNacimiento, edad, correoElectronico, resultado}")
#sumar año + edad, restar el mes, multiplicar por el día y dividir por el añomatya
