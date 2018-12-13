"""
--- Day 2: Inventory Management System ---

You stop falling through time, catch your breath, and check the screen on the device. "Destination reached. Current Year: 1518. Current Location: North Pole Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that so many people have chimneys, maybe he could sneak in that way?" Another voice responds, "Actually, we've been working on a new kind of suit that would let him fit through tight spaces like that. But, I heard that a few days ago, they lost the prototype fabric, the design plans, everything! Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs should be similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk too far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
"""

box_ids = "jplenqtlagxhivmwmscfukzodp jbrehqtlagxhivmeyscfuvzodp jbreaqtlagxzivmwysofukzodp jxrgnqtlagxhivmwyscfukwodp jbrenqtwagjhivmwysxfukzodp jbrenqplagxhivmwyscfuazoip jbrenqtlagxhivzwyscfldzodp jbrefqtlagxhizmwyfcfukzodp jbrenqtlagxhevmwfsafukzodp jbrunqtlagxrivmsyscfukzodp jbrenqtlaguhivmwyhlfukzodp jbrcnstsagxhivmwyscfukzodp jbrenqtlagozivmwyscbukzodp jbrenqwlagxhivswysrfukzodp jbrenstlagxhuvmiyscfukzodp jbranqtlhgxhivmwysnfukzodp jbrenqtvagxhinmxyscfukzodp jbrenqtlagdhivmwyscfukxody jbrenqtlagelavmwyscfukzodp jbrenqtlagxhtvmwyhcfukzbdp jbrenqwlagxhivmwyscfutzopp jbrenqtlavxhibmtyscfukzodp jbronqtlagxnivmwyscfuzzodp jbredqtlagxhppmwyscfukzodp jbrcnqtlogxhivmwysxfukzodp jbremqtlagehivswyscfukzodp jbrenqolagxhivmcyscfukzokp jbrehqtlacxhgvmwyscfukzodp fbrlnqtlagxhivmwyscbukzodp zbrfnqtlagxhivrwyscfukzodp jbregqtlagxnivmwyscfhkzodp jbrenqtllgxnivmwystfukzodp jurenqtlagxhivmwyscfulzoup jbrenitdagxhivmwyxcfukzodp jbrenqtlagxqivmwyscvuszodp jbqenqwlagxhivmwyscfckzodp jbrenqtlagxhivmwxscqupzodp jbrenqtlagxhivmwysciuqiodp jbrjnjtlagxhivmwyscfukzode jbrenqtlagxhuvmwqscfukzods jbrenqtlagxhuvmuyscfukzudp ibrenqtlagxhivmwyscfuktokp jbsenqtlagxhivcwyscfuksodp jbrfnntlagxhivmwnscfukzodp jzrenqulagxhivmwyscfukzodx jbrenqtqygxhivmwyscfukzwdp jbrenqtlagxfixmwyscfukzcdp jbrenqaoagxhivmwyshfukzodp jbrenqtlazxhivmworcfukzodp jbrenqtlagxhicowyscfukrodp jbrqnqtlagxhivzwyzcfukzodp jbrenqtlalxhuvxwyscfukzodp jbrenqtlqgxhhviwyscfukzodp jbrenqtuggxhivmoyscfukzodp jbrenqtlagxpivmwyscfukkodw zbrenqhlagxhivmwyscdukzodp jbrenutlagxxivmwyscfukzoqp obrenqtlagxhivmwxscfuszodp jbrenqtlagxhlvmwyscfuixodp rbrenqtlagdhixmwyscfukzodp jbrenqtlagxhivmwescfyszodp jbrfnqtlagxhivmwyscaukzhdp jbrenqtiagxhivmbyscfuxzodp cbrrnqtuagxhivmwyscfukzodp jbkenqtlagxhigmwysufukzodp jbjewqtlagxhivmwyscfuqzodp jbrznqtlagxvivmwyscfukzovp jbrenttlacxhivmwyscfhkzodp jblenqtlagxhivmwylcfukaodp jbrenqtlagxhivmqysiftkzodp jbrenqtlagwhikmwyscfukqodp jbrenqtlegxhivmwvsckukzodp jbrenqwzagxhiamwyscfukzodp jbrenqtlagxhivcwyscfgkzodc jbrenqtlagxxhvmwxscfukzodp jbrenqtlngxhivmwyscfukoowp jbreomtlagxhivmwpscfukzodp jfrenqtlagxhivmwyscnumzodp jbrenqtlagphipmwyscfukfodp jvrenqtlagxhivmwyscfmkzodw jbrenqtlaxxoiemwyscfukzodp jbrenqtlagxhivmwyscemkzpdp jbrenyjldgxhivmwyscfukzodp jbrenqtlagxhivfvyspfukzodp kbrenctlakxhivmwyscfukzodp jbrmhqtlagxhivmwyscfuizodp jbjenqtlagxlivmbyscfukzodp jbrenqtlaaxhivmmyshfukzodp jbronqtlagxhirmvyscfukzodp jbcrnqtlagxwivmwyscfukzodp jxrenszlagxhivmwyscfukzodp jbpenqtlagxhivmwyscfukkody jbrewqtlawxhivmwyscfukzhdp jbrenqylagxhivmwlxcfukzodp jbrenqtlagxxivtwywcfukzodp jbrenqtlagxhcvgayscfukzodp jbrenitlagxhivmwiscfukzohp jbrenutlagxhivmwyscbukvodp nbrenqtlagxhivmwysnfujzodp jbrenqtlagxhivmwyqcfupzoop jbrenqtrarxhijmwyscfukzodp jbrenqtlagxhivmwysdfukzovy jbrrnqtlagxhivmwyvcfukzocp jbrenqtlagxhivmwyscfuvzzhp jbhenitlagxhivmwysufukzodp jbrenqtlagxhivmwyscfuwzoqx kbrenqtlagxhivmwysqfdkzodp jbrenqtlagxhivmwyxmfukzodx jbcenatlagxxivmwyscfukzodp jbrenhtlagvhdvmwyscfukzodp jxrenqtlafxhivfwyscfukzodp jbreaztlpgxhivmwyscfukzodp tqrenqtlagxfivmwyscfukzodp jbrenqgllgxhwvmwyscfukzodp jbrejjtlagxhivmgyscfukzodp jbrenqtlagxhivmwyscvukzoqv jbrvnqtlagxsibmwyscfukzodp jbrenqttagxhuvmwyscfukvodp jbrenqteagxhivmwcscfukqodp jbrenqtsabxhivmwyspfukzodp jbbenqtlagxhivmwyscjukztdp jnrenqtlagxhiimwydcfukzodp jbrenqtlagxhfvmwyscxukzodu jbrenqtluyxhiomwyscfukzodp jbrenqvlagxhivmwyscuukzolp ebrenqtlagxnivmwysrfukzodp jbreeqtlatxhigmwyscfukzodp jbrenqtvxgxhivmwyscfukzedp jbrmnqtlagxhivmwywcfuklodp jbreeqtvagxhivmwyscfukzody jbrenptlagxhivmxyscfumzodp jbrenqtlagxhivmwysgfukzfsp jurenqtlagjhivmwkscfukzodp jbrenntlagxhivmwtscffkzodp jbrenqglagxhivmwyocfokzodp wbrenqtlagxhivmwhscfukiodp jbrenqtligxhivmqascfukzodp jbrenqtlagxhivmwxscfukpojp jurenqtlagxhivmmyscfbkzodp jbrenqtmagxhivmwyscfrbzodp jcrenqtlagxhivmwysefukzodm jbrenqtlagxhicmwywcfukzodl jbvanqtlagfhivmwyscfukzodp jbmenqjlagxhivmwyscfdkzodp jbrenqtlagohivvwysctukzodp jbrenqtdagxdivmwyscfckzodp kbrefqtlagxhivmwyscfuazodp jbrwnqtoagxhivmwyswfukzodp jjhenqtlagxhivmwyscfukzorp jbgsnqtlagxhivkwyscfukzodp jbrynqtlagxhivmsyspfukzodp jbrenftlmkxhivmwyscfukzodp nbrenqtxagxhmvmwyscfukzodp jbrunqtlagxhijmwysmfukzodp jbrenqtlagmaivmwyscfukzowp jbrerqtlagxhihmwyscfukzudp jbrenqtlagahivmwysckukzokp kbrenqtlagxhirmwyscfupzodp jbrrnqtlagxhivmwyecfukzodz jbrenqtlavxhivmwyscfusiodp jnrenqtlagxhivmwyhcfukzodw jbretqtlagfhivmwyscfukzrdp jbreoqtnagxhivmwyscfukzopp jbrenbtllgxhivmwsscfukzodp jbrenqtlmgxhivmwyscfuwzedp jbnenqtlagxhivbwyscfukzokp jbrenqslagxhivmvyscfukzndp jbrenqtlagxzivmwuscfukztdp gbrenqtlagxhyvmwyscfukjodp jbrenqteagxhivmwyscfuszedp jbrenqtlaglhivmwysafukkodp jbrenqtlagxhcvmwascfukzogp jbrenqtlagxhsvmkcscfukzodp jbrenqslbgxhivmwyscfufzodp cbrenqtlagxhivkwtscfukzodp jbrenqtltgxhivmzyscfukzodj jbrgnqtlagihivmwyycfukzodp vbrenqauagxhivmwyscfukzodp jbrqnqtlagjhivmwyscfqkzodp jbrenqtlakxhivmwyscfukvobp jcrenqelagxhivmwtscfukzodp jbrrnqtlagxhlvmwyscfukzodw jbrenqtlagxhivmwkscaumzodp jbrenqdlagxhivmiescfukzodp jhrenqtlagxhqvmwyscmukzodp jbrenqtlaghhivmwyscfukkoyp jowenqtlagxyivmwyscfukzodp jbrenitaagxhivmwyscfqkzodp jbrenqtlagxhivmwyscfnkbudp jbyenqtlagxhivmiyscfukzhdp jbrenitlagxhibjwyscfukzodp jbrenqtlavxhjvmwpscfukzodp jbrenqyaagxhivmwyscflkzodp jbrenqylagxhivmwyicfupzodp jbrenqtlagxmevmwylcfukzodp lbrenqtlagxhiqmwyscfikzodp jbrenqtnarxhivmwyscfmkzodp jbrenqtlamxhivmwyscfnkzorp jbbenqtlavxhivmwyscjukztdp jbrenqtlagxhivmwyscfnliodp jbwenetlagxhivmwyscfukzodt jbrenatlagxhivmwysmfujzodp jbrsnstlagxhivmwyscfukgodp jbwvnitlagxhivmwyscfukzodp jbrenqtbagxhkvmwypcfukzodp jbrlnqtlafxhivmwyscfukdodp jbrenztlanxhivmwyscjukzodp jbrepqtlagxhivmwudcfukzodp jbrenqtlagxiivmwdscfskzodp jbrdjqtlagxhivmwyschukzodp jbrenqtoaguhivmwyccfukzodp jdrexqjlagxhivmwyscfukzodp jbrenqtlagxhovmwysckukaodp pbrfnqblagxhivmwyscfukzodp jbrenqtlagxrivgiyscfukzodp jbrelqtgagxhivmryscfukzodp jbrenqtlagxhicmwjscfikzodp jbrenqjlagxhivmwyscfmkjodp jbrenqtlagxpivmwzscgukzodp jbienqzlagxpivmwyscfukzodp jbrenqvlagxhivmwdscfukzodx owrenqtlagxhivmwyicfukzodp gbrenqtlaathivmwyscfukzodp jbgenqtlafxhivmwysqfukzodp jbrenqtlagxhivtwsscfukzokp jbrnnqylanxhivmwyscfukzodp ebrenqolagxhivmcyscfukzodp jbrenqtlarnhivgwyscfukzodp jbmenqtlagxhivmvyscfukzgdp jbrevqtlaglhivmwystfukzodp jbrenqplanthivmwyscfukzodp jbrenqtlagxhivmkyscbukzosp jbrenqtlagxaivmwyscfugzodo jbrenqplagxhnvmwyscfjkzodp jbrenqtlagxhivgwyscfusrodp cbrenqtlagxhivmwysmfukzody jbrenquwaexhivmwyscfukzodp jbredqtlagxhdvmwyscfukzoup jbrxnqtlagxhivmwysczukaodp jbrenqtlafnhivmwyscfuczodp jbbdkqtlagxhivmwyscfukzodp ubrenqtlagxhivkwyucfukzodp ebjenqtlagxhivmwyscfukzodj jbgenqtlugxxivmwyscfukzodp jbrenqtoagxqivmwdscfukzodp bbeenqtlagxhivmwyscfumzodp jbfeeqtlagxhivmwmscfukzodp jbrlnqtlagxhiimwescfukzodp jbrenqtlagwoivmwyscfukhodp jbrenqtlagnhivmwyscfuszovp"
box_id_list = box_ids.split(" ")


def char_checker_checksum(list_of_ids):
    ids_with_dupes = []
    ids_with_thrupes = []
    for elem in list_of_ids:
        for char in elem:
            count = elem.count(char)
            if count == 3 and elem not in ids_with_thrupes:
                ids_with_thrupes.append(elem)
            elif count == 2 and elem not in ids_with_dupes:
                ids_with_dupes.append(elem)
    return len(ids_with_dupes) * len(ids_with_thrupes)


print(char_checker_checksum(box_id_list))

"""
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?

Your puzzle answer was 8118.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)
"""

