import random
import sys


class Trainer:
    pokedex = []    
    
    def __init__(self, name):
        self.name = name
    
    
    def add_pokemon(self, pokemon):
        self.pokedex.append(pokemon)
        print("You have added {} to your pokedex.".format(pokemon.name))

ember = {"move_name":"Ember", "move_type":"Fire"}
tackle = {"move_name":"Tackle", "move_type":"Normal"}
water_gun = {"move_name":"Water gun", "move_type":"Water"}
vine_whip = {"move_name":"Vine Whip", "move_type":"Grass"}   
    
class Pokemon:

    def __init__(self, name, element, weakness, attack):
        self.name = name
        self.element = element
        self.weakness = weakness
        self.attacks = [tackle, attack]
        
        self.health = 10



charmander = Pokemon(
    name="Charmander",
    element="fire",
    weakness="water",
    attack=ember
) 
        
squirtle = Pokemon(
    name="Squirtle",
    element="water",
    weakness="fire",
    attack=water_gun
)

bulbasaur = Pokemon(
    name="Bulbasaur",
    element="grass",
    weakness="fire",
    attack=vine_whip
)

flareon = Pokemon(
    name="Flareon",
    element="fire",
    weakness="water",
    attack=ember
)

vaporeon = Pokemon(
    name="Vaporeon",
    element="water",
    weakness="grass",
    attack=water_gun
)

leafeon = Pokemon(
    name="Leafeon",
    element="grass",
    weakness="fire",
    attack=vine_whip
)

vulpix = Pokemon(
    name="Vulpix",
    element="fire",
    weakness="water",
    attack=ember
)
    
pansear = Pokemon(
    name="Pansear",
    element="fire",
    weakness="water",
    attack=ember
)  

magmar = Pokemon(
    name="Magmar",
    element="fire",
    weakness="water",
    attack=ember
)

shellder = Pokemon(
    name="Shellder",
    element="water",
    weakness="fire",
    attack=water_gun
)

hippopotas = Pokemon(
    name="Hippopotas",
    element="grass",
    weakness="fire",
    attack=vine_whip
)

phanpy = Pokemon(
    name="Phanpy",
    element="grass",
    weakness="fire",   
    attack=vine_whip
)

wild_pokemon = [charmander, squirtle, bulbasaur, flareon, vaporeon, leafeon, vulpix, pansear, magmar, shellder, hippopotas, phanpy]
hit_point_ints = [0,1,2,3]

def pokemon_fight(chosen_pokemon, opponent):
    attacker = chosen_pokemon
    chosen_pokemon.health = 10
    opponent.health = 10

    winner = None

    while winner is None:
        if attacker == chosen_pokemon:
            fight_action = int(input("What do you want to do? \n1. Attack \n2. Switch\n3. Run \n >  "))
            if fight_action == 1: 
                print("Choose an attack:")

                for index, attack in enumerate(chosen_pokemon.attacks):
                    print(index + 1, attack['move_name'])
        
                attack_used_index = int(input(">  ")) - 1
                attack_used_name = chosen_pokemon.attacks[attack_used_index]['move_name']
                hit_points = random.choice(hit_point_ints)
                if attack_used_index == 1 and attacker.element == opponent.weakness:
                    hit_points *= 2
                opponent.health -= hit_points
                
                print(f"{chosen_pokemon.name} used {attack_used_name}, dealing {hit_points} damage.")
                attacker = opponent

            if fight_action == 2:
                if len(trainer.pokedex) > 1:
                    choose_fighter_pokemon()
                    battle(chosen_pokemon, opponent)
                elif len(trainer.pokedex) == 1:
                    print("You only have 1 pokemon in your pokedex") 
                    battle(chosen_pokemon, opponent)
            
            
            elif fight_action == 3:
                winner = opponent
                print("The winner is {}!".format(winner.name))

        elif attacker == opponent:
            hit_points = random.choice(hit_point_ints)
            chosen_pokemon.health -= hit_points
            attacker == chosen_pokemon

            opponent_attack = random.choice(opponent.attacks)
            opponent_attack_index = opponent.attacks.index(opponent_attack)
            opponent_attack_name = opponent.attacks[opponent_attack_index]['move_name']
            print(f"{opponent.name} used {opponent_attack_name}, dealing {hit_points} damage.")
            print(f"Score:\n{chosen_pokemon.name} health:[{chosen_pokemon.health}]\nOpposing {opponent.name} health:[{opponent.health}]")

            attacker = chosen_pokemon

        if chosen_pokemon.health <= 0:
            if len(trainer.pokedex) > 1:
                chosen_pokemon = choose_fighter_pokemon()  
            else:
                print(chosen_pokemon.name + " fainted. Game over.")
                winner = opponent
        elif opponent.health <= 0: 
            winner = chosen_pokemon


    if winner == chosen_pokemon:
        opponent.health = 10
        chosen_pokemon.health = 10
        opponent_index = wild_pokemon.index(opponent)
        wild_pokemon.pop(opponent_index)
        trainer.add_pokemon(opponent)
        print(f"{trainer.name}, you caught {opponent.name}!")
        menu()
    elif winner == opponent:
        opponent.health = 10
        chosen_pokemon.health = 10
        _, selected_pokemon_number = choose_fighter_pokemon()
        # chosen_pokemon, temp = choose_player()
        trainer.pokedex.pop(selected_pokemon_number)
        wild_pokemon.append(chosen_pokemon)
        print(f"Your {chosen_pokemon.name} fainted. Game over...")
        menu()
    
        
        
        #pokemon = wild_pokemon.pop(index)
        # trainer.add_pokemon(pokemon)

                
        
       
