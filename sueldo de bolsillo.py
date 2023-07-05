import math

conf_final=float(input("Ingrse el Conformado Final:"))
expediente=float(input("Ingrese el Exp1338850/09:"))
des_ley=float('19.5')
conf_para=float(conf_final-expediente)
resul=float((des_ley*conf_para)/100)


sueldo_bolsillo=float(conf_para-resul)+expediente



print("El sueldo de bolsillo es: {} ".format(sueldo_bolsillo))
