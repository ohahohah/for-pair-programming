'''
 1. 문제를 여기다가  옮겨온다. testcase 같이. expected, actual.
 2. 문제 접근방법 -
    1) 첫번째 testcase는 홀수네...
    2) alnum만 취급한다. 나머지는 무시한다. 대소문자도 무시: 전처리 필요?
    3) 원래 문장과 reverse한 문장이 동일하다. data == data[::-1] -- list 말고 바로 string으
'''


import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        preprocessed = self.preprocess(s)
        reversed_str = self.reverseString(preprocessed)
        return preprocessed == reversed_str

    def preprocess(self, s: str) -> str:
        '''문자열을 입력받아서, alnum이 아닌 것들을 없애고 문자 하나씩으로 이루어진 list를 반환한다.'''
        '''
        1) regexp
        2) lowercase 로 모두 바꾸고 -> is lowercase || num 
        '''
        lower_s = s.lower()
        return re.sub('[^a-z0-9]', '', lower_s)

    def reverseString(self, s: str) -> str:
        '''문자열을 입력받으면, 문자열을 뒤집자'''
        return s[::-1]


def test_isPalindrome():
    sol = Solution()
    assert sol.isPalindrome('A man, a plan, a canal: Panama') is True
    assert sol.isPalindrome('race a car') is False


def test_preprocess():
    sol = Solution()
    assert sol.preprocess('AAA') == 'aaa'
    assert sol.preprocess('A A 1') == 'aa1'
    assert sol.preprocess('A A 1 !') == 'aa1'


def test_reverseString():
    sol = Solution()
    assert sol.reverseString('ba') == 'ab'
    assert sol.reverseString('bab') == 'bab'


if __name__ == '__main__':
    test_isPalindrome()
    test_preprocess()
    test_reverseString()
