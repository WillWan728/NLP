# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences
#    after you have stored them in a list called garden path Sentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities
# you found that spaCy gave one of the words of your sentences - did you expect this?

import spacy    # This statement should work if you have spaCy installed

nlp = spacy.load('en_core_web_sm')  # written web text including vocab, syntax and entities in the english language.


garden_sentences = ["The horse raced past the barn fell.",
                       "When John called his old mother was happy."
                       "The man who hunts ducks out on weekends.",
                       "The complex houses married and single soldiers and their families.",
                       "The cotton clothing is made of grows in Mississippi."]


for sentence in garden_sentences:
    # Tokenisation
    doc = nlp(sentence)
    print([token.orth_ for token in doc])

#   Entity recognition
    print([(i, i.label_, i.label) for i in doc.ents])

# Unusual entity "John" = Person
# Unusual entity "Mississippi = GPE


