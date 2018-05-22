# Implement a dictionary using trie.
# Populate the dictionary with given words
# Validate the unknown words
import unittest
from collections import defaultdict

sampleText = '''
Snakes are elongated, legless, carnivorous reptiles of the suborder Serpentes.[2] Like all squamates, snakes are ectothermic, amniote vertebrates covered in overlapping scales. Many species of snakes have skulls with several more joints than their lizard ancestors, enabling them to swallow prey much larger than their heads with their highly mobile jaws. To accommodate their narrow bodies, snakes' paired organs (such as kidneys) appear one in front of the other instead of side by side, and most have only one functional lung. Some species retain a pelvic girdle with a pair of vestigial claws on either side of the cloaca. Lizards have evolved elongate bodies without limbs or with greatly reduced limbs about twenty five times independently via convergent evolution, leading to many lineages of legless lizards.[3] Legless lizards resemble snakes, but several common groups of legless lizards have eyelids and external ears, which snakes lack, although this rule is not universal (see Amphisbaenia, Dibamidae, and Pygopodidae).
Living snakes are found on every continent except Antarctica, and on most smaller land masses; exceptions include some large islands, such as Ireland, Iceland, Greenland, the Hawaiian archipelago, and the islands of New Zealand, and many small islands of the Atlantic and central Pacific oceans.[4] Additionally, sea snakes are widespread throughout the Indian and Pacific Oceans. More than 20 families are currently recognized, comprising about 520 genera and about 3,600 species.[5][6] They range in size from the tiny, 10.4 cm (4.1 in)-long thread snake[7] to the reticulated python of 6.95 meters (22.8 ft) in length.[8] The fossil species Titanoboa cerrejonensis was 12.8 meters (42 ft) long.[9] Snakes are thought to have evolved from either burrowing or aquatic lizards, perhaps during the Jurassic period, with the earliest known fossils dating to between 143 and 167 Ma ago.[10] The diversity of modern snakes appeared during the Paleocene period (c 66 to 56 Ma ago). The oldest preserved descriptions of snakes can be found in the Brooklyn Papyrus.
Most species are nonvenomous and those that have venom use it primarily to kill and subdue prey rather than for self-defense. Some possess venom potent enough to cause painful injury or death to humans. Nonvenomous snakes either swallow prey alive or kill by constriction.
'''

NON_CHARACTERS = ['.', ',', '!', '?', '[', '{', '(', ')', '}', ']', ';']


class Dictionary:
    def __init__(self):
        self.dictionary = defaultdict(dict)

    def clean(self, token):
        while token and token[-1] in NON_CHARACTERS:
            token = token[:-1]
        if token and token[0] in NON_CHARACTERS:
            token = token[1:]
        if token and token[0] in '1234567890':
            return ''
        return token

    def addWord(self, dictionary, word):
        if word == '':
            dictionary['#'] = defaultdict(dict)
            return
        if word[0] not in dictionary:
            dictionary[word[0]] = defaultdict(dict)
        self.addWord(dictionary[word[0]], word[1:])

    def addText(self, text):
        for line in text.split('\n'):
            for token in line.split(' '):
                word = self.clean(token)
                if word != '':
                    self.addWord(self.dictionary, word.lower())

    def contains(self, word, dictionary=None):
        if not dictionary:
            dictionary = self.dictionary
        if word == '':
            if '#' in dictionary:
                return True
            return False
        return word[0] in dictionary and self.contains(word[1:], dictionary[word[0]])


class Test(unittest.TestCase):
    def test_balance(self):
        dictionary = Dictionary()
        dictionary.addText(sampleText)
        self.assertTrue(dictionary.contains('snakes'))
        self.assertFalse(dictionary.contains('gopi'))
