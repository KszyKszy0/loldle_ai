import tensorflow as tf

# Definicja modelu
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(122, )),
    tf.keras.layers.Dense(140, activation='relu'),
    tf.keras.layers.Dense(168, activation='softmax'),
])

# Kompilacja modelu
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Podsumowanie modelu
model.summary()

