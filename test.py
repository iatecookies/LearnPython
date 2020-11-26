#Call the function twice instead of once and giving both hands. This will make the function twice as large and twice as long to compute

def check_for_five_of_a_kind(hand_1, hand_2):
    return False, False

# straight flush - contains five cards of sequential rank
def check_for_straight_flush(hand_1, hand_2):
    tel1,tel2 = 0, 0
    hulp = hand_1[0][0]
    for hand in hand_1:
        if hand[0] == hulp:
            tel1 += 1
    if tel1 == 5:
        return True, False

    hulp = hand_2[0][0]
    for hand in hand_2:
        if hand[0] == hulp:
            tel2 += 1
    if tel2 == 5:
        return False, True

    return False, False

def check_for_four_of_a_kind(hand_1, hand_2):
    return False, False


def check_for_fullhouse(hand_1, hand_2):
    return False, False


def check_for_flush(hand_1, hand_2):
    return False, False


def check_for_straight(hand_1, hand_2):
    return False, False


def check_for_three_of_a_kind(hand_1, hand_2):

    valueList = [ ]
    for suit, value in hand_1:
        valueList.append(value)
    valueList.sort()

    for value in valueList:
        if valueList.count(value) == 3:
            return True, False

    valueList1 = [ ]
    for suit, value in hand_2:
        valueList1.append(value)
    valueList1.sort()

    for value in valueList1:
        if valueList1.count(value) == 3:
            return False, True
    return False, False


# two pair -  contains two cards of one rank, two cards of another rank and one card of a third rank
def check_for_two_pair(hand_1, hand_2):
    valueList = [ ]
    for suit, value in hand_1:
        valueList.append(value)
    valueList.sort()
    tel = 0
    for value in valueList:
        if valueList.count(value) == 2:
            tel += 1
            valueList.remove(value)
            if tel == 2:
                return True, False

    valueList1 = [ ]
    for suit, value in hand_2:
        valueList1.append(value)
    valueList1.sort()
    tel = 0
    for value in valueList1:
        if valueList1.count(value) == 2:
            tel += 1
            valueList1.remove(value)
            if tel == 2:
                return False, True

    return False, False


def check_for_one_pair(hand_1, hand_2):
    valueList = [ ]
    for suit, value in hand_1:
        valueList.append(value)
    valueList.sort()
    tel = 0
    for value in valueList:
        if valueList.count(value) == 2:
            return True, False
        else:
            continue

    valueList1 = [ ]
    for suit, value in hand_2:
        valueList1.append(value)
    valueList1.sort()
    tel = 0
    for value in valueList1:
        if valueList1.count(value) == 2:
            return False, True
        else:
            continue

    return False, False


def check_for_high_card(hand_1, hand_2):
    return True, True


def get_hand_from_string(hand_str):
    hand_str = hand_str.replace('[', '')
    hand_str = hand_str.replace(']', '')
    hand_str = hand_str.replace("'", '')

    list = hand_str.split('), (')
    cards = []

    for cardish in list:
        cardish = cardish.replace('(', '')
        cardish = cardish.replace(')', '')
        elements = cardish.split(', ')
        cards.append((elements[0], elements[1]))
    return cards



hands_str = input()
hand_1 = get_hand_from_string(hands_str)
hands_str = input()
hand_2 = get_hand_from_string(hands_str)


listRanks = ["high card", "one pair", "two pair", "three of a kind", "straight", "flush", "full house", "four of a kind", "straight flush", "five of a kind"]

liststuff = [ ] # van laag naar hoog
player1_handRank, player2_handRank = 0, 0

player1_high, player2_high = check_for_high_card(hand_1, hand_2)
liststuff.append( (player1_high, player2_high))

player1_onepair, player2_onepair = check_for_one_pair(hand_1, hand_2)
liststuff.append( (player1_onepair, player2_onepair))

player1_twopair, player2_twopair = check_for_two_pair(hand_1, hand_2)
liststuff.append( (player1_twopair, player2_twopair))

player1_three, player2_three = check_for_three_of_a_kind(hand_1, hand_2)
liststuff.append( (player1_three, player2_three))

player1_straight, player2_straight = check_for_straight(hand_1, hand_2)
liststuff.append( (player1_straight, player2_straight))

player1_flush, player2_flush = check_for_flush(hand_1, hand_2)
liststuff.append( (player1_flush, player2_flush))

player1_fullh, player2_fullh = check_for_fullhouse(hand_1, hand_2)
liststuff.append( (player1_fullh, player2_fullh))

player1_four, player2_four = check_for_four_of_a_kind(hand_1, hand_2)
liststuff.append( (player1_four, player2_four))

player1_straightflush, player2_straightflush = check_for_straight_flush(hand_1, hand_2)
liststuff.append( (player1_straightflush, player2_straightflush))

player1_five, player2_five = check_for_five_of_a_kind(hand_1, hand_2)
liststuff.append( (player1_five, player2_five))

#print (liststuff)
i = 0
for stuff in liststuff:
    if stuff[0] == True:
        player1_handRank = i
        #player1_handRank = liststuff.index(stuff)
    if stuff[1] == True:
        #player2_handRank = liststuff.index(stuff)
        player2_handRank = i
    i += 1
#print(player1_handRank, player2_handRank)

# Check ranking of importance
if player1_handRank > player2_handRank:
    print("player one with " + str(listRanks[player1_handRank]) + " over " + str(listRanks[player2_handRank]))
else:
    print("player two with " + str(listRanks[player2_handRank]) + " over " + str(listRanks[player1_handRank]))
