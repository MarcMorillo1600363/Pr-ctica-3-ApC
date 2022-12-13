# Pràctica-3-ApC
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
| [Random Forest] | 1000 Trees, 1807 | 98.72% | 3.25 s |
| [SVM] | default | 94.23% | 0.1 s |
| [KNN] (link al kaggle) | default | 98.72% | 0.04 ms |
| [Red Neuronal] (link al kaggle) | 500 apochs | 0.98% | 6ms/step |
## Demo
Per tal de fer una prova, es pot fer servir amb la següent comanda
``` python3 demo/demo.py --input here ```
## Conclusions
Podem veure que aquesta és una BD molt senzilla, ja que només té 800 files, que pertanyen cadascuna a un del Pokémon existents, això ha causat alguns petits problemes que no es poden evitar, perquè l'única manera d'ampliar aquesta BD seria afegint informació de Pokémon de futures generacions.

Les principals dificultats trobades han sigut a causa dels valors null que hi havia originalment a la BD, ja que afectaven molt a les porques files on la variable objectiu valia 1. Però una vegada arreglats tot ha funcionat correctament.

Dels models hem vist que l'únic que dona problemes és el SVM, pel fet que encara que la seva accuracy és bona el resultat no ho és, perquè a la confusion matrix es pot veure que no hi ha cap true-negative, sinó que tot són false-positives o true-positives. Això vol dir que està classificant tot com a true, i l'accuracy alta és deguda al fet que hi ha poc nombre de resultats negatius respecte als positius.
La resta de models han funcionat correctament, donant bona accuracy, corbes roc i confusion matrix.
## Idees per treballar en un futur
Aquesta BD opino que podria millorar bastant, ja que hi ha més Pokemons de generacions més noves, i per tant més contingut. També crec que estaria bé afegir algun atribut 
## Llicencia
El projecte s’ha desenvolupat sota llicència ZZZz.
