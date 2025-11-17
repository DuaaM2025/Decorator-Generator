def generate_readfile(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

for l in generate_readfile("data.txt"):
    print(l)

