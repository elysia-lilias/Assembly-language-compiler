from RAMParser import parser
import sys


def ramexe(tree,savedcode,printd):
  savedc = savedcode.split('\n')
  reglist = []
  regvalue = []
  savedlabel = []
  savedline = []
  imax = len(tree)
  try:
   for i in range(len(tree)):
    v1 = tree[i]
    if v1[0] == 'LABEL':
     v1 = tree.pop(i)
     v2 = v1[1]
     savedlabel += [v2]
     savedline += [i]
  except:
    pass
  #print('\n')
  #for i in range(len(tree)):
    #print(tree[i])
  #for i in range(len(savedlabel)):
    #print(savedlabel[i])
    #print(savedline[i])
  i = 0
  set = 0
  fin = 0
  excu = []
  while True:
   if i > len(tree):
     break
   v1 = tree[i]
   #print(v1,'  ',reglist,'   ',regvalue)
   if v1[0] == 'EQ' and set == 0:
        set = 1
        print('Input:')    
   if v1[0] != 'EQ':
    excu += ['Executing: '+ savedc[i]]
   if v1[0] == 'EQ':
     reglist += [v1[1]]
     regvalue += [v1[2]]
     print('R'+ str(v1[1])+' ==> '+str(v1[2]))
####################################
   elif v1[0] == 'AJ':
     term = findwheretojmp(1,i,v1[1],savedlabel,savedline)
     if term== 'Not Found':
        return 'LABEL NOT FOUND'
     else:
        i = term - 1
     #dest = v1[1]
     #if dest in savedlabel:
       #desti = savedlabel.index(dest)
       #if i>=1:
        #i = savedline[desti]-1
       #else:
        #return 'CANNOT JUMP ABOVE FIRST LINE'
####################################
   elif v1[0] == 'BJ':
     term = findwheretojmp(0,i,v1[1],savedlabel,savedline)
     if term== 'Not Found':
        return 'LABEL NOT FOUND'
     else:
        i = term - 1
     #dest = v1[1]
     #if dest in savedlabel:
       #desti = savedlabel.index(dest)
       #i = savedline[desti]


   else:
     if v1[0] == 'ENDE':
        break
     elif v1[1] in reglist:
       if v1[0] == 'INC':
         destreg = reglist.index(v1[1])
         regvalue[destreg] += 1
       elif v1[0] == 'DEC':
         destreg = reglist.index(v1[1])
         regvalue[destreg] -= 1
       elif v1[0] == 'CAJ':
         destreg = reglist.index(v1[1])
         if regvalue[destreg] == 0:
           term = findwheretojmp(1,i,v1[2],savedlabel,savedline)
           if term== 'Not Found':
             return 'LABEL NOT FOUND'
           else:
             i = term - 1  
           #dest = v1[2]
           #if dest in savedlabel:
            #desti = savedlabel.index(dest)
            #if i>=1:
             #i = savedline[desti]-1
            #else:
             #return 'CANNOT JUMP ABOVE FIRST LINE'
       elif v1[0] == 'CBJ':
         destreg = reglist.index(v1[1])
         if regvalue[destreg] == 0:
           term = findwheretojmp(0,i,v1[2],savedlabel,savedline)
           if term== 'Not Found':
             return 'LABEL NOT FOUND'
           else:
             i = term - 1 
           #dest = v1[2]
           #print(dest)
           #print(savedlabel)
           #if dest in savedlabel:
            #desti = savedlabel.index(dest)
            #i = savedline[desti]-1


       elif v1[0] == 'MOVE':
         if v1[2] in reglist:
           temp1 = reglist.index(v1[1])
           temp2 = reglist.index(v1[2])
           regvalue[temp1] = regvalue[temp2]
         else:
           reglist += [v1[2]]
           regvalue += [0]
       elif v1[0] == 'CLR':
           temreg = reglist.index(v1[1])
           regvalue[temreg] = 0
     elif v1[0] == 'MOVE' and v1[2] in reglist:
          temp2 = reglist.index(v1[2])
          reglist += [v1[1]] 
          vtm = regvalue[temp2]
          regvalue += [vtm]
     elif v1 == 'END':
       break
     else:
       reglist += [v1[1]]
       regvalue += [0]
       i = i - 1
   i = i + 1
 
  if printd == 1:
    print('\n\n')
    for i in range(len(excu)):
     print(excu[i])
  result = []
  for i in range(len(reglist)):
    result += [reglist[i],regvalue[i]]
    try:
      i = 0
      while True:
         if result[i] == 1 and fin == 0:
            print('\n\nOutput:')
            print('R1 = ',result[i+1])
            fin = 1
            break
         else:
            i = i + 2
    except:
         i = 0
  return excu    

def findwheretojmp(aboveornot,index,label,savedlabel,savedline) :
   lis = [ind for ind,d in enumerate(savedlabel) if d == label]
   result = 'Not Found'
   delta = 'NONE'
   #print('inside: ')
   #print(lis)
   #print(len(lis))
   #print(label)
   #print(index)
   #print(savedlabel)
   #print(savedline)
   try:
    for k in range(len(lis)):
      #print('here')
      temp = lis[k]
      #print(temp)
      line = savedline[temp]
      if aboveornot == 1 and line <= index:
         if delta == 'NONE':
            delta = index - line
            result = line
         else:
            if index - line < delta:
              delta = index - line
              result = line
      elif aboveornot == 0 and line >= index:
         if delta == 'NONE':
            delta = line - index
            result = line
         else:
            if line - index < delta:
              delta = line - index
              result = line
    return result
   except:
    return 'Not Found'
    
def read_input(data1):
 result = ''
 with open(data1) as fp: 
  line = fp.readline()
  try:
   while line:
      result += line 
      line = fp.readline()
  except Exception as inst:
      result += '\n'
      pass
 #print(result)
 result += '\n'
 return result

def main():
  #while True:
   printd = 0
   dat = sys.argv
   data1 = str(dat[1])
   if(data1 == '-d'):
     data1 = str(dat[2])
     printd = 1
   #print(data1)
   data = read_input(data1)
   #print(data)
   #if data == 'exit;':
    #break;
   try:
      tree = parser.parse(data)
   except Exception as inst:
      print(inst.args[0])
      pass
   #for i in range(len(tree)):
    #print(tree[i])
   excu = ramexe(tree,data,printd)
main() 
