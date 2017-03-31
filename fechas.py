#importamos las librerias de la siguiente manera
import datetime #en este caso importamos absolutamente todo de "datetime"
from dateutil.relativedelta import relativedelta #nos sirve para jugar con las fechas

#me muestra la fecha del dia de hoy, toma la fecha del pc
a = datetime.date.today()

#muestra el momento exacto en el que se ejecuta la funcion
b = datetime.datetime.now()

c = a + relativedelta(days =+ 57)#fecha exacta dentro de x dias

d = b + relativedelta(months =+ 2)#fecha exacta dentro de x meses

print "la fecha de hoy es %s" % a
print "el tiempo de ahora es %s" % b
print "la fecha dentro de 57 dias es: %s" % c
print "la fecha dentro de 2 meses es %s" % d

#formateando una fecha: pasando de string a date
e = "March 7 2009 7:30pm EST" #esta es una variable de tipo string que esta almacenando una fecha
print "la fecha como se ingreso es: %s" % e
formatting = "%B %d %Y %I:%M%p" #formateando un String a una fecha
e = e[:-4]#le recortamos al string la parte que es no compatible con el formato de fecha de python
print "la fecha sin el pedazo que no reconoce python es: %s" % e
e = datetime.datetime.strptime(e,formatting)
print "la fecha formateada es %s" % e