def battle(chosen_pokemon, opponent):
    action_taken = int(input("How do you want to proceed? (enter the corresponding number) \n 1. Fight\n 2. Switch Pokemon\n 3. Run\n >  "))   
    
    if action_taken == 1:
        pokemon_fight(chosen_pokemon, opponent)
    elif action_taken == 2:
        if len(trainer.pokedex) > 1:
            choose_fighter_pokemon()
            battle(chosen_pokemon, opponent)
        elif len(trainer.pokedex) == 1:
            print("You only have 1 pokemon in your pokedex") 
            battle(chosen_pokemon, opponent)
        
    elif action_taken == 3:
        print('\nYou got away safely.')
        opponent.health = 10
        menu()
    print('battle exits')
        

def choose_fighter_pokemon():
    print("Which pokemon would you like to use? Enter the corresponding number:  ")
    for number, pokemon in enumerate(trainer.pokedex):
        print(number, pokemon.name)
    selected_pokemon_index = int(input(">  "))
    selected_pokemon = trainer.pokedex[selected_pokemon_index]
    print(f"Go get 'em, {selected_pokemon.name}!")

    return selected_pokemon, selected_pokemon_index


# opponent = random.choice(wild_pokemon)
# opponent_index = wild_pokemon.index(opponent)

def catch_pokemon(opponent):
    print("You've encountered a wild " + opponent.name + "!")
    chosen_pokemon, _ = choose_fighter_pokemon()
    battle(chosen_pokemon, opponent)



trainer = Trainer(
    name = input("What is your name? \n")) 

    
is_bad_index = True
while is_bad_index:
    print("\nWhich pokemon would you like to add to your pokedex, {}? Enter the corresponding number:  ".format(trainer.name))
    for number, poke in enumerate(wild_pokemon):
        print(number, poke.name)
    index = int(input(">  "))
    try:
        pokemon = wild_pokemon.pop(index)
    except IndexError:
        print("Oops, that's not a valid value. Try again.")
    else:
        is_bad_index = False
        
trainer.add_pokemon(pokemon)

def menu():
    if len(trainer.pokedex) == 12:
        print("You've captured all of pokemon!")
        sys.exit
    opponent = random.choice(wild_pokemon)
    print("\nWhat would you like to do:",
        "\n - Catch pokemon",
        "\n - Quit"
         )
    action_taken = input(">  ")
    action_taken = action_taken.lower()
    if action_taken == "catch pokemon":
        catch_pokemon(opponent)
    elif action_taken == "quit":
        print("Thanks for playing, " + trainer.name + "!")
        

menu()





"""
Things to change
- advantage for opponent
- switch pokemon should not health reset
- have the game end once trainer has caught all of the pokemon
- have the game end when health is 0 


"""





# Notes/ Alternate 
#opponent = random.choice(wild_pokemon).name
    #print("You've encountered a wild " + opponent + "!")
    #print("Which pokemon would you like to use to fight {}? Enter the corresponding number:  ".format(opponent))
    #for number, pokemon in enumerate(trainer.pokedex):
        #print(number, pokemon.name)
    #player = input(">  ")


# index = int(input("\nWhich pokemon would you like to add to your pokedex, {}? Enter the corresponding number:  ".format(trainer.name)))

    
    #for number, pokemon in enumerate(trainer.pokedex):
        #print(number, pokemon.name)
    #player = input("Which pokemon would you like to use to fight {}? Enter the corresponding number:  ".format(opponent))
    #print(f"Go get 'em, {pokemon.name}!")
    

#for number, poke in enumerate(wild_pokemon):
    #print(number, poke.name)

#for pokemon in trainer.pokedex:
    #print(pokemon.name)
   
    
    
    # winner = none
       # while winner is none:
            #if 
        
                
        
    #elif action_taken == "quit":
      #  print("Thanks for playing, " + trainer.name + "!")
    
#for number, pokemon in enumerate(pokedex):
   # print(number, pokemon.name)
    

#print("You've encountered a wild ", random.choice([pokemon.name for pokemon wild_pokemon]))
#print("You've encountered a wild " + (random.choice(wild_pokemon)).name + "!")


# print("You've encountered a wild " + opponent + "!")

