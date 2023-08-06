from math import floor
from re import finditer, sub

def string_format(string, length=40, paragraph_size=2,space_size=1, force_space=False):
    """
    About:
    Shapes a body of text to match within 80%+ of the
    given length. 
    Adds line breaks after every nth time the line length in a string
    has been met,
    provided that part of the string is a space.
    Also makes paragraphs that fit roughly within the specified length. 
    The function does not guarantee a paragraph after every nth sentance,
    but will try to approximate as best as possible.
    If the length you want is too small to generate paragraphs, you can set force_space to True, 
    which will force a new line at the end of every period.
    """
    string_length = len(string)
    #print(f"string length: {string_length}")
    ratio = string_length // length
    index_jump = floor(0.8 * length) 
    composite_string = ''
    nth_snippet = ''
    index_start = 0
    index_end_non_inclusive = 0
    DEFINITE_END = string_length - 1
    rotate = True
    space = False
    collect_lengths = 0
    collect_turns = 0


    while rotate is True:
        for turn, rotation in enumerate(range(ratio)):
            index_start = index_end_non_inclusive
            index_end_non_inclusive += index_jump
            sample = 0
            while string[index_end_non_inclusive] != " ":
                try:
                    index_end_non_inclusive += 1
                except IndexError:
                    index_end_non_inclusive -= 1
        
            if string[index_end_non_inclusive] == " ":
                nth_snippet = string[index_start:index_end_non_inclusive] # initialized nth_snippet
                collect_lengths += len(nth_snippet)
                collect_turns += 1
            try:
                if (turn + 1) % paragraph_size == 0:
                    space = True
            except ZeroDivisionError:
                    space = False
            
            # PARAGRAPH MODE ON 
                #check and see if paragraph mode is on and sentance is invalid
                # what im doing is checking to see if there is a period in here. 
                # if there is, just cleave off the point at the period.

            if space == True and "." in nth_snippet[0:-1]:  # if its time for a space, and there is a period inside the middle of the snippet
                index_zero = nth_snippet[0]  # current nth_snippet character
                index_zero_value = 0 # index value
                hold_this = ''
                period_index = nth_snippet.find(".")
                if index_zero != " " or "\n":  # include char
                    index_zero_value = 0
                else:
                    index_zero_value = 1  # skip char  ##
                    # check length of rest
                    # if rest <= len, crawl and add some more words
                new_line = nth_snippet[period_index + 2:] 

                hold_this = nth_snippet[index_zero_value:period_index + 1] + ("\n" * 2) + new_line + " " #...end[.] + linebreak + rest // 
                sample += len(hold_this)
                composite_string += hold_this.lstrip() 

            else:  # if not paragraph, just slap it on
                nth_snippet += "\n"
                composite_string += nth_snippet.lstrip()
        


        # CONDITIONS FOR TAIL END #        
        nth_snippet = string[index_end_non_inclusive:DEFINITE_END + 1]  # end of string established
        start = 0
        lenth_of_tail_end = len(nth_snippet)  # if greater than length
        if lenth_of_tail_end < length:  # less than length
            #print(f"debug_end_ less than or equal to length #{nth_snippet}#")
            left_over = length - lenth_of_tail_end
            while nth_snippet[left_over] != " ":
                try: 
                    left_over -= 1
                except IndexError:
                    left_over += 1
            if nth_snippet[left_over] == " ":
                hold_this = nth_snippet[start:left_over + 1] + "\n" + nth_snippet[left_over + 1:]  # split the last nth and add a breakline
            nth_snippet = hold_this
        else:
            #print(f"debug_end_ greater than length #{nth_snippet}#")    # greater than length
            averages = collect_lengths//collect_turns  # will make the tail end fit the rest
            left_over = lenth_of_tail_end - averages  # b/c leftover is larger than len, subtract ave
            while nth_snippet[left_over] != " ":
                try:
                    left_over -= 1
                except IndexError:
                    left_over += 1
            if nth_snippet[left_over] == " ":
                hold_this = nth_snippet[start:left_over + 1] + "\n" + nth_snippet[left_over + 1:]  # split the last nth and add a breakline  # repeat but I can fix this another time
            nth_snippet = hold_this   

        composite_string += nth_snippet.lstrip()
        rotate = False
        if force_space == True:
            pattern = r"\.\s?"
            find_period = sub(pattern, ".\n", composite_string)
            find_question = sub(r"\?\s?", "?\n", find_period)
            find_exclaim = sub(r"!\s?", "!\n", find_question)
            composite_string = find_exclaim
        return composite_string
    # TODO
    # the function has to account for spaces
    # FIX the algorithm that divides the last string into two:
    # check to see if the length of the tail is less than
    # or equal to the specified parameter length. 
    # if so, just leave it alone. 
    # if it is get the length total, attempt to chop off another remainder
    # slap the remaining on, then slap on the remainder.  



#print(string_format("Listen to rich people. It's that simple.", length=50))
#print(string_format("Raw action solves everything. Caution breeds fear.", length=40, paragraph_size=0))


