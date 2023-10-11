# Coding Project: Volo’s Journal

## Use Case

- Go through a CSV decklist and identify if there are any duplicate creature types
- If so, return the offending creatures and overlapping types (in CSV)

## How the Code Should Work

1.  User feeds in a CSV decklist
2.  Program uses API to lookup all cards
3.  Filter out all non creature cards
4.  Create a dictionary
    1.  Keys → Creature Name
    2.  Values → Creature Types
        1.  Perhaps filter by everything after “- “
        2.  Use oracle text
5.  Check for duplicate values
6.  Return keys with duplicate values, and said values as CSV

## Initial Considerations

1.  Card name produces multiple or no results in database
2.  Duplicate cards
3.  Creatures with differing number of types
    1.  Minimum: Nameless Race is a creature with no types
    2.  Maximum: Seton’s Scout is a creature with 4 types
    3.  What happens if more longer type strings are added in the future?
4.  Changeling?
5.  While not the immediate use case, can flag cards outside of simic colors

## Revised Code Execution

1.  User feeds in CSV decklist (ideally with full names of all cards)
2.  Program uses API to lookup all cards
    1.  Return any duplicate entries, and names that turn up either multiple or zero results in database
    2.  Note: Typos and name adjacency cannot be accounted for
3.  Create filtered list of creatures
    1.  Might not be necessary but see first
4.  Create 2 empty dictionaries
    1.  Record: Tracks current holder of a specific type
    2.  Dupe: Tracks creatures with duplicated types
5.  For each creature, in an empty dictionary
    1.  IF type is not in Record
        1.  Assign creature TYPE as the key, and creature as value
            1.  Eg. Apex Devastator would result in {’Chimera’: ‘Apex Devastator’, ‘Hydra’: ‘Apex Devastator’}
    2.  Else
        1.  IF type is not in Dupe
            1.  Copy current key and value into Dupe
        2.  Else
            1.  Add current value of type in Record to same type in Dupe
        3.  Then overwrite value in Record with the new creature
6.  Once all creatures have been iterated through, compare Record and Dupe
    1.  If there are matching keys, add the current value in Record to Dupe
        1.  Catches the last duplicate and prevents double counting
        2.  Eg.
            1.  Record = {… ‘Elf’: ‘Tireless Provisioner’…}
            2.  Dupe = {’Elf’: \[’Beast Whisperer’, ‘Fierce Empath’\]}
            3.  Tireless gets added after Fierce Empath into the list
7.  Return CSV with
    1.  Overlapping types
    2.  Offending creatures per type

## Revised Considerations

1.  Could (6) be skipped by making the value types of Dupe be sets?
2.  Rows or columns for output csv?
3.  Can output creatures be single cell?
