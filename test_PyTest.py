import pytest


class TestClass1:

    def test_one(self):
        name = 'John'
        assert 'Joh' in name
        assert 'L' in name
        assert 'oh' in name
        assert 'X' in name

    def test_two(self):
        x = 2
        assert x == 2

    def test_three(self):
        assert self.return_true_1() == True
        assert self.return_false_1() == True, "expected false_1 to be true"
        assert self.return_true_2() == True
        assert self.return_false_2() == True, "expected false_2 to be true"
        


    def return_true_1(self):

        return True

    def return_true_2(self):

        return True

    def return_false_1(self):
        return False

    def return_false_2(self):
        return False