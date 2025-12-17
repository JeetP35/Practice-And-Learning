'''
Curse
An enemy's weapons can be cursed so that they don't deal as much damage.

Assignment
Complete the curse function. It accepts a weapon_damage parameter and returns two values:

The lesser_cursed damage: reduce the input weapon_damage from 100% to 50% (50% reduction).
The greater_cursed damage: reduce the input weapon_damage from 100% to 25% (75% reduction).
A greater curse is more powerful than a lesser curse, so it reduces the damage more.

Tip
You can multiply a number by a decimal to get a percentage of a number. For example:

30% of 50 is 50 * 0.3

Ignore the float function in the print statements. We will introduce floats later.
'''


def curse(weapon_damage):
    lesser_cursed = 0.5 * weapon_damage
    greater_cursed = 0.25 * weapon_damage
    return lesser_cursed, greater_cursed


# Don't modify below this line


def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")


def main():
    test(100)
    test(500)
    test(1000)


main()
