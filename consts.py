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

# DC name to character dict
DC_CHAR_DICT = {CHAD_DC: CHAD, DORYC_DC: DORYC, TURKEY_DC: TURKEY}

# DC name to own bot channel dict
DC_BOT_CHANNEL_DICT = {
    CHAD_DC: CHAD_BOT_C,
    DORYC_DC: DORYC_BOT_C,
    TURKEY_DC: TURKEY_BOT_C,
    DM_DC: DM_BOT_C,
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
# STAT_ = ("death_saves", "Death Saves")
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

# Regexes
ONE_OR_TWO_DIGIT_REGEX = "^\\d{1,2}$"
