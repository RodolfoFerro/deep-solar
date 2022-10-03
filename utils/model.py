import tensorflow as tf


def load_model(architecture, weights):
    """Function to load a trained model.

    Parameters
    ----------
    architecture : str
        The JSON file containing the architecture of the model.
    weights : str
        The H5 file containing the trained weights of the model.

    Returns
    -------
    model : model-like
        A trained and complied TF 2.0 model ready to be used.
    """

    # Load model architecture
    json_file = open(architecture, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = tf.keras.models.model_from_json(loaded_model_json)

    # Load weights into loaded model
    model.load_weights(weights)
    print("[INFO] Loaded model from disk.")

    # Compile model
    loss, optimizer, metrics = 'categorical_crossentropy', 'sgd', ['accuracy']
    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
    print("[INFO] Compiled model.")

    return model
