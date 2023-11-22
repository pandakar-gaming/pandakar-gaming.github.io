Any tools that I've spun up as part of the [Final Fantasy Project](../final-fantasy-project) will be tossed in here.

# Final Fantasy IV

This game made me look at damage numbers because the amount of damage Zeromus was outputting was ridiculous. This is in comparison to the rest of the game, which was already quite frankly putting out ridiculous damage.

The actual damage formula used seems to be something like the following:
```
    [(caster lvl * caster int * magic spell power) / (target lvl + target spirit + target m.def)] * [1+(random(1, 31)/99)]
```

As part of this look, I made a very limited damage calculator focused specifically on Zeromus's damage: [meteor_planner.py](meteor_planner.py). This was to help see whether I needed to grind more levels, if gear would solve the issue or if I could play better.
Since there is a randomness to it, this calculator outputs the extremeties of a given spell. For our purposes, this will output the lowest amount of damage Zeromus's spells *should* do as well as the highest amount of damage they *should* do. 

To run this yourself, with a recent version of Python (3.9+?) run `python meteor_planner.py` and it'll output the numbers for you.