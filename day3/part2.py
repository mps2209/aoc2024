if __name__ == "__main__":
    import re
    with open('input.txt', encoding="utf-8") as f:
        sum=0
        results=[]
        for line in f:
            result= re.findall("mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don\'t\(\)",line)
            for res in result:
                results.append(res)
        isDo=True
        for r in results:
            if(r=="do()"):
                print("do()")
                isDo=True
            elif(r=="don't()"):
                print("don't()")
                isDo=False
            elif isDo:
                pair= re.findall("\d\d?\d?",r)
                sum+=int(pair[0])*int(pair[1])
        print(sum)