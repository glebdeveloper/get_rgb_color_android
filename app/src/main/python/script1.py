from sklearn import tree
samples= [
    [0, 0, 70],
    [160, 0, 0],
    [102, 10, 149],
    [189, 105, 151],
    [71, 206, 215],
    [221, 158, 220],
    [138, 47, 164],
    [255, 134, 141],
    [160, 129, 215],
    [254, 255, 221],
    [31, 140, 156],
    [230, 134, 236],
    [19, 45, 120],
    [131, 68, 81],
    [127, 48, 77],
    [30, 89, 11],
    [216, 152, 10],
    [69, 101, 236],
    [78, 162, 102],
    [194, 240, 96],
    [64, 64, 64],
    [128, 128, 128],
    [217, 217, 217],
    [255, 255, 255],
    [237, 169, 120],
    [243, 198, 165],
    [249, 226, 210],
    [213, 51, 219],
    [150, 83, 229],
    [110, 125, 15],
    [162, 72, 16],
    [70, 31, 7],
    [116, 52, 11],
    [20, 20, 20],
    [0, 0, 0],
    [255, 0, 0],
    [255, 64, 0],
    [255, 128, 0],
    [255, 191, 0],
    [255, 255, 0],
    [191, 255, 0],
    [128, 255, 0],
    [64, 255, 0],
    [0, 255, 0],
    [0, 255, 64],
    [0, 255, 128],
    [0, 255, 191],
    [0, 255, 255],
    [0, 191, 255],
    [0, 128, 255],
    [0, 64, 255],
    [0, 0, 255],
    [64, 0, 255],
    [128, 0, 255],
    [191, 0, 255],
    [255, 0, 255],
    [255, 0, 191],
    [255, 0, 64]
]
labels=[
"blue синий",
"red красный",
"violet фиолетовый",
"burgundy бордовый",
"white blue голубой",
"pink розовый",
"violet фиолетовый",
"pink розовый",
"violet фиолетовый",
"white белый",
"green зелёный",
"pink розовый",
"blue синий",
"burgundy бордовый",
"burgundy бордовый",
"green зелёный",
"orange оранжевый",
"blue синий",
"green зелёный",
"green зелёный",
"black чёрный",
"grey серый",
"grey серый",
"white белый",
"beige бежевый",
"beige бежевый",
"beige бежевый",
"pink розовый",
"violet фиолетовый",
"green зелёный",
"brown коричневый",
"brown коричневый",
"brown коричневый",
"black чёрный",
"black чёрный",
"red красный",
"red красный",
"orange оранжевый",
"orange оранжевый",
"yellow жёлтый",
"green зелёный",
"green зелёный",
"green зелёный",
"green зелёный",
"green зелёный",
"green зелёный",
"green зелёный",
"white blue голубой",
"white blue голубой",
"white blue голубой",
"blue синий",
"blue синий",
"blue синий",
"violet фиолетовый",
"violet фиолетовый",
"pink розовый",
"pink розовый",
"red красный"
]
clf=tree.DecisionTreeClassifier()
clf.fit(samples, labels)
def predictColor(r, g, b):
    return "rgb("+str(r)+", "+str(g)+", "+str(b)+") is "+clf.predict([[r, g, b]])[0]+" color."