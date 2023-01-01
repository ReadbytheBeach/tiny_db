import copy

light_copy = ['me','lisa','bobo','trees']
eggs = copy.copy(light_copy)
print(eggs)
print('内容是否相同： ', light_copy == eggs)
print(light_copy is eggs)
print('id号是否相同: ', id(light_copy)==id(eggs))
print(id(light_copy))
print(id(eggs))

egg_deepcopy = copy.deepcopy(light_copy)
print(egg_deepcopy)
print('内容是否相同： ', light_copy == egg_deepcopy)
print(light_copy is egg_deepcopy)
print('id号是否相同: ', id(light_copy)==id(egg_deepcopy))
print(id(light_copy))
print(id(egg_deepcopy))




numberoftrees={'Cereus': 4,'Orchid':2}
print('I have', numberoftrees.get('Cereus',3),'Cereus' )

numberoftrees.setdefault('Fern',1)  # setdefaut()的字典用法
print('I have ',numberoftrees.get("Fern",10), 'Fern') #get()的字典用法