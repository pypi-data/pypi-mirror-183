if __name__ == "__main__":
    import time
    import re

    def space():
        print('\n' * 3)
    test_string = "Python does not currently have an equivalent to scanf(). Regular expressions are generally more powerful, though also more verbose, than scanf() format strings. The table below offers some more-or-less equivalent mappings between scanf() format tokens and regular expressions."
    bible_string = "1:1 In the beginning God created the heaven and the earth. 1:2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters."

    #rec = time.time_ns()
    # test_1 = print(string_format(test_string, length=50))
    #print(time.time_ns() - rec)

    # pattern = r"\.\s?|\?\s?|!\s?"  # match is (before,on) -> index of exact would be str[on -1]
    # match = re.finditer(pattern, test_string)
    # for num, item in enumerate(match):
    #     print(num)
    #     print(item.group(), item.groups(), item.span())
    # print(len(test_string), test_string[275], test_string[274])
    # first_sent = test_string[0:55 + 1]
    # print(f"{first_sent} {'x' in first_sent}")

    # bible_paragraph = paragraph_maker(bible_string, paragraph_size=3)
    # print(bible_paragraph)
    bible_format = string_format(bible_string, paragraph_size=2, length=40)
    print(bible_format)