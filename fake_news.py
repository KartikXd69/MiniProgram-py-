import random

subjects=[
    "ronaldo",
    "dhoni",
    "Mia Khalifa",
    "Kohli"
]

actions=[
    "Ate a samosa",
    "Danced",
    "Played Cricket with hockey stick",
    "Travalled Space On a Maruti 700"
]

place_or_things=[
    "in a auditorium",
    "in swimming pool",
    "at raju pav bhaji",
    "at garden"
]


while True:
    subject= random.choice(subjects)
    action= random.choice(actions)
    place_or_thing= random.choice(place_or_things)
    
    headline= f"GAND FAAAD Breaking News: {subject} {action} {place_or_thing} "
    print("\n"+ headline)
    user_input = input("\nDo you wanna generate again yes or no :").strip().lower()
    if user_input == "no":
        break
        