"""
ohah
오늘 상호코칭에서 어떤 걸 얻어가면 좋을까? 어떤 걸 예상하고 있었나~ 어떤 기대?
(아...  AC2 에서하면 질문 잘~~해야할 거 같아서 어렵다~~~)

마틴하고 페어프로그래밍한다! 스타일 보자보자! 저는 0개 국어. 닥치는 대로ㅋㅋㅋㅋㅋㅋ 
JS, Java, Python, Go....
coding test는 python 으로 쓰고 있음. 마틴의 스킬 줍줍
아 긴장되요. TDD 잘~~~해야할 거 같고ㅋㅋㅋㅋㅋㅋ

Martin
저는 시영님이 어떻게 코딩하는지 궁금했습니다.
알고리즘을 보는 서로 다른 관점을 배워보자.
시영님 TDD 계속 했으니까 뺏어먹어보자.

#####
문제 : https://leetcode.com/problems/high-five/

increasing order.
dividing it by 5 using **integer** division.

- studuent - sorting 가장
- A 학생의 가장 높은 점수 5개 만 골라서 평균
[1, 90], [2, 95]


#####
오늘 페어프로그래밍에서 발견/탐색한 것 - 필요하다면 어떻게 개선할 수 있을까?

- IDE 가 익숙하지 않았다. 실제 환경에서는 pycharm 을 사용할 것이다. 
-> Pycharm으로 바꾸자 / "code with me" -> 가이드 문서 마틴에게 전달.

합이라고 하면 어떤 합??? 오늘은 탐색하는 시간. 문제 푸는 시간보다는 IDE를 맞춘다던가 코드 스타일을 맞춘다. 여기에 시간을 더 쏟았다.
오늘처럼 설명을 계속 하는 것보다는 뭐하고있는지 중얼중얼하면서 마틴에게 이야기를 하는게 좋겠다.

마틴 : 오늘은 탐색하는 느낌 새로운 걸 배워서 - live share 가 재밌다. 터미널 실행 어떻게 할까? 같이 실행하면 좋을 거 같다. 
- [ ] 개발환경 통일하기
- [ ] 공개 가능한 pair programming 용 repo 를 하나 파야겠다 
"""

from typing import List


test_case = [# items, expected_value
             ([[1, 91], [1,92], [2,93], [2,97], [1,60], [2,77], [1,65], [1,87], [1,100], [2,100], [2,76]], [[1,87], [2,88]])
             ]


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        pass


def test_highfive(test_case):
    sol = Solution()
    assert sol.highFive(test_case[0][0]) == test_case[0][1]

           
if __name__ == '__main__':
    test_highfive(test_case)
