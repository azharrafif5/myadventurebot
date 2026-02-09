#!/usr/bin/env python3
"""
ADVENTURE QUEST - STEP-BY-STEP QUEST COMPLETION GUIDE
======================================================

Follow these steps to complete each quest and progress through the game.
"""

QUEST_GUIDE = """
╔═══════════════════════════════════════════════════════════════════════╗
║          ADVENTURE QUEST - QUEST COMPLETION GUIDE                    ║
╚═══════════════════════════════════════════════════════════════════════╝

🎯 QUEST 1: THE LOST AMULET
───────────────────────────
Location: Dark Forest
NPC: Village Elder (in Village)
Reward: 150 EXP, 100 Gold

STEPS TO COMPLETE:
1. Start in the Village
2. Talk to the Elder → Choose [1] to Talk to NPC → Select Elder
3. Accept the quest "The Lost Amulet"
4. Travel to Dark Forest (type 'dark_forest' when traveling)
5. Explore → Fight Enemy or Pick Up Item
6. Find and pick up "Lost Amulet" from the items
7. Travel back to Village
8. Talk to the Elder again
9. ✅ Quest Completed! Elder thanks you and gives rewards

KEY TIP: The amulet is one of the items in Dark Forest.


🎯 QUEST 2: DEFEAT THE BANDITS
────────────────────────────
Location: Bandit Camp
NPC: Guard Captain (in Village)
Reward: 200 EXP, 150 Gold

STEPS TO COMPLETE:
1. Talk to Guard Captain in Village → Accept quest
2. Travel to Bandit Camp (type 'bandit_camp')
3. Explore → Fight Enemy
4. Defeat the "Bandit Leader" (will be stronger than normal bandits)
   - Use regular attacks, magic attacks, and potions
   - You can buy equipment from the shop to get stronger first
5. After defeating Bandit Leader, the game confirms: "The Bandit Leader defeated!"
6. Travel back to Village
7. Talk to Guard Captain
8. ✅ Quest Completed!

KEY TIP: Buy an Iron Sword (50 gold) and Steel Armor (75 gold) before fighting
the Bandit Leader - it makes the fight MUCH easier.


🎯 QUEST 3: HEALING HERB COLLECTION
───────────────────────────────────
Location: Enchanted Grove
NPC: Grove Keeper (in Enchanted Grove)
Reward: 100 EXP, 80 Gold

STEPS TO COMPLETE:
1. Talk to Grove Keeper in Enchanted Grove → Accept quest
   (You'll need to travel there first)
2. In Enchanted Grove, Explore → Pick Up Item
3. Collect "Healing Herb" (appears multiple times - pick 5 total)
4. Once you have 5 Healing Herbs in inventory:
5. Talk to Grove Keeper again
6. ✅ Quest Completed! Grove Keeper takes the herbs

KEY TIP: Healing Herbs appear as items in the Enchanted Grove location.
Keep picking them up until you have 5.


🎯 QUEST 4: SECRETS OF THE ANCIENT RUINS
────────────────────────────────────────
Location: Ancient Ruins
NPC: Archaeologist (in Ancient Ruins)
Reward: 300 EXP, 250 Gold

STEPS TO COMPLETE:
1. Travel to Ancient Ruins (type 'ancient_ruins')
2. Talk to Archaeologist → Accept quest
3. Explore → Pick Up Item
4. Find "Mysterious Artifact" in the ruins
5. After picking up the artifact, return to Archaeologist
6. Talk to Archaeologist
7. ✅ Quest Completed!

KEY TIP: The Mysterious Artifact is one of the items in Ancient Ruins.


🎯 QUEST 5: SLAY THE DRAGON ⭐ WIN CONDITION
────────────────────────────────────────
Location: Dragon Mountain
NPC: Mountain Hermit (in Dragon Mountain)
Reward: 500 EXP, 500 Gold → WINNING THE GAME!

STEPS TO COMPLETE:
1. Get strong! Complete the other quests first and buy good gear
   - Get Iron Sword (Strength +3)
   - Get Steel Armor (Defense +5)
   - Have plenty of Health and Mana Potions
2. Travel to Dragon Mountain (type 'dragon_mountain')
3. Talk to Mountain Hermit → Accept quest
4. Explore → Fight Enemy
5. Challenge the "Dragon" (the strongest enemy)
   - This is a boss fight - it will be very difficult
   - Use magic attacks and regular attacks
   - Heal frequently with potions
   - Use Mana Potions to restore your magic power
6. Defeat the Dragon (you'll see: "The Dragon has been slain!")
7. Return to Mountain Hermit
8. Talk to Mountain Hermit
9. 🏆 YOU WIN THE GAME! 🏆

KEY TIP: Level up by defeating other enemies and completing other quests first.
The Dragon is the final boss - you MUST have good equipment and be well-leveled.


═══════════════════════════════════════════════════════════════════════

💡 PRO TIPS FOR QUEST COMPLETION:

✓ PROGRESSION ORDER:
  1. The Lost Amulet (easiest, good for starting)
  2. Healing Herb Collection (just need to collect items)
  3. Defeat the Bandits (moderate difficulty)
  4. Secrets of the Ancient Ruins (moderate difficulty)
  5. Slay the Dragon (hardest - final quest)

✓ GETTING STRONGER:
  - Visit the Merchant Shop → Buy Iron Sword (50 gold)
  - Visit the Merchant Shop → Buy Steel Armor (75 gold)
  - Fight enemies to gain experience and level up
  - Each level increases your stats automatically

✓ MANAGING RESOURCES:
  - Gold: Use for equipment and healing services
  - Health Potions: Buy for tough battles (15 gold each)
  - Rest at Inn: Restores 50 HP and 30 Mana for 10 gold (good value!)
  - Don't waste gold, save for equipment first

✓ DURING QUESTS:
  - Inventory has a limit - manage your items wisely
  - Talk to all NPCs for hints and stories
  - Complete objectives in order
  - Return to the NPC who gave the quest to complete it

═══════════════════════════════════════════════════════════════════════

🎮 IN-GAME MENU QUICK REFERENCE:

Main Menu:
  [1] Explore - Visit location, talk to NPCs, fight, pick up items
  [2] Stats - View character level, health, stats
  [3] Inventory - See items you're carrying
  [4] Quests - View active quests and objectives
  [5] Rest at Inn - Heal HP/Mana for 10 gold
  [6] Visit Shop - Buy weapons, armor, potions
  [7] Map - See all locations
  [8] Quit - Exit game

Exploration Menu:
  [1] Talk to NPC - Interact with NPCs (quest givers, quest completion)
  [2] Fight Enemy - Engage in combat
  [3] Pick up Item - Collect items from location
  [4] Travel to Location - Move to a different area

Combat Menu (during fight):
  [1] Attack - Regular attack
  [2] Magic Attack - Use mana for stronger attack
  [3] Defend - Defensive stance
  [4] Item - Use health/mana potions
  [5] Run - Try to escape (40% success rate)

═══════════════════════════════════════════════════════════════════════

NOW YOU'RE READY! Run the game with: python main.py
Good luck, adventurer! May your legend be legendary! 🏆

"""

if __name__ == "__main__":
    print(QUEST_GUIDE)
    
    # Save guide to file
    with open('QUEST_GUIDE.txt', 'w') as f:
        f.write(QUEST_GUIDE)
    print("\nGuide saved to QUEST_GUIDE.txt")
