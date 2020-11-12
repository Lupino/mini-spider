import random
def gennums():
    nums = []
    while True:
        num = random.randint(0, 9)
        if num in nums:
            continue
        nums.append(num)
        if len(nums) >= 4:
            break
    return nums
    
def readnums():
    while True:
        nums = input('请输入四位不重复的数字: ')
        if len(nums) != 4:
            print('只能输入4位数字')
            continue
        if not nums.isdigit():
             print('请输入正确的数字')
             continue
        tempval = []
        isrepeat = False
        for num in nums:
            if num in tempval:
                isrepeat = True
                break
            tempval.append(num)
            
        if isrepeat:
            print('错误有重复的数字')
            continue
        return nums
        
def tostr(nums):
    retval = ''
    for num in nums:
        retval += str(num)

    return retval
    
def calcab(nums1, nums2):
    b = 0
    for num in nums1:
        if nums2.find(num) > -1:
            b += 1
    a = 0
    for num1, num2 in zip(nums1, nums2):
        if num1 == num2:
            a += 1
            
    return a, b - a
    
def guessnums():
    sysnums = tostr(gennums())
    guessed = False
    for _ in range(8):
        inpnums = readnums()
        a, b = calcab(sysnums, inpnums)
        print('{} {}A{}B'.format(inpnums, a, b))
        if a == 4:
            guessed = True
            break
    if guessed:
        print('恭喜你答对了')
    else:
        print('答错了，正确答案：{}'.format(sysnums))
guessnums()