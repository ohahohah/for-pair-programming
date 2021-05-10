'''
A. order 가 있는 케이스
- input[0][0] = 1
- input[1][0] == input[0][0] : input[0][1] 다음에 input[1][1] 온다
- input[1][0] =! input[0][0] : input[0][0] 다음에 input[1][0] 온다

- input[i][0] 를 순서로 만든다.
  'w', ' w', 'e', 'r'
  'w', 'e', 'r'
  망함 - 'w', 'e', 'a' : 'r' 이 없다!

- input[i][1] 를 순서로 만든다.
'r' 'r' 'r' 't' 'f'
'r' 't' 'f'

['w', 'e', 'r', 't', 'f']

'wrt' --> ['w', 'r', 't']
'wrf' ------> ['w', 'r', 't' ..f..?

't' -> 'f'


['w' -> 'r' -> 't']

wrt
wr.. f

trie tree


{}
{'w': {'r': {'t'


d['w']['r']['t']
d['w']['r']['f']


'''



from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        pass


def test_alienOrder():
    sol = Solution()
    assert sol.alienOrder(['wrt', 'wrf', 'er', 'ett', 'rftt']) == 'wertf'
    assert sol.alienOrder(["z", "x"]) == "zx"
    assert sol.alienOrder(["z", "x", "z"]) == ""


if __name__ == '__main__':
    test_alienOrder()
