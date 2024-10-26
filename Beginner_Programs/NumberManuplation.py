def containsDuplicate(nums):
    setNum=set()
    duplicatedNumbers=[]
    for num in nums:
        if num not in setNum:
               setNum.add(num)
        else:
            if num not in duplicatedNumbers:
                duplicatedNumbers.append(num)
    return "There is no number duplicated" if len(duplicatedNumbers)<1 else f"Duplicated Numbers are : {duplicatedNumbers}"
# print(containsDuplicate([]))

def PlusOneList(digits):
    digits=int("".join([str(digit) for digit in digits]))+1
    digits=[int(digit) for digit in str(digits)]
    return digits
# print(PlusOne([9]))