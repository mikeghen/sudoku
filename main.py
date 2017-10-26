print("Hello world")



solution_space=[[ 4, None, 1, 2, 9, None, None, 7, 5],
[2, None, None, 3, None, None, 8, None, None],
[None, 7, None, None,8, None, None, None, 6],
[None, None, None, 1, None, 3, None, 6, 2],
[1, None, 5, None, None, None, 4, None, 3],
[7, 3, None, 6, None, 8, None, None, None],
[6, None, None, None, 2, None, None, 3, None],
[None, None, 7, None, None, 1, None, None, 4],
[8, 9, None, None, 6, 5, 1, None, 7]]

#print(solution_space[0])
# for row in solution_space:
#     print(row[0])

for i in range(9):
    for j in range(9):
        print(solution_space[i][j])
