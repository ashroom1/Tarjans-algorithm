the_graph = {1: [[], [2]], 2: [[], [3]], 3: [[], [4, 5]], 4: [[], [3]], 5: [[], [6]], 6: [[], [7]], 7: [[], [5]], 8: [[]
            , [5, 10]], 9: [[], [8]], 10: [[], [9]]}
index = 0


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return 0
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def contain(self, element):
        if self.items.__contains__(element):
            return True
        return False


my_stack = Stack()


def assignindex(vertex, index1):
    vertex_info = the_graph.get(vertex)
    vertex_info[0].append(index1)


def assign_lowlink(vertex, lowlink1):
    vertex_info = the_graph.get(vertex)
    if len(vertex_info[0]) == 1:
        the_graph.get(vertex)[0].append(lowlink1)
    else:
        the_graph.get(vertex)[0][1] = lowlink1


def getindex(vertex):
    if len(the_graph.get(vertex)[0]) == 0:
        return -1
    return the_graph.get(vertex)[0][0]


def get_lowlink(vertex):
    return the_graph.get(vertex)[0][1]


def strongconnect(v):
    global my_stack
    global index
    assignindex(v, index)
    assign_lowlink(v, index)
    index += 1
    my_stack.push(v)
    for w in the_graph.get(v)[1]:
        if getindex(w) == -1:
            strongconnect(w)
            if get_lowlink(w) < get_lowlink(v):
                assign_lowlink(v, get_lowlink(w))
        elif my_stack.contain(w):
            if getindex(w) < get_lowlink(v):
                assign_lowlink(v, getindex(w))
    if get_lowlink(v) == getindex(v):
        while v != my_stack.peek():
            print(my_stack.pop(), "", end="")
        print(my_stack.pop())


if __name__ == "__main__":
    for key in the_graph.keys():
        if len(the_graph.get(key)[0]) == 0:
            strongconnect(key)
