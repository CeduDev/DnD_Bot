# Player Discord names
CHAD_DC = "3tree6six0ti"
DORYC_DC = "acetara"
TURKEY_DC = "mr_vonbon"
DM_DC = "br4ndt7279"
ALL_CHARACTERS_DC = [CHAD_DC, DORYC_DC, TURKEY_DC, DM_DC]

# Character names
CHAD = "chad"
DORYC = "doryc"
TURKEY = "turkey"
ALL_CHARACTERS = [CHAD, DORYC, TURKEY]

# Players own bot channels
CHAD_BOT_C = "chad-solo"
DORYC_BOT_C = "doryc-solo"
TURKEY_BOT_C = "turkey-solo"
DM_BOT_C = "dm-solo"

# Players own bot channels in array form
CHAD_BOT_C_ARR = ["chad-solo"]
DORYC_BOT_C_ARR = ["doryc-solo"]
TURKEY_BOT_C_ARR = ["turkey-solo"]
DM_BOT_C_ARR = ["dm-solo", "chad-solo", "doryc-solo", "turkey-solo"]

# DC name to character dict
DC_CHAR_DICT = {CHAD_DC: CHAD, DORYC_DC: DORYC, TURKEY_DC: TURKEY}

# DC name to own bot channel array dict
DC_BOT_CHANNEL_DICT = {
    CHAD_DC: CHAD_BOT_C_ARR,
    DORYC_DC: DORYC_BOT_C_ARR,
    TURKEY_DC: TURKEY_BOT_C_ARR,
    DM_DC: DM_BOT_C_ARR,
}

# Character names allowed to modify in bot channels dict
CHAR_BOT_CHANNEL_DICT = {
    CHAD_BOT_C: [CHAD],
    DORYC_BOT_C: [DORYC],
    TURKEY_BOT_C: [TURKEY],
    DM_BOT_C: [CHAD, DORYC, TURKEY],
}

# Stat actions with description
GET = ("get", "Get")
ADD = ("add", "Add")
REMOVE = ("remove", "Remove")
SET = ("set", "Set")

ACTION_ARRAY = [GET, ADD, REMOVE, SET]

# Individual stats with description
STAT_NAME = ("name", "Name")
STAT_LEVEL = ("level", "Level")
STAT_MAX_HP = ("max_hp", "Max HP")
STAT_CURRENT_HP = ("current_hp", "Current HP")
STAT_TMP_HP = ("tmp_hp", "Temporary HP")
STAT_INITIATIVE = ("initiative", "Initiative")
STAT_ARMOR_CLASS = ("armor_class", "Armor Class")
# STAT_ = ("saving_throw_advantage", "Saving Throw Advantage")
# STAT_ = ("defenses", "Defenses")
STAT_ABILITY_SCORE = ("ability_score", "Ability Score")
STAT_ABILITY_SCORE_BASE = ("base", "Base")
STAT_ABILITY_SCORE_MODIFIER = ("modifier", "Modifier")
STAT_ABILITY_SCORE_STRENGTH = ("strength", "Strength")
STAT_ABILITY_SCORE_DEXTERITY = ("dexterity", "Dexterity")
STAT_ABILITY_SCORE_CONSTITUTION = ("constitution", "Constitution")
STAT_ABILITY_SCORE_INTELLIGENCE = ("intelligence", "Intelligence")
STAT_ABILITY_SCORE_WISDOM = ("wisdom", "Wisdom")
STAT_ABILITY_SCORE_CHARISMA = ("charisma", "Charisma")
STAT_SAVING_THROW = ("saving_throw", "Saving Throw")
STAT_SAVING_THROW_STRENGTH = ("strength", "Strength")
STAT_SAVING_THROW_DEXTERITY = ("dexterity", "Dexterity")
STAT_SAVING_THROW_CONSTITUTION = ("constitution", "Constitution")
STAT_SAVING_THROW_INTELLIGENCE = ("intelligence", "Intelligence")
STAT_SAVING_THROW_WISDOM = ("wisdom", "Wisdom")
STAT_SAVING_THROW_CHARISMA = ("charisma", "Charisma")
STAT_DEATH_SAVES = ("death_saves", "Death Saves")
STAT_DEATH_SAVES_SUCCESSES = ("successes", "Successes")
STAT_DEATH_SAVES_FAILURES = ("failures", "Failures")
STAT_SKILL_ACROBATICS = ("acrobatics", "Acrobatics")
STAT_SKILL_ANIMAL_HANDLING = ("animal_handling", "Animal Handling")
STAT_SKILL_ARCANA = ("arcana", "Arcana")
STAT_SKILL_ATHLETICS = ("athletics", "Athletics")
STAT_SKILL_DECEPTION = ("deception", "Deception")
STAT_SKILL_HISTORY = ("history", "History")
STAT_SKILL_INSIGHT = ("insight", "Insight")
STAT_SKILL_INTIMIDATION = ("intimidation", "Intimidation")
STAT_SKILL_INVESTIGATION = ("investigation", "Investigation")
STAT_SKILL_MEDICINE = ("medicine", "Medicine")
STAT_SKILL_NATURE = ("nature", "Nature")
STAT_SKILL_PERCEPTION = ("perception", "Perception")
STAT_SKILL_PERFORMANCE = ("performance", "Performance")
STAT_SKILL_PERSUASION = ("persuasion", "Persuasion")
STAT_SKILL_RELIGION = ("religion", "Religion")
STAT_SKILL_SLEIGHT_OF_HAND = ("sleight_of_hand", "Sleight of Hand")
STAT_SKILL_STEALTH = ("stealth", "Stealth")
STAT_SKILL_SURVIVAL = ("survival", "Survival")

