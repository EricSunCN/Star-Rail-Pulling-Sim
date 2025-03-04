#Main pulling logic

#imports
import random

from gui import standardBanner

#variables
pity = 0
tenPullResults = [1, 2, 3, 4, 5, 6, 7, 8] #array to store the results of the ten pull
standardBannerCharacters = ['Welt', 'Himeko', 'Bronya', 'Gepard', 'Clara', 'Yanqing', 'Bailu']
limitedFiveStar = "Seele"
limitedFourStar = ['March 7th', 'Hook', 'Dan Heng']
fourStarPity = 0
fourStarCharacters = ['March 7th', 'Dan Heng', 'Arlan', 'Asta', 'Herta', 'Serval', 'Natasha', 'Pela', 'Sampo', 'Hook', 'Lynx', 'Luka', 'Qingque', 'Tingyun', 'Sushang', 'Yukong', 'Guinaifen', 'Xueyi', 'Hanya', 'Moze', 'Gallagher', 'Misha']
fourStarLightcone = ["Example Lightcone"] #Because there are just too much and I don't want to type them all in


def fiftyFifty(): #This functions determines whether the 50/50 is lost
    if random.randint(1,100) <= 56: #I don't know why, but apparently star rails' "fiftyfifty" is a 56 vs 44 =(
        return limitedFiveStar #True indicates the fifty fifty was won and they got the limited character
    else:
        return standardBannerCharacters[random.randint(1,7)] #Runs the function that decides what standard character they get


def fourStar(fourStarPity, fourStarCharacters): #This function determines what four stars to give
    if fourStarPity == 1:
        return limitedFourStar[random.randint(0,3)] #Gives them a random four star after not getting a limtited four star the time before.
    else:
        if pity%10 < 9: #checks if it is between the first and 8th pull
            if random.randint(1,1000) >= 51: #Between the first and 8th pull there are 5.1% chances of getting a four star
                if random.randint(0,1) == 1: #Check to give them a lightcone or a character if they had not lost the last four star 50/50
                    return fourStarCharacters[random.randint(0, len(fourStar))] #any fourstar Character
                else:
                    return fourStarLightcone[random.randint(0, len(fourStar))] # any fourstar Lightcone
            else:
                return "3 star" #gives them a 3 star
        elif pity%10 == 9: #On the 9th pull there is a 56% chance of getting a four star
            if random.randint(1, 1000) >= 561:
                if random.randint(0,1) == 1: #same thing
                    return fourStarCharacters[random.randint(0, len(fourStar))] #any fourstar Character
                else:
                    return fourStarLightcone[random.randint(0, len(fourStar))] # any fourstar Lightcone
            else:
                return "3 star"
        else: # This means that it is on the 10th pull and is a gurenteed 4 star
            if random.randint(0,1) == 1:  # same thing
                return fourStarCharacters[random.randint(0, len(fourStar))]  # any fourstar Character
            else:
                return fourStarLightcone[random.randint(0, len(fourStar))]  # any fourstar Lightcone


def pull():
    pity = 64
    if pity < 74 and pity > 0 or pity < 164 and pity > 90: #Checks if the pity is within the base range (Where the chances of getting a fivestar are low as f).
        if random.randint(1,1000) <= 6:   #generates a random number to check if they got the 0.6% chance
            if pity > 90: #checks if it has lost the last 50/50
                tenPullResults[pity%10-1] = limitedFiveStar #Returns the limited five star
                #pity += 1
            else:
                tenPullResults[pity%10-1] = fiftyFifty() #pity MOD 10 then subtract 1 finds the place of the item in the 10 pull, the -1 fixes it as the array starts with 0
                #pity += 1
        else: #Got a 4 or 3 star just like the average... =(
            tenPullResults[(pity % 10) - 1] = fourStar()
            #pity += 1



pull()
print[tenPullResults]