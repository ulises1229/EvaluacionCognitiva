import spacy
import numpy as np

spa_lex = spacy.load('es_core_news_md')

def analize(base, comparer):
    for token_base in base:
        for token_toCompare in comparer:
            t1 = token_base.text
            t2 = token_toCompare.text
            simil = token_base.similarity(token_toCompare)
            results['token_base'].append(t1)
            results['token_toCompare'].append(t2)
            results['similarity'].append(simil)

results = {
    'token_base': [],      # tokens originales
    'token_toCompare': [], # token con el que se comparo
    'similarity': [],      # valor de la similitud de ambos
    'total_sim_mean': 0    # promedio similitud por frase
}
# bd cruda
master_row = spa_lex('por que hace mucho ruido')
# row = spa_lex('nolo se xd') # 1 real, 0.0083847332 calculado
# row = spa_lex('porque el niño grita mucho') # 3 real, 0.7266240727901458 calculado
# row = spa_lex('porque su hermano sube demasiado la voz') # 3 real, 0.7209052 calculado
# row = spa_lex('por que no habla en voz baja') # 3 real, 0.7523396730422973 calculado
row = spa_lex('que es fastidioso') # 1 real, 0.7051820238431294 calculado
analize(master_row, row)
results['total_sim_mean'] = np.mean(results['similarity'])
print('\n')
print(results)
print('\n')
print(list(zip(results['token_base'], results['token_toCompare'], results['similarity'])))
