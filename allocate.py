tables = [2, 2, 3, 10]
num_guests = 5
# T is matrix of optimal solutions for ea/ num_guests, tables subset pair.
# With solutions for 0 guests & 0 no tables prepended.
T = [[None] * (len(tables)+1) for _ in range(num_guests+1)]
# T[num_guests][table_subset]
# Initialize table counts for n=0 & T_0 solutions.
T[0][0] = 0
for i in range (1, num_guests+1): # No tables, can't accomodate n > 0 guests.
    T[i][0] = 999

for j in range(1,len(tables)+1): # No guests
    T[0][j] = 0
"""
 T[i][j] corresponds w/ tables[j-1] because a 0 column is added to T 
 for solutions to subproblems containing table nullset.
"""
for i in range (1, num_guests+1):
    for j in range (1, len(tables)+1):
        # j'th table seats i (remaining) guests, avoid negative indexing.
        # TODO: Add empty seats to T[i][j] to minimize.
        if i-tables[j-1] <= 0:            
            #T[i][j] = min(T[i-tables[j-1]][j-1] + 1, T[i][j-1])        
            T[i][j] = 1 + (abs(i-tables[j-1]))
        else: # take the minimum table of table included or not included solutions.
            T[i][j] = min(T[i-tables[j-1]][j-1] + 1, T[i][j-1])
answer = [0] * len(tables)
while j > 0 and i > 0:
    # Solution including j'th table at least as optimal than solution w/o it.
    if T[i][j] <= T[i][j-1]: 
        answer[j-1] = 1
        i -= tables[j-1]
    j -= 1

print("answer vector: ")
for i in range(len(answer)):
    print(answer[i])
tables_used = sum(answer)
print("tables required: ", tables_used)
#print("end")