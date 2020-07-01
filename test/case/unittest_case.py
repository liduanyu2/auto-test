#coding=utf-8
import unittest
class FirstCase1(unittest.TestCase):

    def setUp(self):
        print("前置")

    def tearDown(self):
        print("后置")

    def test1(self):
        print("1")
    def test2(self):
        print("2")

if __name__=="__main__":
    unittest.main()