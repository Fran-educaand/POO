

import random;
class SalesPerson:  
   
   names = []
   total_revenues = 0

   def __init__(self,name,age):
       self.name = name

       self.age = age
       self.sales_amount = 0
       
 
   def make_sale(self,money):
       self.sales_amount += money
       SalesPerson.total_revenues += self.sales_amount
 
   def show(self):
       print(self.name, self.age, self.sales_amount)


for i in range(12):
  n= SalesPerson(('Alumno'+str(i)),i)
  SalesPerson.names.append(n)
  SalesPerson.names[i].make_sale(random.randint(1000,5000))
  print(SalesPerson.names[i].total_revenues)
  SalesPerson.names[i].show()

#for i in range(len(SalesPerson.names)):
   #SalesPerson.names[i].make_sale(random.randint(1000,5000))

#for i in range ( len(SalesPerson.names)):
   # print(SalesPerson.names[i].total_revenues)
   # SalesPerson.names[i].show()

