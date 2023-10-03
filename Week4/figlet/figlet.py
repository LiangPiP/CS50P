import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts=figlet.getFonts()
if len(sys.argv)==1:
    str=input("Input: ")
    fn=random.randint(0,len(fonts)-1)
    figlet.setFont(font=fonts[fn])
    print(Figlet.renderText(str))
elif len(sys.argv)==3 and (sys.argv[1]=='-f' or sys.argv[1]=='-font'):
    if not sys.argv[2] in fonts:
        sys.exit("Invalid usage")
    str=input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(str))
else:
    sys.exit("Invalid usage")

