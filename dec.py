#!/usr/bin/python3
import sys

file = sys.argv[1]

CAP = '⠠' 
def braille(first, s):
    if (first.isupper()):
        return CAP + s
    return s

asciicodes = [' ','!','"','#','$','%','&','(',')','*','+',',','-','.','/',
          '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']


brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
        '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
        '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']


res = dict(zip(brailles, asciicodes));
transtab = str.maketrans(res)

with open(file) as f:
   content = f.readlines()

capNext = True;
for line in content:
   for c in line:
      if (c == CAP):
         capNext = True;
      elif (capNext):
         c = c.translate(transtab);
         c = c.upper();
         print(c, end='');
         capNext = False;
      else:
         c = c.translate(transtab);
         print(c, end='');
         capNext = False;
