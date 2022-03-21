def solution_1(_input):

    result =  []

    # 2 loop with the pointer i  check from first list to near end list
    #each i the pointer j check from agument i+1 to end list
    for i in range(0,len(_input)-1):
        for j in range(i+1,len(_input)):
            #check position i and j is equal
            if(_input[i]==_input[j]):
                #append the tuple with position i and j 
                result.append((i,j))                
    return result


example1 = [1,2,3,1,1,3]

print('Example1: {}\nOutPut: {}\n\n'.format(example1,solution_1(example1)))

example2 = [1,1,1,1]

print('example2: {}\nOutPut: {}\n\n'.format(example2,solution_1(example2)))

example3 = [1,2,3]

print('example3: {}\nOutPut: {}\n\n'.format(example3,solution_1(example3)))
