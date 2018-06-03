# coding: utf-8

# 'rules' is an array of 2-tuples: first element of tuple specifies variable, second one specifies string it is to be replaced by
# theorem is the string to which rules are to be applied   
def propogate(theorem,rules):
    construct = ''
    # iterate over characters in theorem
    for c in theorem:
        # check if character is a variable, then construct according to rule
        found = 0
        for key in rules:
            if c == key[0]:
                construct += key[1]
                found = 1
                break
        if found == 0:
            construct += c
    return construct

# root is 0th string
# n is the iteration number
# 'rules' is an array of 2-tuples: first element of tuple specifies variable, second one specifies string it is to be replaced by
def findnth(root,rules,n):
    for i in range(n):
        root = propogate(root,rules)
    return root

# string is the theorem to be executed
# actrules is the action dictionary: a dictionary which maps keys to functions to be called
# the functions necessarily take no arguement, and the dictionary is of form : {'k1':fin1,'k2':fun2}
def execute(string, actrules):
    for c in string:
        for key in actrules:
            #print(key[0])
            if (key[0] == c):
                execute_from_dictionary(key[0],actrules)
                print("executed",key[0])
                break
#helper function, you will never call this

def execute_from_dictionary(trigger,dictionary):
    dictionary[trigger]()


