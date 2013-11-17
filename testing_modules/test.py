import sys
from array import *


def ref_parse(ref_pointer):
    # Parses the reference file and check for mutiple renderings.
    reference_file = ref_pointer.read()
    ref_list = []
    ref_lines = reference_file.replace('[', '').replace(']', '')
    clean_file = ref_lines.split('\n')
    glyph_array = array('i', [])
    optional_list = []
    multiple_glyphs = []
    # Checking for multiple correct renderings, i.e checking for ';'
    for aline in clean_file:
        if aline.find(';') != -1:
            optional_list = []
            # glyph array has index of words with multiple renderings
            glyph_array.append(clean_file.index(aline))
            opt_list = aline.split(';')
            for a_glyph in opt_list:
                oneword = a_glyph.split(',')
                optional_list.append(oneword)
            multiple_glyphs.append(optional_list)
        aword = aline.split(',')
        ref_list.append(aword)
    return glyph_array, ref_list, multiple_glyphs, clean_file


def rendering_parse(rend_pointer):
    # parses the rendered output and make a list hb_out
    rendered_file = rend_pointer.read()
    rend_list = []
    rend_lines = rendered_file.replace('[', '').replace(']', '')
    rend_file_lines = rend_lines.split('\n')
    for line in rend_file_lines:
        each_name = line.split('|')
        rend_list.append(each_name)
    hb_out = []
    for x in rend_list:
        n = []
        for y in x:
            n.append(y.split('=')[0])
        hb_out.append(n)
    return hb_out, rend_file_lines


def render_test(test_case, ref_list, hb_out):
    # compares rendered output and reference glyphs
    result_list = []
    wordlist = []
    result_list = [i for i, j in zip(ref_list, hb_out) if i != j]
    if result_list == []:
        print "\nNo rendering problems found!"
        sys.exit()
    else:
        f = 1
        a = array('i', [])
        for word in result_list:
            d = ref_list.index(word)
            a.append(d)
    if test_case:
        wordfile_content = test_case.read()
        wordlist = wordfile_content.split('\n')
        test_case.close()
    return a, wordlist, f


def multiple_render_check(a, glyph_array, multiple_glyphs, hb_out):
   # test if any one of multiple renderings is correct
    common_words_index = list(set(a).intersection(set(glyph_array)))
    common_words_index = array('i', sorted(common_words_index))
    for each_term, value in zip(multiple_glyphs, common_words_index):
        flag = 0
        for one_glyph in each_term:
            if one_glyph == hb_out[value]:
                flag = 1
                break
        if flag == 1:
            a.remove(value)
    return a


def main(ref_pointer, rend_pointer, test_case):
    glyph_array, ref_list, multiple_glyphs, ref_file_lines = ref_parse(ref_pointer)
    hb_out, rend_file_lines = rendering_parse(rend_pointer)
    a, wordlist, f = render_test(test_case, ref_list, hb_out)
    a = multiple_render_check(a, glyph_array, multiple_glyphs, hb_out)
    return a, wordlist, f, ref_file_lines, hb_out
