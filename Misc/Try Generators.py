""" What are Generators in Python?
Generators are basically functions that return traversable objects or items. 
These functions do not produce all the items at once, rather they produce them one at a time and only 
when required. Whenever the for statement is included to iterate over a set of items, a generator 
function is run. Generators have a number of advantages as well.


Advantages of using Generators
Without Generators in Python, producing iterables is extremely difficult and lengthy.

Generators easy to implement as they automatically implement __iter__(), __next__() and StopIteration 
which otherwise, need to be explicitly specified.

Memory is saved as the items are produced as when required, unlike normal Python functions. 
This fact becomes very important when you need to create a huge number of iterators. 
This is also considered as the biggest advantage of generators.

Can be used to produce an infinite number of items.

They can also be used to pipeline a number of operations

 """

""" def square_nos(N):
    result = []
    for i in N:
        result.append(i*i)
    return result

numbers = square_nos([1,2,3,4,5,6])
print(numbers)
 """

""" Conerting the above funtion as Generator """


""" def square_nos(N):
    for i in N:
        yield i*i

numbers = square_nos([1,2,3,4,5,6])
for i in numbers:
    print(i) """

""" print (next(numbers))
print (next(numbers))
print (next(numbers))
print (next(numbers))
print (next(numbers))
print (next(numbers))
print (next(numbers)) """


""" Conerting the above funtion as Generator as List Comprehension """

square_nos = (i*i for i in [1,2,3,4,5,6])

print(square_nos)

for i in square_nos:
    print(i) 
 

""" Example with time complexity """

""" import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print 'Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil())

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print 'Took {} Seconds'.format(t2-t1) """