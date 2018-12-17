import keras  # pylint: disable=E0401
from keras.layers import Input, Dense  # pylint: disable=E0401
from keras.models import Model  # pylint: disable=E0401
import numpy as np  # pylint: disable=E0401
from tensorflow import set_random_seed  # pylint: disable=E0401
import os


def seedy(s):
    np.random.seed(s)
    set_random_seed(s)


class AutoEncoder:
    def __init__(self, encoding_dim=3):
        self.encoding_dim = encoding_dim
        # declare array of 8 inputs
        self.x = np.array([[int('00000001', 2), int('00000010', 2), int('00000100', 2),
                            int('00001000', 2), int('00010000', 2), int('00100000', 2), int('01000000', 2), int('10000000', 2)]])
        print(self.x)

    # encoder part of the network
    def _encoder(self):
        inputs = Input(shape=(self.x[0].shape))
        encoded = Dense(self.encoding_dim, activation='relu')(inputs)
        model = Model(inputs, encoded)
        self.encoder = model
        return model

    # decoder part of the network
    def _decoder(self):
        inputs = Input(shape=(self.encoding_dim,))
        decoded = Dense(8)(inputs)
        model = Model(inputs, decoded)
        self.decoder = model
        return model

    # concatenate encoder and decoder together
    def encoder_decoder(self):
        ec = self._encoder()
        dc = self._decoder()

        inputs = Input(shape=self.x[0].shape)
        ec_out = ec(inputs)
        dc_out = dc(ec_out)
        model = Model(inputs, dc_out)

        self.model = model
        return model

    # fit model to the data
    def fit(self, batch_size=10, epochs=2000):
        # optimize with stochastic gradient descent to minimize loss
        self.model.compile(optimizer='sgd', loss='mse')
        self.model.fit(self.x, self.x,
                       epochs=epochs,
                       batch_size=batch_size)

    # save the model
    def save(self):
        if not os.path.exists(r'./weights'):
            os.mkdir(r'./weights')
        else:
            self.encoder.save(r'./weights/encoder_weights.h5')
            self.decoder.save(r'./weights/decoder_weights.h5')
            self.model.save(r'./weights/ae_weights.h5')


if __name__ == '__main__':
    seedy(2)
    ae = AutoEncoder(encoding_dim=3)
    ae.encoder_decoder()
    ae.fit(batch_size=50, epochs=2000)
    ae.save()
