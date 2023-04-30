side1=int(input("enter number"))
side2=int(input("enter number"))
side3=int(input("enter number"))
if(side1<side2+side3)or(side2<side1+side3)or(side3<side1+side2):
 print("draw the triangle")
else:
 print("you can not draw the Triangle")