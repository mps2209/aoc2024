if __name__ == "__main__":
    with open('input.txt', encoding="utf-8") as f:
        import re
        rulespart=True
        rules=[]
        corrected_pages=[]
        for line in f:
            pages=[]
            if line == "\n":
                rulespart=False
                continue
            if rulespart:
                rules.append(re.findall("(\d+)",line))
            else:
                pages=re.findall("(\d+)",line)
                corrected=False
                didCorrect=True
                while(didCorrect):
                    didCorrect=False
                    for rule in rules:
                        if pages.count(rule[0])>0:
                            if pages.count(rule[1])>0:
                                leftIndex=pages.index(rule[0])
                                rightIndex=pages.index(rule[1])
                                if not leftIndex<rightIndex:
                                    pages[leftIndex]=rule[1]
                                    pages[rightIndex]=rule[0]
                                    corrected=True
                                    didCorrect=True
                if corrected:
                    corrected_pages.append(pages)                
        sum=0
        for page in corrected_pages:
            middle= int(page[int(len(page)/2)])
            sum+=middle
        print(sum)