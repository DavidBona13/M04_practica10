
import exercici1_A as Retriever
import exercici2_A as List

#Ex1_A

#Get user response
RetrievedAge = input("Tell me when you were born\n")

#Print stuff
print("Your age is : " + str(Retriever.GetAge(int(RetrievedAge))) if RetrievedAge != "" else "Input something!")


#Ex2_A

#Print length
print(len(List.Fruits))

#Print the list values
print(List.Fruits.values())

#Pop out the last item
print( "Popped item : " + str(List.Fruits.popitem()))


