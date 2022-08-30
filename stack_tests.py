# Stack Unittests [Data Structures]
# Joshua Estrada

import unittest
from stack_array import Stack
# from stack_linked import Stack


class TestLab2(unittest.TestCase):
    def test_standard(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)

    def test_full_stack(self):
        stack = Stack(5)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(), 5)
        self.assertRaises(IndexError, stack.push, 0)

    def test_empty_stack(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        self.assertRaises(IndexError, stack.pop)

    def test_pop(self):
        stack = Stack(10)
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        for i in range(10):
            stack.push(i + 1)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(), 10)
        stack.pop()
        self.assertEqual(stack.pop(), 9)
        self.assertFalse(stack.is_full())
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 8)
        self.assertEqual(stack.peek(), 8)

    def test_peek(self):
        stack = Stack(1)
        self.assertRaises(IndexError, stack.peek)
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_none(self):
        stack = Stack(3)
        stack.push(None)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.size(), 1)
        stack.pop()
        self.assertTrue(stack.is_empty())


if __name__ == '__main__':
    unittest.main()