# General stat array
STAT_ARRAY = [
    STAT_LEVEL,
    STAT_MAX_HP,
    STAT_CURRENT_HP,
    STAT_TMP_HP,
    STAT_INITIATIVE,
    STAT_ARMOR_CLASS,
]

# Death saves array
DEATH_SAVES_ARR = [STAT_DEATH_SAVES_SUCCESSES, STAT_DEATH_SAVES_FAILURES]

# Ability score array
ABILITY_SCORE_ARRAY = [
    STAT_ABILITY_SCORE_STRENGTH,
    STAT_ABILITY_SCORE_DEXTERITY,
    STAT_ABILITY_SCORE_CONSTITUTION,
    STAT_ABILITY_SCORE_INTELLIGENCE,
    STAT_ABILITY_SCORE_WISDOM,
    STAT_ABILITY_SCORE_CHARISMA,
]

# Saving throws array
SAVING_THROW_ARRAY = [
    STAT_SAVING_THROW_STRENGTH,
    STAT_SAVING_THROW_DEXTERITY,
    STAT_SAVING_THROW_CONSTITUTION,
    STAT_SAVING_THROW_INTELLIGENCE,
    STAT_SAVING_THROW_WISDOM,
    STAT_SAVING_THROW_CHARISMA,
]

# Skill array
STAT_SKILL_ARRAY = [
    STAT_SKILL_ACROBATICS,
    STAT_SKILL_ANIMAL_HANDLING,
    STAT_SKILL_ARCANA,
    STAT_SKILL_ATHLETICS,
    STAT_SKILL_DECEPTION,
    STAT_SKILL_HISTORY,
    STAT_SKILL_INSIGHT,
    STAT_SKILL_INTIMIDATION,
    STAT_SKILL_INVESTIGATION,
    STAT_SKILL_MEDICINE,
    STAT_SKILL_NATURE,
    STAT_SKILL_PERCEPTION,
    STAT_SKILL_PERFORMANCE,
    STAT_SKILL_PERSUASION,
    STAT_SKILL_RELIGION,
    STAT_SKILL_SLEIGHT_OF_HAND,
    STAT_SKILL_STEALTH,
    STAT_SKILL_SURVIVAL,
]

# Commands
HELP_COMMAND = "help"
CAST_DICE_COMMAND = "cast_dice"
GET_CHARACTER_STAT_COMMAND = "get_stats"
FUNNY1_COMMAND = "kikkeli"
FUNNY2_COMMAND = "pippeli"
SKILL_COMMAND = "skill"
STAT_COMMAND = "stat"
DEATH_SAVES_COMMAND = "death_saves"
SAVING_THROWS_COMMAND = "saving_throws"
ABILITY_SCORE_COMMAND = "ability_score"

# Regexes
ONE_OR_TWO_DIGIT_REGEX = "^\\d{1,2}$"
