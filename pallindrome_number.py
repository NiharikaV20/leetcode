# -*- coding: utf-8 -*-
"""pallindrome number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ED7QNQQVTLrbg_dW0o6oIrVtdaDH2sfZ
"""

#Pallindrome number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False