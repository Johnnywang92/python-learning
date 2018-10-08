##Area Calculator, Circle and Triangle
print "the  caculator is starting now"
name = raw_input("Enter C for Circle or T for Triangle: ")
option = name
if (option == 'C'):
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * (radius)**2
  print "Area : %f" % area
elif (option == 'T'):
      base = float(raw_input("Enter base: "))
      height = float(raw_input("Enter height: "))
      area = 0.5 * base * height
      print "Area : %f" % area
else:
  print "the input value is invalid shape"
print "Exiting the Caculator"
