import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
 
# cargamos las 4 combinaciones 
dato_entrenamiento = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
 
# y estos son los resultados que se obtienen, en el mismo orden
dato_salida = np.array([[0],[0],[0],[1]], "float32")
 
model = Sequential()
model.add(Dense(16, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
 
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['binary_accuracy'])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
 


model.fit(dato_entrenamiento, dato_salida, epochs=1000)
# evaluamos el modelo
scores = model.evaluate(dato_entrenamiento, dato_salida)
resultado=model.predict(dato_entrenamiento).round()
 
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

print (resultado)



