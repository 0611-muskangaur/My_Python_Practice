#for loop
name="muskan"   #string-characters
for i in name:
    print(i, end=",")
 
colors=["red","orange","blue","black","brown"]   #list-elements
for color in colors:
  print(color)
  for i in color:
   print(i)

#range function in for loop
for i in range(1,20,2):    #(start, stop , step)
 print(i+1)


#while loop
count = 1

while count <= 5:
    print(count)
    count += 1  # Increment the count


#break statement
string= input("Enter any string: ")
for i in string:
  if( len(string)>20):
    print("breaking out from the loop." )
    break
  print(i,end=",")