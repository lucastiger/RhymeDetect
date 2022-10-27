import time
import sqlite3

def takeinput():
    global takeinput_permstorage_id
    global takeinput_permstorage_dict
    takeinput_permstorage_dict = {}
    takeinput_permstorage_id = 0
    tempstorage_list = []
    n = 0
    while n == 0:
        tempstorage_input = input('RhymeBot doesn\'t know much English. Enter a few words! Enter 1 to quit. ')
        time.sleep(1)
        print ('Processing...')
        time.sleep(1)
        if tempstorage_input == '1':
            n = 1
        else:
            tempstorage_list.append(tempstorage_input)
    takeinput_permstorage_dict['takeinput_permstorage_id' + str(takeinput_permstorage_id)]=tempstorage_list
    takeinput_permstorage_id +=1
    print('Thanks! RhymeBot is happy now. ')
    time.sleep(3)
    print('Teleporting you back to the menu...')
    time.sleep(3)
    menu()
    
def checkrhyme():
    global checkrhyme_permstorage_dict_cat1
    global checkrhyme_permstorage_dict_cat2
    global checkrhyme_permstorage_dict_cat3
    global checkrhyme_permstorage_dict_cat4
    global takeinput_permstorage_dict
    global takeinput_permstorage_id
    global checkrhyme_permstorage_keys
    global checkrhyme_permstorage_id
    global checkrhyme_permstorage_vals
    checkrhyme_permstorage_keys = list(takeinput_permstorage_dict.keys())
    checkrhyme_permstorage_vals = list(takeinput_permstorage_dict.values())
    tempstorage_input = input('Enter a word that you want to check if it rhymes with the given data. Enter 1 to quit. ')
    time.sleep(1)
    print('Processing...')
    tempstorage_list = []
    tempstoage_dict = {}
    n = 0
    if tempstorage_input == '1':
        None
    else:
        while n == 0:
            tempstorage_len = len(tempstorage_input)
            for g in range(2, tempstorage_len+1):
                tempstorage_ending = tempstorage_input[(g-2):tempstorage_len]
                for value in takeinput_permstorage_dict.values():
                    tempstorage_listlen = len(value)
                    for i in range(tempstorage_listlen):
                        if (tempstorage_ending in (checkrhyme_permstorage_vals[0])[i]):    
                            n = 1
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
                            print ('Match detected! ')
                            time.sleep(1)
                            print('Analyzing... ')
                            time.sleep(1)
                            print('Position: ', tempstorage_position)
                            print ('Position ID: ', checkrhyme_permstorage_id)                                      
                            print ('Rhyming Part: ', tempstorage_ending)
                            print('matches with' )
                            print (tempstorage_list)                                                                                                               
                            break 
                        elif i == (tempstorage_listlen-1) and g == tempstorage_len:                                                                                                                                                  
                            print('Sorry, no match detected. ')                                                                                                                                                                                
                            n = 1
                            break
                        time.sleep(3)
                        input('Press Enter to continue. ')
                        time.sleep(1.5)
                        print('Teleporting you back to the menu...')
                        time.sleep(3)
                        menu()
                            
                            
def menu():
    print('MENU')
    print('=========================')
    print('Options: ')
    menuinput = ('1. Input words to teach RhymeBot \n '
         '2. Check if a word rhymes with an existing word \n '
         '3. Give feedback on the software \n \n '
         'Your input: ')
    time.sleep(1)
    print('Processing...')
    time.sleep(1.5)
    if menuinput == '1':
        takeinput()
    elif menuinput == '2':
        checkrhyme()
    elif menuinput == '3':
        print('Sorry, this area is under construction. Check back later! ')
        time.sleep(4)
    else:
        print('Sorry, invalid input. ')
        time.sleep(3)
        menu()
        

                                                                                                                    
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
    menu()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
         
         
         
         
       
          
