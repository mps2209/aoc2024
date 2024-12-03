if __name__ == "__main__":
    import re
    with open('input.txt', encoding="utf-8") as f:
        sum=0
        for line in f:
            result= re.findall("mul\((\d\d?\d?),(\d\d?\d?)\)",line)
            print(result)
            for pair in result:
                sum+=int(pair[0])*int(pair[1])
        print(sum)