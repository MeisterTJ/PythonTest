# https://www.daleseo.com/python-unittest-testcase/
from unittest import TestCase, main

class MyTests(TestCase):
    # 테스트 메서드의 이름은 반드시 test로 시작을 해야 메서드가 누락되지 않고
    # 정확히 테스트 케이스로 인식이 된다.
    def test_one_plus_two(self):
        self.assertEqual(1 + 2, 3)
        # 테스트 실패시 피드백을 준다.
        #self.assertEqual(1 + 2, 5)

    def test_other_assertions(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 2)
        self.assertGreater(2, 1)
        self.assertLess(1, 2)
        self.assertIn(1, [1, 2])
        self.assertIsInstance(1, int)

    def test_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
        with self.assertRaises(TypeError):
            1 + '2'


# 아래 구문 없어도 전혀 상관없긴 하다.
if __name__ == '__main__':
    main()
