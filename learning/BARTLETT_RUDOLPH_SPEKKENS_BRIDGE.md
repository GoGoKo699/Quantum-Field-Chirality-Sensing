# From collective rotations to field chirality

**Educational anchor.** Stephen D. Bartlett, Terry Rudolph, and Robert W. Spekkens, *Reference frames, superselection rules, and quantum information*, Reviews of Modern Physics **79**, 555–609 (2007). [Published review](https://doi.org/10.1103/RevModPhys.79.555) · [Open text, arXiv:quant-ph/0610030v3](https://arxiv.org/abs/quant-ph/0610030v3)

The experiment has three labeled sites. A spin at site $`i`$ picks up an unknown rotation set by a local field $`\boldsymbol b_i`$. The target is the sign of $`\chi=\boldsymbol b_1\cdot(\boldsymbol b_2\times\boldsymbol b_3)`$. A common proper rotation leaves $`\chi`$ unchanged. Reversing all three fields changes its sign, while preserving their lengths and pairwise angles. Pairwise comparisons therefore leave out precisely the sign the experiment asks for.

## Read the review by concept

| Anchor section | Read for | Use in this project |
|---|---|---|
| § II.C, Eqs. (2.14), (2.16), and (2.20) | Group averaging of states, operations, and effects | The review's $`T(g)`$ becomes the action of the same spin rotation on every spin, including the sheltered one. We apply this averaging to the unknown exposure channel. [Model](../science/model.md) |
| § II.C, Theorem 1, and § III.A.2(b–d) | The difference between a spin representation and its multiplicity | The whole system can carry rotationally invariant information even though a single spin has no invariant direction. The total-spin $`1/2`$ sector of three spins has multiplicity two. That multiplicity does not guarantee sensitivity to two inverse local-rotation channels. [Converse](../science/converse.md) |
| § III.B, Eq. (3.24) | Pairings $`S_{12}S_{34}`$ and $`S_{13}S_{24}`$ as four-spin singlet states | The project uses the first two pairings, changes their ordering around a local field exposure, and reads one singlet and one triplet. [Protocol](../science/protocol.md) |
| § VI.A.2 | Extracting relative information with invariant observables | The review treats relational parameters of states. Here the fields are encoded in a channel, so the invariant relation must be transferred into a difference of transition probabilities. [Model](../science/model.md) |

The distinction between common rotation and local exposure matters. In the review, the group element describes an unknown relation between frames. Here a participant can rotate the *description* of the whole field triad without affecting any probabilities. During exposure each sensor instead evolves with its own $`U_i=\exp(-it\boldsymbol b_i\cdot\boldsymbol\sigma/2)`$. The fourth spin has the identity exposure. Sheltering it changes which field acts there and still allows it to participate in an invariant singlet.

## Worked example with opposite field signs

Let the three unit fields be the ordered axes $`(e_x,e_y,e_z)`$. In a second example use $`(-e_x,-e_y,-e_z)`$. The two triads have the same pairwise dot products and opposite values of $`\chi`$. Each laboratory run starts from the same double singlet. The binary detector reports whether pair 12 is a singlet and pair 34 is a triplet. Put $`\mathrm{SWAP}_{23}`$ after the exposure in the forward setting or before it in the reverse setting.

Write $`c=\cos(t/2)`$ and $`s=\sin(t/2)`$. With the positive triad the probabilities of that event are

```math
p_\mathrm{f}=\tfrac14-\tfrac14(c^3-s^3)^2,
\qquad
p_\mathrm{r}=\tfrac14-\tfrac14(c^3+s^3)^2.
```

For the negative triad the two probabilities are exchanged. The difference for the positive triad is $`c^3s^3=t^3/8+O(t^5)`$. Each individual probability starts at $`3t^2/16+O(t^3)`$. The two settings thus have a cubic difference and quadratic variances at short exposure. Across independent repetitions, a quadratic variance divided by the square of a cubic gap gives a fourth-power sample cost. The [protocol](../science/protocol.md) makes this uniform over the whole promised family, and the [converse](../science/converse.md) shows the exponent cannot be improved under the same exposure and memory rules.

## Where the project extends the review

The review supplies the group average, the singlet pairings, and the idea of using joint effects to learn relative information. The project proves the three-spin obstruction by using Pauli supports, derives an exact signed difference for the crossed pairings, and bounds the information per experiment at short exposure. The [robustness analysis](../science/robustness.md) then connects the rare-event gain to a realistic issue. A common detector offset cancels from the mean difference, but its shot noise remains. Continue to the [milestone map](MILESTONES.md) for the full sequence.
