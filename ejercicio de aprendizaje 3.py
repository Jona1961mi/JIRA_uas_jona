alumno={}

alumno={"jonathan miguel " ,"edad : ",22," informatica ","Grupo :","4-4"}
alumno.add("desarrolador de software ")
#el set no adminte duplicados y solo lo imprime igual si esta si es algun valor que no esta se agrega 
alumno_1={"jonathan miguel " ,"edad : ",22," informatica ","Grupo :","4-4"}
print(alumno)
print(alumno_1)
alumno.difference_update(alumno_1)
print(alumno)