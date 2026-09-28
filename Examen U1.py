Ip_Direccions = {
"01":{
"id:":'001',
"ip:":'192.168.1.10',
"divice_name:":'Router',
"policy:":'ALLOW_ALL',
"status:":'Activo',
},
"02":{
"id:":'002',
"ip:":'192.168.1.20',
"divice_name:":'Router',
"policy:":'ALLOW_ALL',
"status:":'Activo',
},
"03":{
"id:":'003',
"ip:":'192.168.1.30',
"divice_name:":'Router',
"policy:":'BLOCK_IP',
"status:":'Inactivo',
},
"04":{
"id:":'004',
"ip:":'192.168.1.40',
"divice_name:":'Router',
"policy:":'BLOCK_IP',
"status:":'Inactivo',

},
"05":{
"id:":'005',
"ip:":'192.168.1.50',
"divice_name:":'Router',
"policy:":'REQUIRED_IP',
"status:":'Activo',
},

}

a = (Ip_Direccions.get("01"))
b =(Ip_Direccions.get("01","02","03","04","05"))
Mostrar_dispositivos1 = (a.get("id:"))
Mostrar_dispositivos2 = (a.get("ip:"))
Mostrar_dispositivos3 = (a.get("divice_name:"))
Mostrar_dispositivos4 = (a.get("policy:"))
Mostrar_dispositivos5 = (a.get("status:"))

""""
Mostrar_dispositivos1 = (print(f"ID:{Mostrar_dispositivos1}"))

Mostrar_dispositivos1 = (print(f"Nombre:{Mostrar_dispositivos2}"))

Mostrar_dispositivos1 = (print(f"IP:{Mostrar_dispositivos3}"))

Mostrar_dispositivos1 = (print(f"Politica:{Mostrar_dispositivos4}"))

Mostrar_dispositivos1 = (print(f"Estado:{Mostrar_dispositivos5}"))
"""

Ip_Direccions['01']['Resultado'] = "Configuracion valida"


Mostrar_dispositivos6 = (a.get("Resultado"))





Mostrar_dispositivos1 = (print(f"ID:{Mostrar_dispositivos1}"))

Mostrar_dispositivos1 = (print(f"Nombre:{Mostrar_dispositivos2}"))

Mostrar_dispositivos1 = (print(f"IP:{Mostrar_dispositivos3}"))

Mostrar_dispositivos1 = (print(f"Politica:{Mostrar_dispositivos4}"))

Mostrar_dispositivos1 = (print(f"Estado:{Mostrar_dispositivos5}"))

Mostrar_dispositivos1 = (print(f"Resultado:{Mostrar_dispositivos6}"))



generar_resumen = (b.get("status:"))

if i in generar_resume:
    




  





















