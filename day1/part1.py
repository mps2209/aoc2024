if __name__ == "__main__":
    import math
    with open('input.txt', encoding="utf-8") as f:
        leftList = []
        rightlist = []
        for line in f:
            tuples = line.partition("   ")
            # print("left: " + tuples[0] + " right: " + tuples[2])
            leftList.append(tuples[0])
            rightlist.append(tuples[2])
        leftList.sort()
        rightlist.sort()
        sum = 0
        i = 0
        for l in leftList:
            sum += math.fabs(int(rightlist[i])-int(l))
            i += 1
        print(sum)
