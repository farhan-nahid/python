
def count_frequency_with_list(n: list[int], m: list[int]):
    hash_list = [0] * 11

    for num in n:
        hash_list[num] += 1

    for num in m:
        if num < 0 or num > 10:
            print(f"{num}: 0")
        else:
            print(f"{num}: {hash_list[num]}")



def count_frequency_with_dict(n: list[int], m: list[int]):
    hash_dict = {}

    for num in n:
        hash_dict[num] = hash_dict.get(num, 0) + 1

    for num in m:
        print(f"{num}: {hash_dict.get(num, 0)}")



count_frequency_with_list([5,3,2,2,1,5,5,7,5,10], [10, 111, 1, 9,5, 67, 2])
count_frequency_with_dict([5,3,2,2,1,5,5,7,5,10], [10, 111, 1, 9,5, 67, 2])