s = input('enter a string:')
reverse_s = ''

for ch in s:
    reverse_s = ch + reverse_s


if reverse_s == s:
    print('Palindrome')
else:
    print('Not Palindrome')


#Another approach using slicing in string concept:
# text = input('Enter string to check palindrome or not: ')
# reverse_text = text[::-1]

# if reverse_text == text:
#     print('Palindrome')
# else:
#     print('Not Palindrome')    