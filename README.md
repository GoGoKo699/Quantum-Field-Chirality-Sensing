# Quantum Field Chirality Sensing

Can three spin sensors determine the handedness of their local magnetic fields without a calibrated spin axis? With one simultaneous exposure per round, three spins alone are blind to simultaneous field reversal. Add one sheltered spin and prepare two singlets. Moving the same exchange SWAP from before to after the exposure changes a rare-event rate by a signed multiple of the three fields’ scalar triple product.

The contrast is cubic in exposure time $t$. The two rare-event rates are quadratic, so the sign can be recovered in $`\Theta(t^{-4}\log(1/\delta))`$ independent rounds for error $\delta$ at fixed field bound and nonzero chirality gap. This scaling is optimal for invariant controls and fresh probes, even with arbitrarily many sheltered spins in each round.

| Read next | What it covers |
| --- | --- |
| [Science](science/README.md) | Exact protocol, minimal spectator, acquisition bound and resource accounting |
| [Experimental constraints](science/robustness.md) | Detector false counts, exchange miscalibration and leakage to the sheltered spin |
| [Two coherent exposures](science/two-exposures.md) | An alternative using three spins and an additional sensing window |
| [Learning route](learning/README.md) | A reference-frame tutorial and 30 project milestones |
| [Verification](verification/README.md) | Direct finite-matrix checks of the protocol and its limits |
| [References](references/RELATED_WORK.md) | Prior spin chirality, unitary comparison and exchange-readout work |

The main result uses ideal rotation-invariant preparation and readout. A fixed false-positive floor can change the exposure-time scaling of the binary test. The field vectors are angular-frequency vectors, and the handedness is the sign of their ordered scalar triple product.

## Reproduce the checks

```sh
python -m pip install -r verification/requirements.txt
python verification/verify.py
```

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
