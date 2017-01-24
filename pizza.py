#Attempting to solve the pizza problem for the HashCode competition 2017
#sample input file saved as input.txt


input = open("input.txt", "rt")
instructions = []
for line in input:
    instructions.append(line.strip())
rows_cols = instructions[0].split(' ')[0:2] #extracting rows and columns from the file
contents = instructions[1:]                 #extracting the pizza contents
for i in range(int(rows_cols[0])):          #printing the picture of the pizza
    print(contents[i])
    print()

input.close()
print('these are all the instructions:',instructions)
print('these are all the contents: {}'.format(contents))
