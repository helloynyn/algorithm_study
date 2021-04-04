from itertools import combinations

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.loc=0
        self.combinations=list(combinations(characters, combinationLength))

    def next(self) -> str:
        self.loc+=1
        return "".join(self.combinations[self.loc-1])

    def hasNext(self) -> bool:
        return self.loc<len(self.combinations)

itr=CombinationIterator("abc", 2);
print(itr.next())    # return "ab"
print(itr.hasNext()) # return True
print(itr.next())
print(itr.hasNext())
print(itr.next())
print(itr.hasNext())

'''
1. 순열

[함수]
permutations(반복 가능한 객체, r)

[코드]
from itertools import permutations

for i in permutations([1,2,3,4], 2):
    print(i, end=" ")

[결과]
(1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3) 

2. 조합

[함수]
combinations(반복 가능한 객체, r)

[코드]
from itertools import combinations

for i in combinations([1,2,3,4], 2):
    print(i, end=" ")

[결과]
(1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4) 

3. 중복순열

[함수]
product(반복 가능한 객체, repeat=1)

[코드]
for i in product([1,2,3],'ab'):
    print(i, end=" ")

[결과]
(1, 'a') (1, 'b') (2, 'a') (2, 'b') (3, 'a') (3, 'b')

4. 중복조합

[함수]
combinations_with_replacement(반복 가능한 객체, r)

[코드]
from itertools import combinations_with_replacement

for cwr in combinations_with_replacement([1,2,3,4], 2):
    print(cwr, end=" ")

[결과]
(1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4) 


https://juhee-maeng.tistory.com/91
'''