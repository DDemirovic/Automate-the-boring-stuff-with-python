#Coin Flip Streaks experiment
import random
import time

streakCounter = 0
numberOfStreaks = 0
totalHeadsStreakCounter = 0
totalTailsStreakCounter = 0
longestStreak = 0

start = time.time()
for experimentNumber in range(100000):
    #Code der eine zufällige Liste mit 100 (H)ead oder (T)ails Einträgen generiert
    listOfHeadsOrTails = []
    for listFiller in range(100):
        headsOrTails = random.randint(0, 1)
        if 0 == headsOrTails:
            listOfHeadsOrTails += ['H']
        else:
            listOfHeadsOrTails = listOfHeadsOrTails + ['T']
        
    #Code der überprüft ob es streaks gibt und einige weitere Statistiken
    for streakCheckerLoop in range(len(listOfHeadsOrTails)):
        #Spätere abfrage geschieht "Rückwärts", aka wir vergleichen die aktuelle
        #Position mit der vorherigen, das geht natürlich nicht beim ersten
        #Eintrag in der Liste
        if 0 == streakCheckerLoop:
            headsOrTailsMarker = listOfHeadsOrTails[streakCheckerLoop]
            continue
        #Sonderfall 2: Sind Eintrag 1 und 2 identisch, dann haben wir schon eine
        #streak von 2 und nicht 1
        elif 1 == streakCheckerLoop:
            if listOfHeadsOrTails[1] == listOfHeadsOrTails[0]:
                streakCounter = 2
        #eigentlicher Normalfall, Position x wird mit x-1 verglichen, Abfrage für
        #den Fall das die identisch sind
        elif listOfHeadsOrTails[streakCheckerLoop] == listOfHeadsOrTails[streakCheckerLoop - 1]:
            streakCounter += 1
            #Hier wird nur Statistik betrieben (gecheckt ob Kopf/Zahl geworfen
            #wurde. headsOrTailsMarker merkt sich ebendiesen Eintrag
            if 'H' == listOfHeadsOrTails[streakCheckerLoop]:
                headsOrTailsMarker = 'H'
            else:
                headsOrTailsMarker = 'T'
            if streakCounter > longestStreak:
                longestStreak = streakCounter
        #Falls vorherige Abfrage nicht erfolgreich war, dann ist die streak
        #abgebrochen
        else:
            if streakCounter > longestStreak:
                longestStreak = streakCounter
            streakCounter = 1

        if 6 == streakCounter:
            numberOfStreaks += 1
            if 'H' == headsOrTailsMarker:
                totalHeadsStreakCounter += 1
            elif 'T' == headsOrTailsMarker:
                totalTailsStreakCounter += 1
end = time.time()

print('Statistic time:\n\
The total number of streaks overall is:', numberOfStreaks,\
      '\nThe total number of head streaks is:', totalHeadsStreakCounter,\
      '\nThe total number of tails streaks is:', totalTailsStreakCounter,\
      '\nThe longest streak overall is:', longestStreak)
        
print('\nChance of head streaks: %s%%' % (totalHeadsStreakCounter / 1000),\
      '\nChance of tail streaks: %s%%' % (totalTailsStreakCounter / 1000))
print('\nTime elapsed while execution (in seconds):', end-start)