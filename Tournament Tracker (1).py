#!/usr/bin/env python
# coding: utf-8

# In[21]:


import json
def get_valid_int():
    valid_guess = 0
    while valid_guess == 0:
        n=input()
        valid_guess=1 #first assume guess is valid
        for char in n:#make sure all chars in word are letters
            if char.isdigit()!=1:
                print('\nInvalid number inputted >:(')
                valid_guess=0 #non-digit entry detected,entry
                break
    return n
    
def new_tournament():
    '''
    This function initiates a new dictionary to store a tournament participant's names.
    return: empty dictionary of user speficied length, tournament name
    rtype: dictionary, string
    '''  
    print("\nCreating new Tournament")
    print("=========================")
    print("Enter the number of tournament slots.")
    n= get_valid_int()
    name=input("What is the tournament name?:")

    #initiate a dictionary that's the same length as the number of participants using for loop.
    tournamentDict={}
    for i in range(int(n)):
        tournamentDict[str(i+1)]=None
    #keys are slot numbers, values are empty strings
    return tournamentDict, name


def sign_up(tournamentDict):
    '''
    This function prompts the user for a participant name and desired starting slot and stores the name 
    in the corresponding dictionary key. If the starting slot is unavailable, the function will ask the user
    to pick another slot. 
    
    param tournamentDict: Dictionary that has slot values as the key, and participant's name as the value.
    return               :None
    '''
    print("\nParticipant Sign Up")
    print("=====================")
    name=input("What is the participant's name (first,last):").strip().lower()
    success=0
    while success==0:
        if None in tournamentDict.values():
            hi=0
        else:
            print("\nAll Slots Full\n")
            break
        
        print("Enter a desired starting slot[1-%i]" % len(list(tournamentDict.keys())))
        
        slot= get_valid_int()
        if tournamentDict[slot]!=None:
            print("This slot is taken")
        else:
            tournamentDict[slot]=name
            success=1
            print("Success:")
            print("%s is signed up in starting slot #%s." %(name,slot))

def cancel_sign_up(tournamentDict):
    '''
    This function prompts the user for a participant name and existing starting slot and deletes the name 
    from the corresponding dictionary key. If the participant given is not in the slot given, the function will
    tell the user the participant is not in that slot.
    
    param tournamentDict: Dictionary that has slot values as the key, and participant's name as the value.
    return               :None
    '''
    print("\nParticipant Cancellation")
    print("===================")
    success=0
    while success==0:
        name=input("What is the participant's name:(Enter 0 to exit)").strip().lower()
        if name == '0':
            break
        else:
            print("Enter the participant's starting slot[1-%i]" % len(list(tournamentDict.keys())))
            slot= get_valid_int()
            
        if tournamentDict[slot]!=name:
            print(f"Error {name} is not signed up for this starting slot.")
        else:
            tournamentDict[slot]=None
            success=1

def view_participants(tournamentDict):
    '''
    This function prints all tournament slots and their corresponding participant.
    
    param tournamentDict: Dictionary that has slot values as the key, and participant's name as the value.
    return               :None
    '''
    print("\nView Participants")
    print("=================")
    #split names into first and last
    first=[]
    last=[]
    names=tournamentDict.values()
    for name in names:
        try:
            storage=name.split(',')
            last.append(str(storage[1]))
            first.append(str(storage[0]))
        except:
            first.append(None)
            last.append(str(storage[0]))
    
    last_sort=last.copy()
    #sort alphabetically by last name
    last_sort.sort()
    slots=list(tournamentDict.keys())
    print("Starting Slot : Last Name, First Name")
    for name in last_sort:
        index= last.index(name)
        if last[index]!=None:
            print("%s : %s , %s" %(slots[index],last[index],first[index]))
    print("\nEmpty Slots:")   
    for key in tournamentDict.keys():
        if tournamentDict[key]==None:
            print(key)
        
            

