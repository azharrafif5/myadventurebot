"""Player class for managing character attributes and progression."""


class Player:
    """Represents the player character with stats, inventory, and quest tracking."""
    
    def __init__(self, name):
        """Initialize the player with starting attributes."""
        self.name = name
        self.level = 1
        self.experience = 0
        self.max_health = 100
        self.health = self.max_health
        self.max_mana = 50
        self.mana = self.max_mana
        self.strength = 10
        self.defense = 5
        self.magic = 8
        
        self.inventory = []
        self.gold = 50
        self.quests = {}  # quest_id: quest_data
        self.completed_quests = set()
        self.current_location = "village"
        self.equipment = {
            "weapon": None,
            "armor": None,
        }
        
        # Quest tracking flags
        self._bandit_leader_defeated = False
        self._dragon_defeated = False
        
    def add_experience(self, amount):
        """Add experience points and check for level up."""
        self.experience += amount
        exp_required = 100 * self.level
        if self.experience >= exp_required:
            self.level_up()
    
    def level_up(self):
        """Level up the player and increase stats."""
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.max_mana += 10
        self.mana = self.max_mana
        self.strength += 2
        self.defense += 1
        self.magic += 2
        print(f"\n🎉 LEVEL UP! You are now level {self.level}!")
        print(f"   Max Health: +20 (now {self.max_health})")
        print(f"   Strength: +2 (now {self.strength})")
        
    def add_item(self, item):
        """Add an item to inventory."""
        self.inventory.append(item)
        
    def remove_item(self, item):
        """Remove an item from inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            
    def heal(self, amount):
        """Restore health."""
        self.health = min(self.health + amount, self.max_health)
        
    def restore_mana(self, amount):
        """Restore mana."""
        self.mana = min(self.mana + amount, self.max_mana)
        
    def add_gold(self, amount):
        """Add gold to inventory."""
        self.gold += amount
        
    def spend_gold(self, amount):
        """Spend gold if player has enough."""
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    def add_quest(self, quest_id, quest_data):
        """Add a quest to the player's quest log."""
        self.quests[quest_id] = quest_data
        
    def complete_quest(self, quest_id):
        """Mark a quest as completed."""
        if quest_id in self.quests:
            self.completed_quests.add(quest_id)
            del self.quests[quest_id]
            
    def get_stats(self):
        """Return player stats as a formatted string."""
        stats = f"""
╔═══════════════════════════════════════════════════════════╗
║                    CHARACTER STATS                        ║
╠═══════════════════════════════════════════════════════════╣
║ Name:        {self.name:43} ║
║ Level:       {self.level:<43} ║
║ Experience:  {self.experience}/{100 * self.level:<40} ║
║                                                           ║
║ Health:      {self.health}/{self.max_health:<43} ║
║ Mana:        {self.mana}/{self.max_mana:<45} ║
║ Gold:        {self.gold:<43} ║
║                                                           ║
║ Strength:    {self.strength:<43} ║
║ Defense:     {self.defense:<43} ║
║ Magic:       {self.magic:<43} ║
║                                                           ║
║ Weapon:      {str(self.equipment['weapon'] or 'None'):<43} ║
║ Armor:       {str(self.equipment['armor'] or 'None'):<43} ║
║ Inventory:   {len(self.inventory)} items{'':<39} ║
╚═══════════════════════════════════════════════════════════╝
"""
        return stats
    
    def get_inventory(self):
        """Return inventory as a formatted string."""
        if not self.inventory:
            return "Your inventory is empty."
        
        items_str = "\n".join([f"  • {item}" for item in self.inventory])
        return f"Inventory ({len(self.inventory)} items):\n{items_str}"
    
    def get_quests(self):
        """Return active quests as a formatted string."""
        if not self.quests:
            return "You have no active quests."
        
        quests_str = []
        for quest_id, quest in self.quests.items():
            quests_str.append(f"  • [{quest_id}] {quest['name']}\n    {quest['description']}")
        
        return "Active Quests:\n" + "\n".join(quests_str)
