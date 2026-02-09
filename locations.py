"""Game locations and world map."""


class Location:
    """Represents a location in the game world."""
    
    def __init__(self, name, description, enemies=None, items=None, npcs=None):
        self.name = name
        self.description = description
        self.enemies = enemies or []
        self.items = items or []
        self.npcs = npcs or {}  # npc_id: npc_data
        self.visited = False
        
    def get_description(self):
        """Return the location description."""
        desc = f"\n🌍 [{self.name}]\n"
        desc += f"{self.description}\n"
        
        if self.enemies:
            desc += f"\n⚔️  Enemies here: {', '.join(self.enemies)}\n"
        if self.items:
            desc += f"📦 Items available: {', '.join(self.items)}\n"
        if self.npcs:
            desc += f"👥 NPCs: {', '.join(self.npcs.keys())}\n"
        
        return desc


class World:
    """Manages all game locations."""
    
    def __init__(self):
        """Initialize the game world."""
        self.locations = self._create_world()
        self.current_location = None
    
    def _create_world(self):
        """Create all game locations."""
        locations = {}
        
        # Starting location
        locations['village'] = Location(
            name='The Starting Village',
            description='A peaceful village where your adventure begins. The town square is bustling with activity.',
            items=['Health Potion'],
            npcs={
                'Elder': 'The village elder can give you quests',
                'Guard Captain': 'Protects the village',
                'Healer': 'Can heal your wounds for Gold'
            }
        )
        
        # Dark Forest
        locations['dark_forest'] = Location(
            name='The Dark Forest',
            description='A dense, dark forest filled with mysterious sounds. Tall trees block out most of the sunlight.\nThis is where the Lost Amulet awaits discovery.',
            enemies=['Goblin', 'Goblin', 'Wolf', 'Shadow Creature'],
            items=['Lost Amulet', 'Herb', 'Herb', 'Gold Coin'],
            npcs={
                'Hermit': 'An old hermit living in the forest'
            }
        )
        
        # Bandit Camp
        locations['bandit_camp'] = Location(
            name='The Bandit Camp',
            description='A hidden camp in the hills where bandits have been gathering.\nThe air is tense and filled with danger.',
            enemies=['Bandit', 'Bandit', 'Bandit', 'Bandit Leader'],
            items=['Bandit Gold', 'Leather Armor', 'Iron Sword'],
            npcs={
                'Bandit Leader': 'The ruthless leader of the bandits'
            }
        )
        
        # Enchanted Grove
        locations['enchanted_grove'] = Location(
            name='The Enchanted Grove',
            description='A beautiful and magical forest grove. Strange plants glow with magical energy.\nRare healing herbs grow abundantly here.',
            enemies=['Magic Sprite', 'Enchanted Wolf'],
            items=['Healing Herb', 'Healing Herb', 'Healing Herb', 'Healing Herb', 'Healing Herb', 'Mana Potion'],
            npcs={
                'Grove Keeper': 'A mystical guardian of the grove'
            }
        )
        
        # Ancient Ruins
        locations['ancient_ruins'] = Location(
            name='The Ancient Ruins',
            description='Mysterious structures of an ancient civilization. Strange symbols cover the walls.\nAn ancient power emanates from deep within.',
            enemies=['Stone Golem', 'Skeleton', 'Skeleton Warrior', 'Ancient Guardian'],
            items=['Mysterious Artifact', 'Ancient Scroll', 'Gold Coin'],
            npcs={
                'Archaeologist': 'A scholar studying these ruins'
            }
        )
        
        # Dragon Mountain
        locations['dragon_mountain'] = Location(
            name='Dragon Mountain',
            description='A towering mountain peak shrouded in clouds and smoke.\nLegendary tales speak of dragon treasure hidden here.',
            enemies=['Drake', 'Drake', 'Dragon'],
            items=['Dragon Fang', 'Dragon\'s Treasure', 'Ancient Gem'],
            npcs={
                'Mountain Hermit': 'A dangerous dragon lives on this mountain'
            }
        )
        
        # Tavern
        locations['tavern'] = Location(
            name='The Dragon\'s Tavern',
            description='A cozy tavern filled with adventurers and traders.\nThe smell of ale and roasted meat fills the air.',
            items=['Ale', 'Bread'],
            npcs={
                'Bartender': 'Serves food and drinks',
                'Merchant': 'Sells rare items',
                'Storyteller': 'Tells tales of adventure'
            }
        )
        
        # Merchant Shop
        locations['merchant_shop'] = Location(
            name='The Merchant\'s Shop',
            description='A small but well-stocked shop selling weapons and armor.\nThe merchant has items for adventurers of all levels.',
            npcs={
                'Merchant': 'Sells weapons, armor, and potions'
            }
        )
        
        # Healing Temple
        locations['healing_temple'] = Location(
            name='The Healing Temple',
            description='A sacred temple dedicated to healing magic.\nYou feel rejuvenated just by being here.',
            npcs={
                'High Priestess': 'Can fully restore your health and mana for a price'
            }
        )
        
        return locations
    
    def get_location(self, location_id):
        """Get a location by ID."""
        return self.locations.get(location_id)
    
    def travel_to(self, location_id):
        """Travel to a location."""
        location = self.get_location(location_id)
        if location:
            self.current_location = location_id
            location.visited = True
            return location
        return None
    
    def list_locations(self):
        """Return a formatted list of all available locations."""
        loc_list = "═══════════════════════════════════════════════════════════\n"
        loc_list += "                   GAME LOCATIONS                          \n"
        loc_list += "═══════════════════════════════════════════════════════════\n"
        
        for loc_id, location in self.locations.items():
            loc_list += f"\n[{loc_id.upper()}] {location.name}\n"
            loc_list += f"   {location.description[:100]}...\n"
        
        return loc_list


# Shortcuts for location IDs
VILLAGE = 'village'
DARK_FOREST = 'dark_forest'
BANDIT_CAMP = 'bandit_camp'
ENCHANTED_GROVE = 'enchanted_grove'
ANCIENT_RUINS = 'ancient_ruins'
DRAGON_MOUNTAIN = 'dragon_mountain'
TAVERN = 'tavern'
MERCHANT_SHOP = 'merchant_shop'
HEALING_TEMPLE = 'healing_temple'
