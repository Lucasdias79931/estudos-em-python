'''boolean  = False

def troca():
    global boolean
    if boolean:
       boolean = False
        
        
    elif not boolean:
       
        boolean = True
      

print(boolean)
troca()
print(boolean)

'''

def infinito(a):
    let =3
    print(hex(id(a)))
    infinito(a + let)


var = 2

infinito(var)