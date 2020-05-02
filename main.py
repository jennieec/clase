from  student import student

def crea_estudiantes(count_estudiantes):
	count = 0
	list_students = []
	
	while count < int(count_estudiantes):
    student_code = input ("dame la matricula: ")
    student_name = input ("dame el nombre: ")
    student_aje = input ("dame la edad: ")
    student_gender = input ("dame el genero: ")
    student_carreer = input ("dame la carrera: ")

    list_students.append(student(student_code, student_name, student_aje, student_gender, student_carreer))

    count= count+1
return list_students

def ordena_edades(list_students):
	
	student_aje.sort() 
	print list_students[]:

def separa_generos(list_students):

    if student_gender == ("masculino"):
            list_students[count]= name:
                print list_students[]:
    else: 
            list_students[count]= name:
                print list_students[]:
def main():
	

    options=1
    list_stud=[]

    while options != "0":
        options=input("menu opciones 1. crea estudiantes 2.ordena edodes  3.separa generos 0. salir: ")

        if options == "1":
            print("crea estudiantes")
        
        if options == "2":
            print("ordena edodes")
        
        if options == "3":
            print("separa generos")
        
if __name__ == "__main__":
    main()
