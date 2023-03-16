from typing import Optional, Sized
import requests, sys, datetime, os, pprint 
from datetime import datetime

def esmoneda(cripto):
    return cripto in monedas 

def nombre(cripto):
    monedas_dict={}
    for coin in data["data"]:
        monedas_dict[coin["symbol"]]=coin["name"]
    return monedas_dict.get(cripto)

monedas=()
monedas_dict={}
diccionario={}
transacciones=list()
wallet={'BTC':0, 'ETH':0, 'LTC':0, 'ETC':0}

COINMARKET_API_KEY = "76903a15-84b1-4ed2-8ea4-4d7cce59d5cb"
headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': COINMARKET_API_KEY}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for cripto in data["data"]:
    monedas_dict[cripto["symbol"]]=cripto["name"]

for cripto in data["data"]:
    diccionario[cripto["symbol"]] = float(cripto["quote"]["USD"]["price"]) 
    
now = datetime.now()
fechaHora = now.strftime("%d/%m/%Y %H:%M:%S")

file = open("billetera_digital.txt", "w+")
file. write("BILLETERA DIGITAL" + os.linesep)
file. write("")
file. close()

file = open("Historial_Transacciones.txt", "w+")
file. write("HISTORIAL DE TRANSACCIONES" + os.linesep)
file. write("")
file. close()

nombre_usuario=str(input("Ingrese su nombre: "))
codigo_usuario=(input("Ingrese un código de 4 digitos, este será su código personal para transacciones: "))

if len(codigo_usuario)== 4:
    confirmacion_codigo=(input("confime su código de usuario: "))
    if  confirmacion_codigo == codigo_usuario:
        print("código aceptado")
    else: 
        print("el código no coincide, confirme su código")
else:
    print("Código inválido")


file= open("billetera_digital.txt","w")
file.write(nombre_usuario)
file.write(codigo_usuario)
file.close()

