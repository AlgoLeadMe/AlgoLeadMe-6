while(True) : 
   a,b,c = map(int, input().split())
   
   if (a == 0 and b == 0 and c == 0) :
        break
   

   maxLen = max(a,b,c)
   if (maxLen == a) : 
        B,C = b,c
   elif (maxLen == b) :
        B,C = a,c
   else :
        B,C = a,b
   
   if (maxLen >= B+C) :
        print("Invalid")
   else :    
        if (a==b and b==c) :
            print("Equilateral")
        elif (a==b or b==c or a==c) :
            print("Isosceles")
        else :
             print("Scalene")

 
  