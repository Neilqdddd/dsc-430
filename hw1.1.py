'''
Yili Lin
1/22/2019
I have not given or received any unauthorized assistance on this assignment
'''
#1
def overlap(lst1, lst2):
    'calculate the overlap of two square'
    x1=lst1[0] #suqare1 x
    y1=lst1[1] #suqare1 y
    h1=lst1[2] #height
    x2=lst2[0] #suqare2 x
    y2=lst2[1] #suqare2 y
    h2=lst2[2] #height
    startX=min(x1,x2)#the far point of x
    endX=max(x1+h1,x2+h2) #the near point of x
    Wide=h1+h2-(endX-startX)#wide of the overlap
    startY=min(y1,y2)#the far point of y
    endY=max(y1+h1,y2+h2)#near point of y
    Height=h1+h2-(endY-startY)#height of the overlap
    if Wide<=0 or Height<=0:# no overlap
        return 0
    else:
        return Wide*Height #square of overlap



totalScore = 0

S1 = [1, 5, 3]
S2 = [5, 6, 2]
S3 = [2, 1, 2]
S4 = [9, 6, 2]
S5 = [7, 2, 3]
S6 = [3, 2, 5]
S7 = [5, 3, 1]

# ---------- ---------- ---------- ---------- ----------
print("Test 1: " + str(S1) + str(S6))
print("Correct Answer: 2")
r1 = overlap(S1, S6)
r2 = overlap(S6, S1)
print("Result 1: " + str(r1))
print("Result 2: " + str(r2))
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print("Score: " + str(s1))
print()

totalScore = totalScore + s1

# ---------- ---------- ---------- ---------- ----------
print("Test 2: " + str(S2) + str(S6))
print("Correct Answer: 2")
r1 = overlap(S2, S6)
r2 = overlap(S6, S2)
print("Result 1: " + str(r1))
print("Result 2: " + str(r2))
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print("Score: " + str(s1))
print()

totalScore = totalScore + s1

# ---------- ---------- ---------- ---------- ----------
print("Test 3: " + str(S3) + str(S6))
print("Correct Answer: 1")
r1 = overlap(S3, S6)
r2 = overlap(S6, S3)
print("Result 1: " + str(r1))
print("Result 2: " + str(r2))
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print("Score: " + str(s1))
print()

totalScore = totalScore + s1

# ---------- ---------- ---------- ---------- ----------
print("Test 4: " + str(S4) + str(S6))
print("Correct Answer: 0")
r1 = overlap(S4, S6)
r2 = overlap(S6, S4)
print("Result 1: " + str(r1))
print("Result 2: " + str(r2))
s1 = 0
if r1 == 0:
    s1 = s1 + 1
if r2 == 0:
    s1 = s1 + 1
print("Score: " + str(s1))
print()

totalScore = totalScore + s1

# ---------- ---------- ---------- ---------- ----------
print("Test 5: " + str(S5) + str(S6))
print("Correct Answer: 3")
r1 = overlap(S5, S6)
r2 = overlap(S6, S5)
print("Result 1: " + str(r1))
print("Result 2: " + str(r2))
s1 = 0
if r1 == 3:
    s1 = s1 + 1
if r2 == 3:
    s1 = s1 + 1
print("Score: " + str(s1))
print()

totalScore = totalScore + s1

# ---------- ---------- ---------- ---------- ----------
print("Test 6: " + str(S6) + str(S6))
print("Correct Answer: 25")
r1 = overlap(S6, S6)
r2 = overlap(S6, S6)
print("Result 1: " + str(r1))
print("Result 2: " + str(r2))
s1 = 0
if r1 == 25:
    s1 = s1 + 1
if r2 == 25:
    s1 = s1 + 1
print("Score: " + str(s1))
print()

totalScore = totalScore + s1

# ---------- ---------- ---------- ---------- ----------
print("Test 7: " + str(S7) + str(S6))
print("Correct Answer: 1")
r1 = overlap(S7, S6)
r2 = overlap(S6, S7)
print("Result 1: " + str(r1))
print("Result 2: " + str(r2))
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print("Score: " + str(s1))
print()

totalScore = totalScore + s1

# ---------- ---------- ---------- ---------- ----------
print("Total Score: " + str(totalScore))
print("Percentage: " + str(100 * totalScore / 14))






