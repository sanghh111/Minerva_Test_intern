import string

lowercase = string.ascii_lowercase


#process string becomes a list count 
#Exameple "bbbaacdafe"  
#[  a  ,   b    ,     c      ,      d    ,    f    ,     e     ]
#[  3  ,   3    ,     1      ,      1    ,    1    ,     1     ]
def process_beautiful_string(_input):
    
    #find max character
    temp_char = max(_input)

    #position max in a lowercase
    max_number_char = lowercase.find(temp_char)+1

    temp_str = lowercase[:max_number_char]

    #initiate list atribute iteam eqal = 0
    list_count_char = [0 for i in range(max_number_char)]

    #check from frist list to last list  
    for _char in _input:
        for  pointer in range(max_number_char):
            #find position character
            if _char == temp_str[pointer]:
                list_count_char[pointer]+=1
                break

    return list_count_char

#check string is beautiful ?        
def is_beautiful_string(_input):
    
    list_count_char = process_beautiful_string(_input)

    # print(list_count_char)

    for pointer in range(len(list_count_char)-1):
        if list_count_char[pointer] == 0:
            return False
        else :
            if list_count_char[pointer] < list_count_char[pointer+1]:
                return False

    return True
    




exmaple =  "bbbaacdafe"

print("Input: {}\nOutPut: {}\n\n".format(exmaple,is_beautiful_string(exmaple)))


exmaple =  "aabbb"

print("Input: {}\nOutPut: {}\n\n".format(exmaple,is_beautiful_string(exmaple)))

exmaple =  "bbbbcbaacdafe"

print("Input: {}\nOutPut: {}\n\n".format(exmaple,is_beautiful_string(exmaple)))
