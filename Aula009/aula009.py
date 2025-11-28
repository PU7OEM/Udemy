x = "incrível"

def myFunc():
    global x
    x = "inacreditável"
    y = "fantástico"
    global z
    z = "Bem-vindo ao curso!"
    print("Python é " + x + " e " + y)
    print(z)

myFunc()

print("============================")
print("Você é " + x + '!')
print(z)

