import random
from colorama import Fore
from pydub import AudioSegment
from pydub.playback import play
loop = AudioSegment.from_wav("D:\\programstuff\\progs\\pyProgs\\tubemix\\Cli\\jjj.wav")
def game(h,n):
    def printt():
        for i in range(h-1,-1,-1):#displax3s the tubes
            for j in range(0,n):
                print(' '*(len(str(j))-1),end='')
                print('  |',''.join([colors_256(tubes[j][i])]),end='| ',sep='')
            print()
        for i in range(1,n+1):#printing tube nos
                print(' Tube'+str(i),end='')  
        l=[]
        for j in range(0,n):
            stq=''
            for i in range(h-1,-1,-1):
                stq+='|'+str(''.join([colors_256(tubes[i][j])]))+'|'
                stq+='\n'
            l.append(stq)   
    def colors_256(color_):
        num1 = str(color_)
        if color_==0:
            return(' ')
        else:
            if color_ % 16 == 0:
                return(f"\033[38;5;{num1}m{'▇'}\033[0;0m")
            else:
                return(f"\033[38;5;{num1}m{'▇'}\033[0;0m")
    def checks():
        check=0
        for i in range(0,n):#verifx3ing the tubes
                for j in range(h):
                    if tubes[i][1]!=tubes[i][j]:
                        break
                else :check+=1#adding one if the tube has same elemnt
        return check
    '''this is a soley built water fill game and doesn't use much function but purely based on logic '''
    
    while True:
        pow=0
        q=0#n=3
        while n>pow:
            q+=1
            pow=2**(q)
        q-=1
        raoms=[]#declaring a list for the list of numbers to be created
        for i in range(1,(n-q)+1):#filling the list wiht numbers as a sequence
            for j in range(h):raoms.append(i)
        random.shuffle(raoms)#scrambling the sequence
        tubes=[]
        for i in range(n):tubes.append([])#appending no of lists acc to the difficultx3
        c=0
        #filling the list
        for i in range(n-q):
            for j in range(0,h):tubes[i].append(raoms[c]);c+=1
        for i in range(n-q,n):
            for j in range(0,h):tubes[i].append(0)
        #appending 0's to sublist for error escpae
        for i in range(n):tubes[i].append(0)
        check=checks()
        if check==q:
            break
    noofMoves=0  
    print()
    while True:
        nfro=h-1
        nto=0
        c=0
        for i in range(0,n-1):
            for j in range(i+1,n):
                while tubes[i][nfro]==0 and nfro>-1:#decreasing the nth substance of the tube from where the elemnt has to be taken
                    nfro-=1
                while tubes[j][nto]!=0 and nto<h:##increasing  the nth element that has to changed
                    nto+=1
                if nto<h+1 and (tubes[i][nfro]==tubes[j][nto-1]or nto-1==-1):
                    c=1
                nfro=h-1
                nto=0  
        if c!=1 :
            print('there are no moves possible ')
            a='q'  
            break
        printt()
        a=input('\nenter the transfer of tubes or "q" to exit or "undo" to undo:').split('-')#asking input
        
        if a[0] in 'exitquit':
            checki=1
            break
        if len(a)==2 and a[0] not in 'exitquit'or a[0] not in 'undoUNdo':
             fro,to=a
        
        fro, to=int(fro),int(to)
        while 0>=fro or fro>n or 0>=to or to>n or to==fro:#checking inputs
            fro,to=input('enter the transfer of tubes in correct manner:').split('-')
            fro, to=int(fro),int(to)
        fro, to=int(fro)-1,int(to)-1#concerning normal user input for use of index2ing
        while tubes[fro][nfro]==0 and nfro>-1:#decreasing the nth substance of the tube from where the elemnt has to be taken
            nfro-=1
        while tubes[to][nto]!=0 and nto<h:##increasing  the nth element that has to changed
            nto+=1
        if nto<h:#the changing 
            while (tubes[fro][nfro]==tubes[fro][nfro-1] )and(nfro!=-1) and nto<h-1 and(tubes[fro][nfro]==tubes[to][nto-1]or nto-1==-1):
                tubes[to][nto],tubes[fro][nfro]=tubes[fro][nfro],0
                nfro-=1;nto+=1
                play(loop)
            if nto<h+1 and (tubes[fro][nfro]==tubes[to][nto-1]or nto-1==-1):
                tubes[to][nto],tubes[fro][nfro]=tubes[fro][nfro],0
                play(loop)
        else :
            if tubes[fro][nfro]!=0:#condition if overfills
                print(Fore.RED+'!!!!!!!OverFilled!!!!!!!')
        check=checks()
        noofMoves+=1
        if check==n:#this checks the tubes of same elemnt with the total no of tubes
            printt()
                
            print(Fore.GREEN+"\nx3ou've completed !!!!!",'in just' ,Fore.WHITE+str(noofMoves) 
                ,Fore.GREEN+'moves',chr(1),chr(2),chr(3),Fore.BLUE+"\nThank u for playing,",'Byebye:)'
                ,Fore.WHITE+'')#greetings!!!!!!!!!!!!!!!
            checki=0
            break
    return checki
    


                    
    


    
    




        
