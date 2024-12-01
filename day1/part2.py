if __name__ == "__main__":
    with open('input.txt', encoding="utf-8") as f:
        leftList = []
        rightlist = []
        for line in f:
            tuples = line.partition("   ")
            # print("left: " + tuples[0] + " right: " + tuples[2])
            leftList.append(int(tuples[0]))
            rightlist.append(int(tuples[2]))
        sum = 0
        i = 0
        for l in leftList:
            list_to_filter = rightlist.copy()
            result = filter(lambda x: x == l, list_to_filter)
            sum += int(l)*len(list(result))
            i += 1
        print(sum)