#print(string_format("Listen to rich people. It's that simple.", length=50))


#print(string_format("If you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways.", paragraph_size=2, length=40))

def copy_write_maker(string, paragraph_size=3, space_size=1):
    """
    Info:
    Will write "copyright" style where each sentance is its own line. 
    There is a linebreak after every line.
    
    big_space_size:
    This will attempt to seperate 

    space_size:
    Determines the size of the linebreaks and of the space. 
    1 is default, 2 is double-spaced, ect. Must be an int.
    """
    default_pattern = r"\.\s?|\?\s?|!\s?" # space optional
    matches = finditer(default_pattern, string)
    start = 0
    end = 0
    split = False
    composite_string = ''
    for match_number, match in enumerate(matches):
        start = end
        try:
            if (match_number + 1) % paragraph_size == 0:  # check if every nth line
                split = True
            else:
                split = False
        except ZeroDivisionError:
            pass
        end = match.span()[1]   
        iter_string = string[start:end] # no need for +1 b/c  .span()[1] is already an overshoot of + 1
        if split == True:
            iter_string += ("\n" * 2) * space_size
            split = False
        else:
            iter_string += "\n" * space_size
        composite_string += iter_string
    return composite_string



def push(string, length=25, force_space=False):
    """
    'push' is for when you want to make sure your text conforms without the possibility of an index error. 
    Really helpful for when your incoming string data has huge variance or the strings are very small.
    
    force_space will force a double linebreak at the end of every ? ! or .
    """

    # after nth char look for space - done
    # make that space a \n  - done
    # after every period add \n\n - done

    # post-processing
    # get all \n
    # compare len of \n to \n
    space = False
    char_list = [char for char in string]
    #print(len(string))
    for index, char in enumerate(char_list):  # ( i, c)
        #print(index, char)
        if (index + 1) % length == 0:
            space = True
        if space == True and char == " ":
            char_list[index] = "\n"
            space = False
        if force_space == True:
            if char == ".":
                char_list.insert(index + 1, "\n" * 2)
            elif char == "?":
                char_list.insert(index + 1, "\n" * 2)
            elif char == "!":
                char_list.insert(index + 1, "\n" * 2)
        else:
            pass
    for _ in range(2):
        if char_list[-1] == "\n\n" or char_list[-1] == " " or char_list[-1] == "\n":
            char_list.pop()
    #print(char_list)
    new_string = "".join(char for char in char_list)
    # print(char_list)
    cleanup_space = sub(r"\s\n\n|\n\n\s", "\n\n", new_string) # get rid of space
    new_string = cleanup_space
    return new_string

# TODO
# make a function that takes a long string and makes a dict or list of lists, each list containing a sentance. 
# each list is a segment, of a given length L
# append each list with \n
# compile entire list
# go through every character and wherever there is a ! ? . insert at index + 1 a \n\n if the ! ? . % P == 0: 

# def paragraph_maker(string, length=50, paragraph_length=5, space_size=1):
#     list_of_sentances = []
#     list_of_chars = []
#     char_all = [char for char in string]
#     initial = 0
#     final = 0
#     space = False
#     final_sent = ''
#     for index, char in enumerate(string):
#         if char == r"." or char == r"?" or char == "!":
#             #print(char)
#             final = index
#             list_of_sentances.append([string[initial:final + 1]])
#             initial = final + 1  # account for period inclusive, and space
    
#     for index, sentance in enumerate(list_of_sentances):
#         if index + 1 >= paragraph_length and index % paragraph_length == 0:
#             sentance.append("\n\n")
    
#     for sentance in list_of_sentances:
#         if len(sentance) > 1:
#             if sentance[1] == "\n":
#                 if sentance[0][0] == " ":
#                     sentance[0] = sentance[0][1:]

#     # for sentance in list_of_sentances:
#     #     start = 0
#     #     end = 0
#     #     for internal_string in sentance:
#     #         for index, char in enumerate(internal_string):
#     #             compiled = ''
#     #             if index > length:
#     #                 if index % length == 0:
#     #                     space = True
#     #                 if space == True and char == " ":
#     #                     start = end
#     #                     end = index
#     #                     compiled = internal_string[start:index + 1] + "\n" + internal_string[index + 1:]
#     #                     sentance[0] = compiled
#     #                     space = False
#     #                     break                    

#     final_string_1 = ''
#     final_string_2 = ''        
#     for sentance in list_of_sentances:
#         for internal_string in sentance:
#             final_string_1 += internal_string
    
#     space = False
#     list_again = [char for char in final_string_1]
    
#     for index, char in enumerate(list_again):
#         if index > length and index % length == 0:
#             space = True
#         if space == True and char == " ":
#             list_again[index] = "\n"
#             space = False
    
#     for char in list_again:
#         final_string_2 += char
        
    
    
        

#     #print(final_string_1)
#     print(final_string_2)

    


# test = "Only absolute losers 'suffer' with the inability to strive to become something. Here is another string test. Another sentance! And Another One. Skooby Doobie."

# paragraph_maker(test, paragraph_length=5, length=35)



