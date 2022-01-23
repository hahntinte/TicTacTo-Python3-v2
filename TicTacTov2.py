from random import *
bl=["8!a","7!a","6","8!a","6!a","7","6!a","7!a","8","5!a","4!a","3","3!a","4!a","5","5!a","3!a","4","1!a","2!a","0","1!a","0!a","2","0!a","2!a","1","6!a","4!a","2","2!a","4!a","6","6!a","2!a","4","8!a","4!a","0","8!a","0!a","4","0!a","4!a","8"
    ,"6!a","3!a","0","6!a","0!a","3","0!a","3!a","6","7!a","4!a","1","7!a","1!a","4","1!a","4!a","7","8!a","5!a","2","8!a","2!a","5","2!a","5!a","8",]
l=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
pa=["P2 = "," 0"]
pb=["P1 = "," 0"]
spm= ""
ende=""
def spilfeld():
  print(l[6] + "I" + l[7] + "I" + l[8] + "\n" + "-----\n" + l[3] + "I" + l[4] + "I" + l[5] + "\n" + "-----\n" + l[0] + "I" + l[1] + "I" + l[2])
def bot():
 i=1
 while i< len(bl):
  if len(bl[i])==1:
   iback = i-1
   Xo0="a"
   while len(bl[iback])==3:
    bs0 =l[int(bl[iback].split("!")[0])]
    bli =bl[iback].split("!")[1]
    if bli== "b"and bs0!= "0"or bli== "g"and bs0!= "X"or bs0!=Xo0 and Xo0!= "a"or len(bl[iback - 1])==1 and Xo0=="a"or bli== "b-"and bs0!= "0"or bli== "g-"and bs0!= "X":
      break
    elif Xo0=="a" and bs0!=" ":
      Xo0=bs0
    iback-=1
   if l[int(bl[i])]== " " and len(bl[iback])==1:
    l[int(bl[i])]= "0"
    break
  i+=1
 if i==len(bl):
  i = randrange(0, 8, 1)
  while l[i]!= " ":
   i = randrange(0, 8, 1)
  l[i]= "0"
def mg(pl):
 global ende
 ende="0"
 while ende == "0":
  if pl == 1:
   a=pa[0]
   pl=0
   b="X"
   spilfeld()
   inpu=input(a + " = ")
  elif spm == "1":
   bot()
   a=pb[0]
  else:
   a=pb[0]
   pl=1
   b="0"
   spilfeld()
   inpu=input(a + " = ")
  try:
   if inpu!="" and l[int(inpu) - 1]== " ":
    l[int(inpu) - 1]=b
   else:
    pl+=1
  except:
   pl+=1
  if l[0] == l[1] == l[2] != " " or l[3] == l[4] == l[5] != " " or l[6] == l[7] == l[8] != " " or l[0] == l[3] == l[6] != " ":
   ende=a+"!"+" won!\n"
   break
  if l[1] == l[4] == l[7] != " " or l[2] == l[5] == l[8] != " " or l[0] == l[4] == l[8] != " " or l[6] == l[4] == l[2] != " ":
    ende=a+"!"+" won!"
    break
  if l[0]!= " " and l[1] != " " and l[2]!= " " and l[3] != " " and l[4] != " " and l[5] != " " and l[6] != " " and l[7] != " " and l[8] != " ":
   ende="Unendschieden! "
   break
while spm != "1" :
 spm=input("\n\n\n\n\n(1)1player-(2)2player\n")
 if(spm == "1"):
  pb[0]="bot"
 elif(spm == "2"):
  pb=input(pb[0])+"!0"
  break
pa[0]=input(pa[0])
mg(randrange(0, 1))
while spm!= "10":
 ends=ende.split("!")
 if ends[0]==pa[0]:
  pa[1]=" "+str(int(pa[1])+1)
 elif ends[0]==pb[0]:
  pb[1]=" "+str(int(pb[1])+1)
 print(ends[0]+ends[1]+"\n"+pa[0]+pa[1]+"\n"+pb[0]+pb[1])
 endin=""
 while endin != "1":
  endin=input("(1) next round - (2)end game\n")
  if (endin == "1"):
   l=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
   mg(1 if int(pa[1]) < int(pb[1]) else 0)
  elif (endin == "2"):
   endin="1"
   spm= "10"