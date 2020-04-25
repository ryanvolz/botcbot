"""Contains the base game characters' rules texts."""

rules_texts = {
    "Character": "Character. If you're seeing this, something has gone wrong.",
    "Townsfolk": "Townsfolk. If you're seeing this, something has gone wrong.",
    "Outsider": "Outsider. If you're seeing this, something has gone wrong.",
    "Minion": "Minion. If you're seeing this, something has gone wrong.",
    "Demon": "Demon. If you're seeing this, something has gone wrong.",
    "Traveler": "Traveler. If you're seeing this, something has gone wrong.",
    "Storyteller": "Storyteller. If you're seeing this, something has (probably) gone wrong.",
    "Witch": "Each night, choose a player: if they nominate tomorrow, they die. If just 3 players live, you lose this ability.",
    "NoDashii": "Each night\\*, choose a player: they die. Your 2 Townsfolk neighbours are poisoned.",
    "Monk": "Each night\\*, choose a player (not yourself): they are safe from the Demon tonight.",
    "Empath": "Each night, you learn how many of your 2 alive neighbours are evil.",
    "Cerenovus": 'Each night, choose a player & a good character: they are "mad" they are this character tomorrow, or might be executed.',
    "Chambermaid": "Each night, choose 2 alive players (not yourself): you learn how many wake tonight due to their character ability.",
    "Clockmaker": "You start knowing how many steps from the Demon to its nearest Minion.",
    "Innkeeper": "Each night\\*, choose 2 players: they can't die tonight, but 1 is drunk until dusk.",
    "Pacifist": "Executed good players might not die.",
    "Juggler": "On your 1st day, publicly guess up to 5 players' characters. That night, you learn how many you got correct.",
    "Shabaloth": "Each night\\*, choose 2 players: they die. A dead player you chose last night might be regurgitated.",
    "Sage": "If the Demon kills you, you learn that it is 1 of 2 players.",
    "Recluse": "You might register as evil & as a Minion or Demon, even if dead.",
    "Mastermind": "If the Demon dies by execution, play for one more day. If a player is then executed, their team loses.",
    "SnakeCharmer": "Each night, choose an alive player: a chosen Demon swaps characters & alignments with you & is then poisoned.",
    "Baron": "There are extra Outsiders in play. [+2 Outsiders]",
    "Courtier": "Once per game, at night, choose a character: they are drunk for 3 nights & 3 days.",
    "DevilSAdvocate": "Each night, choose a living player (not the same as last night): if executed tomorrow, they don't die.",
    "Sailor": "Each night, choose a player: either you or they are drunk until dusk. You can't die.",
    "Moonchild": "When you learn that you died, choose 1 alive player: if good, they die tonight.",
    "TeaLady": "If both your alive neighbours are good, they can't die.",
    "Assassin": "Once per game, at night\\*, choose a player: they die, even if for some reason they could not.",
    "Dreamer": "Each night, choose a player (not yourself): you learn 1 good & 1 evil character, 1 of which is correct.",
    "Ravenkeeper": "If you die at night, you are woken to choose a player: you learn their character.",
    "Librarian": "You start knowing that 1 of 2 players is a particular Outsider. (Or that zero are in play)",
    "Gambler": "Each night\\*, choose a player & guess their character: if you guess wrong, you die.",
    "Flowergirl": "Each night\\*, you learn if the Demon voted today.",
    "Spy": "Each night, you see the Grimoire. You might register as good & as a Townsfolk or Outsider, even if dead.",
    "Fool": "The first time you die, you don't.",
    "Washerwoman": "You start knowing that 1 of 2 players is a particular Townsfolk.",
    "Tinker": "You might die at any time.",
    "Sweetheart": "If you die, 1 player is drunk from now on.",
    "FangGu": "Each night\\*, choose a player: they die. The 1st Outsider chosen becomes an evil Fang Gu & you die instead. [+1 Outsider]",
    "Exorcist": "Each night\\*, choose a player (not the same as last night): the Demon, if chosen, learns who you are & doesn't act tonight.",
    "Klutz": "When you learn that you died, publicly choose an alive good player, or your team loses.",
    "Mathematician": "Each night, you learn how many players' abilities worked abnormally (since dawn) due to another character\xe2\x80\x99s ability.",
    "Butler": "Each night, choose a player (not yourself): tomorrow, you may only vote if they are voting too.",
    "Undertaker": "Each night\\*, you learn which character died by execution today.",
    "Artist": "Once per game, during the day, privately ask the Storyteller any yes/no question.",
    "Poisoner": "Each night, choose a player: their ability malfunctions tonight and tomorrow day.",
    "Barber": "If you die, tonight the Demon may choose 2 players to swap characters.",
    "Grandmother": "You start knowing a good player & character. If the Demon kills them, you die too.",
    "Pukka": "Each night, choose a player: they are poisoned until tomorrow night, then die. You act on the 1st night.",
    "Professor": "Once per game, at night\\*, choose a dead player: if they are a Townsfolk, they are resurrected.",
    "Savant": "Each day, you may visit the Storyteller to learn 2 things in private: 1 is true & 1 is false.",
    "Zombuul": "Each night\\*, if no one died today, choose a player: they die. The 1st time you die, you live but register as dead.",
    "PitHag": "Each night\\*, choose a player & a character they become (if not in play). If a Demon is made, deaths tonight are arbitrary.",
    "Virgin": "The 1st time you are nominated, if the nominator is a Townsfolk, they are executed immediately.",
    "Gossip": "Each day, you may make a public statement. Tonight, if it was true, a player dies.",
    "Seamstress": "Once per game, at night, choose 2 players (not yourself): you learn if they are the same alignment.",
    "TownCrier": "Each night\\*, you learn if a Minion nominated that day.",
    "Po": "Each night,\\* you may choose a player: they die. If you chose no one last night, choose 3 players tonight.",
    "Philosopher": "Once per game, at night, choose a good character: become them. If you duplicate an in-play character, they are drunk.",
    "Saint": "If you are executed, your team loses.",
    "Oracle": "Each night\\*, you learn how many dead players are evil.",
    "FortuneTeller": "Each night, choose 2 players: you learn if either is a Demon. There is 1 good player that registers falsely to you.",
    "Investigator": "You start knowing that 1 of 2 players is a particular Minion.",
    "Slayer": "Once per game, during the day, publicly choose a player: if they are the Demon, they die.",
    "Lunatic": "You think you are a Demon, but your abilities malfunction. The Demon knows who you are & who you attack.",
    "ScarletWoman": "If there are 5 or more players alive & the Demon dies, you become the Demon. (Travelers don't count)",
    "Soldier": "You are safe from the Demon.",
    "Vortox": "Each night\\*, choose a player: they die. Good abilities yield false information. Each day, if no one is executed, evil wins.",
    "Chef": "You start knowing how many pairs of evil players there are.",
    "Drunk": "You do not know you are the Drunk. You think you are a Townsfolk, but your ability malfunctions.",
    "EvilTwin": "You & an opposing player know each other. If the good player is executed, evil wins. Good can't win if you both live.",
    "Godfather": "You start knowing which Outsiders are in play. If 1 died today, choose a player tonight: they die. [-1 or +1 Outsider]",
    "Imp": "Each night\\*, choose a player: they die. If you kill yourself this way, a Minion becomes the Imp.",
    "Vigormortis": "Each night\\*, choose a player: they die. Minions you kill keep their ability & poison 1 Townsfolk neighbour. [-1 Outsider]",
    "Goon": "Each night, the 1st player to choose you with their ability is drunk until dusk. You become their alignment.",
    "Minstrel": "If a Minion died today, all other players (except Travellers) are drunk all night, until dusk.",
    "Mutant": 'If you are "mad" about being an Outsider, you might be executed.',
    "Mayor": "If only 3 players live & no execution occurs, your team wins. If you die at night, another player might die instead.",
}