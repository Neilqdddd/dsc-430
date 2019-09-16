'''
Yili Lin
3/1/2019
I have not given or received any unauthorized assistance on this assignment.
'''
from csv import DictReader
import statistics
import math
from csv import reader

def readFileVariable(variable):
    'read a variable into a list'
    with open ('avocado.csv','r') as file:
        datalist=[row[variable] for row in DictReader(file)]
        datalist=list(map(eval,datalist))
    return datalist
'a)'
def readAndComputeMean_SM(variable):
    'use statistics mean '
    return eval(format(statistics.mean(readFileVariable(variable)),'.3f'))
'b)'
def readAndComputeSD_SM(variable):
    'use statistics standard deviation'
    return eval(format(statistics.stdev(readFileVariable(variable)),'.3f'))

'c)'
def readAndComputeMedian_SM(variable):
    'use statistics median'
    return statistics.median(readFileVariable(variable))

'd)'
def readAndComputeMean_HG(variable):
    'mean'
    data=readFileVariable(variable)
    return eval(format(sum(data)/len(data),'.3f'))

def readAndComputeSD_HG(variable):
    'standard deviation'
    sum=0
    data=readFileVariable(variable)
    mean_HG = readAndComputeMean_HG(variable)
    for i in data:
        sum+=(i-mean_HG)**2
    return eval(format(math.sqrt(sum/(len(data)-1)),'.3f'))

def readAndComputeMedian_HG(variable):
    'median'
    data = readFileVariable(variable)
    data.sort()
    halfdata=len(data)//2
    return (data[halfdata]+data[~halfdata])/2

'e)'
def readAndComputeMean_MML(variable):
    'computer the mean'
    with open('avocado.csv', 'r') as file:
        fileread = reader(file)
        header=next(fileread)
        variableloc = header.index(variable)
        count=0
        sum=0
        while True:
                line=file.readline()
                if line=='':
                    break
                else:
                    number=eval(next(reader([line]))[variableloc])
                    sum+=(number)
                    count+=1
    return eval(format(sum/count,'.3f'))




def readAndComputeSD_MML(variable):
    'compute the sd'
    mean_mml=readAndComputeMean_MML(variable)
    with open('avocado.csv', 'r') as file:
        fileread = reader(file)
        header=next(fileread)
        variableloc = header.index(variable)
        count=0
        sum=0
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                number = eval(next(reader([line]))[variableloc])
                sum+=(number-mean_mml)**2
                count+=1
    return eval(format(math.sqrt(sum/(count-1)),'.3f'))



def getMinMaxAndN(variable):
    'get min max and n'
    with open('avocado.csv', 'r') as file:
        fileread = reader(file)
        header=next(fileread)
        variableloc = header.index(variable)
        line = file.readline()
        number = eval(next(reader([line]))[variableloc])
        n=1
        minnum=number
        maxnum=number
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                number = eval(next(reader([line]))[variableloc])
                minnum=min(minnum,number)
                maxnum=max(maxnum,number)
                n+=1
        return minnum,maxnum,n



def getCounts(minnum,maxnum,n,variable):
    'count the place of the number'
    belowcount=0
    abovecount=0
    with open('avocado.csv', 'r') as file:
        fileread = reader(file)
        header = next(fileread)
        variableloc = header.index(variable)
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                number = eval(next(reader([line]))[variableloc])
                if number < minnum:
                    belowcount+=1
                elif number > maxnum:
                    abovecount+=1
                counter=n-belowcount-abovecount
    return belowcount,counter


def computeNewMinMax(minnum,maxnum,belowcount,counter,n):
    'get the new min and max'
    if belowcount+counter<(n/2+1):# if median is not in the bin move to next bin
        bucketrange=(maxnum-minnum)
        minnum=minnum+bucketrange
        maxnum=maxnum+bucketrange
    elif belowcount+counter>=(n/2+1):# if median is in the bin divide into 5 small bin
        bucketrange=(maxnum-minnum)/5
        maxnum=minnum+bucketrange
    return minnum, maxnum


def getMedian(minnum,maxnum,variable):
    'get the median number'
    with open('avocado.csv', 'r') as file:
        fileread = reader(file)
        header = next(fileread)
        variableloc = header.index(variable)
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                number = eval(next(reader([line]))[variableloc])
                if number<maxnum and number>minnum:
                    return number


def readAndComputeMedian_MML(variable):
    'computer median'
    getnum=getMinMaxAndN(variable)
    minnum=getnum[0]
    maxnum=getnum[1]
    n=getnum[2]
    while True:
        outcount=getCounts(minnum,maxnum,n,variable)
        belowcount=outcount[0]
        counter=outcount[1]
        if n%2==1:#when n is odd
            if counter == 1 and (belowcount + counter) == (n + 1) / 2:
                median = getMedian(minnum, maxnum, variable)
                return median
        elif n%2==0: #when n is even
            if counter == 1 and (belowcount + counter) == (n/2):#get the first half median
                median1 = getMedian(minnum, maxnum, variable)
            elif counter == 1 and (belowcount + counter) == (n/2)+1:#get the second half median
                median2 = getMedian(minnum, maxnum, variable)
                return (median1+median2)/2
        #get the new min and max
        outcome=computeNewMinMax(minnum,maxnum,belowcount,counter,n)
        minnum=outcome[0]
        maxnum=outcome[1]


