def majorityelementII(nums):
    n=len(nums)
    d={}
    out=[]
    for i in range(n):
        if nums[i] in d:
            d[nums[i]]+=1
        else:
            d[nums[i]]=1
    for key,value in d.items():
        if value>n//3:
            out.append(key)
            return out
nums=list(map(int,input().split()))
print(majorityelementII(nums))
