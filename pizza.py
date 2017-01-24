#Attempting to solve the pizza problem for the HashCode competition 2017
#sample input file saved as input.txt


input = open("input.txt", "rt")
instructions = []
for line in input:
    instructions.append(line.strip())
input.close()
rows_cols = instructions[0].split(' ')[0:2] #extracting rows and columns from the file
contents = instructions[1:]                 #extracting the pizza contents
for i in range(int(rows_cols[0])):          #printing the picture of the pizza
    print(contents[i])
    print()

min_ing_per_slice = instructions[0].split(' ')[2]
max_cells_per_slice = instructions[0].split(' ')[-1]


print('these are all the instructions:',instructions)
print('these are all the contents: {}'.format(contents))
print('these is the min ingredients per slice:',min_ing_per_slice)
print('these are the max cells per slice:',max_cells_per_slice)
