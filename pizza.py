#Attempting to solve the pizza problem for the HashCode competition 2017
#sample input file saved as input.txt
import copy



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

SIZE = [1,3] #cols X rows
START = [1,0] #

def one_slice(piza, size, start): #function to cut out one slice of any size without holes starting from anywhere
    one_slice = []                # for start coords i have used zero based coords so that the frst line is 0,0 not 1,1

    if size[1] > len(piza[start[1]:]) or size[0] > len(piza[0][start[0]:]): #check if slice size can fit in pizza
            return "Size too big for this portion"

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
    #new_lst = [list(x) for x in lst]
    new_lst = list(lst)
    for row in pos:         #pos must be a list of lists
        new_lst[row[1]][row[0]] = 'X'
    return new_lst

def replace_many_elements(lst,start, size): #replaces many elements of lst depending on strt and size
    indexes = []
    for row in range(size[1]):
        for i in range(size[0]):
            index = [start[0] + i, start[1] + row]
            indexes.append(index)
    return replace_element(lst, indexes)


def number_factors(x):#function to get factors of H which will be the potential size of the slice 
    fact = []
    for i in range(1, x + 1):
        if x % i == 0:
            fact.append(i)
    combinations = []
    for i in range(len(fact)):
        combinations.append([fact[i],fact[-(i+1)]])       
    return combinations

def slice_whole_piza(pizza): #function to cut whole piza to valid max sized slices starting from any where
    new_pizza = copy.deepcopy(pizza)
    slices = []
    start = [2,0]
    for y in range(len(pizza)):
        y += start[1]
        if y < len(pizza):
            for x in range(len(pizza[0])):
                x += start[0]
                if x < len(pizza[0]):
                    if new_pizza[y][x] != 'X' and (len(pizza[0]) - (x)) >= SIZE[0]  and (len(pizza) - y) >= SIZE[1]:
                        slce = one_slice(new_pizza, SIZE, [x, y])
                        if is_slice_valid(slce):
                            slices.append(slce)
                            replace_many_elements(new_pizza, [x, y], SIZE)
    print('full pizza', *new_pizza,sep = '\n')
    for slce in slices:
        print('slice', *slce, sep = '\n')
        print('+++++++++')

    return len(slices)


piza_slice = one_slice(piza = contents, size = SIZE, start = START)
# print('these are all the instructions:',instructions)
# print('these are all the contents: {}'.format(contents))
# print('these is the min ingredients per slice:',min_ing_per_slice)
# print('these are the max cells per slice:',max_cells_per_slice)
# print("Full pizza:\n", contents)
# print("+++++++++++++++++++++++++++++")
# print("one slice:\n", piza_slice)
# print("+++++++++++++++++++++++++++++")
# print ("Replaced sliced elements from full piza:\n",replace_many_elements(contents, START, SIZE))
# print("+++++++++++++++++++++++++++++")
print(slice_whole_piza(contents))


