def reverse(s):
   str = ""
   for i in s:
      str = i + str
   return str

#def check(s):
#   if s == reverse(s):
#      return True
#   else:
#      return False

a = 100
b = 100
larg = 0
for a in range(1,1000):
   #print ("a", a, b, a*b)
   for b in range(1,1000):
      #print("b", a, b, a*b)
      if str(a*b) == reverse(str(a * b)):
         if (a * b) > larg:
            larg = a * b
      b += 1
   a += 1
print (larg)