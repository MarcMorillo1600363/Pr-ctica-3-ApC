# Pr-ctica-3-ApC
# Pràctica Kaggle APC UAB 2022-23
### Nom: Marc Morillo Rubio 
### DATASET: The Complete Pokemon Dataset
### URL: [kaggle](https://www.kaggle.com/rounakbanik/pokemon)
## Resum
El dataset utilitza dades de tots els 802 pokemons de primera a septima generació. La informació que conte inclou les estadístiques bàsiques, ventatge o desaventatge davant altres tipus, altura, pes, clasificació, punts d'experiencia, abilitats, etc.
Tenim 802 dades amb 41 atributs.
### Objectius del dataset
Volem fer un classificador que ens digui si un pokemon és o no legendari.
## Experiments
Durant aquesta pràctica hem realitzat diferents experiments.
### Preprocessat
Quines proves hem realitzat que tinguin a veure amb el pre-processat? com han afectat als resultats?
Al preprocessat he realitzat diverses proves, la primera ha sigut veure si hi havia valors a null, a continuació, com una variable si que habia de tindre valors a null, els he transformat a 0, i he eliminat els nulls de la resta de variables eliminant la fila on es trobaben. També he transformat les variables string que tenia a valors int, per poder treballar amb més facilitat. Per últim a partir de les correlacions he eliminat aquells atributs que no aportaven informació útil.
### Model
| Model | Hiperparametres | Accuracy | Temps |
| -- | -- | -- | -- |
| [Random Forest](https://www.kaggle.com/rounakbanik/pokemon) | 500 Trees, 1807 | 100% | 0.557 s |
| Random Forest | 1000 Trees, 1807 | 100% | 1.234 s |
| SVM | default | 98.54% | 0.017 s |
| KNN (link al kaggle) | default | 100% | 0.021 ms |
| Red Neuronal (link al kaggle) | XXX | 62% | ?ms |
## Demo
Per tal de fer una prova, es pot fer servir amb la següent comanda
``` python3 demo/demo.py --input here ```
## Conclusions
Els tres models probats, SVM, KNN i Random Forest, han donat una accuracy practicament perfecta, probablement degut a la simplesa de la BD i a la alta concurrencia entre algunes variables amb la variable objectiu.
En comparació amb l'estat de l'art i els altres treballs que hem analitzat....
## Idees per treballar en un futur
Crec que seria interesant indagar més en...
## Llicencia
El projecte s’ha desenvolupat sota llicència ZZZz.
