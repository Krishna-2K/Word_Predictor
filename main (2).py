import string
import random
s=''
count=0
count1=0
step_count=0
print('HELLO BUD')
print('WELCOME TO BEST WORD PREDICTOR')
print("LET'S DISCUSS SOME RULES WITH AN EXAMPLE")
print("1.LET THE COMPUTER GENERATED WORD BE 'JKF'.\n2.LET THE WORD YOU'VE ENTERED BE 'JFK'.\n3.THEN IT DISPLAYS\n\t1\n\tSAME\n\t2\n\tDIFFERENT\n\tIN 'JFK' AND 'JKF' BOTH THE WORDS HAVE 'J' IN COMMON AND IS IN SAME POSITION.\n\tIN 'JFK' AND 'JKF' BOTH THE LETTERS ARE HAVING 'F' AND 'K' IN COMMON BUT THEY ARE IN DIFFERENT POSITIONS.\n4.IF THE WORD THAT YOU'VE ENTERED IS 'TYU', SINCE NO LETTER IS MATCHING WITH 'JKF' SO IT DISPLAYS 'NO LETTER IS MATCHING'.\n5.THE LENGTH OF THE WORD THAT YOU ENTER MUST NOT BE MORE OR LESS THAN THE LENGTH OF THE COMPUTER GENERATED WORD.\n6.LENGTH OF THE WORD WILL BE DISPLAYED BASED ON THE DIFFICULTY YOU CHOOSE.\n7.MAXIMUM NUMBER OF CHANCES ARE 20 AND IS SAME FOR ALL THE LEVELS OF DIFFICULTY.")
print('BEGIN THE GAME NOW')
print('**ENTER THE GAME**')
print('1.EASY\n2.MEDIUM\n3.DIFFICULT')
ch=int(input('CHOOSE LEVEL OF DIFFICULTY:'))
if ch==1:
    n=2
if ch==2:
    n=3
if ch==3:
    n=4
if ch==0 or ch>=4:
    n=3
print('START GUESSING THE',n,'LETTERED WORD')
for i in range(n):
    word = random.choice(string.ascii_letters)
    word=word.upper()
    s=s+word
#print(s)
while n>0 and i!=0:
    input_word=input("ENTER YOUR WORD(ONLY IN CAPITALS):")
    list1=list(s)
    list2=list(input_word)
    if len(list1)==len(list2):
        for i in range(n):
            if list2[i]==list2[i].lower():
                print('!!!WARNING:ENTER CAPITAL LETTERS!!!')
                break
    if len(list2)<len(list1):
        print('!!!WARNING:YOUR WORD LENGTH IS LESS THAN THE LENGTH',n,'!!!')
        continue
    if len(list2)>len(list1):
        print('!!!WARNING:YOUR WORD LENGTH IS EXCEEDING THE LENGTH',n,'!!!')
    for i in range(n):
        for j in range(n):
            if list1[i]==list2[j] and i==j:
                count=count+1
            if list1[i]==list2[j] and i!=j:
                count1=count1+1
    if count==0 and count1==0:
        print('NO LETTER IS MATCHING')
    if count>0:
        print(count,'LETTERS ARE SAME AND ARE IN SAME POSITION AS WELL')
        count=0
    if count1>0:
        print(count1,'LETTERS ARE SAME BUT IN DIFFERENT POSITIONS')
        count1=0
    step_count+=1
    if ch==2 and step_count==5:
        print("HINT..?(1/0)\n1-YES\n0-NO")
        hint=input()
        if hint=='1':
            print('FIRST LETTER',list1[0])
        else:
            pass
    if ch==2 and step_count==10:
        print("HINT..?(1/0)\n1-YES\n0-NO")
        hint=input()
        if hint=='1':
            print('LAST LETTER',list1[n-1])
        else:
            pass
    if ch==3 and step_count==10:
        print("HINT..?(1/0)\n1-YES\n0-NO")
        hint=input()
        if hint=='1':
            print('FIRST LETTER',list1[0],'LAST LETTER',list1[n-1])
        else:
            pass
    if step_count==13:
        print('DO YOU WIS TO CONTINUE THE GAME?(1/0)\n1-YES\n0-NO')
        game_ch=input()
        if game_ch=='0':
            print('SORRY')
            print("THE WORD IS",s)
            print('BETTER LUCK NEXT TIME')
            print('STEPS TAKEN TO COMPLETE THE LEVEL:',step_count)
            i=0
        else:
            pass
    if input_word==s and step_count<=20:
        print("HEY...YOU WON")
        print('STEPS TAKEN TO COMPLETE THE LEVEL:',step_count)
        i=0
    if step_count>20 and input_word!=s:
        print("OOPS...SORRY...YOU ARE OUT OF STEPS")
        print("THE WORD IS",s)
        print('BETTER LUCK NEXT TIME')
        i=0