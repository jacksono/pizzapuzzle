#Attempting to solve the pizza problem for the HashCode competition 2017
#sample input file saved as input.txt
import copy



input = open("input.txt", "rt")
instructions = []
contents = []
for line in input:
    instructions.append(line.strip())
input.close()
rows_cols = [int(instructions[0].split(' ')[0:2][0]), int(instructions[0].split(' ')[0:2][1])] #extracting rows and columns from the file
for line in instructions[1:]:                 #extracting the pizza contents
    contents.append(list(line))
min_ing_per_slice = int(instructions[0].split(' ')[2])
max_cells_per_slice = int(instructions[0].split(' ')[-1])

START = [0,0] # cols X rows

def one_slice(piza, size, start): #function to cut out one slice of any size without holes starting from anywhere
    one_slice = []                # for start coords i have used zero based coords so that the frst line is 0,0 not 1,1

    if size[1] > len(piza[start[1]:]) or size[0] > len(piza[0][start[0]:]): #check if slice size can fit in pizza
            return "Size too big for this portion"                          #may not ned this check since its checked in slice_whole_pizza()

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

def slice_whole_piza(pizza, start, sizes): #function to cut whole piza to valid max sized slices starting from any where
    new_pizza = copy.deepcopy(pizza)
    slices = []
    slice_no = 0
    total_cells = 0
    for y in range(len(pizza)): #nesting too much
        y += start[1]
        if y < len(pizza):
            for x in range(len(pizza[0])):
                if slice_no < rows_cols[1]:
                    size = sizes[slice_no]
                x += start[0]
                if x < len(pizza[0]):
                    if new_pizza[y][x] != 'X' and (len(pizza[0]) - (x)) >= size[0]  and (len(pizza) - y) >= size[1]:
                        slce = one_slice(new_pizza, size, [x, y])
                        if is_slice_valid(slce):
                            slices.append(slce)
                            replace_many_elements(new_pizza, [x, y], size)
                            slice_no += 1
                            for row in slce:
                                total_cells += len(row)

    print('full pizza', *new_pizza,sep = '\n')
    for slce in slices:
        print('slice', *slce, sep = '\n')
        print('+++++++++') 

    return [slice_no, total_cells]

def possible_sizes(rows_cols): # function to extract possible slice sizes
    sizes= []
    for n in range(rows_cols[1]):
        n += 1
        row = rows_cols[0]
        col = n
        if (row * col) <= max_cells_per_slice:
            sizes.append([col, row])
    return sizes

def size_alt(rows_cols):# to generate alternative slice sizes
    pos = possible_sizes(rows_cols)
    options = []
    new = []
    n = 0
    for size in pos:
        options.append([size] * 5)
    new1 = copy.deepcopy(options[0])
    while n < len(options[0]):
        new1.insert(n, pos[1])
        new.append(new1)
        n += 2
    opt1 = new[0][:5]
    opt2 = new[1][1:6]
    options.append(opt1)
    options.append(opt2)
    return options

def final(piza, start, rows_cols):#ALLTOGETHER NOW
    slice_sizes = size_alt(rows_cols)
    bestcut = 0
    bestslice = ['x']
    for size in slice_sizes:
        slice_no, total_cells = slice_whole_piza(piza, start, size)
        print("There are {} slices of {} total cells cut".format(slice_no, total_cells))
        if total_cells > bestcut:
            bestslice[0] = total_cells
            bestcut = total_cells

        print("**************************************************************")
    print("highest no of cells cut is : ", bestcut)

print(*size_alt(rows_cols), sep = "\n")
print(final(contents, START, rows_cols))

