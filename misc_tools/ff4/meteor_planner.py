"""
Small tool to help calculate how much damage Zeromus is doing in theory.
Damage formula found on Gamefaqs somewhere? 
"""

from dataclasses import dataclass, field

@dataclass
class Character:
    name: str = field()
    level: int = field()
    spirit: int = field()
    magic_defense: int = field()

@dataclass
class Enemy:
    name: str = field()
    level: int = field()
    intelligence: int = field()

@dataclass
class Spell:
    name: str = field()
    power: int = field()

def magic_formula(caster: Enemy, spell: Spell, character_stats: Character) -> tuple:
    """
    Damage formula is as follows:
    [(caster lvl * caster int * magic spell power) / (target lvl + target spirit + target m.def)] * [1+(random(1, 31)/99)]
    """
    caster_power = caster.level * caster.intelligence * spell.power
    target_defense = character_stats.level + character_stats.spirit + character_stats.magic_defense

    lower_bound = int(caster_power / (target_defense * (1 + (31/99))))
    upper_bound = int(caster_power / (target_defense * (1 + ( 1/99))))
    return (lower_bound, upper_bound)

def main():
    """
    Note that all of this math is predated around seeing how much of a difference Shell would make.
    The claim is that Shell halves magic damage taken.
    From what I could see, Shell should affect all damage coming from Zeromus as it only casts spells.
    """
    zeromus = Enemy("Zeromus", 68, 33)
    # Zeromus spell powers are pulled from here - https://finalfantasy.fandom.com/wiki/Zeromus_(Final_Fantasy_IV_3D)
    METEOR = Spell("Meteor", 250)
    # this is wrong because of the following sample points with below char stats
    # Rosa - 4422 dmg
    # Edge - 7460 dmg
    # Rydia - 4740 dmg
    # Cecil - 5521 dmg
    # HOWEVER, it's a good enough approximation
    BIG_BANG = Spell("Big Bang", 315)
    FLARE = Spell("Flare", 160)

    kain = Character("Kain", 56, 33, 16)
    cecil = Character("Cecil", 57, 38, 22)
    rydia = Character("Rydia", 56, 30, 23)
    edge = Character("Edge", 55, 20, 16)
    rosa = Character("Rosa", 57, 79, 28)

    characters = [kain, cecil, rydia, edge, rosa]
    for char in characters:
        print(char.name)
        meteor = magic_formula(zeromus, METEOR, char)
        meteor_after_shell = (int(meteor[0] / 2), int(meteor[1] / 2))
        print(F"\t{METEOR.name} - Before shell: [{meteor}] // After shell: [{meteor_after_shell}]")
        big_bang = magic_formula(zeromus, BIG_BANG, char)
        big_bang_after_shell = (int(big_bang[0] / 2), int(big_bang[1] / 2))
        print(F"\t{BIG_BANG.name} - Before shell: [{big_bang}] // After shell: [{big_bang_after_shell}]")
        flare = magic_formula(zeromus, FLARE, char)
        flare_after_shell = (int(flare[0] / 2), int(flare[1] / 2))
        print(F"\t{FLARE.name} - Before shell: [{flare}] // After shell: [{flare_after_shell}]")

if __name__ == "__main__":
    main()