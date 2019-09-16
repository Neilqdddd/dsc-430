'''
Yili Lin
1/26/2019
I have not given or received any unauthorized assistance on this assignment.
'''
def lastwordcount(file1,file2):
    ' reads the two datafiles into memory storing them in two lists.'
    infile1=open(file1)
    infile2=open(file2)
    list1 = infile1.read().split('\n')
    list2 = infile2.read().split('\n')
    infile1.close()
    infile2.close()
    counter1={}
    counter2={}

    # count the alp of two list
    for word in list1:
        if len(word)>1:
            if word[-1] in counter1:
                counter1[word[-1]]+=1
            else:
                counter1[word[-1]]=1


    for word in list2:
        if len(word) > 1:
            if word[-1] in counter2:
                counter2[word[-1]]+=1
            else:
                counter2[word[-1]]=1

    # sort key into one list with order
    al1=sorted(counter1.keys())
    al2=sorted(counter2.keys())
    #print(al1)
    #print(al2)
    alplist=sorted(list(set(al1+al2)))
    #print(alplist)
    blank=0

    # out print
    print('{:8}{:8}{:8}'.format('Letter','Boys','Girls'))
    for alp in alplist:
        if alp not in al1:#when that alph didn't show
            print ('{}{:9}{:9}'.format(alp,blank,counter2[alp]))
        elif alp not in al2: #when that alph didn't show
            print('{}{:11}{:9}'.format(alp,counter1[alp],blank))
        else:
            print('{}{:11}{:9}'.format(alp,counter1[alp],counter2[alp]))


'''
Letter N is used by boys most while letter A is used by girls mostly.
There is none name ends in letter Q.
Boy names use almost all alphabets.
Girl names have no ends in 'B,F,G,Q,J,K,O,P,R'.
380 girl names end in 'a', while only 9 boy names end in 'a'.
'''