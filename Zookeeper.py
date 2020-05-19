 # Project zookeeper ( Jet Brains)
 
# Objectives
# In this stage your program should:

# Ask for a number of the habitat using the following phrase: Which habitat # do you need?.
# Use the input number as an index of your habitats to print its content.
# End with the following phrase:
# ---
# The end of the program. To check another habitat restart the watcher please.
# Example 1

# Which habitat # do you need? > 5
# Switching on camera from the habitat with rabbits...
#         ,
#        /|      __
#       / |   ,-~ /
#      Y :|  //  /
#      | jj /( .^
#      >-"~"-v"
#     /       Y
#    jo  o    |
#   ( ~T~     j
#    >._-' _./
#   /   "~"  |
# Y     _,  |
#  /| ;-"~ _  l
#/ l/ ,-"~    \
#\//\/      .- \
# Y        /    Y
# l       I     !
# ]\      _\    /"\
#(" ~----( ~   Y.  )
#It seems there will be more rabbits soon!
#---
#The end of the program. To check another habitat restart the watcher please.


habitat = ['camel','lion','deer','goose','bat','rabbit']
habitat = int(input('Which habitat # do you need? > '))
print(habitat,'''
''')
