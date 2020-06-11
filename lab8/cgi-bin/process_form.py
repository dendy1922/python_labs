#!/usr/bin/env python3
import cgi
import sys
import codecs
import numpy as np

form = cgi.FieldStorage()
# utf-8 to html
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# get koef from form
koef = form.getfirst("koef", "0 0 0")

try:
    # solve the equation
    a, b, c = koef.split(" ")
    z = np.roots([a, b, c])
except ValueError:
    z = "Неправильно введены данные"
except:
    z = "Неправильные коэффициенты"

# output
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body bgcolor=#aabbff>""")

print("<h1>Вычисление данных полинома из формы!</h1>")
print("<p>Корни полинома второго уровня:  <strong>{}</strong></p>".format(z))

print("""</body>
        </html>""")
