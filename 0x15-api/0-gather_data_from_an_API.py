#!/usr/bin/python3
import json, requests

empID = eval(input("Your employee ID? "))
empName = "Felicia"
nDone = 1
nTotal = 5
title = "testTitle"
print("Employee {} is done with tasks({}/{}):".format(empName, nDone, nTotal))
for i in range(nTotal):
    print("{}".format(title))
