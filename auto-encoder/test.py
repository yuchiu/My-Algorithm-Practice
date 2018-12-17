from keras.models import load_model  # pylint: disable=E0401
import numpy as np  # pylint: disable=E0401

encoder = load_model(r'./weights/encoder_weights.h5')
decoder = load_model(r'./weights/decoder_weights.h5')

inputs = np.array([[3, 30, 60, 56, 17, 31, 64, 88]])
x = encoder.predict(inputs)
y = decoder.predict(x)

print('Test Input: {}'.format(inputs))
print('Test Output: {}'.format(y))
