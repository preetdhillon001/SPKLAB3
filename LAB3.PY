#declaring dictonary
shoppingCart={}
#introducing variable
i=0
j=0
#print statements
print("1.Add product to the cart")
print("2.Search the product")
print("3.Delete the product from the cart")
print("4.Quit")
#while loop
while(i!=4):
 i=int(input("ENTER YOUR OPTION:"))
 if(i==1):#option for adding item
    p=int(input("enter the number of items to be added "))
    g=0
    
    while(g<p):
     if(p<5):
      b=input("Enter an item:")
      a=input("Enter brand name:")
  #updating dictionary
      shoppingCart.update({b:a})
      print("YOU ADDED FOLLOWING ITEMS TO CART SUCCESSFULLY")
     else:
       pass
       if(g==0):
        print("CART IS FULL")
     g=g+1
    print(shoppingCart) #output after addition of items 
 elif(i==2):#option for searching item
   b=input("Enter an item:")
   x=0
   for j in shoppingCart.keys():
      if (j==b):
       print(j+":"+shoppingCart[j])#displaying searched item
       x=1
      else:
       pass
   
   if(x==0):
      print("No product exists with this name")

#option for deleting item
 elif(i==3):
   b=input("Enter an item:")
  #output after deleting items
   shoppingCart.pop(b)
   print("Cart is empty, no item is found") 
#option for quiting 
 else:
  print("Quiting")