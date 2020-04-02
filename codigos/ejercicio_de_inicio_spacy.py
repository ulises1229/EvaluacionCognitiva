# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:50:30 2019

@author: Alex Isasi
"""

#%%
import spacy
nlp = spacy.load("es_core_news_md")
texto_1 = nlp(u"SpaCy es una grandiosa herramienta")
print(texto_1)


#%%

ex1 = nlp("¿Cómo es la sonrisa?")
for word in ex1:
    #word.pos_
    #word.tag_
    print(word.text, word.pos_,word.dep_)
print(spacy)

#%%
print(spacy.explain('nsubj')) #sujeto nominal
print(spacy.explain('ADP')) #preposición
print(spacy.explain('nmod')) #modificador del nominal
print(spacy.explain('obl')) #oblique nominal
print(spacy.explain('DET')) #determiner, determinador
#%%
que_significa_6 = nlp("mi")
for token in que_significa_6:
    print('Texto: ',token.text,
          '\nLemma: ',token.lemma_,
          '\nTipo de palabra:: ',token.pos_,
          '\nCaracterísticas: ',token.tag_,
          '\nSubtipo: ',token.dep_,
          '\nEstructura: ',token.shape_,
          '\nSólo caracteres: ',token.is_alpha, 
          '\nStopword:',token.is_stop,
          '\nHijos: ',[child for child in token.children],
          '\n=====================================================================')
#%%
#pedazos de sustantivos
doc = nlp("el lapiz tiene un sabor a madera de México")
for chunk in doc.noun_chunks:
    print('Chunk text: ',chunk.text,
          '\nChunk root text: ',chunk.root.text,
          '\nChunk root dep: ',chunk.root.dep_,
          '\nChunk root head text: ',chunk.root.head.text,
          '\n=========================================================================================')


#%%
#identifica verbos
verbs = set()
for sujeto_posible in doc:
    if sujeto_posible.dep == spacy.symbols.nsubj and sujeto_posible.head.pos == spacy.symbols.VERB:
        verbs.add(sujeto_posible.head)
print(verbs)

#%%
# Entidades

for ent in doc.ents:
    print('Texto de la entidad: ', ent.text,
          '\nStart char: ', ent.start_char,
          '\nEnd char: ', ent.end_char,
          '\nEtiqueta: ',ent.label_,
          '\n=========================================================================================')
    
#%%
#Tokenización personalizada
print([w.text for w in doc])

caso_especial = [{spacy.symbols.ORTH: "tie"}, {spacy.symbols.ORTH: "ne"}]
nlp.tokenizer.add_special_case("tiene", caso_especial)

#Se imprime la nueva tokenizacion
print([w.text for w in nlp("el lapiz tiene un sabor a madera de México")])
    
#%%
#Entrenamiento de información
train_data = [
    ("Who is Chaka Khan?", [(7, 17, "PERSON")]),
    ("I like London and Berlin.", [(7, 13, "LOC"), (18, 24, "LOC")]),
]
#doc = Doc(nlp.vocab, ["rats", "make", "good", "pets"])
#gold = GoldParse(doc, entities=["U-ANIMAL", "O", "O", "O"])

    

    
    
    
    