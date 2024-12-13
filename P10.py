def main():
    thetext = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.'''
    print('Original length of text:-> ', len(thetext))
    print('-----------------------------------------')

    thetext = thetext.strip()

    print('length of text with beginning and trailing spaces removed ->',len(thetext))
    print('----------------------------------------')
    print("count of word 'the' from text -> ",thetext.count('the'))
    print('------------------------------------------------')

    if 'little' in thetext:
          print("'little' is  found.")
          print('--------------------------------------')

    else:
        print("'little is not found.")
        print('------------------------------------------')
    if 'titan' in thetext:
        print("titan' is found.")
        print("------------------------------------------")
    print("Position number of 'appl' is ->" ,thetext.find("appl"))
    print('------------------------------------------------------')

    thetext2=thetext

    print(thetext2.replace('Python','Python'))
    print('----------------------------------------------------')

main()
              
    
    

    
