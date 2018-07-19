from zeep import Client

client = Client("http://localhost:7777/ws/AcademicoWebService?wsdl")

listaClientes = client.service.getAllEstudiante()
print("Listado de Estudiantes")
print (listaClientes)

asignatura = client.service.getAsignatura(1)
print("\nAsignatura")
print(asignatura)
print("\n Profesor")
profesor = client.service.getProfesor("1234")
print(profesor)