while True:
    opcion=int(input("""Del menú anterior, seleccione la opción que desea utilizar

....MENÚ DE INICIO:

1.Recibir transferencia
2.Realizar una transferencia
3.Mostrar el balance de una moneda
4.Mostrar balance general
5.Mostrar histórico de transacciones
6.Salir

"""))
    
    if opcion == 1:
        codigo_usuario_receptor=(input("Ingrese su código personal: "))
        while not codigo_usuario==codigo_usuario_receptor:
            print("Código incorrecto. Ingrese nuevamente su codigo")
            codigo_usuario_receptor=int(input("Ingrese su código personal: "))
                                    
        else:
             print("Código correcto")        
            
       
        codigo_emisor=int(input("Ingrese el código del Emisor de la transacción: "))
        cirptomoneda_recibir=str(input("Ingrese el nombre de la criptomoneda a recibir((BTC, ETH, LTC o ETC)): "))

        while not nombre(cirptomoneda_recibir): 
            print("Moneda Invalida.")
            cirptomoneda_recibir=str(input("Ingrese el nombre de la criptomoneda a recibir((BTC, ETH, LTC o ETC)): "))
        else:                
            cantidad_recibir=float(input("Ingrese la cantidad de"+"_"+str(cirptomoneda_recibir)+"_"+"que va a recibir: "))

        linea_recibida="OUT\t"+fechaHora+" "+cirptomoneda_recibir+":"+str(cantidad_recibir)+":"+"enviada por: "+str(codigo_emisor)+":"+"RECIBIDO"
    
        file = open("Historial_Transacciones.txt", "a")
        file.write(linea_recibida+os.linesep)
        file.close()

        if cirptomoneda_recibir == "BTC":
            wallet['BTC']=wallet['BTC']+cantidad_recibir
        if cirptomoneda_recibir == "ETH":
            wallet['ETH']=wallet['ETH']+cantidad_recibir
        if cirptomoneda_recibir == "LTC":
            wallet['LTC']=wallet['LTC']+cantidad_recibir
        if cirptomoneda_recibir == "ETC":
            wallet['ETC']=wallet['ETC']+cantidad_recibir

        print("Transacción Exitosa")
    
    elif opcion == 2:
        codigo_usuario_receptor=(input("Ingrese su código personal: "))
        while not codigo_usuario==codigo_usuario_receptor:
            print("Código incorrecto. Ingrese nuevamente su codigo")
            codigo_usuario_receptor=int(input("Ingrese su código personal: "))
                                    
        else:
             print("Código correcto") 

        codigo_usuario_a_recibir=int(input("Ingrese el código de destinatario que recibirá el monto: "))

        cirptomoneda_enviar=str(input("Ingrese el nombre de la criptomoneda a enviar((BTC, ETH, LTC o ETC)): "))
        
        while not nombre(cirptomoneda_enviar): 
            print("Moneda Invalida.")
            cirptomoneda_enviar=str(input("Ingrese el nombre de la criptomoneda a enviar((BTC, ETH, LTC o ETC)): "))
        else:

            cantidad_enviar=float(input("Ingrese la cantidad de"+"_" +str(cirptomoneda_enviar)+"_"+"que va a enviar: "))
        
        if wallet[cirptomoneda_enviar]<cantidad_enviar:
            print("No cuenta con el saldo suficiente para esta transacción")
        else:
            print("transacción en proceso")

        linea_enviada="OUT\t"+cirptomoneda_enviar+":"+str(cantidad_enviar)+":"+fechaHora+"enviada a: "+str(codigo_usuario_a_recibir)+":"+"ENVIADO"

        

        file = open("Historial_Transacciones.txt", "a")
        file.write(linea_enviada)
        file.close()

        if cirptomoneda_recibir == "BTC":
            wallet['BTC']=wallet['BTC']-cantidad_enviar
        if cirptomoneda_recibir == "ETH":
            wallet['ETH']=wallet['ETH']-cantidad_enviar
        if cirptomoneda_recibir == "LTC":
            wallet['LTC']=wallet['LTC']-cantidad_enviar
        if cirptomoneda_recibir == "ETC":
            wallet['ETC']=wallet['ETC']-cantidad_enviar
        
        print("Transacción Exitosa")


    elif opcion ==3:
        buscar=(input("indique el el simbolo de la moneda que desea consultar(BTC, ETH, LTC o ETC): "))
        while not nombre(buscar): 
            print("Moneda Invalida.")
            buscar=(input("indique el el simbolo de la moneda que desea consultar"))
        else:
            print("La moneda es válida")
        
        for clave, valor in wallet.items():
            if clave==buscar:
                cotizacionbuscar=float(valor*diccionario.get(buscar))
                print("la moneda"+"_"+clave+"_"+ " tiene un saldo de: "+str(valor)+"y su monto en actual es de: "+str(cotizacionbuscar))
    
    elif opcion == 4: 
        dic_arr=[wallet]
        pprint.pprint(dic_arr)
        valorbtc=wallet.get('BTC')
        valoreth=wallet.get('ETH')
        valorltc=wallet.get('LTC')
        valoretc=wallet.get('ETC')
        
        cotizacionbtc=valorbtc*diccionario.get("BTC")
        cotizacioneth=valoreth*diccionario.get("ETH")
        cotizacionltc=valorltc*diccionario.get("LTC")
        cotizacionetc=valoretc*diccionario.get("ETC")

        monto_total=float(cotizacionbtc+cotizacionetc+cotizacionltc+cotizacioneth)

        linebtc="OUT\t"+fechaHora+" " +str(monedas_dict.get('BTC'))+"\t\t " +str(valorbtc)+" " +str(cotizacionbtc)+":"+"recibido"
        lineeth="OUT\t"+fechaHora+" " +str(monedas_dict.get('ETH'))+"\t\t " +str(valoreth)+" " +str(cotizacioneth)+":"+"recibido"
        lineltc="OUT\t"+fechaHora+" " +str(monedas_dict.get('LTC'))+"\t\t " +str(valorltc)+" " +str(cotizacionltc)+":"+"recibido"
        lineetc="OUT\t"+fechaHora+" " +str(monedas_dict.get('ETC'))+"\t\t " +str(valoretc)+" " +str(cotizacionetc)+":"+"recibido"
        linea_monto_total="OUT\t"+fechaHora+" "+str(monto_total)

        print("La moneda BTC =", monedas_dict.get(wallet['BTC']), "con un cantidad de: ", valorbtc, "con una cotización de: ", cotizacionbtc)
        print("La moneda ETH =", monedas_dict.get(wallet['ETH']), "con un cantidad de: ", valoreth, "con una cotización de: ", cotizacioneth)
        print("La moneda LTC =", monedas_dict.get(wallet['LTC']), "con un cantidad de: ", valorltc, "con una cotización de: ", cotizacionltc)
        print("La moneda ETC =", monedas_dict.get(wallet['ETC']), "con un cantidad de: ", valoretc, "con una cotización de: ", cotizacionetc)
        print("El monto total en dolares es de: ",str(monto_total))

        file = open("billetera_digital.txt", "a")
        file. write(linebtc+os.linesep)
        file. write(lineetc+os.linesep)
        file. write(lineltc+os.linesep)
        file. write(lineetc+os.linesep)
        file. write(linea_monto_total+os.linesep)
        file. close()
    
    elif opcion == 5:
        with open("Historial_Transacciones.txt","r") as archivo:
            for linea in archivo:
                print(linea)

    elif opcion == 6:
        print("Muchas gracias por usar esta aplicación. Siempre a su servicio")
        break

    else: 
        print("Ingrese una opción válida")