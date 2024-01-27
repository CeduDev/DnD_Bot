from consts import HELP_COMMAND, CAST_DICE_COMMAND, GET_CHARACTER_STAT_COMMAND

CAST_DICE_DESCRIPTION = "Beware cryptic dice! Honor sacred numerals 4, 6, 8, 9, 12, 20 for destiny's true reveal."

GET_CHARACTER_STAT_DESCRIPTION = "Invoke your character's name for mystic insights; the Dungeon Master alone commands its full power."

HELP_DESCRIPTION = "Scroll reveals mystic secrets, guiding thee on thy journey."

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

May the arcane forces guide you on your quest, and may the digits align in your favor, brave adventurer!
"""

ONLY_DM_TEXT_AND_YOUR_CHARACTER = f"""
Take heed, for a crucial caveat graces this command! Only the Dungeon Master, the weaver of destinies, may wield this power. To seek the statistics of a character, beseech the Dungeon Master to utter this command on thy behalf.

Furthermore, be aware that the privilege to invoke this enchantment is granted solely to those whose character name mirrors their own. Let the whispers of the command echo true, resonating only with the chosen character of the invoking soul. Trust in the Dungeon Master's guidance, and may the digital tapestry be enriched by the revelations of each character's mystic prowess.
"""
