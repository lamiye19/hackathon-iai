#


def autocompletion(dictionnary, words):
    print(dictionnary)
    print(words)
    for word in words:
        the_word = word
        tmp_word = word
        cost = 0
        for dic in dictionnary:
            char_added = 0
            char_deleted = 0
            char_replaced = 0
            char_switched = 0
            if dic.find(word[0]) != -1:
                char_deleted = dic.index(word[0])
                sub_dic = [dic[i] for i in range(len(dic)) if i > char_deleted]

                if len(word) == 1:
                    char_deleted = len(sub_dic)
                else:
                    if word[1] == dic[char_deleted - 1]:
                        char_deleted = char_deleted - 1
                        char_switched = char_switched + 1

                    for i in range(1, len(word)-1):
                        for j in range(len(sub_dic)-1):
                            if word[i] != sub_dic[j]:
                                if word[i] == sub_dic[j+1]:
                                    char_added = char_added + 1
                                elif word[i+1] == sub_dic[j+1]:
                                    char_replaced = char_replaced + 1
                                elif word[i] == sub_dic[j + 1]:
                                    char_deleted = char_deleted + 1
                                elif word[i] == sub_dic[j+1] and word[i-1] == sub_dic[j]:
                                    char_switched = char_switched + 1
                        sub_dic = sub_dic[1:]

                sub_cost = 2*(char_added + char_deleted) + 3*(char_replaced + char_switched)

                if len(dic)-char_deleted+char_added == len(word):
                    cost = sub_cost
                    tmp_word = dic
                if cost == sub_cost:
                    tmp_word = dic if dic < the_word else tmp_word

                the_word = tmp_word
        print("\t"+word+"\t->\t"+the_word+": "+str(cost))

if __name__ == '__main__':
    dictionnary1 = ["algorithme", "ahgorithme", "arbre", "barbe", "globe", "orbe"]
    words1 = ["rythme", "arbore", "logarithme", "lobe", "robe"]

    print("*** Test 1")
    autocompletion(dictionnary1, words1)

    dictionnary2 = ["bulbizarre", "herbizarre", "carapuce", "salameche"]
    words2 = ["carteapuce", "salamuce", "saramuce", "blubizarre", "herbebizarre", "xxxbizarre"]

    print("*** Test 2")
    autocompletion(dictionnary2, words2)

    dictionnary3 = ["ba", "abbab", "bbbaa", "baab", "bb", "bb", "bbaaabb", "bb", "bbaabba", "bbb"]
    words3 = ["abbbbbb", "aaab", "bbab", "b", "baabbab", "bbabbbba", "babbbb", "bbbb", "b"]

    print("*** Test 3")
    autocompletion(dictionnary3, words3)