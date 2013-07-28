#Generating a file test_result.txt with all test cases and its rendering status
from array import *
import sys
def get_result(a, wordlist,ch, fontfile):
  test_file = open("test_result.txt", 'w')
  test_file.write("Number\tWord\t\t\tRendering status\n\n")
  j = 1
  res = array('i', [])
  for rline in wordlist:
    flag = 0
    k =  wordlist.index(rline)
    for i in a:
      if k == i:
        flag = 1
        a.remove(i)
        break
    if flag:
      res.insert(k, 1)
    else:
      res.insert(k, 0)
    test_file.write('%d' % (j))
    if res[j - 1 ] == 1:
      test_file.write('\t'+ rline + '\t\t\t' + "Rendering is wrong" + '\n')
    else:
      test_file.write('\t' + rline + '\t\t\t' + "Rendering is correct" + '\n')
    j = j + 1
  test_file.close()
  return 0

