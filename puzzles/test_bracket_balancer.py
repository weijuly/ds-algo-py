import unittest


def balance(string):
    stack = []
    for c in string:
        if c in ['[', '(', '{']:
            stack.append(c)
        if c in [']', ')', '}']:
            if not stack:
                return 'NO'
            if (stack[-1] == '(' and c == ')') or (stack[-1] == '{' and c == '}') or (stack[-1] == '[' and c == ']'):
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


class Test(unittest.TestCase):
    def test_balance(self):
        self.assertTrue(balance('(())'))
        self.assertTrue(balance('({([])})'))
        self.assertFalse(balance('({[(])})'))
        self.assertTrue(balance(''))


if __name__ == '__main__':
    unittest.main()
