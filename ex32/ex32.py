fruits = ["Apple", "Mangoes", "Oranges", "Bananas", "Peaches"]
fruita = ["Watermelon", "Guavava", "Kiwi", "Jack Daniels"]
for fruit in fruits:
    print fruit

print len(fruits)
print cmp(fruits, fruita)
fruits.append("Grapes")
for fruit in fruits:
    print fruit
    
i = 0

while i < 100:
    print "This is like %d th time " %i
    i += 1