import exercise1 as ex1
import exercise2 as ex2
import exercise3 as ex3
import exercise4 as ex4
import numpy as np
import sys, ast, os

with open("tmp.txt","w") as f:
  f.write("1,2,3\n")
  f.write("1.5,{2.5}\n")
  f.write("1.5,3.5,5.5\n")
  f.write("5.5\n")
  f.write("[3.5,2.5]\n")
  f.write("1.5,2.5\n")
  f.write("1.5,2.5\n")

my_stdin = sys.stdin
sys.stdin = open('tmp.txt','r')

a = ex1.input_row(0,"prompt1> ")
if len(a) != 3 or a[0] != 1 or a[1] != 2 or a[2] != 3:
  print("#### ERROR ####")

a = ex1.input_row(2,"prompt2> ")
if len(a) != 2 or a[0] != 1.5 or a[1] != 2.5:
  print("#### ERROR ####")

a = ex1.input_row(0,"prompt3> ")
if len(a) != 2 or a[0] != 1.5 or a[1] != 2.5:
  print("#### ERROR ####")

sys.stdin.close()
sys.stdin = my_stdin
input("\n*********************END OF TEST for exercise1.py********************")

with open("tmp.txt","w") as f:
  f.write("1,2\n{2,-3}\n")
  f.write("3,4\n")
  f.write("1,3,5\n")
  f.write("2,4,6\n[7],3,9\n")
  f.write("7,8,9\n")

sys.stdin = open('tmp.txt','r')

a = ex2.input_matrix()
if len(a) != 2 or a[0,0] != 1 or a[0,1] != 2 or a[1,0] != 3 or a[1,1] != 4:
  print("#### ERROR ####")

a = ex2.input_matrix()
if len(a) != 3 or a[0,0] != 1 or a[1,1] != 4 or a[2,2] != 9:
  print("#### ERROR ####")

sys.stdin.close()
sys.stdin = my_stdin
input("\n*******************END OF TEST for exercise2.py*****************\n")

a = np.array([[1,3,5,7],[2,4,6,8],[9,7,5,3],[8,6,4,2]])
ex3.write_matrix(a,"tmp.csv")
with open("tmp.csv","r") as f:
  lines = f.readlines()
b = []
for t in lines:
  b.append(ast.literal_eval(t.strip()))

if len(b) != 4 or b[0][0] != 1 or b[1][1] != 4 or b[2][2] != 5 or b[3][3]!=2:
  print("#### ERROR ####")

input("\n*******************END OF TEST for exercise3.py*****************\n")

b = ex4.read_matrix("tmp.csv")

if len(b) != 4 or b[0][0] != 1 or b[1][1] != 4 or b[2][2] != 5 or b[3][3]!=2:
  print("#### ERROR ####")

input("\n*******************END OF TEST for exercise4.py*****************\n")

import matrix_io as mio

with open("tmp.txt","w") as f:
  f.write("1,2,3\n")
  f.write("1.5,{2.5}\n")
  f.write("1.5,3.5,5.5\n")
  f.write("5.5\n")
  f.write("[3.5,2.5]\n")
  f.write("1.5,2.5\n")
  f.write("1.5,2.5\n")

sys.stdin = open('tmp.txt','r')

a = mio.input_row(0,"prompt1> ")
if len(a) != 3 or a[0] != 1 or a[1] != 2 or a[2] != 3:
  print("#### ERROR ####")

a = mio.input_row(2,"prompt2> ")
if len(a) != 2 or a[0] != 1.5 or a[1] != 2.5:
  print("#### ERROR ####")

a = mio.input_row(0,"prompt3> ")
if len(a) != 2 or a[0] != 1.5 or a[1] != 2.5:
  print("#### ERROR ####")

sys.stdin.close()

with open("tmp.txt","w") as f:
  f.write("1,2\n{2,-3}\n")
  f.write("3,4\n")
  f.write("1,3,5\n")
  f.write("2,4,6\n[7],3,9\n")
  f.write("7,8,9\n")

sys.stdin = open('tmp.txt','r')

a = mio.input_matrix()
if len(a) != 2 or a[0,0] != 1 or a[0,1] != 2 or a[1,0] != 3 or a[1,1] != 4:
  print("#### ERROR ####")

a = mio.input_matrix()
if len(a) != 3 or a[0,0] != 1 or a[1,1] != 4 or a[2,2] != 9:
  print("#### ERROR ####")

sys.stdin.close()

a = np.array([[1,3,5,7],[2,4,6,8],[9,7,5,3],[8,6,4,2]])
mio.write_matrix(a,"tmp.csv")
with open("tmp.csv","r") as f:
  lines = f.readlines()
b = []
for t in lines:
  b.append(ast.literal_eval(t.strip()))

if len(b) != 4 or b[0][0] != 1 or b[1][1] != 4 or b[2][2] != 5 or b[3][3]!=2:
  print("#### ERROR ####")

b = mio.read_matrix("tmp.csv")

if len(b) != 4 or b[0][0] != 1 or b[1][1] != 4 or b[2][2] != 5 or b[3][3]!=2:
  print("#### ERROR ####")

sys.stdin = my_stdin
input("\n*******************END OF TEST for exercise5.py*****************\n")

s = os.getcwd()
if ( s.find("/lab3") >= 0 ):
  os.chdir("..")

with open("lab3/exercise7.txt","w") as f:
  f.write(" 3,  1, -1\n")
  f.write(" 2, -4, -2\n")
  f.write("-1,  2, -3\n")
  f.write("0,  2, -9\n")





