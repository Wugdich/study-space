# Grokking Algorithms
# An Illustrated Guid for Programmers and Other Curious People

import random
import time
from collections import deque
from typing import List
import string


def binary_search(sort_list: list, searched_item) -> int or None:
    low = 0
    high = len(sort_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sort_list[mid]
        if guess == searched_item:
            return mid
        if guess < searched_item:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_tests() -> None:
    test_array_1 = [1, 5, 6, 9, 15, 33, 56, 63, 72, 77, 93, 100]
    test_array_2 = [1, 2, 3, 4, 5, 12, 23, 32, 33, 45, 49, 59, 77, 99, 100]
    test_array_3 = [12, 33, 65, 99, 123, 138, 358, 458, 4578, 8458, 18834]
    test_arrays = [test_array_1, test_array_2, test_array_3]
    print("Binary search tests.")
    for one_array in test_arrays:
        req_index = random.randint(1, len(one_array) - 1)
        print(
            f"Input array: {one_array}.\n"
            f"Required index - {req_index}, binary search result - {binary_search(one_array, one_array[req_index])}.\n"
        )
    print(
        f"Input array: {test_array_3}.\n"
        f"Required index - None, binary search result {binary_search(test_array_3, 100)}.\n"
    )


def find_smallest(digit_list: list) -> int:
    smallest = digit_list[0]
    smallest_index = 0
    for index in range(len(digit_list)):
        if smallest > digit_list[index]:
            smallest = digit_list[index]
            smallest_index = index
    return smallest_index


def selection_sort(unsorted_array: list) -> list:
    sorted_array = []
    for iteration in range(len(unsorted_array)):
        smallest = find_smallest(unsorted_array)
        sorted_array.append(unsorted_array.pop(smallest))
    return sorted_array


def selection_sort_tests() -> None:
    test_data = [[random.randint(1, 100) for iteration in range(15)] for iteration in range(3)]
    print("Selection sort tests.")
    for one_data_set in test_data:
        print(f"Array before sort: {one_data_set}.\nArray after sort: {selection_sort(one_data_set)}\n")


def countdown(start):
    print(f"{start}...")
    time.sleep(1)
    if start - 1 == 0:
        print("Поехали!")
        return
    countdown(start - 1)


def factorial(number: int) -> int:
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def sum_recursion(array: list) -> int:
    if array:
        return array.pop() + sum_recursion(array)
    else:
        return 0


def recursion_elements_count(array: list) -> int:
    if array:
        array.pop()
        return 1 + recursion_elements_count(array)
    else:
        return 0


def recursion_max(array: list) -> int:
    # base case
    if len(array) == 1:
        return array[0]
    # recursion case
    else:
        return array[0] if array[0] > recursion_max(array[1:]) else recursion_max(array[1:])


def quick_sort(array: list) -> list:
    # base case
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        before_array = [element for element in array[1:] if element <= pivot]
        after_array = [element for element in array[1:] if element > pivot]
        return quick_sort(before_array) + [pivot] + quick_sort(after_array)


def missing(numbers: str) -> int:
    """
    На вход подаются числа от 1 до 9 в виде строки. При этом одно число пропущено.
    Функция возвращает пропущенное число в int.
    Решение реализовано с использованием контрольно суммы чисел от 1 до 9, которая равна 45
    :param numbers:
    :return:
    """
    return 45 - sum(int(number) for number in numbers)


def latin_square(size: int) -> None:
    """
    Функция выводит латинский квадрат заданного размера.
    """
    letters = list(string.ascii_letters[:size])
    random.shuffle(letters)

    for i in range(size):
        for j in range(size):
            print(letters[(i + j) % size], end=' ')
        print()


def snail(snail_map: list) -> list:
    """
    Function get n x n array, and it returns array elements arranged
    from outermost elements to the middle element, traveling clockwise.
    """
    # 0x0 matrix
    if len(snail_map) == 1:
        return snail_map[0]

    size = len(snail_map)
    # Borders realization: l - left, r - right, u - up, d - down
    # Example: lu = [0, 0] - [y, x] coordinate
    # 3x3 matrix visualisation
    # [lu, x, ru]
    # [x,  x,  x]
    # [ld, x, rd]
    lu = [1, 0]
    ru = [0, size - 1]
    ld = [size - 1, 0]
    rd = [size - 1, size - 1]
    direction = "right"
    current_position = [0, 0]  # [y, x]
    output_array = [snail_map[0][0]]

    while len(output_array) != size ** 2:

        # clockwise movement through matrix
        if direction == "right":
            current_position[1] += 1
        elif direction == "down":
            current_position[0] += 1
        elif direction == "left":
            current_position[1] -= 1
        else:
            current_position[0] -= 1

        output_array.append(snail_map[current_position[0]][current_position[1]])

        # direction and border change
        if current_position == ru:
            direction = "down"
            ru[0] += 1
            ru[1] -= 1
        elif current_position == rd:
            direction = "left"
            rd[0] -= 1
            rd[1] -= 1
        elif current_position == ld:
            direction = "up"
            ld[0] -= 1
            ld[1] += 1
        elif current_position == lu:
            direction = "right"
            lu[0] += 1
            lu[1] += 1

    return output_array


def depth_first_search(graph: dict, start_node: str, finish_node: str) -> bool:
    search_queue = deque()
    search_queue += graph[start_node]
    checked = []
    while search_queue:
        current_node = search_queue.popleft()
        if current_node not in checked:
            if current_node == finish_node:
                return True
            else:
                checked.append(current_node)
                search_queue += graph[current_node]
    return False


def depth_first_search_test() -> None:
    graph_1 = {
        'A': ['B', 'D'],
        'B': [],
        'C': ['K'],
        'D': ['C', 'M'],
        'E': ['B'],
        'F': ['D', 'G'],
        'G': ['K'],
        'M': ['E', 'S'],
        'S': ['F'],
        'K': []
    }

    graph_2 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': ['E', 'G', 'M'],
        'E': [],
        'G': [],
        'M': ['K'],
        'K': ['F'],
        'F': []
    }
    graph_num = 0
    for graph in [graph_1, graph_2]:
        graph_num += 1
        for test_number in range(1, 6):
            print(f"Test {test_number}. Graph {graph_num}.\n", end='')
            start_node = random.choice(list(graph))
            end_node = random.choice(list(graph))
            test_result = depth_first_search(graph, start_node, end_node)
            print(f"Start node - {start_node}, end node - {end_node}. Test output - {test_result}.\n")


