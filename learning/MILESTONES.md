# Project understanding map

This route has **30 milestones**. The first 11 connect the local spin rotation, the allowed joint operations, and the statistics of a round. The remaining 19 build the sensing experiment, establish its two resource bounds, and compare the ideal experiment with changes to the detector and exposure. The [Bartlett–Rudolph–Spekkens bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md) maps the relevant sections of the single educational anchor to the project.

| Milestones | What comes together |
|---|---|
| [M01](#m01-an-ordered-field-triad)–[M06](#m06-invariant-pauli-tensors) | Local fields, spin rotations, and rotational scalars |
| [M07](#m07-a-singlet-triplet-test)–[M11](#m11-the-complete-sensing-task) | Pair operations, trial statistics, and the complete interface |
| [M12](#m12-inversion-on-three-spins)–[M19](#m19-an-orthogonal-triad) | The three-spin obstruction and exact four-spin experiment |
| [M20](#m20-a-detector-with-a-dark-baseline)–[M25](#m25-the-sharp-short-exposure-rate) | Rare-event acquisition and the matching information bound |
| [M26](#m26-a-common-false-count-floor)–[M30](#m30-the-complete-resource-account) | Detector noise, imperfect shelter, two exposures, and scope |

## Background and preliminaries

### M01 An ordered field triad

**Central question.** Which feature of three labeled field vectors survives a common change of axes and changes sign under field reversal?

**Understanding target.** Explain how the scalar triple product records the oriented volume, and why its sign carries information beyond the six entries of the Gram matrix.

**Dependencies and story role.** Start with vectors, labels, and a proper rotation. This fixes the target before introducing any spin model.

**Conceptual connection.** A control need only reveal the sign of this invariant. It can leave all three field directions undetermined.

**Source.** [Model](../science/model.md) · [Review bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)

### M02 From a local field to a spin rotation

**Central question.** How does an interrogation of duration $`t`$ encode one field in a unitary?

**Understanding target.** Connect the Pauli generator $`\boldsymbol b_i\cdot\boldsymbol\sigma/2`$ to its cosine and sine coefficients. Explain the full reversal as $`U_i\mapsto U_i^\dagger`$.

**Dependencies and story role.** M01 gives the field variables. This step identifies the three channels used by the sensor.

**Conceptual connection.** The multiplication rule for Pauli matrices supplies the dot product and the ordered cross product in the eventual signal.

**Source.** [Model](../science/model.md) · [Protocol](../science/protocol.md)

### M03 Pauli support and labeled sites

**Central question.** What does it mean for an operator to have exact support on a subset of sensed sites?

**Understanding target.** Expand an operator in tensor products of identity and Pauli operators, and group terms by the sites on which their Pauli factors are traceless.

**Dependencies and story role.** M02 supplies the local action. Now identify the blocks left separate by its tensor product.

**Conceptual connection.** A local rotation mixes Pauli components at a site and preserves whether the factor is the identity. This preserves orthogonal exact-support blocks.

**Source.** [Converse](../science/converse.md)

### M04 Collective rotation invariance

**Central question.** How can a state or measurement be invariant when its individual spins transform nontrivially?

**Understanding target.** Distinguish the common spin rotation $`g^{\otimes m}`$ from the product of separately determined exposure rotations, and state the invariance condition for a preparation and a POVM effect.

**Dependencies and story role.** M01 fixes common rotations and M02 fixes the exposure. Their distinction defines the allowed controls.

**Conceptual connection.** The restrictions apply to preparation and readout. The unknown channel can convert information into the invariant sector between them.

**Source.** [Review bridge, § II.C](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#read-the-review-by-concept) · [Model](../science/model.md)

### M05 Group averaging

**Central question.** Why may a calculation average the full field triad over a common rotation?

**Understanding target.** Show how invariance of both endpoints lets the group action pass through the Born probability, making each rotated description yield the same statistic.

**Dependencies and story role.** Use M04 to reach the group-average description of the unknown channel.

**Conceptual connection.** Common averaging can simplify amplitudes before deriving a lower bound. Averaging each site separately would remove the relative information that the task seeks.

**Source.** [Review bridge, § II.C](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#read-the-review-by-concept) · [Converse](../science/converse.md)

### M06 Invariant Pauli tensors

**Central question.** What coefficient tensors on one, two, and three vector slots are invariant under the same proper rotation?

**Understanding target.** Identify no nonzero invariant vector, one dot-product tensor on a pair, and one Levi-Civita tensor on a triple, up to their respective scalar factors.

**Dependencies and story role.** Combine M03's exact supports with M04's simultaneous action.

**Conceptual connection.** Each support available to the three sensors contains at most one invariant Pauli tensor. The one-dimensionality drives the reversal obstruction.

**Source.** [Converse](../science/converse.md) · [Review bridge, § II.C](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#read-the-review-by-concept)

### M07 A singlet-triplet test

**Central question.** What can a two-spin detector report without distinguishing spin axes?

**Understanding target.** Distinguish the one-dimensional total-spin-zero singlet from the three-dimensional triplet, and explain why the projector onto each full sector is invariant.

**Dependencies and story role.** M04 supplies the symmetry. This milestone gives the physical pair measurement that will be used twice in each trial.

**Conceptual connection.** The detector classifies the triplet as a whole. Its outcome label carries relational information about the pair.

**Source.** [Review bridge, § III.A.2](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#read-the-review-by-concept) · [Protocol](../science/protocol.md)

### M08 Alternate singlet pairings

**Central question.** How do four spins support two different product-of-singlets preparations under the same symmetry?

**Understanding target.** Label $`A=S_{12}S_{34}`$ and $`B_{\mathrm{pair}}=S_{13}S_{24}`$, recognize their overlap of $`1/2`$, and show why both are globally invariant.

**Dependencies and story role.** M07 gives one singlet. Pair two singlets in two orders to connect the invariant sector to a concrete sensor.

**Conceptual connection.** The nonorthogonal pairings can interfere through the exposure even though neither carries a preferred spatial axis.

**Source.** [Review bridge, § III.B](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#read-the-review-by-concept) · [Protocol](../science/protocol.md)

### M09 Exchange as a site permutation

**Central question.** What happens to the source state and the detector when the spins at sites 2 and 3 are exchanged?

**Understanding target.** Track the exchange on $`A`$ and on the pair-12-singlet, pair-34-triplet effect. Explain why SWAP commutes with collective rotations.

**Dependencies and story role.** M07 defines the effect, and M08 defines the states. This operation connects their two pairings with a fixed hardware layout.

**Conceptual connection.** A swap changes which field acts on which quantum information during the exposure. Its position in the sequence is a controllable variable.

**Source.** [Protocol](../science/protocol.md)

### M10 A binary event and its evidence

**Central question.** How do the mean and variance of a detector bit set the cost of comparing two settings?

**Understanding target.** Relate a Bernoulli probability $`p`$ to variance $`p(1-p)`$, and the variance of a difference of independent bits to the sum of their variances.

**Dependencies and story role.** M07 gives a detector event. Connect repetition of that event to the sign decision.

**Conceptual connection.** An event may carry a small mean difference while occurring rarely enough to give a useful gain in precision.

**Source.** [Protocol](../science/protocol.md)

### M11 The complete sensing task

**Central question.** Which resources does an independent one-exposure round have, and which unknowns are fixed by the promise?

**Understanding target.** Specify the three local fields, their norm bound and nonzero chirality gap, the simultaneous exposure, invariant controls, spectator count, and classical data available for later rounds.

**Dependencies and story role.** Assemble M01–M10 into one operational model.

**Conceptual connection.** The exact blindness claim, sample lower bound, and alternative two-window setting compare different resources and can be read against this same model.

**Source.** [Model](../science/model.md) · [Science index](../science/README.md)

## Narrative and innovation

### M12 Inversion on three spins

**Central question.** Why can three sensors fail to see reversal despite admitting a chirality observable?

**Understanding target.** On each exact support, contract the local rotation with the same unique invariant tensor on both ends. Under reversal the rotation transposes and the scalar self-contraction stays unchanged.

**Dependencies and story role.** M02, M03, and M06 turn the model of M11 into an exact inversion symmetry of the outcome probabilities.

**Conceptual connection.** A nonzero chirality observable on a supplied state need not respond asymmetrically when the preparation also has to be invariant and the fields act as channels.

**Source.** [Converse](../science/converse.md)

### M13 Which auxiliary systems can help

**Central question.** Can a larger system that is unchanged by spin rotations break the three-spin obstruction?

**Understanding target.** Distinguish arbitrary coefficients on a rotation-trivial auxiliary system from an auxiliary spin that transforms under the same group. Explain why the former leaves the self-contraction argument intact.

**Dependencies and story role.** M04 fixes the symmetry actions and M12 gives the exact obstruction without extra spin.

**Conceptual connection.** A sheltered spin transforms under a change of frame even though the unknown field exposure on that spin is the identity. Its relative spin information is a resource.

**Source.** [Model](../science/model.md) · [Converse](../science/converse.md)

### M14 One apparatus and two settings

**Central question.** How does moving one SWAP across the exposure change a single laboratory setup into two crossed tests?

**Understanding target.** Translate a post-exposure SWAP into an exchanged readout and a pre-exposure SWAP into an exchanged input. Both settings start at $`A`$ and use the same physical detector.

**Dependencies and story role.** Apply M08 and M09 within the resource counts of M11.

**Conceptual connection.** Fixed source and detector make a shared detector offset meaningful when comparing the two settings.

**Source.** [Protocol](../science/protocol.md) · [Robustness](../science/robustness.md)

### M15 The crossed marginal

**Central question.** Where does the exact quarter probability come from in each crossed test?

**Understanding target.** Each spin of a crossed pair comes from a distinct singlet. Its two-spin marginal is $`I/4`$, which survives product local rotations, so one crossed pair alone has singlet probability $`1/4`$.

**Dependencies and story role.** M07 gives the rank-one singlet effect and M14 gives the crossed geometry.

**Conceptual connection.** The singlet–triplet probability equals this quarter probability minus the probability that both crossed pairs are singlets.

**Source.** [Protocol](../science/protocol.md)

### M16 A transition amplitude as a trace

**Central question.** How do four singlet tensors simplify the amplitude between $`A`$ and $`B_{\mathrm{pair}}`$?

**Understanding target.** Follow indices around the singlet contractions to the ordered trace of three local unitaries. Account for the singlet normalization and for the daggers induced by crossing the two ends of a singlet.

**Dependencies and story role.** M02 supplies the unitaries, M08 the pairings, and M15 the probability that contains the transition amplitude.

**Conceptual connection.** The order in the trace can retain a sign that a symmetric product of pairwise quantities would discard.

**Source.** [Protocol](../science/protocol.md)

### M17 Even and odd parts of the transition

**Central question.** Which term in that ordered trace changes under field reversal?

**Understanding target.** Identify the real even contribution $`C`$ built from cosines and dot products, and $`D=\boldsymbol q_1\cdot(\boldsymbol q_2\times\boldsymbol q_3)`$ from the sine vectors of the unitaries.

**Dependencies and story role.** M02 supplies the Pauli algebra, and M16 fixes the trace order.

**Conceptual connection.** The two opposite signs of $`D`$ in the amplitudes survive probability squaring through their cross term with $`C`$. The rare-event difference is exactly $`CD`$.

**Source.** [Protocol](../science/protocol.md)

### M18 Why the sign is uniform

**Central question.** How can one sign rule work for all unknown field magnitudes and Gram matrices in the promise?

**Understanding target.** Use the short-exposure bound to control the angles of products of the three unitaries, keep $`C`$ positive, and bound $`|D|`$ below using the field chirality gap.

**Dependencies and story role.** M11 fixes the promises and M17 finds the product that sets the measured sign.

**Conceptual connection.** A positive scale factor and a nonzero gap let the comparison report the sign without estimating the nuisance parameters individually.

**Source.** [Protocol](../science/protocol.md)

### M19 An orthogonal triad

**Central question.** What changes in the two measured rates when all three unit basis fields are reversed?

**Understanding target.** For fields along three ordered orthogonal axes, reduce the even term to a product of cosines and the odd term to a product of sines. Track how reversal exchanges the outcome rates.

**Dependencies and story role.** Use M01 and M17–M18 to see the exact decision in an example without any pairwise dot-product terms.

**Conceptual connection.** The example verifies the sign convention, gives a visible cubic signal, and prepares the comparison with the detector's quadratic event rate.

**Source.** [Worked example](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#worked-example-with-opposite-field-signs) · [Protocol](../science/protocol.md)

### M20 A detector with a dark baseline

**Central question.** Why compare singlet–triplet events instead of the two bright singlet–singlet probabilities?

**Understanding target.** Show that the rare-event projector annihilates the prepared state at zero exposure. A transition amplitude bounded by a constant times $`t`$ then gives event probability $`O(t^2)`$.

**Dependencies and story role.** M15 gives the complementary probabilities and M19 shows their rates in one triad.

**Conceptual connection.** Taking the complementary event inside a crossed pair changes the noise scale while preserving the same cubic difference.

**Source.** [Protocol](../science/protocol.md)

### M21 Learning the sign from repeated rounds

**Central question.** How does the experiment turn a cubic contrast and quadratic variance into a reliable decision?

**Understanding target.** Form paired differences from separately prepared forward and reverse shots. Use a bounded-variable concentration estimate with the measured variance scale to obtain the $`t^{-4}`$ sample exponent.

**Dependencies and story role.** M10 supplies the binary variance, M18 supplies a promised contrast, and M20 bounds the noise.

**Conceptual connection.** Both settings, including trials where the rare event fails to occur, count toward error probability and cost.

**Source.** [Protocol](../science/protocol.md)

### M22 Probability affinity and decision error

**Central question.** Which statistic captures how hard it is to tell apart two records with rare outcomes?

**Understanding target.** Relate the affinity $`\sum_j\sqrt{p_j q_j}`$ to the distance between vectors of square-root probabilities, and connect high affinity to a large error for binary discrimination.

**Dependencies and story role.** M10 introduces the outcome distributions and M21 gives an attainable rate. This milestone starts a lower bound that can apply to arbitrary outcomes.

**Conceptual connection.** Square-root probabilities let the argument include outcomes with zero probability at the baseline without dividing by that baseline value.

**Source.** [Converse](../science/converse.md)

### M23 The same first-order lengths

**Central question.** Why does the first-order unitary term fail to separate the two signs at first order in affinity?

**Understanding target.** Express a square-root probability as the norm of a measurement-filtered amplitude in an averaged Hilbert space. Use the vanishing Haar mean of the generator to show equal norms for the positive and negative linearized amplitudes.

**Dependencies and story role.** Combine M05's common rotation average with M22's square-root probability vectors.

**Conceptual connection.** The second-order unitary remainder controls the amplitude-normalized difference. Summing over all POVM effects gives a bound independent of spectator count.

**Source.** [Converse](../science/converse.md) · [Review bridge, § II.C](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md#read-the-review-by-concept)

### M24 Classical adaptation across shots

**Central question.** Can outcomes from early trials make later trials distinguish inversion faster?

**Understanding target.** Apply the uniform single-round affinity bound to every shared history of outcomes and iterate it for the full transcript, including when the measurement settings are chosen in response to that history.

**Dependencies and story role.** M11 specifies fresh preparation and classical retention. M22–M23 give the quantity and its bound.

**Conceptual connection.** A per-round lower bound survives feedback because its constant holds for every allowed preparation and measurement at every history.

**Source.** [Converse](../science/converse.md)

### M25 The sharp short-exposure rate

**Central question.** In what sense do the achieved and required repetition counts match?

**Understanding target.** Compare the fourth-power exposure dependence and logarithmic confidence cost at fixed field norm bound and positive chirality promise. Identify which bound additionally tracks the size of the chirality gap explicitly.

**Dependencies and story role.** Join the attainable estimate of M21 with the transcript lower bound of M24.

**Conceptual connection.** One sheltered spin meets the same exposure-rate lower bound as experiments with arbitrarily many sheltered spins, within the independent-round model.

**Source.** [Protocol](../science/protocol.md) · [Converse](../science/converse.md)

### M26 A common false-count floor

**Central question.** What does an identical detector misclassification in both settings do to the mean and the variance?

**Understanding target.** Under an affine readout model, cancel the common additive offset in the contrast and retain its contribution to the outcome variance.

**Dependencies and story role.** M14 gives one physical detector and M20–M21 explain why the ideal scheme gains from low variance.

**Conceptual connection.** A fixed positive false-count floor eventually dominates the quadratic event rate. The simple detector then requires sixth-power exposure scaling at sufficiently short time.

**Source.** [Robustness](../science/robustness.md)

### M27 Differential offsets and imperfect shelter

**Central question.** Which imperfections can change the sign of the contrast?

**Understanding target.** Compare a setting-dependent readout bias with the cubic contrast, and interpret a fourth local rotation through the three relative rotations obtained by factoring out a common rotation.

**Dependencies and story role.** M17–M18 establish the ideal sign gap, and M26 distinguishes common offsets from statistical noise.

**Conceptual connection.** A shared readout offset adds noise. A differential offset can imitate chirality. A leaking spectator changes the field reference itself.

**Source.** [Robustness](../science/robustness.md)

### M28 A second coherent exposure

**Central question.** What extra operation lets three spins sense the handedness?

**Understanding target.** Track spin routing between two exposure windows to obtain ordered products of local unitaries. Connect the change in order to an inversion-odd singlet test.

**Dependencies and story role.** Revisit M09's swap, M12's single-window obstruction, and M17's order-sensitive term.

**Conceptual connection.** The obstruction prices one simultaneous exposure. A second coherent exposure plus permutation spends more local field interactions and can replace the sheltered spin.

**Source.** [Two-exposure comparison](../science/two-exposures.md)

### M29 What each check establishes

**Central question.** Why compare explicit matrices and numerical scaling with the analytical proofs?

**Understanding target.** Use direct matrix checks to verify normalization, contrast sign, and special examples. Identify the uniform quantifiers over fields, measurements, and classical adaptation that require proofs.

**Dependencies and story role.** M12–M28 give exact statements and experimentally relevant changes to the assumptions.

**Conceptual connection.** The project uses finite numerical checks to catch convention errors. Its conclusions over all allowed inputs follow from the stated identities and bounds.

**Source.** [Verification](../verification/verify.py) · [Science index](../science/README.md)

### M30 The complete resource account

**Central question.** What quantum information does the apparatus gain from what physical resources?

**Understanding target.** Explain the field-reversal blindness with three spins, how a sheltered fourth spin plus one SWAP gives a signed readout, why the ideal short-exposure rate is optimal, and which practical assumptions delimit it.

**Dependencies and story role.** Use M11 for the model, M12–M18 for the exact signal, M20–M25 for its rate, and M26–M29 for the nearby experiments.

**Conceptual connection.** The signed response requires a way to compare ordered field rotations. The acquisition cost then depends on how much statistical noise the detector adds to that response.

**Source.** [Science index](../science/README.md) · [Review bridge](BARTLETT_RUDOLPH_SPEKKENS_BRIDGE.md)
