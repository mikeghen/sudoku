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

pprint(solving_space[0][1] - set(solution_space[0]) - set([row[1] for row in solution_space]))

# #print(solution_space[0])
# # for row in solution_space:
# #     print(row[0])
#
# for i in range(9):
#     for j in range(9):
#         print(solution_space[i][j])
