# The field-handedness decision

Three labeled spin-½ sites experience local precession vectors $`\mathbf b_1,\mathbf b_2,\mathbf b_3`$. We ask for the sign of their ordered scalar triple product. Reversing all three fields reverses the sign. A common proper rotation leaves it invariant. Thus the question is meaningful without a directional spin reference. For magnetic fields this is a statement about simultaneous field reversal.

## Exposure and available operations

Use units in which a field vector is an angular frequency. In a sensing window of duration $t$ the exposed spins evolve independently:

```math
U_i=\exp\!\left(-\frac{it}{2}\mathbf b_i\cdot\boldsymbol\sigma_i\right),
\qquad U=U_1\otimes U_2\otimes U_3.
```

The triplet of fields is unknown, with the supplied promises $`\|\mathbf b_i\|\le B`$ and

```math
|\chi|\ge\chi_0>0,\qquad
\chi=\mathbf b_1\cdot(\mathbf b_2\times\mathbf b_3).
```

A common proper rotation may vary arbitrarily between rounds. The three vectors are otherwise fixed and act simultaneously inside a window. Labeled positions, elapsed time, classical randomness and classical records are available. Preparation and readout commute with a common spin rotation on all spin registers. In particular, singlet initialization, pair-spin measurement and exchange SWAPs are allowed. The exposure is indivisible.

In the primary model, each round consumes one such window and a freshly prepared state. A readout can depend on all earlier classical results. Spinful ancillas that avoid exposure are counted as sheltered spins, even when prepared in a rotationally invariant joint state. Ancillas that transform trivially under spin rotations can be included without a spin resource. The bounds for this model concern fresh rounds with only classical information carried across them. [Two coherent windows](two-exposures.md) examines a different exposure budget.

## Results and accounting

1. With three exposed spins and no sheltered spin, every invariant experiment gives the same probabilities under simultaneous reversal. Classical adaptation and additional fresh shots leave this exact equality intact.
2. With one additional sheltered spin, a protocol with two configurations of one exchange SWAP returns the sign uniformly for $`0\lt tB\le\pi/4`$. With ideal binary readout, it needs order $`B^2 t^{-4}\chi_0^{-2}\log(1/\delta)`$ rounds for error at most $\delta$.
3. At fixed $B$ and $\chi_0$, the powers of $t$ and the confidence dependence are optimal as exposure shrinks. The lower bound permits arbitrarily many sheltered spins in each round. It covers independent fresh rounds and does not optimize the dependence on the chirality gap.

Every round consumes three local field exposures, two prepared singlets, the fourth spin kept outside the field, one exchange SWAP, and one pair readout per tested pair. All runs count, including the usual outcome where the rare event is absent. See [the sensing protocol](protocol.md), [the two converses](converse.md), and [detector and shelter errors](robustness.md).
