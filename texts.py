from consts import (
    HELP_COMMAND,
    CAST_DICE_COMMAND,
    GET_CHARACTER_STAT_COMMAND,
    SKILL_COMMAND,
)

CAST_DICE_DESCRIPTION = "Beware cryptic dice! Honor sacred numerals 4, 6, 8, 9, 12, 20 for destiny's true reveal."

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

HELP_TEXT = f"""

Greetings, noble user of the arcane arts! Behold the mystic commands at your disposal:

/{HELP_COMMAND}:
Ah, ye seeker of wisdom, to unravel the mysteries, invoke this incantation "/{HELP_COMMAND}". A scroll of knowledge shall be revealed, unfurling the secrets of our mystical realm to guide thee on thine journey.

/{CAST_DICE_COMMAND}:
Venture forth into the unknown with the command "/{CAST_DICE_COMMAND}" Craft your fate by providing a single or double-digit offering, forsooth, but beware, for only the digits 4, 6, 8, 9, 12, and 20 are permitted in this sacred chant. May the roll of the enchanted dice shape thy destiny and unveil the path that lies ahead.

/{GET_CHARACTER_STAT_COMMAND} <character_name>:
And lo! A command of great import — '/{GET_CHARACTER_STAT_COMMAND} <character_name>'. This incantation, whispered in the shadows, unveils the arcane statistics of a character within our digital realm. Take heed, for a crucial caveat graces this command! Only the Dungeon Master, the weaver of destinies, may wield this power to its fullest. Furthermore, be aware that the privilege to invoke this enchantment is granted solely to those whose character name mirrors their own.

/{SKILL_COMMAND} <action> <attribute> <character> <value>:
In the symphony of commands, '/{SKILL_COMMAND} <action> <attribute> <character> <value>' performs a mystical action upon a character. May the harmonies of this command resonate with precision, shaping the destiny of characters in the cosmic dance of our digital tapestry.

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
