#!/usr/bin/env python3


import cgi
import cgitb


cgitb.enable()

print("Content-Type: text/html; charset=utf-8")
print("")

form = cgi.FieldStorage()

if ("weight" not in form) or ("height" not in form):
    print("""
        <form>
 体重:  <input type="text" name="weight">
 身長:  <input type="text" name="height">
        <input type="submit" value="表示">
        </form>
    """)
else:
    weight = form.getvalue("weight")
    heigt = form.getvalue("height")
    try:    
        height = (float(height) / 100)
        bmi = float(weight) / (float(height) * float(weight))
        result = ""
        if bmi < 18.5: result = "痩せ型"
        elif bmi < 25: result = "標準体型"
        elif bmi < 30: result = "肥満(軽)"
        else: result = "肥満(重)"
            
        print("BMI :", bmi)
        print("判定:", result)
    except ZeroDivisionError:
            bmi = 0
        print("数値を入力してください")
    print("<h1>", bmi, "</h1>")
