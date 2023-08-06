__version__ = '1.0'

from random import choice as ch

def display(team, x):
  print(f"\nTEAM {x}")

  i = 0
  for item in team:
    i += 1
    print(f"{i}. {item.title()}.")


def createteam(participants, amtofteams):

  if len(participants) < amtofteams:
    raise ValueError(
      "The amount of participants can not exceed the amount of teams")

  ppt = round(len(participants) / amtofteams)

  for i in range(amtofteams):
    team = []
    try:
      for x in range(ppt):
        item = ch(participants)
        team.append(item)
        participants.remove(item)
    except:
      pass

    #display
    display(team, i + 1)
