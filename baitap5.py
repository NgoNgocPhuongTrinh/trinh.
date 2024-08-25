# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:00:17 2024

@author: trinh
"""

chuoi = "Dai hoc Quoc gia, Khu pho 6, P. Linh Trung, Q. Thu Duc, Tp. Ho Chi Minh"
chuoitach = chuoi.split(",")
print("1. Tách thành các sub-string:")
print("\n".join(chuoitach))

print("2. Tách thành các sub-tring:")
print(chuoitach[0])
print(chuoitach[1])
print(chuoitach[2].replace("P. ", ""))
print(chuoitach[3].replace("Q. ", ""))
print(chuoitach[4].replace("Tp. ",""))
                