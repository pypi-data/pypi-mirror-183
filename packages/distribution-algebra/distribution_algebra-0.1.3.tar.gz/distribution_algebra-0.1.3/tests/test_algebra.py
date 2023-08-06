#!/usr/bin/env python3

import itertools as it
from random import random
from typing import TypeAlias

import numpy as np
import pytest
from hypothesis import Verbosity, given, settings
from hypothesis import strategies as st

from distribution_algebra.beta import Beta
from distribution_algebra.distribution import (UnivariateDistribution,
                                               VectorizedDistribution)
from distribution_algebra.lognormal import Lognormal
from distribution_algebra.normal import Normal
from distribution_algebra.poisson import Poisson
from tests.conftest import DISTRIBUTIONS


@given(st.data())
def test_operations(data: st.DataObject) -> None:
    # Normal + Normal ~ Normal
    x: Normal = data.draw(st.from_type(Normal))
    y: Normal = data.draw(st.from_type(Normal))
    assert x + y == Normal(mean=x.mean + y.mean,
                           var=x.var + y.var)

    # Poisson + Poisson ~ Poisson
    z: Poisson = data.draw(st.from_type(Poisson))
    w: Poisson = data.draw(st.from_type(Poisson))
    assert z + w == Poisson(lam=z.lam + w.lam)

    # Lognormal * Lognormal ~ Lognormal
    a: Lognormal = data.draw(st.from_type(Lognormal))
    b: Lognormal = data.draw(st.from_type(Lognormal))
    assert a * b == Lognormal.from_normal_mean_var(a.normal_mean + b.normal_mean,
                                                   a.normal_var + b.normal_var)


UnivariateUnion: TypeAlias = \
    UnivariateDistribution[np.float64] | UnivariateDistribution[np.int_]
VectorizedUnion: TypeAlias = \
    VectorizedDistribution[np.float64] | VectorizedDistribution[np.int_]


@pytest.mark.parametrize("udist1", [Normal(mean=random(), var=random()),
                                    Lognormal(mean=random(), var=random()),
                                    Beta(alpha=random(), beta=random()),
                                    Poisson(lam=random())],
                         ids=["Normal", "Lognormal", "Beta", "Poisson"])
@pytest.mark.parametrize("udist2", [Normal(mean=random(), var=random()),
                                    Lognormal(mean=random(), var=random()),
                                    Beta(alpha=random(), beta=random()),
                                    Poisson(lam=random())],
                         ids=["Normal", "Lognormal", "Beta", "Poisson"])
def test_all_pairwise_combinations(udist1: UnivariateUnion, udist2: UnivariateUnion) -> None:
    addition: UnivariateUnion | VectorizedUnion = udist1 + udist2
    multiplication: UnivariateUnion | VectorizedUnion = udist1 * udist2
    match udist1, udist2:
        case (Normal(), Normal()) | (Poisson(), Poisson()):
            assert isinstance(addition, type(udist1))
            assert isinstance(multiplication, VectorizedDistribution)
        case (Lognormal(), Lognormal()):
            assert isinstance(addition, VectorizedDistribution)
            assert isinstance(multiplication, Lognormal)
        case _:
            assert isinstance(addition, VectorizedDistribution)
            assert isinstance(multiplication, VectorizedDistribution)
