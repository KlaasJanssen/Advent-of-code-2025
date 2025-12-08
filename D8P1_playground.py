from math import sqrt

class Box:
    def __init__(self, ID, pos, circuit):
        self.ID = ID
        self.pos = pos
        self.circuit = circuit

    def combine_circuits(self, box2):
        for box in box2.circuit:
            self.circuit.append(box)
        circuits.remove(box2.circuit)
        for box in self.circuit:
            boxes[box].circuit = self.circuit

def get_dist(box1, box2):
    dist = 0
    for index in range(len(box1)):
        dist += (box1[index] - box2[index])**2
    return sqrt(dist)

test = False

with open("data/D8.txt" if not test else "test.txt", "r") as f:
    input = [x.strip("\n") for x in f.readlines()]

boxes = {}
circuits = []
for ID, line in enumerate(input):
    circuit = [ID]
    circuits.append(circuit)
    boxes[ID] = Box(ID, [int(x) for x in line.split(",")], circuit)

dists = {}
for ID1 in range(len(boxes) - 1):
    for ID2 in range(ID1 + 1, len(boxes)):
        dists[(ID1, ID2)] = get_dist(boxes[ID1].pos, boxes[ID2].pos)

sorted_dists = sorted(dists.items(), key = lambda x: x[1])

index = 0
while index < 10 if test else index < 1000:
    (ID1, ID2), dist = sorted_dists[index]
    if not ID2 in boxes[ID1].circuit:
        boxes[ID1].combine_circuits(boxes[ID2])
    index += 1

cir_length = [len(x) for x in circuits]
answer = 1
for n in sorted(cir_length, reverse=True)[:3]:
    answer *= n
print(answer)


