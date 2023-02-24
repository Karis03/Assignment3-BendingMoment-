#script for a car dealership
print(input("Welcome to Miss K's Car Dealership."))
Make=input("Which car brand are you interested in purchasing? ")

#Car Braunds Available
Cars=['Audi','Bentley','BMW','Cadillac','Chevrolet','Suzuki','Tesla','Toyota',
      'Volkswagen','Volvo']
if str(Make) in Cars:
    Model=input("Which car model do you believe is right for you? ")
else:
    print(input("Sorry we have none available."))
    
    
#car models available
Models=['Audi A4','Audi A6','Audi R8','2023 Bentayga','Flying Spur','Bentayga \
      Hybrid', 'X1','X3','X4','XT4','XT5','XT6','Bolt EV','Bolt EUV','Silverado',\
      'Suzuki Celerio','Suzuki Swift','Suzuki Jimny','Tesla Model 3','Tesla\
      Model S','Tesla Model X','Camry','Fortuner','Yaris','Atlas','Atlas Cross\
      Sport','Tiguan','2023 Volvo XC40','2023 Volvo XC90','2023 Volvo XC60']
      
      
#Prices of car models available
RetailPrice={'Audi A4':39100,'Audi A6':54900,'Audi R8':208100,'2023 Bentayga':200025,\
             'Flying Spur':211325,'Bentayga Hybrid':166000,'X1':35400,'X3':43000,\
             'X4':53400,'XT4':36790,'XT5':55895,'XT6':48595,'Bolt EV':26595,\
             'Bolt EUV':28195,'Silverado':37664,'Suzuki Celerio':5000,'Suzuki Swift'\
             :6000,'Suzuki Jimny':7000,'Tesla Model 3':7500,'Tesla Model S':94990,\
             'Tesla Model X':120990,'Camry':26220,'Fortuner':122900,'Yaris':17750,\
             'Atlas':30545,'Atlas Cross Sport':31545,'Tiguan':48995,'2023 Volvo XC40'\
             :36350,'2023 Volvo XC90':57100,'2023 Volvo XC60':43450} 
    

for index, dictionary in enumerate(RetailPrice): 
    Cost= RetailPrice.get(str(Model))

if str(Model) in Models:
    print("The cost of " +str(Model)+ " is $"+str(Cost))
else:
    print("Sorry,we do not have that model of your desired car currently\
 available.")
 
print("Thank you!You were a pleasure to work with.")
 
 
          
"""
Github:Karis03
"""

