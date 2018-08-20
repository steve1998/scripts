import sys
import os
# get the directory path of this file.
dirname = os.path.dirname(os.path.abspath(__file__))
# get the root of this child directory.
rootdir = os.path.dirname(dirname)
sys.path.append(rootdir)

import calculator

class TestCalculatorClass(object):

    firstNumber = 10
    secondNumber = 5.5

    def test_add(self):

        # arrange
        expectedResult = 15.5

        # act 
        actualResult = calculator.add(self.firstNumber, self.secondNumber)
        
        # assert
        assert expectedResult == actualResult

    def test_min(self):

        # arrange
        expectedResult = 4.5

        # act 
        actualResult = calculator.min(self.firstNumber, self.secondNumber)
            
        # assert
        assert expectedResult == actualResult

    def test_div(self):

        # arrange
        expectedResult = 1.818181818

        # act 
        # checks up to 9 decimal place accuracy
        actualResult = round(calculator.divide(self.firstNumber, self.secondNumber), 9)
            
        # assert
        assert expectedResult == actualResult

    def test_multiply(self):
        # arrange
        expectedResult = 55

        # act 
        actualResult = calculator.multiply(self.firstNumber, self.secondNumber)

        # assert
        assert expectedResult == actualResult
