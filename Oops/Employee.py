""" Making an end to end Employee Pay Service using the OOPS concept. 
Features should contain:
1. Add/Remove Employees
2. Edit the calculating crieria for salary
3. Print all the details at one page """



class Employee:

    total_employees = 0
    raise_amount = 1.04

    def __init__(self,name,age,pay,phone_no):         # It acts as a contructor to initialize variables

        self.name = name
        self.age = age
        self.pay = pay
        self.phone_no = phone_no
        self.email = name + '.' + '@company.com'
        Employee.total_employees += 1

    def salary(self):
        return self.pay*100

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount )


class Developer(Employee):
    raise_amount=1.15

class Manager(Employee):
    raise_amount = 2.12



emp_1 = Employee('TestUser 1',24,1400,999999999)
emp_2 = Employee('TestUser 2',21,1100,999999999)

man_1 = Manager('TestUser 3',45,3300,999999999)
man_2 = Manager('TestUser 4',36,3500,999999999)

dev_1 = Developer('TestUser 5',29,1700,999999999)
dev_2 = Developer('TestUser 6',27,2100,999999999)




print('*************************************************************************************************')
print('*                                                                                               *')
print('*                                                                                               *')
print('*                             Title  : Employee Pay Service                                     *')
print('*                             Author : Abhishek Choudhury                                       *')
print('*                             Date   : 27th July 2020                                           *')
print('*                                                                                               *')
print('*                                                                                               *')
print('*                                                                                               *')
print('*************************************************************************************************')
print('\n')



print('Total number of Employees on the system :' ,Employee.total_employees)
print('\n')
#print(emp_1.__dict__)                       #Namespace


print('Name:', emp_1.name)
print('Pay:', emp_1.pay)
print('Age:', emp_1.age)
#print('salary:',Employee.salary(emp_1))
print('Salary:',emp_1.salary())
emp_1.apply_raise()
print('Raise Amount:', Employee.raise_amount)
print('Salary after raise :',emp_1.salary())

print('\n')

print('Name:', emp_2.name)
print('Pay:', emp_2.pay)
print('Age:', emp_2.age)
#print('salary:',Employee.salary(emp_1))
print('Salary:',emp_2.salary())
emp_2.apply_raise()
print('Raise Amount:', Employee.raise_amount)
print('Salary after raise :',emp_2.salary())

print('\n')

print('Name:', dev_1.name)
print('Pay:', dev_1.pay)
print('Age:', dev_1.age)
#print('salary:',Employee.salary(emp_1))
print('Salary:',dev_1.salary())
dev_1.apply_raise()
print('Raise Amount:', Manager.raise_amount)
print('Salary after raise :',dev_1.salary())

print('\n')


print('Name:', dev_2.name)
print('Pay:', dev_2.pay)
print('Age:', dev_2.age)
#print('salary:',Employee.salary(emp_1))
print('Salary:',dev_2.salary())
dev_2.apply_raise()
print('Raise Amount:', Manager.raise_amount)
print('Salary after raise :',dev_2.salary())

print('\n')



print('Name:', man_1.name)
print('Pay:', man_1.pay)
print('Age:', man_1.age)
#print('salary:',Employee.salary(emp_1))
print('Salary:',man_1.salary())
man_1.apply_raise()
print('Raise Amount:', Developer.raise_amount)
print('Salary after raise :',man_1.salary())


print('\n')


print('Name:', man_2.name)
print('Pay:', man_2.pay)
print('Age:', man_2.age)
#print('salary:',Employee.salary(emp_1))
print('Salary:',man_2.salary())
man_2.apply_raise()
print('Raise Amount:', Developer.raise_amount)
print('Salary after raise :',man_2.salary())