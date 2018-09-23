def weight_on_planets():
   weightEarth = int(input("What do you weigh on earth? "))
   weightMars = weightEarth * 0.38
   weightJupiter = weightEarth * 2.34
   print("\nOn Mars you would weigh", weightMars, "pounds.")
   print("On Jupiter you would weigh", weightJupiter, "pounds.")
   
   return
   
   
   
if __name__ == '__main__':
   weight_on_planets()