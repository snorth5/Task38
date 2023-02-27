print("\nPart1\n")

import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# It's interesting that Monkey and Cat are considered more similar - presumably due to the fact they are both animals.
# Monkey and Banana score relatively high, presumably because monkeys eat bananas.
# The similarity between Cat and banana scores lower - but I would expect closer to zero. 

print("\nPart2\n")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Again, the similarity between cat and monkey scores relatively high, presumably due to them both being animals.
# Likewise apples and bananas similarity score is high due to them both being fruit.
# Again, bananas have a higher scoring relationship with monkeys.
# Monkey and cat both score similarly when compared with apples, as with the cat and banana.

print("\nPart3\n")

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Interesting to see how high these scores are for seemingly unrelated sentences.
# Similarities seem to be based upon 
# cars and boats being modes of transport 
# and dogs and cats being animals 
# and also spacial on, where, there, lost type words/phases.

print("\nPart4 - My example\n")
tokens = nlp('rocket space train parking lettuce ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# The similarities for these words are lower than in the examples, which suprised me a bit.
# I thought rocket and train might score higher because they are both modes of transport.
# I thought rocket and lettuce would score highly as rocket is a type of lettuce.
# Parking and space score a higher similarity than rocket and space. 
# Relative to the monkey, cat, banana and apple example the scores are very low.


# Changing to 'en_core_web_sm':
# The single word comparisons seem to have generally had their similarity scores increase.
# apple cat comparison has jumped from about 0.2 to 0.7! and monkey apple is 0.73!
# Whereas the sentences seem to have had their scores generally lower.
# But it does seem to be a bit random.