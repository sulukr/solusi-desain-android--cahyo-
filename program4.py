# Program 4 - String Manipulation

input1 = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
input2 = "pizzachickenfriesburgercokemilkshakefriessandwich"
urutan = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]

def StringManipulation(stringIn, urutan):
    stringOut = ""
    for word in urutan:
        countWord = stringIn.count(word.lower())
        for i in range(countWord):
            stringOut = stringOut + word + " "
    print(stringOut)

StringManipulation(input1, urutan)
StringManipulation(input2, urutan)
