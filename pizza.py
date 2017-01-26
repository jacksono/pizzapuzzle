#Attempting to solve the pizza problem for the HashCode competition 2017
#sample input file saved as input.txt
SIZE = [2,3]
START = [0,0]

input = open("input.txt", "rt")
instructions = []
contents = []
for line in input:
    instructions.append(line.strip())
input.close()
rows_cols = instructions[0].split(' ')[0:2] #extracting rows and columns from the file
for line in instructions[1:]:                 #extracting the pizza contents
    contents.append(list(line))
min_ing_per_slice = int(instructions[0].split(' ')[2])
max_cells_per_slice = int(instructions[0].split(' ')[-1])

def one_slice(piza, size, start): #function to cut out one slice of any size without holes starting from anywhere
    one_slice = []                # for start coords i have used zero based coords so that the frst line is 0,0 not 1,1

    if size[1] > len(piza[start[1]:]) or size[0] > len(piza[0][start[0]:]): #check if slice size can fit in pizza
        return ('Size too big for this piza')

    else:
        new_piza = piza[start[1]:]
        for row in new_piza[0:size[1]]:
            new_row = row[start[0]:]
            slice_row = new_row[0:size[0]]
            one_slice.append(slice_row)
        return one_slice
    
def is_slice_valid(piza_slice): #function to check a slice for min and max ingredients
    num_of_tomato = 0
    num_of_mush = 0
    for row in piza_slice:
        for ing in row:
            if ing == "T":
                num_of_tomato += 1
            elif ing == "M":
                num_of_mush += 1
            else:
                return "Error"
    if num_of_tomato >= min_ing_per_slice and num_of_mush >=min_ing_per_slice and (num_of_mush + num_of_tomato) <= max_cells_per_slice:
        return True
    else:
        return False

def replace_element(lst, pos): #replaces an elemnt in the position pos with an X 
    new_lst = list(lst)
    new_lst[pos[1]][pos[0]] = 'X'
    return new_lst

def replace_many_elements(lst,start, size): #replaces many elements of lst depending on strt and size
    indexes = []
    for row in range(size[1]):
        for i in range(size[0]):
            index = [start[0] + i, start[1] + row]
            indexes.append(index)
    for row in indexes:
        replaced_list = replace_element(lst, row)
    return replaced_list


def number_factors(x):#function to get factors of H which will be the potential size of the slice 
    fact = []
    for i in range(1, x + 1):
        if x % i == 0:
            fact.append(i)
    combinations = []
    for i in range(len(fact)):
        combinations.append([fact[i],fact[-(i+1)]])       
    return combinations

# def cut_one_slice(piza):
#     size = number_factors(max_cells_per_slice)[1]
#     piza_slice = one_slice(piza, size , [0,0])
#     if  is_slice_valid(piza_slice):
#         for row in range(size[1]:
#             for  


#         return piza
#     return piza_slice


piza_slice = one_slice(piza = contents, size = SIZE, start = START)
# print('these are all the instructions:',instructions)
# print('these are all the contents: {}'.format(contents))
# print('these is the min ingredients per slice:',min_ing_per_slice)
# print('these are the max cells per slice:',max_cells_per_slice)
print("Full pizza:\n", contents)
print("+++++++++++++++++++++++++++++")
print("one slice:\n", piza_slice)
print("+++++++++++++++++++++++++++++")
print ("Replaced sliced elements from full piza:\n",replace_many_elements(contents, START, SIZE))
print("+++++++++++++++++++++++++++++")
print(contents)

