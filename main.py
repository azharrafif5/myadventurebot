#!/usr/bin/env python3
"""
Adventure Quest: A Text-Based RPG Adventure Game
Explore a mystical realm, complete quests, and become a legendary hero!
"""

from game import Game


def main():
    """Main entry point for the adventure game."""
    print("\n" + "="*60)
    print(" "*15 + "WELCOME TO ADVENTURE QUEST")
    print(" "*10 + "A Text-Based RPG Adventure Game")
    print("="*60 + "\n")
    
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
