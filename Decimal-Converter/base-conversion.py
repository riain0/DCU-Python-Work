val = input("Enter number to convert: ")
base = input("Enter base of number system you wish to convert to: ")

d = 1
i = 0

while (base ** d) <= val:
   d += 1

while i < d:
   power = (base ** (d - i -1))
   output = val / power
   if (base == 16) and (output >= 10) and (output < 16):
      if output == 10:
         print "A"
      elif output == 11:
         print "B"
      elif output == 12:
         print "C"
      elif output == 13:
         print "D"
      elif output == 14:
         print "E"
      else:
         print "F"
   else:
      print output
   val = val % power
   i += 1
