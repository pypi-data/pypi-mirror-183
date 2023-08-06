import tensorflow as tf

from experiments.van_der_pol.ivp import cp
from pararealml.operators.fdm import (
    FDMOperator,
    ForwardEulerMethod,
    ThreePointCentralDifferenceMethod,
)
from pararealml.operators.ml.auto_regression import (
    AutoRegressionOperator,
    SKLearnKerasRegressor,
)
from pararealml.operators.ml.pidon import (
    PIDeepONet,
    PIDONOperator,
    UniformRandomCollocationPointSampler,
)
from pararealml.utils.tf import create_fnn_regressor

fine_fdm = FDMOperator(
    ForwardEulerMethod(), ThreePointCentralDifferenceMethod(), 1e-4
)

coarse_fdm = FDMOperator(
    ForwardEulerMethod(), ThreePointCentralDifferenceMethod(), 1e-3
)

coarse_fast_fdm = FDMOperator(
    ForwardEulerMethod(), ThreePointCentralDifferenceMethod(), 2e-3
)

coarse_ar = AutoRegressionOperator(
    10.0, coarse_fdm.vertex_oriented, time_variant=False
)
ar_model = create_fnn_regressor(
    [cp.differential_equation.y_dimension]
    + [50] * 7
    + [cp.differential_equation.y_dimension]
)
sklearn_ar_model = SKLearnKerasRegressor(ar_model)
sklearn_ar_model.model = ar_model
coarse_ar.model = sklearn_ar_model

coarse_pidon = PIDONOperator(
    UniformRandomCollocationPointSampler(),
    10.0,
    coarse_fdm.vertex_oriented,
    auto_regression_mode=True,
)
coarse_pidon.model = PIDeepONet(
    branch_net=tf.keras.Sequential(
        [tf.keras.layers.InputLayer(cp.differential_equation.y_dimension)]
        + [tf.keras.layers.Dense(50, activation="tanh") for _ in range(7)]
    ),
    trunk_net=tf.keras.Sequential(
        [tf.keras.layers.InputLayer(cp.differential_equation.x_dimension + 1)]
        + [tf.keras.layers.Dense(50, activation="tanh") for _ in range(7)]
    ),
    combiner_net=create_fnn_regressor(
        [150] + [50] * 3 + [cp.differential_equation.y_dimension]
    ),
    cp=cp,
)