def dijkstra_algorithm(graph: dict, costs: dict, parents: dict) -> str:
    # it's necessary to named start node "start" and finish node "finish"
    processed = list()
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors:
            new_cost = cost + neighbors[neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    # back way
    way = ['finish']
    current_node = way[0]
    while current_node != 'start':
        step_back_node = parents[current_node]
        way.append(step_back_node)
        current_node = step_back_node
    way.reverse()
    return f"Dijkstra algorithm work result.\nWay:\n{' -> '.join(way)}.\nWay weight = {costs['finish']}.\n"


def dijkstra_algorithm_test() -> None:
    graph = {'start': {'a': 6, 'b': 2}, 'a': {'finish': 1}, 'b': {'a': 3, 'finish': 5}, 'finish': {}}
    graph_a = {'start': {'a': 5, 'c': 2}, 'a': {'b': 4, 'd': 2}, 'b': {'finish': 3, 'd': 6},
               'c': {'a': 8, 'd': 7}, 'd': {'finish': 1}, 'finish': {}}
    costs = {'a': 6, 'b': 2, 'finish': float('inf')}
    costs_a = {'a': 5, 'b': float('inf'), 'c': 2, 'd': float('inf'), 'finish': float('inf')}
    parents = {'a': 'start', 'b': 'start', 'finish': None}
    parents_a = {'a': 'start', 'b': None, 'c': 'start', 'd': None, 'finish': None}
    dijkstra_algorithm(graph, costs, parents)
    print(dijkstra_algorithm(graph, costs, parents))
    print(dijkstra_algorithm(graph_a, costs_a, parents_a))


def find_lowest_cost_node(costs: dict, processed: list) -> object:
    lowest_cost = float('inf')
    lowest_node_cost = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_node_cost = node
    return lowest_node_cost


def set_digits(seconds: int) -> dict:
    # years, days, hours, minutes, seconds
    dividers = [60, 60, 24, 365]
    digits = []
    captions = ['year', 'day', 'hour', 'minute', 'second']
    for divider in dividers:
        digits.append(seconds % divider)
        seconds = seconds // divider
    digits.append(seconds)
    digits.reverse()
    # set plural
    for index in range(len(digits)):
        if digits[index] != 1:
            captions[index] += 's'
    output_hash_table = {caption: digit for caption, digit in zip(captions, digits) if digit != 0}
    return output_hash_table


def format_duration(seconds: int) -> str:
    if seconds == 0:
        return "now"
    calculated_values = set_digits(seconds)
    list_of_keys = list(calculated_values)
    caption = ''
    if len(list_of_keys) == 1:
        caption = str(calculated_values[list_of_keys[0]]) + ' ' + list_of_keys[0]
    else:
        for index in range(len(list_of_keys) - 1):
            caption += str(calculated_values[list_of_keys[index]]) + ' ' + list_of_keys[index] + ', '
        caption = caption.rstrip(', ')
        caption += ' and ' + str(calculated_values[list_of_keys[-1]]) + ' ' + list_of_keys[-1]
    return caption


def expressing_format(list_of_numbers: List[int]) -> str:
    list_of_numbers.append(list_of_numbers[-1] + 2)
    output_strings = []
    temp_data = []
    for index in range(len(list_of_numbers) - 1):
        temp_data.append(list_of_numbers[index])
        if list_of_numbers[index] + 1 != list_of_numbers[index + 1]:
            if len(temp_data) == 1:
                output_strings.append(str(temp_data[0]))
            elif len(temp_data) == 2:
                for number in temp_data:
                    output_strings.append(str(number))
            else:
                output_strings.append(str(temp_data[0]) + '-' + str(temp_data[-1]))
            temp_data.clear()

    return ','.join(output_strings)


def rearrange_to_largest(number: int) -> int:
    list_of_digits = [int(digit) for digit in str(number)]
    list_of_digits.sort(reverse=True)
    return int(''.join(str(digit) for digit in list_of_digits))


def next_bigger(num: int) -> int:
    """Takes a positive integer and return next bigger number that can be formed by rearranging its digits"""
    controller = sorted(str(num))
    for pot_bigger in range(num + 1, rearrange_to_largest(num) + 1):
        if sorted(str(pot_bigger)) == controller:
            return pot_bigger
    return -1


def set_visualisation() -> None:
    fruits = {"avocado", "tomato", "banana"}
    vegetables = {"beets", "carrots", "tomato"}
    print(
        f"Sets working explanation.\n"
        f"Sets: fruits - {fruits}, vegetables - {vegetables}.\n"
        f"-----------------------------------------------------------------------------------------------------------"
        f"---------------------------------------------\n"
        f"The union for fruits and vegetables:                               {fruits | vegetables}.\n"
        f"The intersection of fruits and vegetables:                         {fruits & vegetables}.\n"
        f"The relative component of vegetables in fruits\n"
        f"also called the set-theoretic difference of fruits and vegetables: {fruits - vegetables}.\n"
        f"And reverse difference:                                            {vegetables - fruits}.\n"
    )


def main() -> None:
    print("This is the main function\n")
    # test_array_1 = [random.randint(1, 100) for iteration in range(1, 20)]
    # test_dict_1 = {random.choice(string.ascii_uppercase): random.randint(1, 100) for iteration in range(20)}
    # from datetime import datetime
    # print(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
    # for char in test_dict_1:
    #     print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S;'):22} {char}")


if __name__ == "__main__":
    main()
