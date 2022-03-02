import json
import random

ResultSize = 10

ids = []
rar = []
nam = []
wei = []
siz = []
val = []
ris = []

mod1name = []
mod1Weight = []
mod1Size = []
mod1Value = []
mod1Risk = []


ids2 = []
rar2 = []
nam2 = []
wei2 = []
siz2 = []
val2 = []
ris2 = []

mod2name = []
mod2Weight = []
mod2Size = []
mod2Value = []
mod2Risk = []

ids3 = []
rar3 = []
nam3 = []
wei3 = []
siz3 = []
val3 = []
ris3 = []

common = []
uncommon = []
rare = []
epic = []
legendary = []


with open('baseItems.json') as f:
    data = json.load(f)
for item in data['baseItems']:
    ids.append(item['itemId'])
    rar.append(item['itemRarity'])
    nam.append(item['itemName'])
    wei.append(item['itemWeight'])
    siz.append(item['itemSize'])
    val.append(item['itemValue'])
    ris.append(item['itemRisk'])

with open('mod1.json') as f1:
    data1 = json.load(f1)
for mod in data1['mod1']:
    mod1name.append(mod['modName'])
    mod1Weight.append(mod['modWeight'])
    mod1Size.append(mod['modSize'])
    mod1Value.append(mod['modValue'])
    mod1Risk.append(mod['modRisk'])

items_len = len(data['baseItems'])
print(items_len)











i=0
while i < items_len:
    if rar[i] == "legendary":
        legendary.append(ids[i])
    elif rar[i] =="epic":
        epic.append(ids[i])
    elif rar[i] =="rare":
        rare.append(ids[i])
    elif rar[i] =="uncommon":
        uncommon.append(ids[i])
    else:
        common.append(ids[i])
    i = i + 1








print("Legendary = ",legendary)
print("Epic = ",epic)
print("Rare = ",rare)
print("Uncommon = ",uncommon)
print("Common = ",common)

i =0
sedes = 0
while i < ResultSize:
    r = random.uniform(0.0,1.0)
    if r < 0.0005:
        sedes = sedes + 1
        r2 = random.choice(legendary)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    elif (r < 0.01 and r >= 0.0005):
        r2 = random.choice(epic)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    elif (r < 0.03 and r >= 0.01):
        r2 = random.choice(rare)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    elif (r < 0.15 and r >= 0.03):
        r2 = random.choice(uncommon)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    else:
        r2 = random.choice(common)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    i = i + 1


print(sedes)
print(ids2)
print(nam2)
print(wei2)
print(siz2)
print(val2)
print(ris2)

