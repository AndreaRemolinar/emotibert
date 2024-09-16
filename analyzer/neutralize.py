# neutralize.py
import spacy

nlp = spacy.load('fr_core_news_sm')

sentiment_words = {
    'frustration': ['putain', 'merde', 'ras-le-bol', 'gonfle'],
    'tristesse': ['triste', 'pleurer', 'déprimé', 'malheureux', 'deprimé'],
    'colere': ['colère', 'fâché', 'furieux', 'énervé'],
    'joie': ['joie', 'content', 'heureux', 'adoré','parfait'],
}

def neutralize_text(text, sentiment_words):
    doc = nlp(text)
    neutral_text = []
    
    for token in doc:
        if any(token.lemma_ in words for words in sentiment_words.values()):
            neutral_text.append('')
        else:
            neutral_text.append(token.text)
    
    return ' '.join(neutral_text)
