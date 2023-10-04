if __name__ == '__main__':
    n = int(input())
    if(n>=2 and n<=10):
        b = input()
        c = map(int,b.split())
        arr=[]
        for item in c:
            arr.append(item)
        arr.sort()
        c = set(arr)
        d = list(c)
        
    else:
        pass
            
    print(d[-2])
