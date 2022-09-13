def BFS(graph, source):
    visited = [False] * len(graph.data)
    queue = []

    visited[source] = True
    queue.append(source)

    i = 0
    while i < len(queue):
        for v in graph.data[queue[i]]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
        i += 1

    return queue


def to_lwer(char):
    dict = {}
    for i in range(65, 120, 1):
        dict[chr(i)] = i

    if chr(dict[char]) >= 'a' and chr(dict[char]) <= 'z':
        return
    else:
        tmp = chr(dict[char]) - chr(dict) + 'a'
        return tmp

def to_lower(*char):
    try:
        # char = char.split("")
        if type(char) == int:
            dictint = {}
            for i in range(65, 91, 1):
                dictint[i] = i + 32
            return chr(dictint[char])
        else:
            dict = {}
            for i in range(65, 91, 1):
                dict[i] = i + 32
            dictal = {}
            for i in range(65, 91, 1):
                dictal[chr(i)] = i
            if dictal[char]:
                return chr(dict[dictal[char]])
            else:
                tmp = "invalid character"
                return tmp
    except Exception as e:
        print("Already lower", e)
# dict = {}
# for i in range(65, 91, 1):
#     dict[i] = i + 32
# dictal = {}
# for i in range(65, 91, 1):
#     dictal[chr(i)] = i
# char = 'A'
# if dictal[char]:
#     print(dict[dictal[char]])
# # to_lwer("V")
# print(chr(97))

# print(to_lower("BNC"))

print(to_lower("d"))
print(to_lower(100))