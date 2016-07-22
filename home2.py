print('zavdanna1')
def zav1(array):
    if len(array)==0:
        return 0
    nums=[array[i] for i in range (len(array))
          if i%2==0]
    return sum(nums)*array[len(array)-1]
print(zav1([2,3]))
print()

print('zavdanna2',end='\n\n')
import re
print(''.join(re.findall('[A-Z]','How are you? Eh,ok. Low or Lower?Ohhh')))
print()
print('zavdanna3')
s='How are you?'
print(s.lower().count("how"))

word = input ('Vvedit slovo:')
word_list ='How are you'
for word in word_list:
    count1= word_list.lower().count(word)
print(count1)



