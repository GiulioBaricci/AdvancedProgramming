def find_stable(menDict, womenDict):

    currentMenDict = {}
    currentWomenDict = {}
    currentMenDict.update(menDict)
    currentWomenDict.update(womenDict)
    return find_couples(menDict, womenDict, currentMenDict, [])


def find_couples(menDict, womenDict, currentMenDict, couples):

    menList = [manKey for manKey in currentMenDict]
    womenList = [womenKey for womenKey in womenDict]

    if(len(menList) == 0):
        return couples
    else:
        coppia = [(man, woman) for man, woman in couples if menDict[menList[0]][0] == woman]
        if(len(coppia) > 0):
            if(womenDict[coppia[0][1]].index(coppia[0][0]) < womenDict[coppia[0][1]].index(menList[0])):
                menDict[menList[0]] = menDict[menList[0]][1:]
            else:
                currentMenDict[coppia[0][0]] = menDict[coppia[0][0]]
                couples.remove(coppia[0])
            return find_couples(menDict, womenDict, currentMenDict, couples)
        else:
            couples.append((menList[0],menDict[menList[0]][0]))
            menDict[menList[0]] = menDict[menList[0]][1:]
            currentMenDict.pop(menList[0])
            return find_couples(menDict, womenDict, currentMenDict, couples)