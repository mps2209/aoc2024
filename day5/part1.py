if __name__ == "__main__":
    with open('input.txt', encoding="utf-8") as f:
        import re
        rulespart=True
        rules=[]
        valid_pages=[]
        for line in f:
            pages=[]
            if line == "\n":
                rulespart=False
                continue
            if rulespart:
                rules.append(re.findall("(\d+)",line))
            else:
                pages=re.findall("(\d+)",line)
                valid=True
                for rule in rules:
                    if pages.count(rule[0])>0:
                        if pages.count(rule[1])>0:
                            if not pages.index(rule[0])<pages.index(rule[1]):
                                valid=False
                if valid:
                    valid_pages.append(pages)                
        sum=0
        for page in valid_pages:
            middle= int(page[int(len(page)/2)])
            sum+=middle
        print(sum)