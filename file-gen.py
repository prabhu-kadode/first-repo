def loadfile(filename):
    with open(filename,"r") as file:
        for f in file:
            yield f

for content in loadfile("logs.txt"):
    print(content)

