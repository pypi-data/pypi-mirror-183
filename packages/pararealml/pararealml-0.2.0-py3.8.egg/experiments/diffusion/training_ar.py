import numpy as np
import tensorflow as tf

from pararealml.operators.ml.auto_regression import SKLearnKerasRegressor
from pararealml.utils.rand import SEEDS, set_random_seed
from pararealml.utils.tf import use_deterministic_ops
from pararealml.utils.time import time

if __name__ == "__main__":
    set_random_seed(SEEDS[0])

    use_deterministic_ops()

    from experiments.diffusion.operators import ar_model, coarse_ar

    ar_data = (
        np.load("data/ar_features.npy"),
        np.load("data/ar_labels.npy"),
    )
    ar_train_loss, ar_test_loss = time("ar model fitting")(
        coarse_ar.fit_model
    )(
        SKLearnKerasRegressor(
            ar_model,
            optimizer=tf.optimizers.Adam(
                learning_rate=tf.optimizers.schedules.ExponentialDecay(
                    1e-3, decay_steps=60000, decay_rate=0.1
                )
            ),
            batch_size=94080,
            epochs=60000,
            verbose=True,
            validation_split=0.2,
            callbacks=[
                tf.keras.callbacks.EarlyStopping(
                    monitor="val_loss",
                    min_delta=0,
                    patience=5000,
                    restore_best_weights=True,
                )
            ],
        ),
        ar_data,
        test_size=0.2,
    )[
        0
    ]
    print("ar train loss:", ar_train_loss)
    print("ar test loss:", ar_test_loss)
    coarse_ar.model.model.save_weights("weights/ar")
