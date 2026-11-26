# Verification

Run in a Python environment with NumPy:

```sh
python -m pip install -r verification/requirements.txt
python verification/verify.py
```

| Check | Evidence produced |
| --- | --- |
| [One exposure](verify_protocol.py) | Direct four-spin matrices compared with the signed closed forms, on 500 reproducibly seeded bounded field triples. The three-spin invariant Pauli basis is used to check equality with reversed fields. An orthogonal triad gives short-time log-log slopes near 2, 3 and 4 for event rate, signed contrast magnitude and squared Hellinger distance. |
| [Two exposures](verify_two_exposures.py) | Direct three-spin matrix circuit with two windows and the intervening cycle in each direction, on 500 bounded triads. The orthogonal triad gives the exact cubic sine contrast and the same three limiting slopes. |
| [Detector and routing](verify_robustness.py) | Direct matrix checks of the relative quaternion determinant, the spectator-error sign guarantee, a common exchange-area perturbation and the ideal versus fixed-floor distinguishability crossover. |

Expected residuals in the finite algebra checks are below $10^{-12}$. Small-time fitted slopes in the ideal tests should be within 0.01 of their limiting integer values. These are finite arithmetic checks at the sampled points. Uniform guarantees and the converse for all allowed experiments use the [analytical arguments](../science/README.md).
