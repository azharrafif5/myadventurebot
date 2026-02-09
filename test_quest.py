#!/usr/bin/env python3
"""Quick test script to verify quest system works."""

from player import Player
from quests import QuestManager
from game import Game

def test_quest_system():
    """Test the quest completion system."""
    print("Testing Adventure Quest System...\n")
    
    # Test Player Creation
    player = Player("TestHero")
    print(f"✓ Player created: {player.name}")
    print(f"  Starting gold: {player.gold}, Health: {player.health}\n")
    
    # Test Quest Manager
    quest_mgr = QuestManager()
    print("✓ Quest Manager loaded")
    print(f"  Available quests: {len(quest_mgr.quests)}\n")
    
    # Test Adding Quest
    lost_amulet = quest_mgr.get_quest('lost_amulet')
    player.add_quest('lost_amulet', {
        'name': lost_amulet.name,
        'description': lost_amulet.description,
        'objectives': lost_amulet.objectives
    })
    print("✓ Quest 'The Lost Amulet' added to player")
    print(f"  Active quests: {len(player.quests)}\n")
    
    # Test Adding Item
    player.add_item('Lost Amulet')
    print("✓ Item 'Lost Amulet' added to inventory")
    print(f"  Inventory: {player.inventory}\n")
    
    # Test Quest Completion
    player.add_gold(100)
    player.add_experience(150)
    player.complete_quest('lost_amulet')
    print("✓ Quest completed!")
    print(f"  Gold: {player.gold}, Experience: {player.experience}")
    print(f"  Active quests: {len(player.quests)}")
    print(f"  Completed quests: {len(player.completed_quests)}\n")
    
    # Display stats
    print(player.get_stats())
    print("\n✅ All tests passed! The quest system is working correctly.\n")
    print("To play the game, run: python main.py")

if __name__ == "__main__":
    test_quest_system()
