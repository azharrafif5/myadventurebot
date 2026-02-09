"""Main game logic and game flow control."""

import random
import sys
from player import Player
from locations import World, VILLAGE, DARK_FOREST, BANDIT_CAMP, ENCHANTED_GROVE, ANCIENT_RUINS, DRAGON_MOUNTAIN, TAVERN, MERCHANT_SHOP, HEALING_TEMPLE
from quests import QuestManager
from combat import CombatSystem


class Game:
    """Main game controller."""
    
    def __init__(self):
        """Initialize the game."""
        self.player = None
        self.world = World()
        self.quest_manager = QuestManager()
        self.combat_system = CombatSystem()
        self.game_over = False
        self.game_won = False
        
    def run(self):
        """Main game loop."""
        self.setup_game()
        self.main_game_loop()
        self.end_game()
    
    def setup_game(self):
        """Setup the game and create the player."""
        print("\nWhat is your character's name?")
        name = input("> ").strip()
        if not name:
            name = "Adventurer"
        
        self.player = Player(name)
        self.world.travel_to(VILLAGE)
        
        print(f"\n✨ Welcome, {name}! Your adventure begins in the village...")
        self._display_location()
    
    def main_game_loop(self):
        """Handle the main game loop."""
        while not self.game_over:
            print("\n" + "="*60)
            print("[1] Explore  [2] Stats  [3] Inventory  [4] Quests")
            print("[5] Rest at Inn  [6] Visit Shop  [7] Map  [8] Quit")
            print("="*60)
            
            try:
                choice = input("> ").strip()
                
                if choice == '1':
                    self._explore()
                elif choice == '2':
                    self._show_stats()
                elif choice == '3':
                    self._show_inventory()
                elif choice == '4':
                    self._show_quests()
                elif choice == '5':
                    self._rest_at_inn()
                elif choice == '6':
                    self._visit_shop()
                elif choice == '7':
                    self._show_map()
                elif choice == '8':
                    self.game_over = True
                else:
                    print("Invalid choice!")
            except KeyboardInterrupt:
                print("\n\nGame interrupted!")
                self.game_over = True
            except Exception as e:
                print(f"An error occurred: {e}")
    
    def _explore(self):
        """Handle exploration."""
        location = self.world.get_location(self.player.current_location)
        
        print(location.get_description())
        
        print("\nWhat would you like to do?")
        print("[1] Talk to NPC  [2] Fight Enemy  [3] Pick up Item  [4] Travel to Location")
        
        choice = input("> ").strip()
        
        if choice == '1':
            self._talk_to_npc()
        elif choice == '2':
            self._fight_enemy()
        elif choice == '3':
            self._pick_up_item()
        elif choice == '4':
            self._travel()
        else:
            print("Invalid choice!")
    
    def _talk_to_npc(self):
        """Talk to NPCs in the location."""
        location = self.world.get_location(self.player.current_location)
        
        if not location.npcs:
            print("There are no NPCs here.")
            return
        
        print("\nWho would you like to talk to?")
        npcs = list(location.npcs.items())
        for i, (npc_name, description) in enumerate(npcs, 1):
            print(f"[{i}] {npc_name}")
        print("[0] Cancel")
        
        try:
            choice = int(input("> ").strip())
            if choice == 0:
                return
            if 1 <= choice <= len(npcs):
                npc_name, description = npcs[choice - 1]
                print(f"\n👤 {npc_name}: {description}")
                
                # Check for quest completion first
                quest_completed = self._try_complete_quest(npc_name)
                if quest_completed:
                    return
                
                # Quest givers
                if self.player.current_location == VILLAGE:
                    if npc_name == 'Elder' and 'lost_amulet' not in self.player.completed_quests:
                        self._offer_quest('lost_amulet')
                    elif npc_name == 'Guard Captain' and 'defeat_bandits' not in self.player.completed_quests:
                        self._offer_quest('defeat_bandits')
                    elif npc_name == 'Healer':
                        self._talk_to_healer()
                
                elif self.player.current_location == ENCHANTED_GROVE:
                    if npc_name == 'Grove Keeper' and 'collect_herbs' not in self.player.completed_quests:
                        self._offer_quest('collect_herbs')
                
                elif self.player.current_location == ANCIENT_RUINS:
                    if npc_name == 'Archaeologist' and 'ancient_ruins' not in self.player.completed_quests:
                        self._offer_quest('ancient_ruins')
                
                elif self.player.current_location == DRAGON_MOUNTAIN:
                    if npc_name == 'Mountain Hermit' and 'slay_dragon' not in self.player.completed_quests:
                        self._offer_quest('slay_dragon')
        except ValueError:
            print("Invalid choice!")
    
    def _offer_quest(self, quest_id):
        """Offer a quest to the player."""
        quest = self.quest_manager.get_quest(quest_id)
        if quest:
            print(f"\n✨ New Quest: {quest.name}")
            print(f"{quest.description}")
            print(f"Reward: {quest.reward_exp} EXP, {quest.reward_gold} Gold")
            
            response = input("\nAccept this quest? [yes/no] > ").strip().lower()
            if response == 'yes':
                self.player.add_quest(quest_id, {
                    'name': quest.name,
                    'description': quest.description,
                    'objectives': quest.objectives
                })
                print("Quest accepted!")
    
    def _talk_to_healer(self):
        """Talk to the healer."""
        if self.player.health < self.player.max_health:
            cost = 20
            if self.player.gold >= cost:
                response = input(f"\nFull healing costs {cost} gold. Accept? [yes/no] > ").strip().lower()
                if response == 'yes':
                    self.player.heal(self.player.max_health)
                    self.player.restore_mana(self.player.max_mana)
                    self.player.spend_gold(cost)
                    print("You are fully healed!")
            else:
                print(f"You need {cost} gold for healing.")
        else:
            print("You are already at full health!")
    
    def _fight_enemy(self):
        """Fight an enemy in the location."""
        location = self.world.get_location(self.player.current_location)
        
        if not location.enemies:
            print("There are no enemies here.")
            return
        
        enemy_name = random.choice(location.enemies)
        result = self.combat_system.start_combat(self.player, enemy_name)
        
        if result == "victory":
            # Track defeated boss enemies for quests
            if enemy_name == "Bandit Leader":
                self.player._bandit_leader_defeated = True
                print("\n💀 The Bandit Leader has been defeated!")
                self._show_quest_boss_hint('defeat_bandits')
            elif enemy_name == "Dragon":
                self.player._dragon_defeated = True
                print("\n🐉 The Dragon has been slain!")
                self._show_quest_boss_hint('slay_dragon')
            
            # Check for quest completion
            self._check_quest_objectives()
    
    def _pick_up_item(self):
        """Pick up items from a location."""
        location = self.world.get_location(self.player.current_location)
        
        if not location.items:
            print("There are no items here.")
            return
        
        print("\nAvailable items:")
        for i, item in enumerate(location.items, 1):
            print(f"[{i}] {item}")
        print("[0] Cancel")
        
        try:
            choice = int(input("> ").strip())
            if choice == 0:
                return
            if 1 <= choice <= len(location.items):
                item = location.items.pop(choice - 1)
                self.player.add_item(item)
                print(f"You picked up: {item}")
                
                # Show hints for quest items
                self._show_quest_item_hint(item)
                
                # Check for quest objectives
                self._check_quest_objectives()
        except ValueError:
            print("Invalid choice!")
    
    def _travel(self):
        """Travel to a different location."""
        print(self.world.list_locations())
        
        location_map = {name.lower(): loc_id for loc_id, loc in self.world.locations.items()
                       for name in [loc.name.lower(), loc_id]}
        
        print("\nWhere would you like to go? (Enter location ID or name)")
        destination = input("> ").strip().lower()
        
        if destination in self.world.locations:
            new_location = self.world.travel_to(destination)
            self.player.current_location = destination
            print(f"\n🚀 You travel to {new_location.name}...")
            self._display_location()
        else:
            print("Invalid destination!")
    
    def _display_location(self):
        """Display the current location."""
        location = self.world.get_location(self.player.current_location)
        print(location.get_description())
    
    def _show_stats(self):
        """Display player stats."""
        print(self.player.get_stats())
    
    def _show_inventory(self):
        """Display player inventory."""
        print(self.player.get_inventory())
    
    def _show_quests(self):
        """Display active quests."""
        print(self.player.get_quests())
    
    def _rest_at_inn(self):
        """Rest at the inn to restore health and mana."""
        cost = 10
        if self.player.gold >= cost:
            self.player.heal(50)
            self.player.restore_mana(30)
            self.player.spend_gold(cost)
            print(f"\n😴 You rest at the inn and recover some health and mana! ({cost} gold spent)")
        else:
            print(f"You need {cost} gold to rest at the inn.")
    
    def _visit_shop(self):
        """Visit the merchant shop."""
        print("""
╔═══════════════════════════════════════════════════════════╗
║              THE MERCHANT'S SHOP                          ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  [1] Iron Sword      - 50 Gold  (Strength +3)            ║
║  [2] Steel Armor     - 75 Gold  (Defense +5)             ║
║  [3] Health Potion   - 15 Gold  (Restore 30 HP)          ║
║  [4] Mana Potion     - 25 Gold  (Restore 30 Mana)        ║
║  [0] Leave Shop                                          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
""")
        
        choice = input("What would you like to buy? > ").strip()
        
        items = {
            '1': ('Iron Sword', 50, 'weapon'),
            '2': ('Steel Armor', 75, 'armor'),
            '3': ('Health Potion', 15, 'potion'),
            '4': ('Mana Potion', 25, 'potion'),
        }
        
        if choice == '0':
            return
        
        if choice in items:
            item_name, cost, item_type = items[choice]
            if self.player.gold >= cost:
                if item_type == 'weapon':
                    self.player.equipment['weapon'] = item_name
                    self.player.strength += 3
                    print(f"Bought {item_name}! Strength +3")
                elif item_type == 'armor':
                    self.player.equipment['armor'] = item_name
                    self.player.defense += 5
                    print(f"Bought {item_name}! Defense +5")
                else:
                    self.player.add_item(item_name)
                    print(f"Bought {item_name}!")
                
                self.player.spend_gold(cost)
                print(f"Gold remaining: {self.player.gold}")
            else:
                print(f"You need {cost - self.player.gold} more gold!")
        else:
            print("Invalid choice!")
    
    def _show_map(self):
        """Show the game map."""
        print(self.world.list_locations())
    
    def _show_quest_item_hint(self, item):
        """Show hints when a quest item is collected."""
        hints = {
            'Lost Amulet': """
            💡 HINT: You found the Lost Amulet! 
               → Next: Travel back to the VILLAGE
               → Then: Talk to the ELDER to complete the quest!""",
            
            'Healing Herb': """
            💡 HINT: You collected a Healing Herb!
               → Collect 5 total Healing Herbs
               → Then return to the GROVE KEEPER to complete the quest!""",
            
            'Mysterious Artifact': """
            💡 HINT: You found the Mysterious Artifact!
               → Next: Return to the ARCHAEOLOGIST in the ANCIENT RUINS
               → Then: Talk to them to complete the quest!""",
        }
        
        if item in hints:
            print(hints[item])
    
    def _show_quest_boss_hint(self, quest_id):
        """Show hints when a quest boss is defeated."""
        hints = {
            'defeat_bandits': """
            💡 HINT: Victory! The Bandit Leader is defeated!
               → Next: Travel back to the VILLAGE
               → Then: Talk to the GUARD CAPTAIN to complete the quest!""",
            
            'slay_dragon': """
            💡 HINT: Legendary! The Dragon is slain!
               → Next: Talk to the MOUNTAIN HERMIT to complete the quest
               → This will complete the final quest and WIN THE GAME!""",
        }
        
        if quest_id in hints:
            print(hints[quest_id])
    
    def _check_quest_objectives(self):
        """Check and update quest objectives."""
        location = self.world.get_location(self.player.current_location)
        
        # Lost Amulet quest
        if 'lost_amulet' in self.player.quests:
            if 'Lost Amulet' in self.player.inventory:
                print("✓ Quest objective completed: Found the Lost Amulet!")
                print("   → Return to the Village and talk to the Elder!")
        
        # Defeat Bandits quest
        if 'defeat_bandits' in self.player.quests:
            if 'Bandit Leader' not in location.enemies:
                # Enemy defeated in combat
                pass
        
        # Collect Herbs quest
        if 'collect_herbs' in self.player.quests:
            herb_count = self.player.inventory.count('Healing Herb')
            if herb_count >= 5:
                print(f"✓ Quest objective completed: Collected {herb_count} Healing Herbs!")
                print("   → Return to the Grove Keeper and talk to them!")
                if not hasattr(self.player, '_herbs_hint_shown'):
                    self.player._herbs_hint_shown = True
        
        # Ancient Ruins quest
        if 'ancient_ruins' in self.player.quests:
            if 'Mysterious Artifact' in self.player.inventory:
                print("✓ Quest objective completed: Found the Mysterious Artifact!")
                print("   → Return to the Archaeologist and talk to them!")
    
    def _try_complete_quest(self, npc_name):
        """Try to complete a quest by talking to an NPC. Returns True if a quest was completed."""
        # Lost Amulet quest completion (talk to Elder)
        if npc_name == 'Elder' and 'lost_amulet' in self.player.quests:
            if 'Lost Amulet' in self.player.inventory:
                print("\n✨ Elder: Excellent! You have found my amulet!")
                print("   I was beginning to lose hope. This treasure means everything to me.")
                self._complete_quest('lost_amulet', 'You completed the quest: The Lost Amulet!')
                self.player.remove_item('Lost Amulet')
                print("\n💡 NEXT: Talk to the Guard Captain to get a new quest!")
                return True
            else:
                print("Elder: Come back when you have found my amulet.")
                print("💡 HINT: Check the Dark Forest for my amulet!")
                return False
        
        # Defeat Bandits quest completion (talk to Guard Captain)
        if npc_name == 'Guard Captain' and 'defeat_bandits' in self.player.quests:
            # Check if player has defeated bandits (tracking by defeating Bandit Leader)
            if hasattr(self.player, '_bandit_leader_defeated') and self.player._bandit_leader_defeated:
                print("\n✨ Guard Captain: Outstanding! You have defeated those bandits!")
                print("   The roads are safe again thanks to you!")
                self._complete_quest('defeat_bandits', 'You completed the quest: Defeat the Bandits!')
                self.player._bandit_leader_defeated = False
                print("\n💡 NEXT: Explore other locations for more quests and challenges!")
                return True
            else:
                print("Guard Captain: Those bandits are still out there. We need them dealt with!")
                print("💡 HINT: Travel to the Bandit Camp and defeat their leader!")
                return False
        
        # Collect Herbs quest completion (talk to Grove Keeper)
        if npc_name == 'Grove Keeper' and 'collect_herbs' in self.player.quests:
            herb_count = self.player.inventory.count('Healing Herb')
            if herb_count >= 5:
                print(f"\n✨ Grove Keeper: Wonderful! You've collected {herb_count} healing herbs!")
                print("   These will help many people. Thank you, brave adventurer.")
                self._complete_quest('collect_herbs', 'You completed the quest: Healing Herb Collection!')
                for _ in range(5):
                    self.player.remove_item('Healing Herb')
                print("\n💡 NEXT: Visit the Ancient Ruins to find the Archaeologist!")
                return True
            else:
                print(f"Grove Keeper: We still need more herbs. You have {herb_count}/5. Please collect more.")
                print("💡 HINT: Keep picking up Healing Herbs in this grove!")
                return False
        
        # Ancient Ruins quest (talk to Archaeologist)
        if npc_name == 'Archaeologist' and 'ancient_ruins' in self.player.quests:
            if 'Mysterious Artifact' in self.player.inventory:
                print("\n✨ Archaeologist: By the ancients! You found it!")
                print("   This artifact holds the secrets of an ancient civilization.")
                self._complete_quest('ancient_ruins', 'You completed the quest: Secrets of the Ancient Ruins!')
                self.player.remove_item('Mysterious Artifact')
                print("\n💡 NEXT: Prepare yourself! The final quest awaits at Dragon Mountain!")
                return True
            else:
                print("Archaeologist: The artifact must be deep within the ruins. Please find it.")
                print("💡 HINT: Explore the Ancient Ruins thoroughly to find the artifact!")
                return False
        
        # Slay Dragon quest (talk to Mountain Hermit)
        if npc_name == 'Mountain Hermit' and 'slay_dragon' in self.player.quests:
            if hasattr(self.player, '_dragon_defeated') and self.player._dragon_defeated:
                print("\n✨ Mountain Hermit: You have done the impossible!")
                print("   You have slain the dragon! You are a true legend!")
                print("   Your name will be remembered for all eternity!")
                self._complete_quest('slay_dragon', 'You completed the quest: Slay the Dragon!')
                print("\n🏆🏆🏆 YOU HAVE WON THE GAME! 🏆🏆🏆")
                print("   Victory is yours, legendary adventurer!")
                self.game_won = True
                self.game_over = True
                return True
            else:
                print("Mountain Hermit: The dragon still flies above this mountain. Can you defeat it?")
                print("💡 HINT: Explore Dragon Mountain and find the Dragon to battle!")
                return False
        
        return False
    
    def _complete_quest(self, quest_id, message):
        """Complete a quest."""
        if quest_id in self.player.quests:
            quest = self.quest_manager.get_quest(quest_id)
            print(f"\n🎉 {message}")
            print(f"   Received {quest.reward_exp} EXP and {quest.reward_gold} Gold!")
            
            self.player.add_experience(quest.reward_exp)
            self.player.add_gold(quest.reward_gold)
            self.player.complete_quest(quest_id)
    
    def end_game(self):
        """Handle game end."""
        print("\n" + "="*60)
        if self.game_won:
            print("🏆 YOU HAVE WON THE GAME! 🏆")
            print(f"\n{self.player.name} has slain the dragon and become a legend!")
            print(f"Final Level: {self.player.level}")
            print(f"Final Experience: {self.player.experience}")
            print(f"Final Gold: {self.player.gold}")
        else:
            print("Thanks for playing Adventure Quest!")
            print(f"\n{self.player.name}'s Journey:")
            print(f"  Level Reached: {self.player.level}")
            print(f"  Total Experience: {self.player.experience}")
            print(f"  Gold Earned: {self.player.gold}")
        
        print("="*60 + "\n")
