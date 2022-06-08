actors = input().split(",")
for a in range(0, len(actors)):
    actors[a] = "Actors:" + actors[a]
while True:
    n = input()
    print(actors.index("Actors:" + n) + 1)
