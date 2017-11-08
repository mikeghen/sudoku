from pprint import pprint

solution_space = [[ 4, None, 1, 2, 9, None, None, 7, 5],
[2, None, None, 3, None, None, 8, None, None],
[None, 7, None, None,8, None, None, None, 6],
[None, None, None, 1, None, 3, None, 6, 2],
[1, None, 5, None, None, None, 4, None, 3],
[7, 3, None, 6, None, 8, None, None, None],
[6, None, None, None, 2, None, None, 3, None],
[None, None, 7, None, None, 1, None, None, 4],
[8, 9, None, None, 6, 5, 1, None, 7]]

L_FULL = {1,2,3,4,5,6,7,8,9}

solving_space = []
for i in range(9):
    solving_space.append([])
    for j in range(9):
        solving_space[i].append(L_FULL)
#pprint(solving_space)

def row_set(i):
    return set(solution_space[i])

def column_set(j):
    return set([row[j] for row in solution_space])

def ninth_set(i,j):
    a = 3*(i/3)
    b = 3*(j/3)
    return set([solution_space[a][b], solution_space[a][b+1], solution_space[a][b+2], solution_space[a+1][b], solution_space[a+1][b+1], solution_space[a+1][b+2], solution_space[a+2][b], solution_space[a+2][b+1], solution_space[a+2][b+2]])

for k in range(10):
    is_done = True
    for i in range(9):
        for j in range(9):
            if solution_space[i][j] is not None:
                solving_space[i][j] = set([solution_space[i][j]])
            else:
                solving_space[i][j] = solving_space[i][j] - row_set(i) - column_set(j) - ninth_set(i,j)
            if len(solving_space[i][j]) == 1:
                solution_space[i][j] = (solving_space[i][j]).pop()
            if solution_space[i][j] == None:
                is_done = False
    if is_done:
        print(k)
        break

pprint(solution_space)
pprint(solving_space)



# #print(solution_space[0])
# # for row in solution_space:
# #     print(row[0])
#
# for i in range(9):
#     for j in range(9):
#         print(solution_space[i][j])
