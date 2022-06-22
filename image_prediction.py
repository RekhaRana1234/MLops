from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from tensorflow.keras.models import load_model

img_one = 'test.png'
model_path = 'model/resnet50.h5'

model = load_model(model_path)

model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

img_path = img_one
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model.predict(x)
print('Predicted:', decode_predictions(preds, top=3)[0])
