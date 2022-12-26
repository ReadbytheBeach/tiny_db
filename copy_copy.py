import copy

light_copy = ['me','lisa','bobo','trees']
eggs = copy.copy(light_copy)
print(eggs)
print(light_copy == eggs)
print(light_copy is eggs)
print(id(light_copy)==id(eggs))
print(id(light_copy))
print(id(eggs))


numberoftrees={'Cereus': 4,'Orchid':2}
print('I have', numberoftrees.get('Cereus',3),'Cereus' )

numberoftrees.setdefault('Fern',1)  # setdefaut()的字典用法
print('I have ',numberoftrees.get("Fern",10), 'Fern') #get()的字典用法