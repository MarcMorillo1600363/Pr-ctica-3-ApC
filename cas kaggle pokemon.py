#!/usr/bin/env python
# coding: utf-8

# # CAS KAGGLE POKEMON

# El primer que fem es importar les llibreries necesàries i la nostra base de dades, que en aquest cas tracta sobre pokemon.

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

dataset = pd.read_csv(r"C:\Users\marcm\Downloads\pokemon.csv")


# Ara mostrarem algunes de les dades per poder entendre millor que estem buscant, i altres dades informatives per veure si tenim algun problema previ, com per exemple nulls o variables continues

# In[2]:


pd.set_option('display.max_columns', None)
dataset.head(10)


# In[3]:


dataset.describe()


# Despres de veure una mica les dades observem que la nostra variable objectiu sera is_legendary, es a dir volem predir si un pokemon es o no legendary.
# 
# A més hem pogut veure que tenim valors nulls, principalment a la variable de type2, aixo es degut a que alguns pokemons només tenen 1 tipus, per tant el segon es null.

# In[4]:


dataset.isnull().sum()


# Aqui podem veure el comentat anteriorment, la variable type2 te molts nulls, pero son necesaris.
# 
# En canvi veiem que també tenim nulls a les variables weight_kg i height_m. Aquests si que els considerem error, per tant eliminarem les files respectives. Pero primer transformarem els nulls de la variable type2 en 0.

# In[5]:


dataset = dataset.fillna({'type2': 0})


# Amb aquesta funcio hem transformat els nulls de la variable type2 en 0, per tant ara podrem eliminar les files que tinguin un null en altres variables.

# In[6]:


dataset['type2'].isnull().sum()


# Observem que la variable type2 ara te 0 valors a null, per tant podem eliminar la resta de files amb nulls.

# In[7]:


dataset = dataset.dropna()
dataset.isnull().sum()


# Observem que ja no hi ha nulls, per tant podem continuar treballant amb la BD.
# 
# Ara, com hem vist que hi ha variables que son strings, els transformarem en ints per poder treballar amb més facilitat

# In[8]:


dataset['capture_rate'] = dataset['capture_rate'].astype(int)


# Continuem observant les correlacions

# In[9]:


correlacio = dataset.corr()

plt.figure()

ax = sns.heatmap(correlacio, annot=True, linewidths=.5 ,annot_kws={'fontsize':5})


# Com d'aquesta manera no es veuen bé les correlacións les representare d'una altra manera

# In[10]:


correlacions = dataset.corr()['is_legendary'].to_frame().T 
plt.figure(figsize=(80,1))
plt.subplots(figsize=(80, 1))
sns.heatmap(correlacions, linewidths=0.3, annot=True)
plt.show()


# D'aquestes correlacions podem deduir i descartar moltes coses. 
# 
# La principal idea que veiem es que la variable que te una correlació més important amb el nostre objectiu es base_egg_steps, amb una correlació del 75%.
# 
# També veiem que hi ha moltes variables que no té sentit relacionarles amb la nostra variable objectiu is_legendary, com és el cas de les variables name, japanese_name, generation i pokedex_number entre d'altres, ja que es informació única de cada pokemon, no tenen relació en si es legendari o no, i aixó es pot veure reflectit en les correlacions tan baixes que representen. 
# 
# Amés podem descartar variables com per exemple tots els against_X, ja que es pot veure que tenen una  correlacio molt petita, fins i tot <0, i es normal ja que aquestes variables son en funció del tipus del pokemon, i un pokemon legendary pot ser de qualsevol tipus. 

# Per tant procedim a eliminar les variables innecesaries.

# In[11]:


dataset = dataset.drop(['against_bug','against_dark','against_dragon','against_electric','against_fairy','against_fight','against_fire','against_flying','against_ghost','against_grass','against_ground','against_ice','against_normal','against_poison','against_psychic','against_rock','against_steel','against_water','capture_rate','percentage_male','pokedex_number','name','japanese_name','generation'],axis = 1)
dataset = dataset.drop(['abilities','classfication','type1','type2'],axis = 1)
dataset.head(10)


# In[12]:


correlacions = dataset.corr()['is_legendary'].to_frame().T 
plt.figure(figsize=(80,1.5))
plt.subplots(figsize=(80, 1.5))
sns.heatmap(correlacions, linewidths=0.3, annot=True)
plt.show()


# Ara podem observar que ens hem quedat amb aquelles variables que mes afecten a la nostra variable objectiu.
# 
# El següent pas a fer és normalitzar les variables, ja que hi ha algunes que poden tenir uns valors molt dispersos.

# In[13]:


datasetNormalitzat = preprocessing.normalize(dataset)


# # Models

# El primer que hem de fer avanç de començar a fer models es dividir la nostra BD en train i test, utilitzarem un 80% de les dades per el train i el 20% restant per el test

# In[ ]:


variableObjectiu = datasetNormalitzat['is_legendary']
train, test, objectiuTrain, objectiuTest = train_test_split(datasetNormalitzat, varialbleObjectiu, train_size=0.8)

