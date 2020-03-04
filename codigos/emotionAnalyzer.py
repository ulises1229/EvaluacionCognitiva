"""
-> NEVER forget to cite!

Crowdsourcing a Word-Emotion Association Lexicon, Saif Mohammad and Peter Turney, Computational Intelligence, 29 (3), 436-465, 2013.

Emotions Evoked by Common Words and Phrases: Using Mechanical Turk to Create an Emotion Lexicon, Saif Mohammad and Peter Turney, In Proceedings of the NAACL-HLT 2010 Workshop on Computational Approaches to Analysis and Generation of Emotion in Text, June 2010, LA, California.

"""

import matplotlib.pyplot as plt
import pandas as pd
from quickPlotter import colnames, unique, colvals, countInstances

lexicon = pd.read_csv("C:/Users/Drablaguna/Desktop/UNAM/EvaluacionCognitiva/Bases de datos/Lexicones/NRC-Emotion-Lexicon-v0.92-In105Languages-Nov2017Translations_ES.csv")
df_secu = pd.read_csv("C:/Users/Drablaguna/Desktop/UNAM/EvaluacionCognitiva/Bases de datos/Secundaria/SECU_TODO_CLEAN.csv")

column = colvals(df_secu, "por_que_pelota_que_canta")
c=0
"""
tokenArray = ['porque',
 'las',
 'pelotas',
 'no',
 'tienen',
 'voz',
 'ni',
 'pueden',
 'cantar',
 'sin',
 'embargo',
 'cuando',
 'lo',
 'pones',
 'en',
 'el',
 'poema',
 'si',
 'tiene',
 'sentido',
 'porque',
 'esta',
 'diciendo',
 'que',
 'todo',
 'es',
 'una',
 'pelota'
]
"""

tokenArray = ['Un', 'tigre', 'que', 'cuando', 'cachorro', 'habia', 'sido', 'capturado', 'por', 'humanos', 'fue', 'liberado', 'luego', 'de', 'varios', 'años', 'de', 'vida', 'domestica', 'La', 'vida', 'entre', 'los', 'hombres', 'no', 'habia', 'menguado', 'sus', 'fuerzas', 'ni', 'sus', 'instintos', 'en', 'cuanto', 'lo', 'liberaron', 'corrio', 'a', 'la', 'selva', 'Ya', 'en', 'la', 'espesura', 'sus', 'hermanos', 'teniéndolo', 'otra', 'vez', 'entre', 'ellos', 'le', 'preguntaron']
# lex[1]
def checkEmotionValues(lexicon, tokenArray):
    # cambio el index, id por la palabra en espanol
    lexicon.set_index("es", inplace = True)

    positiveScore     = 0
    negativeScore     = 0
    angerScore        = 0
    anticipationScore = 0
    disgustScore      = 0
    fearScore         = 0
    joyScore          = 0
    sadnessScore      = 0
    surpriseScore     = 0
    trustScore        = 0

    for token in tokenArray:
        try:
            row = lexicon.loc[token]
            positiveScore     += row.positive.sum()
            negativeScore     += row.negative.sum()
            angerScore        += row.anger.sum()
            anticipationScore += row.anticipation.sum()
            disgustScore      += row.disgust.sum()
            fearScore         += row.fear.sum()
            joyScore          += row.joy.sum()
            sadnessScore      += row.sadness.sum()
            surpriseScore     += row.surprise.sum()
            trustScore        += row.trust.sum()
        except:
            print("Key no encontrada: " + token)
        
    print("\n")
    print("TOTAL positiveScore: " + str(positiveScore))
    print("TOTAL negativeScore: " + str(negativeScore))
    print("TOTAL angerScore: " + str(angerScore))
    print("TOTAL anticipationScore: " + str(anticipationScore))
    print("TOTAL disgustScore: " + str(disgustScore))
    print("TOTAL fearScore: " + str(fearScore))
    print("TOTAL joyScore: " + str(joyScore))
    print("TOTAL sadnessScore: " + str(sadnessScore))
    print("TOTAL surpriseScore: " + str(surpriseScore))
    print("TOTAL trustScore: " + str(trustScore))
        

checkEmotionValues(lexicon, tokenArray)

# for sentence in column:
#     tokens = []
#     tokens = sentence.split(" ")
#     print(tokens)
#     c+=1
#     # if sentence.lower() not in ["nn", "no se", "no se entiende", "ns"]:
#     #     tokens = sentence.split(" ")        
#     #     print(tokens)
# print(c)