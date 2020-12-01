import random 
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sumCards(some_cards):
  totalValue = 0
  for card in some_cards:
    totalValue += card
  return totalValue

def stringifyCards(some_cards):
  cardString = ""
  for card in some_cards:
    cardString += str(card) + ","
  return cardString

def blackJack(playerScore,dealerScore):
  print(logo)
  yourCards = [];
  dealersCards = [];
  print(f"Total Score - player: {playerScore}, dealer: {dealerScore}")
  print("")

  yourCards.append(random.choice(cards))
  dealersCards.append(random.choice(cards))

  gameContinues = True
  while gameContinues:
    print(f"Your cards: {stringifyCards(yourCards)}")
    print(f"The dealers card: {stringifyCards(dealersCards)}")
    should_continue = input("another cards (y,n)? ")
    if(should_continue == "y"):
      yourCards.append(random.choice(cards))
      if(sumCards(yourCards)>21):
        gameContinues = False
    else:
      gameContinues = False
  
  while sumCards(dealersCards)<=sumCards(yourCards):    
    dealersCards.append(random.choice(cards))

  if(sumCards(yourCards)>21):
     print(f"Bust ! You went over 21 ({sumCards(yourCards)}), you loose")
     dealerScore +=1 
  elif(sumCards(dealersCards)>= 21):  
    print(f"Bust! The dealer went over 21 ({sumCards(dealersCards)}), you win")
    playerScore +=1
  elif(sumCards(yourCards)>sumCards(dealersCards)):
    print(f"you have {sumCards(yourCards)}, the dealer has {sumCards(dealersCards)}, you win!")
    playerScore +=1   
  elif(sumCards(yourCards)<sumCards(dealersCards)):
    print(f"you have {sumCards(yourCards)}, the dealer has {sumCards(dealersCards)}, you loose!")
    dealerScore +=1
  elif(sumCards(yourCards)==sumCards(dealersCards)):
    print(f"Draw! You both have: {sumCards(yourCards)}")  

  playAgain = input("Play again (y,n)? ")
  if(playAgain == "y"):
    clear()
    blackJack(playerScore,dealerScore)
  else:
    clear()
    print(f"Final Score - player: {playerScore}, dealer: {dealerScore}")
    print("go home!")

blackJack(0,0)  
