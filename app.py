#python
print("I'm learning Git merge conflicts")
#<<<<<<< HEAD
name = input('Please enter your name:')
last_name = input('Please enter your last name:')
#print('Hi, {} {}!'.format(name, last_name))
#=======

nick = input('Please enter your nickname:')
print('Hi, {} {} a.k.a {}!'.format(name, last_name, nick))
#>>>>>>> Bekzod_Shavkatov_4
