"""Combat system for battles."""

import random


class Enemy:
    """Represents an enemy in combat."""
    
    def __init__(self, name, health, attack, defense, exp_reward, gold_reward):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
        
    def take_damage(self, damage):
        """Apply damage to the enemy."""
        actual_damage = max(1, damage - (self.defense // 2))
        self.health -= actual_damage
        return actual_damage
    
    def is_alive(self):
        """Check if enemy is still alive."""
        return self.health > 0
    
    def attack_player(self, player):
        """Enemy attacks player and returns damage dealt."""
        base_damage = random.randint(self.attack - 3, self.attack + 3)
        damage = max(1, base_damage - (player.defense // 3))
        return damage


class CombatSystem:
    """Handles combat between player and enemies."""
    
    def __init__(self):
        """Initialize combat system."""
        self.enemies_data = {
            'Goblin': Enemy('Goblin', 20, 8, 2, 25, 10),
            'Wolf': Enemy('Wolf', 30, 12, 3, 40, 15),
            'Shadow Creature': Enemy('Shadow Creature', 35, 15, 4, 60, 25),
            'Bandit': Enemy('Bandit', 25, 10, 3, 35, 20),
            'Bandit Leader': Enemy('Bandit Leader', 60, 16, 6, 150, 100),
            'Magic Sprite': Enemy('Magic Sprite', 15, 14, 2, 50, 30),
            'Enchanted Wolf': Enemy('Enchanted Wolf', 40, 14, 5, 80, 40),
            'Stone Golem': Enemy('Stone Golem', 80, 10, 8, 120, 80),
            'Skeleton': Enemy('Skeleton', 22, 9, 2, 30, 15),
            'Skeleton Warrior': Enemy('Skeleton Warrior', 40, 12, 4, 70, 40),
            'Ancient Guardian': Enemy('Ancient Guardian', 100, 18, 7, 200, 150),
            'Drake': Enemy('Drake', 70, 16, 6, 150, 100),
            'Dragon': Enemy('Dragon', 200, 25, 10, 500, 300),
        }
    
    def get_enemy(self, enemy_name):
        """Get an enemy instance by name."""
        if enemy_name in self.enemies_data:
            enemy_data = self.enemies_data[enemy_name]
            return Enemy(enemy_data.name, enemy_data.max_health, enemy_data.attack,
                        enemy_data.defense, enemy_data.exp_reward, enemy_data.gold_reward)
        return None
    
    def start_combat(self, player, enemy_name):
        """Start a combat session."""
        enemy = self.get_enemy(enemy_name)
        if not enemy:
            print(f"Enemy '{enemy_name}' not found!")
            return
        
        print(f"\n⚔️ A wild {enemy.name} appears!")
        print(f"   {enemy.name} HP: {enemy.health}/{enemy.max_health}")
        
        turn = 0
        while player.health > 0 and enemy.is_alive():
            turn += 1
            print(f"\n--- Turn {turn} ---")
            print(f"Your HP: {player.health}/{player.max_health}")
            print(f"{enemy.name} HP: {enemy.health}/{enemy.max_health}")
            print("\n[1] Attack  [2] Magic Attack  [3] Defend  [4] Item  [5] Run")
            
            choice = input("Choose action: ").strip()
            
            if choice == '1':
                self._player_attack(player, enemy)
            elif choice == '2':
                self._player_magic_attack(player, enemy)
            elif choice == '3':
                self._player_defend(player)
            elif choice == '4':
                self._use_item(player)
                continue  # Don't let enemy attack after using item
            elif choice == '5':
                if random.random() < 0.4:
                    print("You escaped successfully!")
                    return "escaped"
                else:
                    print("Failed to escape!")
            else:
                print("Invalid action!")
                continue
            
            # Enemy attacks
            if enemy.is_alive():
                damage = enemy.attack_player(player)
                player.health -= damage
                print(f"\n{enemy.name} attacks you for {damage} damage!")
                
                if player.health <= 0:
                    print("\n💀 You have been defeated!")
                    player.health = 1  # Keep alive for game over handling
                    return "defeated"
        
        if enemy.health <= 0:
            print(f"\n🎉 Victory! You defeated the {enemy.name}!")
            print(f"   Gained {enemy.exp_reward} EXP and {enemy.gold_reward} Gold!")
            player.add_experience(enemy.exp_reward)
            player.add_gold(enemy.gold_reward)
            return "victory"
    
    def _player_attack(self, player, enemy):
        """Handle player regular attack."""
        weapon_bonus = 0
        if player.equipment['weapon']:
            weapon_bonus = 5
        
        base_damage = random.randint(player.strength - 2, player.strength + 2)
        damage = base_damage + weapon_bonus
        actual_damage = enemy.take_damage(damage)
        print(f"You attack for {actual_damage} damage!")
    
    def _player_magic_attack(self, player, enemy):
        """Handle player magic attack."""
        mana_cost = 20
        if player.mana < mana_cost:
            print("Not enough mana!")
            return
        
        player.mana -= mana_cost
        base_damage = random.randint(player.magic - 2, player.magic + 5)
        damage = base_damage + 10  # Magic bonus
        actual_damage = enemy.take_damage(damage)
        print(f"You cast a magic spell for {actual_damage} damage!")
        print(f"Remaining mana: {player.mana}/{player.max_mana}")
    
    def _player_defend(self, player):
        """Handle player defending."""
        print("You take a defensive stance!")
        # In a real combat system, this would reduce damage for the next turn
    
    def _use_item(self, player):
        """Handle using an item during combat."""
        if not player.inventory:
            print("No items in inventory!")
            return
        
        print("\nItems:")
        for i, item in enumerate(player.inventory, 1):
            print(f"[{i}] {item}")
        print("[0] Cancel")
        
        choice = input("Use which item? ").strip()
        
        try:
            choice = int(choice)
            if choice == 0:
                return
            if 1 <= choice <= len(player.inventory):
                item = player.inventory[choice - 1]
                if 'Potion' in item or 'Health' in item:
                    player.heal(30)
                    player.inventory.remove(item)
                    print(f"You used {item} and restored 30 HP!")
                else:
                    print(f"Cannot use {item} in combat!")
        except ValueError:
            print("Invalid choice!")
