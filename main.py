import random 
 
pile = []
 
with open('deck.txt') as pilefile:
    for line in pilefile:
        line = line.rstrip()
        number = int(line[0])
        for i in range(number):
            pile.append(line[2:])
 
extender = ['Reckless Greed', 'Legacy of Yata-Garasu','jar of greed']
 
for i in range (1):
 
    print('Pile', pile,'\n')
 
    hand = random.choices(pile, k=5) #( 5 CARTES en main mais changeable)
 
    print('Hand',hand,'\n')
 
    two_cards_combos = False
    extender_cond = False
 
    if 'Pantheism of the Monarchs' in hand and 'The Prime Monarch' in hand or 'Bamboo broken' in hand and 'Bamboo gold' in hand:
        two_cards_combos = True
        print('you have a two card combos')
   
    if any(extender in hand for extender in extender):
        extender_cond = True
        print("you have a extender")
       
    if two_cards_combos in hand and any(extender in hand for extender in extender):
        print('good hand')
   
           
    card_at_3 = ['Allure of Darkness', 'Hand Destruction', 'Pantheism of the Monarchs', 'Reinforcement of the Army', "White Elephant's Gift", "Reckless Greed", "The Prime Monarch"]
    duplicates = []
 
    for x in hand: # tu itere au travers de 3 cartes du meme nom (card at 3)
        if hand.count(x) > 1:
            duplicates.append(x)
 
    print('Duplicates:',duplicates,'\n')
 
    if len(duplicates) >= 3:
        print("bad hand")    
    else:
        print("")
