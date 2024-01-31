from consts import (
    HELP_COMMAND,
    CAST_DICE_COMMAND_GENERAL,
    CAST_DICE_COMMAND_SKILL,
    CAST_DICE_COMMAND_SAVING,
    CAST_DICE_COMMAND_DEATH_SAVE,
    GET_CHARACTER_STAT_COMMAND,
    SKILL_COMMAND,
    STAT_COMMAND,
    DEATH_SAVES_COMMAND,
    SAVING_THROWS_COMMAND,
    ABILITY_SCORE_COMMAND,
)

CAST_DICE_DESCRIPTION_GENERAL = "Beware cryptic general dice! Honor sacred numerals 2, 4, 6, 8, 9, 12, 20 for destiny's true reveal."

# CAST_DICE_DESCRIPTION_ATTACK = "Beware cryptic attack dice!"

CAST_DICE_DESCRIPTION_SKILL = "Beware cryptic attack dice!"

CAST_DICE_DESCRIPTION_SAVING = "Beware cryptic saving dice!"

CAST_DICE_DESCRIPTION_DEATH_SAVE = "Beware cryptic death save dice!"

GET_CHARACTER_STAT_DESCRIPTION = "Invoke your character's name for mystic insights; the Dungeon Master alone commands its full power."

HELP_DESCRIPTION = "Scroll reveals mystic secrets, guiding thee on thy journey."

SKILL_DESCRIPTION = "Mystic command shaping the skill destiny in our digital tapestry."

STAT_DESCRIPTION = "Mystic command shaping the general stats in our digital tapestry."

DEATH_SAVES_DESCRIPTION = (
    "Mystic command shaping the death saves in our digital tapestry."
)

SAVING_THROWS_DESCRIPTION = (
    "Mystic command shaping the saving throws in our digital tapestry."
)

ABILITY_SCORE_DESCRIPTION = (
    "Mystic command shaping the ability scores in our digital tapestry."
)

UNKNOWN_COMMAND_TEXT = f"""
Hail, seeker of the arcane! Thy attempt at an unknown command hath stirred the ethereal winds. Fear not, for guidance lies in the sacred "/{HELP_COMMAND}" command, unveiling the secrets of our realm. Let the mystic incantations guide thee, and may the digital ether reveal its wisdom on this path of discovery.
"""

HELP_TEXT1 = f"""

Greetings, noble user of the arcane arts! Behold the mystic commands at your disposal:

/{HELP_COMMAND}:
Ah, ye seeker of wisdom, to unravel the mysteries, invoke this incantation "/{HELP_COMMAND}". A scroll of knowledge shall be revealed, unfurling the secrets of our mystical realm to guide thee on thine journey.

/{CAST_DICE_COMMAND_GENERAL}:
Venture forth into the unknown with the command "/{CAST_DICE_COMMAND_GENERAL}" Craft your fate by providing a single or double-digit offering, forsooth, but beware, for only the digits 4, 6, 8, 9, 12, and 20 are permitted in this sacred chant. May the roll of the enchanted dice shape thy destiny and unveil the path that lies ahead.

/{CAST_DICE_COMMAND_SKILL}: <skill> <character>:
Behold, noble seeker! The command '/{CAST_DICE_COMMAND_SKILL} <skill> <character>' beckons you to cast the sacred 20-sided dice, infusing the result with your skill's mystic modifier. May this enchantment unfold the fortunes of your character in the cosmic dance of our digital realm.

/{CAST_DICE_COMMAND_SAVING}: <saving_type> <character>:
Hearken, intrepid adventurer! Unveil the command '/{CAST_DICE_COMMAND_SAVING} <saving_type> <character>', an arcane ritual to cast the sacred 20-sided dice, enhancing the outcome with your saving modifier. May this mystic incantation guide your character through the perilous dance of our digital tapestry.

/{CAST_DICE_COMMAND_DEATH_SAVE}: <character>:
Hark, brave seeker! Behold the command '/{CAST_DICE_COMMAND_DEATH_SAVE} <character>' — a mystical incantation casting a 50/50 fate. Should the dice foretell failure, it adds to the count of dire death throws; success, it augments the tally of triumphant revival throws. May this arcane dice ritual shape the destiny of thy character in the intricate dance of our digital realm.
"""

