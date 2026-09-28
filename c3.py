nums =['Uno','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve','Diez']
Colors =['Morado','Rojo','Negro','Blanco','Azul','Rosa','Gris','Amarillo','Naranja','Cafe']
A = []
nums.reverse()
Colors.reverse()
for num in nums:
    out = f"[{num},{Colors[nums.index(num)]}]"
    A.append(out)

    
print(A)

