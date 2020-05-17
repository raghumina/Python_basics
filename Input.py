# Input in Python 

#  user_name = input()
#  print("hello"+ user_name)

#  another example 
#  address = input()
#  print("your address is :"+address)

# If you want a number to be a number, you should write it explicitly:
#number = input('Please entre your id_no')
#print(number)
#print("What's your favorite number?")
#value = (input())  # now value keeps an integer number


# lets take an example of someone's data 
#print("Please enter your details here ")
#print("What is your name ? ")
#name = input()
#print("Where do you live ?")
#address = input()
#print("What is your contact number ?")
#number = int(input())   # here int is used to specify the value of number should be int value


#print("Enter a number: ")  # user enters 10
#user_num = input()
#print(user_num + user_num)



# Input Problem 1 
# Have you ever dreamed of becoming a songwriter? It's time to make a hit. We will leave a verse for later and write the chorus part instead.
# All you need to do is to read the input number n and an input word (they are given on separate lines) and to repeat this word exactly n times.
# Finally, print your song for us, please!
# Sample Input 1:
# 7
# la
# Sample Output 1:
# lalalalalalala
n = int(input())
word = input()
print(n*word)