import random

def pick_words():
    with open('triangle_word_list.txt') as f:
        valid_triangles_raw = f.readlines()

    words = valid_triangles_raw[random.randint(0,len(valid_triangles_raw)-1)].strip().split('|')
    subst = []
    #words = ['boarding', 'backboard', 'backing']
    for i in range(1,len(words[0])):
        #split words 2 and 3
        if words[1].find(words[0][:i]) >= 0 and words[2].find(words[0][i:]) >= 0 or words[1].find(words[0][i:]) >= 0 and words[2].find(words[0][:i]) >= 0:
            subst.append([words[0][:i], words[0][i:]])
    
    subst_w1 = subst[0]
    if len(subst) > 1:
        #print('too many splits!!')
        for i in subst:
            if words[1].replace(i[0],'') == words[2].replace(i[1],'') or words[1].replace(i[1],'') == words[2].replace(i[0],''):
                subst_w1 = i
                break
    if words[1].find(subst_w1[0]) != -1:
        subst_other = words[1][len(subst_w1[0]):] if words[1].find(subst_w1[0]) == 0 else words[1][:words[1].find(subst_w1[0])]
        substrings = [subst_w1[1]] + [subst_w1[0]] + [subst_other]
    else:
        subst_other = words[1][len(subst_w1[1]):] if words[1].find(subst_w1[1]) == 0 else words[1][:words[1].find(subst_w1[1])]
        substrings = [subst_w1[0]] + [subst_w1[1]] + [subst_other]
    #subst_w1.insert(1,subst_other)
    #substrings = subst_w1 + [subst_other]
    return substrings, words

#for word in words:
#    goog.search(word)
#tri.make_triangle(words[0], words[1], words[2], substrings[0], substrings[1], substrings[2])


