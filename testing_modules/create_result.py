# Generating a file test_result.txt with all test cases and its rendering
# status
from array import *
import sys
import os
import re


def get_result(a, wordlist, res_file_pointer, dirflag, dirname, ref_list, rend_list):
    res_file_pointer.write(
        "<html><head><title>Harfbuzz render results</title>")
    res_file_pointer.write(
        "<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>")
    res_file_pointer.write("</head>")
    res_file_pointer.write("<body>")
    res_file_pointer.write("<table border=1 align='center'>")
    res_file_pointer.write(
        "<tr><th>No.</th><th>Word</th><th>Rendering status</th> \
            <th>Current glyph sequence</th><th>Expected glyph sequence</th>")
    if dirflag:
        res_file_pointer.write("<th align = 'left'>Harfbuzz rendering</th>")
    j = 1
    res = array('i', [])
    for rline in wordlist:
        if rline != "":
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
            if res[j - 1] == 1:
                res_file_pointer.write(
                    "<tr><td align='center' style='color:red'>" + '%d' %
                    (j))
                res_file_pointer.write(
                    "</td><td align='center' style='color:red'>" +
                    rline)
            else:
                res_file_pointer.write("<tr><td align='center'>" + '%d' % (j))
                res_file_pointer.write("</td><td align='center'>" + rline)
            if res[j - 1] == 1:
                res_file_pointer.write(
                    "</td><td align='center' style='color:red'>No")
            else:
                res_file_pointer.write("</td><td align='center'>Yes")
            res_file_pointer.write("</td>")
            if res[j-1] == 1:
                res_file_pointer.write("<td align='center' style='color:red'>")
                for i in rend_list[k]:
                    res_file_pointer.write(i)
                    if rend_list[k].index(i) + 1 != len(rend_list[k]):
                        res_file_pointer.write(',')
                correct_renderings = re.sub(r";", " or ", ref_list[k])
                res_file_pointer.write("</td><td align='center' style='color:red'>" + correct_renderings)
            else:
                res_file_pointer.write("<td align='center'>")
                for i in rend_list[k]:
                    res_file_pointer.write(i)
                    if rend_list[k].index(i) + 1 != len(rend_list[k]):
                        res_file_pointer.write(',')
                res_file_pointer.write("<td align='center'>Same")
            if dirflag:
                res_file_pointer.write(
                    "<td align='left'><img src='hb_images/" + '%d' %
                    (j) + ".png' ></td>")
            j = j + 1
            res_file_pointer.write("</tr>")
    res_file_pointer.close()
    return
