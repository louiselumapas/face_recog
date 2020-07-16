from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import tensorflow as tf
from cv2 import cv2
import numpy as np
import os

img = image.load_img("C:/Users/mikee.saldua/Documents/FacialRecognition/practive/images/Train/Dylan/Dylan1.jpg")
plt.imshow(img)

print(np.__version__)

train = ImageDataGenerator(rescale = 1/255)
validation = ImageDataGenerator(rescale= 1/255)

train_dataset = train.flow_from_directory('images/Train',
                                        target_size= (200,200),
                                        batch_size = 2,
                                        class_mode = 'binary'
                                        )

validation_dataset = train.flow_from_directory('images/Validation',
                                        target_size= (200,200),
                                        batch_size = 3,
                                        class_mode = 'binary'
                                        )
print(train_dataset.class_indices)

model = tf.keras.models.Sequential([ tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape=(200,200,3)),
        tf.keras.layers.MaxPool2D(2,2),
        tf.keras.layers.Conv2D(32,(3,3), activation = 'relu'),
        tf.keras.layers.MaxPool2D(2,2),
        tf.keras.layers.Conv2D(64,(3,3), activation = 'relu'),
        tf.keras.layers.MaxPool2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid'),
        ])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_fit = model.fit(train_dataset, epochs = 10, validation_data = validation_dataset)

test_dataset = 'C:/Users/mikee.saldua/Documents/FacialRecognition/practive/images/Test'

for i in os.listdir(test_dataset):
    print(i)
    img = image.load_img(test_dataset + '//' + i, target_size=(200,200))
    plt.imshow(img)
    plt.show()

    X = image.img_to_array(img)
    X = np.expand_dims(X, axis = 0)
    images = np.vstack([X])
    classifier = model.predict(images)
    if classifier == 0:
        print("DYLAN")
    else:
        print("IU")

model.save('C:/Users/mikee.saldua/Documents/FacialRecognition/practive/models')