def single_search(tournamentDict):
    '''
    This function prompts the user for a participant's name and prints their starting position if the participant exists.
    
    param tournamentDict: Dictionary that has slot values as the key, and participant's name as the value.
    return               :none
    '''
    search= input("Enter user's name(first,last)").strip().lower()
    names=list(tournamentDict.values())
    slots=list(tournamentDict.keys())
    print("\nSingle Participant Search")
    print("===========================")
    found=0
    for i in range(len(names)):
        if names[i]==search:
            print("%s is in slot %s" %(search, slots[i] ))
            found=1
    if found==0:
        print("Participant not found. Make sure you format their name the way it was entered")
        
def save_tournament(tournamentDict, name):
    '''
    saves current tournament dictionary to file 
    
    param tournamentDict: Dictionary that has slot values as the key, and participant's name as the value.
    param tournamentName: Tournament name
    
    return: none
    '''
    jsonObject= json.dumps(tournamentDict,indent=4)
    filePath= name+'.json'
    with open(filePath, "w") as outfile:
        outfile.write(jsonObject)
    print("Tournament Data Successfully Saved")
    
def load_tournament():
    '''
    Loads tournament data from json file if tournament exists.
    returns: tournament data stored in dictionary, tournament name
    rtype: dictionary, string
    '''
    print("Loading Tournament")
    print("==================")
    success=0
    while success==0:
        name=input("What is the name of the tournament you want data loaded for(Enter 0 to exit)").strip()
        fileName=name+'.json'
        try:
            f= open(fileName, 'r')
            #load dictionary object in file
            tournamentDict= json.load(f)
            print("%s was successfully loaded." % fileName)
            f.close()
            success=1
        except:
            print("Invalid tournament name. Make sure you enter the tournament name exactly as it was created")
            
        if name=='0':
            success=1
            
    return tournamentDict, name


# In[ ]:





# In[23]:


#6 states control the flow of the application's functionalities (next state is set by user selections):
#initilialize next 
next_state= 0 

#while loop that terminates and loops the application
while next_state != 9:

    if next_state==0:
        #0:Display Main Menu
        #   print(Main(Menu))
        print("\nWelcome to Tournaments R Us")
        print("Participant Menu")
        print("===========================")
        print("1.) Sign Up")
        print("2.) Cancel Sign Up")
        print("3.) View Participants")
        print("4.) Search for single participant")
        print("5.) Save Current Tournament to File")
        print("6.) Create new tournament")
        print("7.) Load existing Tournament from File")
        print("8.) View Tournament Name")
        print("Enter any other number to exit.\n")
        #   Get user's menu selection 
        print("Enter Menu Selection")
        next_state= get_valid_int()
        
    elif int(next_state)==1:#1Sign Up
        try:
            sign_up(tournamentDict)
        except:
            print("\nNo tournament data loaded.\n")
        next_state=0
            
    elif int(next_state)==2:#2Cancel Sign Up
        try:
            cancel_sign_up(tournamentDict)
        except:
            print("\nNo tournament data loaded.\n")
        next_state=0

    elif int(next_state)==3:#View Participants
        try:
            view_participants(tournamentDict)
        except:
            print("\nNo tournament data loaded.\n")
        next_state=0
    
    elif int(next_state)==4: #search for a single participant
        try:
            single_search(tournamentDict)
        except:
            print("\nNo tournament data loaded.\n")
        next_state=0

    elif int(next_state)==5: #5:Save Current Tournament to File
        try:
            save_tournament(tournamentDict,name)
        except:
            print("\nNo tournament data loaded.\n")
        next_state=0

    elif int(next_state) == 6: #6:Create New Tournament dictionary
        tournamentDict,name= new_tournament()
        next_state=0

    elif int(next_state)==7: #7:Load New Tournamet from File
        
        tournamentDict, name= load_tournament()
        next_state=0

#8:Print tournament name
    elif int(next_state) == 8:
        try:
            print("Tournament Name:",name)
        except:
            print("\nNo tournament data loaded\n")
        next_state=0

#9:Exit application
    else:
        print("Exiting Program")
        next_state=9


# In[ ]:





# In[ ]:




