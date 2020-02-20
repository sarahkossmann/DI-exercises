name=input('type your name')
age=input('type your age')
experience=input('your experience')

html=f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>My CV</h1>
    <p> My name {name}</p>
    <p> I am {age} years old</p>
    <p> Here are my experience : {experience}</p>
</body>
</html>"""


f = open("file.html", "w")
f.write(html)
f.close()

f = open("file.html", "r")
print(f.read())