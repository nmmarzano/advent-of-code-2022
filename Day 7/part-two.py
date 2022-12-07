from sys import argv


total_size = 70000000
space_needed = 30000000


def build_tree(data):
    root = {'/': {}}
    current = root
    for line in data:
        if '$ cd' in line:
                current = current[line.split(' ')[2]]
        elif line != '$ ls':
            if 'dir' in line:
                current[line.split(' ')[1]] = {'..': current}
            else:
                current[line.split(' ')[1]] = line.split(' ')[0]
    return root


def get_size(tree):
    size = 0
    for node in tree:
        if node == '..':
            continue
        if isinstance(tree[node], str):
            size += int(tree[node])
        else:
            size += get_size(tree[node])
    return size


def get_directories(tree):
    directories = []

    for node in tree:
        if node == '..':
            continue
        if isinstance(tree[node], dict):
            directories.append(tree[node])
            directories = directories + get_directories(tree[node])

    return directories


def find_smallest_larger_than(tree, size):
    smallest = get_size(tree)
    cur_size = 0
    for directory in get_directories(tree):
        cur_size = get_size(directory)
        if cur_size < smallest and cur_size > size:
            smallest = cur_size
    return smallest
        


def test_print(tree, level):
    tabs = ''.join(['  ' for x in range(level)])
    for node in tree:
        if node != '..':
            if isinstance(tree[node], dict):
                print(f'{tabs}| {node}')
                test_print(tree[node], level + 1)
            else:
                print(f'{tabs}| {node}: {tree[node]}')        


if __name__ == '__main__':
    with open(argv[1]) as file:
        tree = build_tree(file.read().split('\n'))
        # test_print(tree, 0)
        tree_size = get_size(tree)
        free_space = total_size - tree_size
        print(find_smallest_larger_than(tree, space_needed - free_space))