HELP_TEXT2 = f"""
/{GET_CHARACTER_STAT_COMMAND} <character_name>:
And lo! A command of great import — '/{GET_CHARACTER_STAT_COMMAND} <character_name>'. This incantation, whispered in the shadows, unveils the arcane statistics of a character within our digital realm. Take heed, for a crucial caveat graces this command! Only the Dungeon Master, the weaver of destinies, may wield this power to its fullest. Furthermore, be aware that the privilege to invoke this enchantment is granted solely to those whose character name mirrors their own.

/{SKILL_COMMAND} <action> <attribute> <character> <value>:
In the symphony of commands, '/{SKILL_COMMAND} <action> <attribute> <character> <value>' performs a mystical action upon a character. May the harmonies of this command resonate with precision, shaping the destiny of characters in the cosmic dance of our digital tapestry.

/{STAT_COMMAND} <action> <stat> <character> <value>:
Hark, noble seeker! The command '/{STAT_COMMAND} <action> <stat> <character> <value>' beckons you to weave fate's tapestry by performing a mystical action upon a character's overarching stats. May this incantation sculpt destinies in the cosmic dance of our digital realm.

/{DEATH_SAVES_COMMAND} <action> <version> <character> <value>:
The command '/{DEATH_SAVES_COMMAND} <action> <version> <character> <value>' beckons, allowing thee to manipulate the threads of fate by performing a mystic action upon a character's dire struggle for life. May this incantation shape the outcome in the ethereal dance of our digital tapestry.

/{SAVING_THROWS_COMMAND} <action> <skill> <character> <value>:
Hark, intrepid adventurer! Unveil the command '/{SAVING_THROWS_COMMAND} <action> <skill> <character> <value>', a mystic invocation to wield influence upon a character's saving throws in the cosmic dance of our digital realm. May this incantation sway the tides of destiny in thy favor.
"""

HELP_TEXT3 = f"""
/{ABILITY_SCORE_COMMAND} <action> <ability score> <base or modifier> <character> <value>:
Hear ye, valiant seeker! The command '/{ABILITY_SCORE_COMMAND} <action> <ability score> <base or modifier> <character> <value>' unfolds a mystical avenue to shape the essence of a character's abilities—be it base or modifier. May this incantation sculpt the very core of destiny in the cosmic dance of our digital tapestry.

May the arcane forces guide you on your quest, and may the digits align in your favor, brave adventurer!
"""

ONLY_DM_TEXT_AND_YOUR_CHARACTER = f"""
Take heed, for a crucial caveat graces this command! Only the Dungeon Master, the weaver of destinies, may wield this power. To seek the statistics of a character, beseech the Dungeon Master to utter this command on thy behalf.

Furthermore, be aware that the privilege to invoke this enchantment is granted solely to those whose character name mirrors their own. Let the whispers of the command echo true, resonating only with the chosen character of the invoking soul. Trust in the Dungeon Master's guidance, and may the digital tapestry be enriched by the revelations of each character's mystic prowess.
"""

INCORRECT_CHANNEL_TEXT = f"""
Hark! Thy attempt to summon this incantation in this channel is met with arcane resistance. The command is reserved for the sacred chamber where Dungeon Master's wisdom reigns. Seek the rightful channel - thy personal bot channel - where revelations may unfold seamlessly.
"""

FORGOT_VALUE_TEXT = "Alas, valiant seeker, the mystical forces yearn for a missing value to fuel the spell and shape the destiny of thy character's skill."

OUT_OF_BOUND_DEATH_SAVE = "Beware, intrepid seeker, for the arcane boundaries forbid the alteration of death save values beyond the mortal range; tread carefully, lest the balance of life's delicate weave be disrupted in our digital realm."
