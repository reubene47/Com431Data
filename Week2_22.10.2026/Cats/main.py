from cat import Cat

cat1 = Cat("Binnie", 4)
cat2 = Cat("Clyde", 1)
cat3 = Cat("Old Tom", 6)

print(cat1.getDetails())
print(cat2.getDetails())
print(cat3.getDetails())

cat1.eat(1)
# cat2.eat(1)
cat3.eat(1)

cat1.walk()
cat2.walk()
cat3.walk()

print(cat1.weight)
print(cat2.weight)
print(cat3.weight)