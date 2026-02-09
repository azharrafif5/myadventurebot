#!/usr/bin/env python3
"""
Quick Reference Card - What Happens at Each Quest Step
"""

QUICK_REF = """
╔═══════════════════════════════════════════════════════════════════════╗
║          QUEST COMPLETION QUICK REFERENCE CARD                       ║
╚═══════════════════════════════════════════════════════════════════════╝

🎯 ALL FIVE QUESTS - WHAT YOU'LL SEE AT EACH STEP:


QUEST 1: THE LOST AMULET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: Accept Quest           STEP 2: Find Item in Forest
─────────────────────         ─────────────────────────
Elder: Take this quest        You'll see:
                              ✓ You picked up: Lost Amulet
                              💡 HINT: Return to ELDER!

                              STEP 3: Return & Collect Reward
                              ────────────────────────────
                              Elder: Thank you!
                              🎉 Quest Complete!
                              💡 NEXT: Talk to Guard Captain


QUEST 2: DEFEAT THE BANDITS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: Accept Quest           STEP 2: Defeat Boss
─────────────────────         ─────────────────
Guard Captain: Go fight       Battle the Bandit Leader
               bandits        🎉 Victory!
                              💀 Boss defeated!
                              💡 HINT: Return to Guard Captain!

                              STEP 3: Return & Collect Reward
                              ────────────────────────────
                              Captain: You're a hero!
                              🎉 Quest Complete!
                              💡 NEXT: Explore more


QUEST 3: COLLECT HEALING HERBS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: Accept Quest           STEP 2a-2d: Collect Herbs (1-4)
─────────────────────         ──────────────────────────────
Grove Keeper: Get herbs       Each pickup shows:
              for healer      ✓ You picked up: Healing Herb
                              💡 HINT: Collect 5 total
                              Need to get: X more

                              STEP 2e: Collect 5th Herb
                              ────────────────────
                              ✓ All 5 herbs collected!
                              💡 HINT: Return to Grove Keeper!

                              STEP 3: Return & Collect Reward
                              ────────────────────────────
                              Keeper: Perfect! Thank you!
                              🎉 Quest Complete!
                              💡 NEXT: Visit Ancient Ruins


QUEST 4: ANCIENT RUINS ARTIFACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: Accept Quest           STEP 2: Find Artifact
─────────────────────         ──────────────────
Archaeologist: Find           You'll see:
               artifact       ✓ You picked up: Mysterious Artifact
                              💡 HINT: Return to Archaeologist!

                              STEP 3: Return & Collect Reward
                              ────────────────────────────
                              Archaeologist: Incredible!
                              🎉 Quest Complete!
                              💡 NEXT: Dragon Mountain!


QUEST 5: SLAY THE DRAGON ⭐ FINAL QUEST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STEP 1: Accept Quest           STEP 2: Epic Battle
─────────────────────         ────────────────
Mountain Hermit:              Defeat the Dragon
Go slay it!                    🎉 LEGENDARY VICTORY!
                              🐉 The Dragon slain!
                              💡 HINT: Return to Mountain Hermit!

                              STEP 3: You Win the Game!
                              ──────────────────────
                              Hermit: You're a legend!
                              🏆 YOU WON THE GAME! 🏆
                              Rewards + Victory!


═════════════════════════════════════════════════════════════════════════

💡 THE HINT SYSTEM EXPLAINED:

WHEN YOU PICK UP AN ITEM:
┌─────────────────────────────────────────────────────────┐
│ ✓ You picked up: [Item Name]                            │
│                                                          │
│ 💡 HINT: [Specific instruction for this item]          │
│    → What to do next (e.g., "Return to Village")       │
│    → Who to talk to (e.g., "Talk to Elder")            │
└─────────────────────────────────────────────────────────┘

WHEN YOU DEFEAT A BOSS:
┌─────────────────────────────────────────────────────────┐
│ 💀/🐉 Boss Name defeated!                               │
│                                                          │
│ 💡 HINT: [Next instruction]                            │
│    → Where to go (e.g., "Back to Guard Captain")       │
│    → What to do (e.g., "Complete the quest")           │
└─────────────────────────────────────────────────────────┘

WHEN YOU COMPLETE A QUEST:
┌─────────────────────────────────────────────────────────┐
│ 🎉 You completed the quest: [Quest Name]!               │
│    Received XXX EXP and XXX Gold!                       │
│                                                          │
│ 💡 NEXT: [Hint for the next quest or exploration]      │
└─────────────────────────────────────────────────────────┘

IF YOU TALK TO NPC WITHOUT OBJECTIVES:
┌─────────────────────────────────────────────────────────┐
│ NPC: [Dialogue asking for objective]                    │
│                                                          │
│ 💡 HINT: [Exact location or action needed]             │
└─────────────────────────────────────────────────────────┘


═════════════════════════════════════════════════════════════════════════

🎮 PLAYING WITH HINTS - SIMPLE FLOW:

Quest Item Pickup
    ↓
See Hint (what to do)
    ↓
Follow Hint
    ↓
Return to NPC
    ↓
Quest Complete!
    ↓
See Next Quest Hint
    ↓
Move to Next Quest
    ↓
Repeat until Dragon Slayed!
    ↓
🏆 YOU WIN! 🏆


═════════════════════════════════════════════════════════════════════════

✅ NO MORE CONFUSION:

❌ OLD WAY (without hints):
"I picked up the amulet... now what?"
"Did I defeat the bandit leader correctly?"
"What should I do after getting the herbs?"

✅ NEW WAY (with hints):
"I picked up the amulet!" ← Game shows: "Go talk to Elder in Village"
"I defeated the bandit!" ← Game shows: "Return to Guard Captain"
"I got all 5 herbs!" ← Game shows: "Talk to Grove Keeper"


═════════════════════════════════════════════════════════════════════════

🚀 READY TO PLAY!

Run: python main.py

The game will automatically guide you through every quest step with:
✓ Clear hints
✓ Next step directions
✓ Location guidance
✓ NPC dialogue
✓ Progress tracking

ENJOY YOUR ADVENTURE! 🎮

═════════════════════════════════════════════════════════════════════════
"""

print(QUICK_REF)
