def is_palindrome(a):
    a=a.lower()
    b=a[::-1]
    if a==b:
        print(True)

    else:
        print(False)


def find_nth_occurrence(substring,string,occurrence=0):
    counter = 0
    for i in range(len(string)):
        #
        stringFound=string.find(substring,counter)
        print(f'({substring},{string},{occurrence} ) == {stringFound}')
        counter=string.find(substring,counter)+1
        occurrence+=1
        if stringFound == -1:
            break


solve=lambda a,b:a==b or('*'in a and(lambda l:not(l[0]==l[1]==b)and b.startswith(l[0])and b.endswith(l[1]))(a.split('*')))                