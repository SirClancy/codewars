#! /usr/bin/python
# def namelist(names):
#     #your code here
#     toReturn = ''
#     if(len(names) == 1):
#         return names[0]['name']
#     elif(len(names) == 2):
#         toReturn = toReturn + names[0]['name'] + " & " + names[1]['name']
#     elif(len(names) > 2):
#         for i in range(0, len(names)-1):
#             toReturn = toReturn + names[i]['name'] + ", "
#         toReturn = toReturn[:-2] + " & " + names[len(names)-1]['name']
#     return toReturn


# Best Practise
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return 
print namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])