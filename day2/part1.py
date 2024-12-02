if __name__ == "__main__":
    import math
    with open('input.txt', encoding="utf-8") as f:
        leftList = []
        rightlist = []
        safeReports=0
        for line in f:
            i = 0
            report=[]
            while i < len(line):
                k=i+1
                while(k<=(len(line)+1) and line[i:k].isdigit()):
                    k=k+1
                report.append(int(line[i:k-1]))
                i+=k-i
            safe=True
            j=0
            dir=((report[0]-report[1])<0)
            safe=report[0] != report[1]
            while(j<len(report)-1):
                diff=report[j]-report[j+1]
                if(math.fabs(diff)>3 or diff==0 or ((diff<0)!=dir)):
                    safe=False
                j+=1
            if (safe):
                safeReports=safeReports+1
        print(safeReports)
                    