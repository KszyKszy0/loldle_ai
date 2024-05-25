import tensorflow as tf
from tensorflow import keras

# Ścieżka do modelu SavedModel
model_path = 'model_1.1_loldle'

# Załaduj model SavedModel i sprawdź dostępne endpointy
loaded_model = tf.saved_model.load(model_path)
print(list(loaded_model.signatures.keys()))  # Wypisz dostępne endpointy

# Utwórz warstwę TFSMLayer
tfsm_layer = keras.layers.TFSMLayer(model_path, call_endpoint='serving_default')

# Stwórz nowy model Keras, używając tej warstwy
inputs = keras.Input(shape=(122,))  # Podaj odpowiedni kształt wejściowy
outputs = tfsm_layer(inputs)
model = keras.Model(inputs=inputs, outputs=outputs)

# Wyświetl podsumowanie modelu
model.summary()

model.save('model.keras')