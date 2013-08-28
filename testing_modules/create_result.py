#Generating a file test_result.txt with all test cases and its rendering status
from array import *
import sys


def get_result(a, wordlist, res_file_pointer):
    res_file_pointer.write("Number\tWord\t\t\tRendering status\n\n")
    j = 1
    res = array('i', [])
    for rline in wordlist:
        flag = 0
        k = wordlist.index(rline)
        for i in a:
            if k == i:
                flag = 1
                a.remove(i)
                break
            if flag:
                res.insert(k, 1)
            else:
                res.insert(k, 0)
            res_file_pointer.write('%d' % (j))
            if res[j - 1] == 1:
                res_file_pointer.write('\t' + rline + '\t\t\t' + "No" + '\n')
            else:
                res_file_pointer.write('\t' + rline + '\t\t\t' + "Yes" + '\n')
            j = j + 1
    res_file_pointer.close()
    return
