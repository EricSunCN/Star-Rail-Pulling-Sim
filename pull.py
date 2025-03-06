#Main pulling logic

#imports
import random
#from gui import *
from contextlib import nullcontext



#variables
pity = 0
tenPullResults = [] #array to store the results of the ten pull
standardBannerCharacters = ['Welt', 'Himeko', 'Bronya', 'Gepard', 'Clara', 'Yanqing', 'Bailu']
limitedFiveStar = ""
limitedFourStar = ['March 7th', 'Hook', 'Dan Heng']
fourStarPity = 0
 #Because there are just too much and I don't want to type them all in
fourStarGuarantee = 0

#Allows the limited five star character to be switched depending on the banner
def limitedFiveStarOne():
    global limitedFiveStar
    limitedFiveStar = 'Seele'
def limitedFiveStarTwo():
    global limitedFiveStar
    limitedFiveStar = 'Tribbie'

def tally():
    global pity
    global fourStarPity
    pity += 1
    fourStarPity += 1


def fiftyFifty():#This functions determines whether the 50/50 is lost
    global pity
    if random.randint(1,100) <= 56: #I don't know why, but apparently star rails' "fiftyfifty" is a 56 vs 44 =(
        pity = 0
        return limitedFiveStar #True indicates the fifty fifty was won and they got the limited character
    else:
        pity = 91
        return standardBannerCharacters[random.randint(1,6)] #Runs the function that decides what standard character they get



def fourStar(fourStarCharacters, fourStarLightcone): #This function determines what four stars to give
    global fourStarPity
    global pity
    global fourStarGuarantee

    if fourStarGuarantee == 1:
        fourStarGuarantee = 0
        return limitedFourStar[random.randint(0,2)] #Gives them a random four star after not getting a limtited four star the time before.
    else:
        if fourStarPity%10 < 9 and fourStarPity%10 > 0 or fourStarPity == 0: #checks if it is between the first and 8th pull
            if random.randint(1,1000) <= 51: #Between the first and 8th pull there are 5.1% chances of getting a four star
                if random.randint(0,1) == 1: #Check to give them a lightcone or a character if they had not lost the last four star 50/50
                    fourStarGuarantee = 0
                    fourStarPity = 0
                    return fourStarCharacters[random.randint(0, len(fourStarCharacters)-1)]#any fourstar Character
                else:
                    fourStarGuarantee = 1
                    fourStarPity = 0
                    return fourStarLightcone[random.randint(0, len(fourStarLightcone)-1)]# any fourstar Lightcone
            else:
                return "3 star" #gives them a 3 star
        elif fourStarPity%10 == 9: #On the 9th pull there is a 56% chance of getting a four star
            if random.randint(1, 1000) >= 561:
                if random.randint(0,1) == 1: #same thing
                    fourStarGuarantee = 0
                    fourStarPity = 0
                    return fourStarCharacters[random.randint(0, len(fourStarCharacters)-1)] #any fourstar Character
                else:
                    fourStarGuarantee = 1
                    fourStarPity = 0
                    return fourStarLightcone[random.randint(0, len(fourStarLightcone)-1)]# any fourstar Lightcone
            else:
                return "3 star"
        else: # This means that it is on the 10th pull and is a gurenteed 4 star
            if random.randint(0,1) == 1:  # same thing
                fourStarGuarantee = 0
                fourStarPity = 0
                return fourStarCharacters[random.randint(0, len(fourStarCharacters)-1)]# any fourstar Character
            else:
                fourStarGuarantee = 1
                fourStarPity = 0
                return fourStarLightcone[random.randint(0, len(fourStarLightcone)-1)]# any fourstar Lightcone


def pull(tenPullResults, fourStarCharacters, fourStarLightcone):
    global pity
    if pity == 90 or pity ==180: #Five Star guarantee
        if pity == 90: #50/50
            tally()
            tenPullResults.append((fiftyFifty())) #adds a 50/50 five star
        else:
            tally()
            tenPullResults.append(limitedFiveStar)#adds the limited five star as this is a 100000% guarantee
            pity = 0
    elif pity < 75 and pity >= 0 or pity < 165 and pity > 90: #Checks if the pity is within the base range (Where the chances of getting a fivestar are low as f).
        if random.randint(1,1000) <= 6:   #generates a random number to check if they got the 0.6% chance
            if pity > 90: #checks if it has lost the last 50/50
                 #Returns the limited five star
                 tally() #Increments the tally by 1
                 tenPullResults.append(limitedFiveStar)#adds the limited five star to the list of results
                 pity = 0
            else:
                #Loses the fifty fifty
                tally()
                tenPullResults.append((fiftyFifty())) #addes the standard banner 5 star to the list
        else: #Got a 4 or 3 star just like the average... =(
            tally()
            tenPullResults.append(fourStar(fourStarCharacters, fourStarLightcone))
    elif pity >= 75 and pity < 90 or pity >= 165 and pity < 180: #This is hard pity (where the chances increment by 6% every pull until the guruatee on pull 90
        if random.randint(1,1000) <= (pity%90-74)*66: #The chances increase by 6% per pull until the 16th pull after 74 (90) when it becomes over 100%
            if pity > 90:
                tally()
                tenPullResults.append(limitedFiveStar) #100000% guarantee
                pity = 0
            else:
                tally()
                tenPullResults.append((fiftyFifty()))# fifty fifty at hard pity

        else:
            tally()
            tenPullResults.append(fourStar(fourStarCharacters, fourStarLightcone))
    else:
        print("error")

def tenPull():
    global tenPullResults
    fourStarCharacters = ['March 7th', 'Dan Heng', 'Arlan', 'Asta', 'Herta', 'Serval', 'Natasha', 'Pela', 'Sampo',
                          'Hook', 'Lynx', 'Luka', 'Qingque', 'Tingyun', 'Sushang', 'Yukong', 'Guinaifen', 'Xueyi',
                          'Hanya', 'Moze', 'Gallagher', 'Misha']
    fourStarLightcone = ["Example Lightcone"]
    tenPullResults = []
    counter = 0
    while counter < 10:
        pull(tenPullResults, fourStarCharacters, fourStarLightcone)
        counter += 1
    print(tenPullResults)

def singlePull():
    global tenPullResults
    fourStarCharacters = ['March 7th', 'Dan Heng', 'Arlan', 'Asta', 'Herta', 'Serval', 'Natasha', 'Pela', 'Sampo',
                          'Hook', 'Lynx', 'Luka', 'Qingque', 'Tingyun', 'Sushang', 'Yukong', 'Guinaifen', 'Xueyi',
                          'Hanya', 'Moze', 'Gallagher', 'Misha']
    fourStarLightcone = ["Example Lightcone"]
    tenPullResults = []
    pull(tenPullResults, fourStarCharacters, fourStarLightcone)
    print(tenPullResults)
