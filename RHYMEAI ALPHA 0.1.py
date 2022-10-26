import time

def takeinput():
    global takeinput_permstorage_id
    global takeinput_permstorage_dict
    takeinput_permstorage_dict = {}
    takeinput_permstorage_id = 0
    tempstorage_list = []
    n = 0
    while n == 0:
        tempstorage_input = input('RhymeBot doesn\'t know much English. Enter a few words! Enter 1 to quit. ')
        if tempstorage_input == '1':
            n = 1
        else:
            tempstorage_list.append(tempstorage_input)
    takeinput_permstorage_dict['takeinput_permstorage_id' + str(takeinput_permstorage_id)]=tempstorage_list
    takeinput_permstorage_id +=1
    
def checkrhyme():
    global checkrhyme_permstorage_dict_cat1      #cat 1 is 50% and above rhyme
    global checkrhyme_permstorage_dict_cat2      #cat 2 is 40% and sub rhyme
    global checkrhyme_permstorage_dict_cat3      #cat 3 is 25% and sub rhyme
    global checkrhyme_permstorage_dict_cat4      #cat 4 is 10% and sub rhyme
    global takeinput_permstorage_dict
    global takeinput_permstorage_id
    global checkrhyme_permstorage_keys
    global checkrhyme_permstorage_id
    global checkrhyme_permstorage_vals
    checkrhyme_permstorage_keys = list(takeinput_permstorage_dict.keys())
    checkrhyme_permstorage_vals = list(takeinput_permstorage_dict.values())
    tempstorage_input = input('Enter a word that you want to check if it rhymes with the given data. Enter 1 to quit. ')
    tempstorage_list = []
    tempstoage_dict = {}
    n = 0
    if tempstorage_input == '1':
        None
    else:
        while n == 0:
            tempstorage_len = len(tempstorage_input)
            for g in range(2, tempstorage_len+1):
                tempstorage_ending = tempstorage_input[(g-2):tempstorage_len]           #semantic - does not include full word, change?
                                                                                        #changed
                                                                                        ##
                                                                                        #no match for mow to low, lien 61 responsible, fixed, check line 38 (modified)
                                                                                        #please test
                                                                                        #SECTION FIXED
                for value in takeinput_permstorage_dict.values():
                    tempstorage_listlen = len(value)
                    for i in range(tempstorage_listlen):
                        if (tempstorage_ending in (checkrhyme_permstorage_vals[0])[i]):                             #cannot identify if sliced input is input is a value
                            n = 1                                                                                   #included in a value; can only identify if sliced
                                                                                                                    #fix in progress
                                                                                                                    ##
                                                                                                                    #list index out of range error, fixed confirmed
                                                                                                                    ##
                                                                                                                    #infinited loop, please identify
                                                                                                                    #debugging in progress
                                                                                                                    ##
                                                                                                                    ##SECTION FIXED
                            tempstorage_list = [(checkrhyme_permstorage_vals[0])[i]]
                            while i < (tempstorage_listlen-1):
                                if (tempstorage_ending in (checkrhyme_permstorage_vals[0])[i+1]):
                                    tempstorage_list.append(checkrhyme_permstorage_vals[0][i+1])
                                    i += 1
                                else:
                                    None
                                    i += 1
                            tempstorage_position = checkrhyme_permstorage_vals.index(value)
                            checkrhyme_permstorage_id = checkrhyme_permstorage_keys[tempstorage_position]
                            print ('match')
                            print('position =', tempstorage_position)
                            print ('position id =', checkrhyme_permstorage_id)                                      #add cat identification
                            print ('rhyme part is', tempstorage_ending)
                            print('matches with' )
                            print (tempstorage_list)
                                                                                                                    #semantic - when joe, mow, low
                                                                                                                    #values and sow inputted,
                                                                                                                    #match result is ['mow', 'ow']
                                                                                                                    ##SECTION FIXED
                                                                                                                    
                                                                                                                    
                                                                                                                    #add all rhyming, not just one
                                                                                                                    #
                            break 
                        elif i == (tempstorage_listlen-1) and g == tempstorage_len:                                 #responsible for line 39
                                                                                                                    #SECTION FIXED
                            print('no match')                                                                       #infinitely prints this, debugging
                                                                                                                    #fixed, testing
                                                                                                                    #SECTION FIXED
                            n = 1
                            break
                            
                            
def menu():
    print('=========================')
                                                                                                                    
def run():
    print('EVOLVEAI INTRODUCES')
    time.sleep(5)
    print('RHYMEAI')
    time.sleep(3)
    print('SPONSERED BY LUCAS AIRLINES')
    time.sleep(5)
    print('ALL RIGHTS RESERVED TO EVOLVEAI COPYRIGHT 2022')
    time.sleep(5)
    print('Hey there! I\'m Rhymebot! ')
    time.sleep(3)
    print('Don\'t worry, I\'m friendly. ')
    time.sleep(3)
    print('How about you prove you are a human? I like humans. ')
    time.sleep(3)
    input('PROMPT: Press the Enter Key to prove to RhymeBot that you are a human. ')
    time.sleep(2)
    print('Great! I love humans! ')
    time.sleep(2)
    print("Why don't I show you around? Press the Enter Key again to get to the menu, where you'll find stuff to do! ")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
         
         
         
         
       
          
