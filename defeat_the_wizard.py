import random

# Base Character class
class Character:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power  # Store the original health for maximum limit

    def attack(self, opponent):
        # Randomized damage around base attack power
        dmg = max(1, self.attack_power + random.randint(-3, 3))
        opponent.health = max(0, opponent.health - dmg)
        print(f"{self.name} attacks {opponent.name} for {dmg} damage! Current health: {opponent.health}")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self, amount):
        before = self.health
        self.health = min(self.max_health, self.health + amount)
        gained = self.health - before
        print(f"{self.name} heals for {gained} health! Current health: {self.health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here
    def power_attack(self, target):
        dmg = self.attack_power + 8
        target.health = max(0, target.health - dmg)
        print(f"{self.name} uses Power Attack for {dmg} damage!")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")

    def rally(self):
        self.heal(20)


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Add your cast spell method here
    def cast_spell(self, target):
        dmg = random.randint(20, 45)
        target.health = max(0, target.health - dmg)
        print(f"{self.name} casts Fireball for {dmg} damage!")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")

    def meditate(self):
        self.heal(20)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        before = self.health
        self.health = min(self.max_health, self.health + 5)
        gained = self.health - before
        print(f"{self.name} regenerates {gained} health! Current health: {self.health}")


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=22)

    def quick_shot(self, target):
        first = max(1, self.attack_power - 4 + random.randint(0, 3))
        second = max(1, self.attack_power // 2 + random.randint(0, 2))
        total = first + second
        target.health = max(0, target.health - total)
        print(f"{self.name} uses Quick Shot! Hits for {first} and {second} (total {total}).")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")

    def field_dressing(self):
        self.heal(20)

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=24)

    def holy_strike(self, target):
        base = max(1, self.attack_power + random.randint(-2, 2))
        radiant = random.randint(6, 12)
        dmg = base + radiant
        target.health = max(0, target.health - dmg)
        print(f"{self.name} uses Holy Strike! Base {base} + Radiant {radiant} = {dmg}")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")

    def prayer(self):
        self.heal(20)


# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        # Add Archer class here
        return Archer(name)
    elif class_choice == '4':
        # Add Paladin class here
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Call the special ability here
            if isinstance(player, Warrior):
                print("1) Power Attack   2) Rally")
                pick = input("Choose ability: ")
                if pick == "1":
                    player.power_attack(wizard)
                elif pick == "2":
                    player.rally()
            elif isinstance(player, Mage):
                print("1) Cast Spell (Fireball)   2) Meditate")
                pick = input("Choose ability: ")
                if pick == "1":
                    player.cast_spell(wizard)
                elif pick == "2":
                    player.meditate()
            elif isinstance(player, Archer):
                print("1) Quick Shot   2) Field Dressing")
                pick = input("Choose ability: ")
                if pick == "1":
                    player.quick_shot(wizard)
                elif pick == "2":
                    player.field_dressing()
            elif isinstance(player, Paladin):
                print("1) Holy Strike   2) Prayer")
                pick = input("Choose ability: ")
                if pick == "1":
                    player.holy_strike(wizard)
                elif pick == "2":
                    player.prayer()
        elif choice == '3':
            # Call the heal method here
            player.heal(25)
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()