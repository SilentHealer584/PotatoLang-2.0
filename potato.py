import sys, os

arg = sys.argv[1]

global vars
vars = {}

class PotatoLang:
    
    def newvar(varname, value):
        global vars
        vars[varname] = value
    
    def printl(string):
        if '"' in string:
            print(string.replace('"', ""))
        else:
            print(vars[string])
    
    def getkey(x):
        
        for key in vars:
            if vars[key] == x:
                print(key)
            else:
                pass
            
    def input(varname):
        value = input("")
        PotatoLang.newvar(varname, value)
    
    def addition(varn, num1, num2):
        value = int(num1) + int(num2) 
        PotatoLang.newvar(varn, value)
        

with open(arg, 'r') as file:
    file = file.read()
    file = file.split("\n")
    for line in file:
    
        
        if line == "" or line == " " or line == "\n": 
            pass
        
        else:
            if "=" in line:
                if '"' in line and '+' not in line and '-' not in line and '/' not in line and '*' not in line:
                    x = line.split('=')[0]
                    x = x.replace(" ", "")
                    y = line.split('"')[1]
                    PotatoLang.newvar(x, y)
                
                elif '+' in line:
                    line = line.replace(' ', '')
                    varname = line.split('=')[0]
                    num1 = line.split('=')[1]
                    num1 = num1.split('+')[0]
                    num2 = line.split('+')[1]
                    PotatoLang.addition(varname, num1, num2)
                
                else:
                    line = line.replace(" ", "")
                    x = line.split('=')[0]
                    y = line.split('=')[1]
                    PotatoLang.newvar(x, y)
                
            
            if "ConsolePrint" in line:
                if '"' in line:
                    x = line.split('(')[1]
                    x = x.split(')')[0]
                    PotatoLang.printl(x)
                else:
                    x = line.split('(')[1]
                    x = x.split(')')[0]
                    PotatoLang.printl(x)
                    
            if "Key$" in line:
                if '"' in line:
                    x = line.split('"')[1]
                    PotatoLang.getkey(x)
                else:
                    print("[SYNTAX ERROR] - No value was given.")
            
            if "$Potato$" in line:
                print("""
           ____________
          ╱            \\
         ╱              |
        ╱   You Found   |
       |     Meeeee!    |
       |                |
       |                |
       |      ╳  ╳      |
       |  □          □  |
       |   □        □   |
       |    □□□□□□□□    ╱
       |               ╱
        \\_____________╱
""")
            if "ConsoleInput" in line:
                arg = line.split('(')[1]
                arg = arg.split(')')[0]
                PotatoLang.input(arg)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
