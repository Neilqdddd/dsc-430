#hw1
#Amanda Wang
#2.5.2019
#I have not given or received any unauthorized assistance on this assignment

#problem 1

def countLetter():
    datafile1=open('namesBoys.txt')
    datafile2=open('namesGirls.txt')
    list1=datafile1.read().split('\n') #split the lines
    datafile1.close()
    list2=datafile2.read().split('\n')
    datafile2.close()
    cnt1={} #create a dictionary to keep track of all the letters
    cnt2={}

    for name in list1:
        if len(name)>1:
            if name[-1] in cnt1:
                cnt1[name[-1]]+=1
            else:
                cnt1[name[-1]]=1

    for name in list2:
        if len(name)>1:
            if name[-1] in cnt2:
                cnt2[name[-1]]+=1
            else:
                cnt2[name[-1]]=1

    lst1=sorted(cnt1.keys())
    lst2=sorted(cnt2.keys())
    lst=sorted(list(set(lst1+lst2)))
            
    print('{:8}{:11}{:11}'.format('Letter','Boys','Girls'))
    for letter in lst:
        if letter not in lst1: 
            print ('{}0{:10}'.format(letter,cnt2[letter]))
        elif letter not in lst2: 
            print('{}{:^21}0'.format(letter,cnt1[letter]))
        else:
            print('{}{:11}{:11}'.format(letter,cnt1[letter],cnt2[letter]))



