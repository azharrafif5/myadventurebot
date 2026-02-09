"""Quest system for managing quests and objectives."""


class Quest:
    """Base class for quests."""
    
    def __init__(self, quest_id, name, description, objectives, reward_exp, reward_gold):
        self.quest_id = quest_id
        self.name = name
        self.description = description
        self.objectives = objectives  # Dict of objective_id: description
        self.completed_objectives = set()
        self.reward_exp = reward_exp
        self.reward_gold = reward_gold
        self.completed = False
        
    def complete_objective(self, objective_id):
        """Mark an objective as completed."""
        if objective_id in self.objectives:
            self.completed_objectives.add(objective_id)
            self._check_quest_completion()
            
    def _check_quest_completion(self):
        """Check if all objectives are completed."""
        if len(self.completed_objectives) == len(self.objectives):
            self.completed = True
            
    def is_completed(self):
        """Return whether the quest is completed."""
        return self.completed
    
    def get_progress(self):
        """Return quest progress as a string."""
        progress = f"\n📋 Quest: {self.name}\n"
        progress += f"   {self.description}\n"
        progress += f"   Progress: {len(self.completed_objectives)}/{len(self.objectives)}\n"
        progress += f"   Objectives:\n"
        
        for obj_id, obj_desc in self.objectives.items():
            status = "✓" if obj_id in self.completed_objectives else "✗"
            progress += f"   {status} {obj_desc}\n"
        
        progress += f"   Rewards: {self.reward_exp} EXP, {self.reward_gold} Gold"
        return progress


class QuestManager:
    """Manages all available quests for the game."""
    
    def __init__(self):
        """Initialize quest manager with all available quests."""
        self.quests = self._create_quests()
    
    def _create_quests(self):
        """Create and return all available quests."""
        quests = {}
        
        # Quest 1: The Lost Amulet
        quests['lost_amulet'] = Quest(
            quest_id='lost_amulet',
            name='The Lost Amulet',
            description='The village elder lost a sacred amulet in the Dark Forest. Find it and return it.',
            objectives={
                'explore_forest': 'Explore the Dark Forest',
                'find_amulet': 'Find the Lost Amulet',
                'return_amulet': 'Return to the Elder'
            },
            reward_exp=150,
            reward_gold=100
        )
        
        # Quest 2: Defeat the Bandits
        quests['defeat_bandits'] = Quest(
            quest_id='defeat_bandits',
            name='Defeat the Bandits',
            description='Bandits have been terrorizing the roads. Defeat them to save the village!',
            objectives={
                'find_bandits': 'Locate the bandit camp',
                'defeat_leader': 'Defeat the Bandit Leader',
                'report_victory': 'Report back to the Guard Captain'
            },
            reward_exp=200,
            reward_gold=150
        )
        
        # Quest 3: Collect Herbs
        quests['collect_herbs'] = Quest(
            quest_id='collect_herbs',
            name='Healing Herb Collection',
            description='The healer needs rare healing herbs from the Enchanted Grove.',
            objectives={
                'reach_grove': 'Journey to the Enchanted Grove',
                'collect_herbs': 'Collect 5 Healing Herbs',
                'deliver_herbs': 'Deliver herbs to the Healer'
            },
            reward_exp=100,
            reward_gold=80
        )
        
        # Quest 4: Ancient Ruins
        quests['ancient_ruins'] = Quest(
            quest_id='ancient_ruins',
            name='Secrets of the Ancient Ruins',
            description='Explore the Ancient Ruins and retrieve the mysterious artifact.',
            objectives={
                'reach_ruins': 'Navigate to the Ancient Ruins',
                'solve_puzzle': 'Solve the ancient puzzle',
                'obtain_artifact': 'Obtain the Mysterious Artifact',
                'escape_ruins': 'Escape the collapsing ruins'
            },
            reward_exp=300,
            reward_gold=250
        )
        
        # Quest 5: Dragon Slayer
        quests['slay_dragon'] = Quest(
            quest_id='slay_dragon',
            name='Slay the Dragon',
            description='A mighty dragon threatens the kingdom. You are the only one who can stop it!',
            objectives={
                'reach_mountain': 'Reach Dragon Mountain',
                'face_dragon': 'Confront the Dragon',
                'slay_dragon': 'Defeat the Dragon',
                'claim_treasure': 'Claim the Dragon\'s Treasure'
            },
            reward_exp=500,
            reward_gold=500
        )
        
        return quests
    
    def get_quest(self, quest_id):
        """Get a quest by ID."""
        return self.quests.get(quest_id)
    
    def get_all_quests(self):
        """Return all available quests."""
        return self.quests
    
    def list_quests(self):
        """Return a formatted list of all quests."""
        quest_list = "═══════════════════════════════════════════════════════════\n"
        quest_list += "                    AVAILABLE QUESTS                       \n"
        quest_list += "═══════════════════════════════════════════════════════════\n"
        
        for quest_id, quest in self.quests.items():
            quest_list += f"\n[{quest_id.upper()}] {quest.name}\n"
            quest_list += f"   {quest.description}\n"
            quest_list += f"   Reward: {quest.reward_exp} EXP, {quest.reward_gold} Gold\n"
        
        return quest_list
