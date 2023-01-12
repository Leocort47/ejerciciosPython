class Persona():

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def description(self):

        print("Nombre: ", self.name, "Edad: ",
              self.age, "Pais: ", self.address)


class Empleado(Persona):

    def __init__(self, salary, yearsOfWork, nameEmployee, ageEmployee, adressEmployee):

        super().__init__(nameEmployee, ageEmployee, adressEmployee)

        self.salary = salary
        self.yearsOfWork = yearsOfWork

    def description(self):

        super().description()

        print("Salary:", self.salary, "Antiguedad: ", self.yearsOfWork)


#Antonio = Persona("Antonio", 27, "Colombia")
Manuel = Empleado(1500, 10, "Manuel", 20, "Colombia")

Manuel.description()
