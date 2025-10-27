def uncommon_from_sentences(s1, s2):
    list_s1 = s1.split(" ")
    list_s2 = s2.split(" ")
    list_s1.extend(list_s2)
    list_total = list_s1 #the tests are passing now. list_s1 now has the extended list, for some reason was not registering in list total
    total_dict = dict_helper(list_total) 
    uncommon_list = []
    for word, count in total_dict.items():
        if count == 1:
            uncommon_list.append(word)
    return uncommon_list        

  
# all the tests passed? 
#ok
#thank you so much for trying that 
#all tests in test_original.py
#good job! nice working with you guys
#youre welcome! thanks for your help too!


def dict_helper(list_total):
    dict_words = {}
    for word in list_total:
        if word in dict_words.keys():
            dict_words[word] += 1
        else: 
            dict_words[word] = 1


    return dict_words
