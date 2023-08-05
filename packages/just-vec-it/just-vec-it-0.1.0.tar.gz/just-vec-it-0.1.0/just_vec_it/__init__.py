__version__ = '0.1.0'
import tensorflow_hub
import tensorflow_text

model = {}

def load_model(dir="/home/andrew/Models/universal-text"):
    model["text"] = tensorflow_hub.load(dir)


def get_vecs(texts):
    return model["text"](texts)


def get_vec(text):
    return model["text"]([text])[0]

