# creating an empty set
st = set()

# creating a set with values
st = {'item1', 'item2', 'item3', 'item4'}

# length of the set
len(st)

# checking if an item is present in the set
# print('item1' in st)  # True

#adding an item to the set
st.add('item5')

#add multiple items to the set
st.update(['item6', 'item7', 'item8'])

#removing an item from the set
st.remove('item1')  # if the item is not found, it will raise an error

#removing a random item from the set
st.pop()  # removes a random item from the set and returns the removed item

#emptying the set
st.clear()  # removes all items from the set

#deleting the set
del st  # deletes the set completely

#converting a list to a set
lst = [1, 2, 3, 4, 5]
st = set(lst)  # converting list to set

#joining two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)  # joining two sets using union method

#finding the intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.intersection(set2)  # finding the intersection of two sets using intersection method

#checking subset and superset
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set1.issubset(set2)  # True
set2.issuperset(set1)  # True

#checking the difference between two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set2.difference(set1)  # {4, 5} - returns the difference of set2 from set1
set1.difference(set2)  # {1, 2} - returns the difference of set1 from set2


'''
finding the symmetric difference between two sets
it means the items that are in either set1 or set2 but not in both
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.symmetric_difference(set2)  # {1, 2, 4, 5} - returns the symmetric difference of the two sets

#two sets are disjoint if they have no common items
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set1.isdisjoint(set2)  # True



'''
practice section
Exercises: Level 1
1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4.emove one of the companies from the set it_companies
5. What is the difference between remove and discard
Exercises: Level 2
1. Join A and B
2. Find A intersection B
3. Is A subset of B
4. Are A and B disjoint sets
5. Join A with B and B with A
6. What is the symmetric difference between A and B
7. Delete the sets completely
Exercises: Level 3
1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
2. Explain the difference between the following data types: string, list, tuple and set
3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1.1
it_companiesleng = len(it_companies)
print('the len of the set is: ' + str(it_companiesleng))
#1.2
it_companies.add('Twitter')
print('adding a company to it_companies: ' + str(it_companies))
#1.3
it_companies.update({'Snapchat', 'Meta', 'Steam'})
print('adding multiple companies to it_companies: ' + str(it_companies))
#1.4
it_companies.remove('Meta')
print('removing a company from it_companies: ' + str(it_companies))
#1.5
print('.discard doesnt rise an error if the element isnt a member of the set')

#2.1
AB = A.union(B)
print('join A and B: ' + str(AB))
#2.2
AinsersectionB = A.intersection(B)
print('A interseccion B: ' + str(AinsersectionB))
#2.3
AissubsetB = A.issubset(B)
print('A es un subset de B: ' + str(AissubsetB))
#2.4
ABaredisjoint = A.isdisjoint(B)
print('A y B son sets disjuntos: ' + str(ABaredisjoint))
#2.5
AjoinB = A.union(B)
BjoinA = B.union(A)
print('A union B: ' + str(AjoinB) + ' B union A: ' + str(BjoinA))
#2.6
AsymmetricdiffB = A.symmetric_difference(B)
print('la diferencia simetrica entre a y b es: ' + str(AsymmetricdiffB))
#2.7
del A
del B
del it_companies
print('se eliminan los sets')


#3.1
lenage = len(age)
ages = set(age)
lenages = len(ages)
print('longitud de la lista age: ' + str(lenage) + 'longitud del set ages: ' + str(lenages))

#3.2
print('strig es una cadena de caracteres es ordenable, es inmmutable, permite duplicados y su sintaxis es '' ')
print('lista se caracteriza por ser una coleccion de multiples objetos ordenados es mutable, permite duplicados y su sintaxis es []')
print('tupla tambien es una coleccion de multiples objetos ordenados pero es inmutable, permite duplicados y su sintaxis es ()')
print('set es una coleccion no ordenada, mutable, no permite duplicados y su sintaxis es {}')

#3.3
texto = "I am a teacher and I love to inspire and teach people"
palabras = set(texto.split())
lenpalabras = len(palabras)
print('la cantida de palabras unicas que se usan en el texo: "I am a teacher and I love to inspire and teach people" son: ' + str(lenpalabras))