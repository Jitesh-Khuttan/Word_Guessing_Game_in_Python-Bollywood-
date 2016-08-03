def movie(gfilm,olength,vlength,anss):
    cont='n'
    removed=str()
    count=0
    drepeat=[]  #List containing letters which has been entered by the user
    answer=list(anss)#Answer of the guess movie broken into elements
    filmlist=list(gfilm) #Guess query broken into its elements
    bolly=list('BOLLYWOOD') #Word bollywood broken into its elements
    while cont!='y' or bolly!=[] or vlength!=olength:    #Loop should continue until bolly list gets empty or virtual length gets equal to original length(i.e. if the movie gets completely guessed)
        word=input('\n \nGuess the letters of the movie:')#Prompting the user to input the guess word
        test=dontrep(drepeat,word)
        vow=vowel(word)
        x=srch(answer,word)
        drepeat.append(word)
        if test==-2:
            print('\"THIS LETTER HAS ALREADY BEEN ENTERED,PLEASE ENTER ANY ANOTHER LETTER\"')
        elif vow==-3:
            print('\"THIS LETTER IS A VOWEL,,PLEASE ENTER ANY ANOTHER LETTER,VOWELS ARENOT ALLOWED TO BE ENTERED BECAUSE THEY ARE ALREDAY INCLUDED IN THE MOVIE NAMES\"')
        elif x!=-1:
            print('Good! You got this word right!')
            for j in x:
                filmlist[j]=word #Replacing the blank element of filmlist with the guessed words
                print('NOW YOUR FILM BECOMES:',end='')
            for l in range(len(filmlist)):
                print(filmlist[l],end='')
            vlength+=len(x) #Length is increaing
        
        elif x==-1:
            count+=1
            if count==1:
                removed+=bolly[0]
                rem=bolly[0]
                print(removed,'has been removed,from\'BOLLYWOOD\',now you have',len(bolly)-1,'chances left')
                bolly.pop(0)#Removing the letters from BOLLYWOOD
            else:
                rem+=','+bolly[0]
                print(rem,'has been removed,from\'BOLLYWOOD\',now you have',len(bolly)-1,'chances left')
                bolly.pop(0)#Removing the letters from BOLLYWOOD                
                
            
    
        if bolly==[]:
            return('Sorry! You LOST!,BETTER LUCK NEXT TIME,,,THE CORRECT MOVIE IS:',anss)
            break;
        elif vlength==olength:
            return('\nCONGRATULATIONS!! YOU GUESSED THE MOVIE SUCCESSFULLY!!')
            break;
        cont=input('\nDo you want to quit the game? Enter \'y\' to quit or \'n\' to Continue:')
        if cont=='y':
            return('\nTHANKYOU FOR PLAYING THE GAME!!')
            break;
'''--------------------------------------------------------------------------------------------------------------------------------------------'''
#MULTIPLE SEARCH FUNCTION
def srch(ans,find):
    pele=[] #position elements
    for a in range(len(ans)):
        if ans[a]==find:
            pele.append(a)
    if pele==[]:
        return(-1)
    else:
        return(pele)

'''-------------------------------------------------------------------------------------------------------------------------------------------'''
def dontrep(drepeat,word):
    for i in range(len(drepeat)):
        if drepeat[i]==word:
            return(-2)

'''-------------------------------------------------------------------------------------------------------------------------------------------'''
def vowel(word):
    
    vowels=['a','e','i','o','u']
    for i in range(len(vowels)):
        if vowels[i]==word:
            return(-3)
'''----------------------------------------------------------------------------------------------------------------------------------------------'''
#MAIN FUNCTION
def main():
    import random
    luck=random.randint(1,10)
    if luck==1:
        films='-a--'
        print('Guess the Movie:',films)
        virtuall=1
        originall=4
        answers='karz'
        final=movie(films,originall,virtuall,answers)
        print(final)
    elif luck==2:
        films='--i---'
        print('Guess the Movie:',films)
        virtuall=1
        originall=6
        answers='krishh'
        final=movie(films,originall,virtuall,answers)
        print(final)
    elif luck==3:
        films='--ee-ai e---e--'
        print('Guess the Movie:',films)
        virtuall=7
        originall=15
        answers='cheenai express'
        final=movie(films,originall,virtuall,answers)
        print(final)
    elif luck==4:
        films='--a--a -o--e- -i--a -e-o'
        print('Guess the Movie:',films)
        virtuall=11
        originall=24
        answers='phatta poster nikla hero'
        final=movie(films,originall,virtuall,answers)
        print(final)
    elif luck==5:
        films='e- --a -i-e-'
        print('Guess the Movie:',films)
        virtuall=6
        originall=12
        answers='ek tha tiger'
        final=movie(films,originall,virtuall,answers)
        print(final)
    elif luck==6:
        films='--a-aa-'
        print('Guess the Movie:',films)
        virtuall=3
        originall=7
        answers='dhamaal'
        final=movie(films,originall,virtuall,answers)
        print(final)
    elif luck==7:
        films='--a-- -i---a --a--'
        print('Guess the Movie:',films)
        virtuall=6
        originall=18
        answers='bhagg milkha bhagg'
        final=movie(films,originall,virtuall,answers)
        print(final)
    elif luck==8:
        films='-u--e- -'
        print('Guess the Movie:',films)
        virtuall=4
        originall=8
        answers='murder 2'
        final=movie(films,originall,virtuall,answers)
        print(final)
    elif luck==9:
        films='-i--a-i -a -i-e-i -o-a-a'
        print('Guess the Movie:',films)
        virtuall=13
        originall=24
        answers='zindagi na milegi dobara'
        final=movie(films,originall,virtuall,answers)
        print(final)
    elif luck==10:
        films='-ai -o --e'
        print('Guess the Movie:',films)
        virtuall=6
        originall=10
        answers='kai po che'
        final=movie(films,originall,virtuall,answers)
        print(final)
main()
                        
'''----------------------------------------------------------------------------------------------------------------------------------------------'''                
        
            
