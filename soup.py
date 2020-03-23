import csv
#-*- coding: utf-8 -*-
import os
import pandas as pd
print (os.getcwd())
print (os.listdir())


#f=open("C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\son\\subject.csv")
#f=open("C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\son\\subject.csv",encoding="utf-8")

#f=open("C:\\Users\\tlfqk\\PycharmProjects\\untitled3\\son\\서울교통공사_혼잡도_20171231.csv")

data_seoul=pd.read_csv("data_seoul.csv",encoding ='cp949')

