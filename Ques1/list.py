def twoSumHashing(num_list, pair_sum):
    sums = []
    hashTable = {}

    for i in range(len(num_list)):
        complement = pair_sum - num_list[i]
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (", num_list[i],",",complement,")")
            print("index of Pair with sum", pair_sum,"is: (", num_list.index(num_list[i]),",",complement,")")   #   --> index(num_list[i])     num_list.index(num_list[i])
        hashTable[num_list[i]] = num_list[i]

num_list = [4,1,5,8]
pair_sum = 6

twoSumHashing(num_list, pair_sum)