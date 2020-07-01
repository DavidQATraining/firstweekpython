# file = open("filename.txt", "r")
#
# outfile = ""
#
# for line in range(10):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else:
#         file.readline()
#
# file = open("filename.txt", "w")
# file.write(outfile)
# file.close()

#--------------------------

file = open("teams.txt", "w")

teams = ["Celtic FC", "Man Utd", "Liverpool", "Real Madrid", "Barcelona"]
for n in range(len(teams)):
    file.write(teams[n] + "\n")
file.close()

file = open("teams.txt", "r")
lines = file.readlines()
print(lines)
file.close()

# with open('teams.txt', 'r') as f:
#     myTeams = [line.strip() for line in f]
#
# myNewTeams = [myTeams[1:]]
# #myNewTeams.insert(0, "This is a new line")
# file.close()
#
# file = open("teams.txt", "w")
# for n in range(len(myNewTeams)):
#     file.write(myNewTeams[n] + "\n")
# file.close()
#
# file = open("teams.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()