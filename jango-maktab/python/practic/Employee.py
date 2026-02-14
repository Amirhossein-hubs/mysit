class Employee:
    salary= "3000$"
    def __init__(self, name, lastname):
        self.Name= name
        self.Lastname= lastname
    def name_and_lastname(self):
        return f"name:{self.Name}, Lastname:{self.Lastname}"

print(Employee("amirhossein", "keahany").name_and_lastname())
print(f"salary:{Employee.salary}")

