# Detector errors, spectator leakage, and exchange control

The protocol uses one fresh four-spin state per round. Write $`A=|S_{12}S_{34}\rangle`$ for the source, $`P=\mathrm{SWAP}_{23}`$ for the routing gate, and $`Q=P^{S}_{12}P^{T}_{34}`$ for the rare-event effect. The forward setting applies $`P`$ after the simultaneous field exposure, and the reverse setting applies it before. Ambient fields are fixed during each exposure and the chirality promise is $`|\chi|\geq\chi_0>0`$, with $`\chi=b_1\cdot(b_2\times b_3)`$ and $`\|b_i\|\le B`$ for $`1\leq i\leq3`$. Set $`\mathrm{sinc}(x)=\sin(x)/x`$ with its continuous value at zero.

## A common detector floor changes the sampling rate

Let $`p_s`$ be the true rare-event frequency in setting $`s\in\{F,R\}`$. With an ideally sheltered fourth spin, the exchange protocol gives $`p_F-p_R=CD`$, where

```math
c_i=\cos(t\|b_i\|/2),\qquad
q_i=\frac{t}{2}\mathrm{sinc}(t\|b_i\|/2)b_i,\qquad
D=q_1\cdot(q_2\times q_3),
```

```math
C=c_1 c_2 c_3+c_3(q_1\cdot q_2)+c_2(q_1\cdot q_3)-c_1(q_2\cdot q_3).
```

For $`0\lt tB\leq\pi/4`$, the sign of $`CD`$ is the sign of $`\chi`$. The gap and rate bounds

```math
|p_F-p_R|\geq \kappa t^3\chi_0,\qquad
p_F+p_R\leq \frac92(tB)^2,\qquad
\kappa=\frac{\cos(3\pi/8)\mathrm{sinc}^3(\pi/8)}{8}
```

follow from the singlet contraction and the fact that both ideal event amplitudes vanish at zero exposure. In particular, each event probability is at most $`\|(U-I)A\|^2`$ or the corresponding bound with $`PA`$, where $`U`$ is the joint field evolution and $`\|U-I\|\leq 3tB/2`$.

Suppose the same binary readout channel acts independently in both settings. Its false-positive probability is $`\alpha`$, its false-negative probability is $`\beta`$, and its slope is $`\lambda=1-\alpha-\beta>0`$. The reported event probabilities are $`q_s^{\mathrm{obs}}=\alpha+\lambda p_s`$. The offset cancels in the mean, and the contrast is multiplied by $`\lambda`$. Any common offset still contributes to the variance.

Pair one fresh shot from each setting, and take the sign of the mean of the reported differences. A difference lies in $`[-1,1]`$ and has variance at most $`q_F^{\mathrm{obs}}+q_R^{\mathrm{obs}}`$. Bernstein's inequality gives error at most $`\delta`$ with a total number of sensing shots

```math
N=O\!\left(
\frac{\alpha+\lambda(tB)^2}{\lambda^2 t^6\chi_0^2}
\log\frac1\delta
\right).
```

Here the linear term in Bernstein's denominator is absorbed by the variance bound used for design, since the magnitude of the mean is at most the sum of the two reported event probabilities. The crossover is at $`\alpha`$ of order $`\lambda(tB)^2`$. The ideal weak-exposure rate survives if the floor is at most of this order and the slope stays bounded away from zero. With a fixed positive false-positive probability and fixed positive slope, this detector and protocol require order $`t^{-6}`$ shots at fixed $`B,\chi_0`$.

**Matching lower bound for the paired settings.** Use the eligible triad $`b_i=B e_i`$ and its full reversal, where $`e_i`$ are right-handed coordinate vectors, and let $`x=tB`$. Its two ideal probabilities are $`\sin^2(x)(3\pm\sin x)/16`$. They exchange under reversal, are both of order $`x^2`$, and differ by $`\sin^3(x)/8`$. For $`0\leq\alpha\leq1/4`$, each reported Bernoulli probability lies below $`1/2`$ in the stated exposure regime and is bounded below by a positive constant times $`\alpha+\lambda x^2`$. Therefore the one-shot relative entropy is at most a constant times

```math
\frac{\lambda^2 x^6}{\alpha+\lambda x^2}.
```

This uses $`D(\mathrm{Bern}(u)\|\mathrm{Bern}(v))\leq (u-v)^2/[v(1-v)]`$. The relative-entropy chain rule adds the same bound per shot even when the choice between the two settings depends on earlier records. A sign decision with error at most $`\delta`$ under both hypotheses requires transcript relative entropy at least $`(1-2\delta)\log((1-\delta)/\delta)`$ by data processing. This yields a matching dependence on $`t,\alpha,\lambda,\delta`$ for these settings at fixed $`B,\chi_0`$ and $`0\lt\delta\leq1/8`$.

**Arbitrary invariant binary probes with two-sided report errors.** With fixed positive $`\alpha,\beta,\lambda`$, the $`t^{-6}`$ lower bound holds for any allowed fresh-round invariant quantum preparation and binary measurement followed by this report channel, including probes with additional spectators. For a fixed triad and its inverse, average each invariant probability over a common rotation. In the Taylor expansion of the averaged unitary conjugation channel, the term linear in $`t`$ vanishes because the rotated field generator has zero Haar mean, and the terms quadratic in $`t`$ cancel between the two hypotheses. The trace-norm commutator bound $`\|[K,X]\|_1\leq 2\|K\|\|X\|_1`$, with $`\|K\|\leq3B/2`$, gives a uniform third-order remainder. The true probability difference is $`O((tB)^3)`$. Reported probabilities lie in $`[\alpha,1-\beta]`$, so the relative entropy per shot is $`O((tB)^6)`$ and the same transcript argument applies. The two-sided condition keeps every possible reported binary outcome away from zero. The paired-settings lower bound needs only a false-positive floor.

## Calibration for setting-dependent readout

Allow $`q_s^{\mathrm{obs}}=\alpha_s+\lambda_s p_s`$. Subtract an estimate $`\widehat d`$ of $`\alpha_F-\alpha_R`$ from the reported sample contrast. If the offset error is at most $`\epsilon_0`$ and $`|\lambda_s-\lambda|\leq\epsilon_\lambda`$ for a common positive reference slope, then the corrected population contrast differs from $`\lambda(p_F-p_R)`$ by at most

```math
\epsilon_0+\epsilon_\lambda(p_F+p_R).
```

A sufficient condition is a strictly positive corrected margin $`g=\lambda|p_F-p_R|-\epsilon_0-\epsilon_\lambda(p_F+p_R)`$. With independent shots and a fixed offset correction, $`m`$ pairs give error at most

```math
\exp\!\left[-\frac{m g^2}
{2(q_F^{\mathrm{obs}}+q_R^{\mathrm{obs}}+2g/3)}\right].
```

The additive contrast uncertainty must fit inside a gap of order $`t^3\chi_0`$. The slope mismatch multiplies an outcome rate of order $`(tB)^2`$. A stable additive offset can be calibrated in independent zero-exposure runs if the two setting offsets carry over to the sensing runs. At zero exposure both ideal event probabilities vanish. Applying Bernstein to the calibration contrast gives accuracy $`\epsilon_0`$ at failure probability at most $`\delta_{\mathrm{cal}}`$ using order $`(\alpha_F+\alpha_R+\epsilon_0)\epsilon_0^{-2}\log(1/\delta_{\mathrm{cal}})`$ calibration pairs. These pairs are additional to the sensing shots. A setting-dependent false event introduced by exposure itself needs a separate calibration or a justified bound.

## A fourth field gives relative chirality

Suppose the fourth spin experiences $`U_4=\exp(-it b_4\cdot\sigma/2)`$ during exposure. The two initial pairings and both readouts are invariant under a common spin rotation. Factoring out $`U_4^{\otimes4}`$ makes the same experiment equivalent to local gates $`V_i=U_4^\dagger U_i`$ for $`i=1,2,3`$, and $`V_4=I`$. Hence the same contraction gives contrast $`C(V)D(V)`$ exactly.

Write $`u_i=(c_i,q_i)`$ for the real unit quaternion of $`U_i=c_iI-iq_i\cdot\sigma`$, using the coordinates above for all four sites. Then

```math
D(V)=
\det
\begin{pmatrix}
c_4 & q_4^{\mathsf T}\\
c_1 & q_1^{\mathsf T}\\
c_2 & q_2^{\mathsf T}\\
c_3 & q_3^{\mathsf T}
\end{pmatrix}.
```

Multiplication on the left by the unit quaternion of $`U_4^\dagger`$ is a rotation of real four-dimensional quaternion space. It sends the first row to $`(1,0,0,0)`$, and the other three rows have the imaginary parts of $`V_1,V_2,V_3`$, respectively. This proves the determinant formula. Reversing all four fields changes the sign of the determinant because each term uses three imaginary coordinates.

In the weak-exposure limit the signed quantity is the oriented volume relative to the fourth field,

```math
D(V)=\left(\frac t2\right)^3
\det\big[b_1-b_4,\ b_2-b_4,\ b_3-b_4\big]
+O\!\left(t^5\max(B,\|b_4\|)^5\right).
```

The expansion follows by replacing each $`c_i`$ by $`1+O(t^2\|b_i\|^2)`$ and each $`q_i`$ by $`(t/2)b_i+O(t^3\|b_i\|^3)`$. Row subtraction then gives the displayed leading determinant.

For a finite guarantee about the original three-field sign, suppose $`\|b_4\|\leq L`$ and $`0\lt t(B+L)\leq\pi/4`$. The relative gates have rotation angles from the identity at most $`t(B+L)/2`$ in the unit-quaternion metric, so $`C(V)\geq\cos(3\pi/8)`$. Expansion along the first column and $`\|q_i\|\leq (t/2)\|b_i\|`$ give

```math
\big|D(V)-c_4\,q_1\cdot(q_2\times q_3)\big|
\leq 3(t/2)^3 B^2L.
```

Consequently the sign of the original $`\chi`$ is certified whenever

```math
m_L=\cos(tL/2)\mathrm{sinc}^3(tB/2)\chi_0-3B^2L>0.
```

The contrast then has magnitude at least $`\cos(3\pi/8)(t/2)^3m_L`$. Both rare-event probabilities remain order $`t^2(3B+L)^2`$ or smaller. A uniformly positive leakage margin therefore preserves the ideal sampling exponent. With an uncontrolled fourth field the experiment returns a relative orientation, as specified by its exact determinant.

## Exchange routing error

Let the implemented pulse be a rotation-invariant unitary $`W`$ with $`\epsilon=\min_\phi\|W-e^{i\phi}P\|`$. The source is in the total-spin-zero sector, while the rare-event projector $`Q`$ has total spin one. Therefore $`QWA=QPA=0`$. Put $`h=(3B+L)/2`$, so $`\|U-I\|\le th`$. For the forward setting the difference between actual and ideal rare-event amplitudes is $`Q(W-P)(U-I)A`$, after choosing the phase of $`P`$. For the reverse setting it is $`Q(U-I)(W-P)A`$. Each has norm at most $`\epsilon th`$, and all four amplitude norms are at most $`th`$. Thus the contrast changes by at most $`4\epsilon (th)^2`$. Subtract this amount from the sign margin for a combined guarantee. Rotation-invariant routing errors keep the event dark at zero exposure but can use up the cubic signal margin if left uncalibrated.

**A common exchange-area error attenuates the contrast exactly.** For an isotropic exchange pulse with area $`\pi+\eta`$, its unitary is $`W=\cos(\eta/2)P-i\sin(\eta/2)I`$ up to phase. The four-spin time-reversal antiunitary $`\Theta=(i\sigma_y)^{\otimes 4}\mathcal K`$, with $`\mathcal K`$ conjugation in the computational basis, fixes $`A`$ and commutes with $`U,P,Q`$. Antiunitarity then makes the inner product of any two of $`QPUA,QUPA,QUA`$ real. The two rates consequently have the form

```math
p_s(W)=\cos^2(\eta/2)\,p_s(P)
+\sin^2(\eta/2)\,\|QUA\|^2 .
```

Subtracting cancels the shared extra term, giving $`p_F(W)-p_R(W)=\cos^2(\eta/2)[p_F(P)-p_R(P)]`$. For a common area error with nonzero cosine, the deterministic sign is preserved and the rare-event rates remain quadratic or smaller. The identity assumes isotropic exchange during the pulse, with the same area in both settings and local rotations confined to the field-exposure window.

## Device resources

A nearest-neighbor layout can prepare singlets on pairs 12 and 34, insert one exchange pulse on the 23 link either before or after exposure, then resolve the singlet-versus-triplet outcome on each original pair. The exchange area $`\int J_{23}(s)\,ds=\pi`$ implements a SWAP up to phase when the interaction is $`J_{23}(s)\mathbf S_2\cdot\mathbf S_3`$ with $`\hbar=1`$. Its singlet and triplet eigenvalues differ by one, which gives their relative phase of $`\pi`$. The two settings share the physical pairs, source and detector. Each round uses four spins, three signal exposures in the sheltered model, one exchange SWAP, two binary pair readouts, and no retained quantum state from a previous round. Both event and non-event shots count. The exposure time $`t`$ excludes preparation, switching, the exchange pulse, readout and reset. A wall-clock comparison must charge those times and calibration rounds.

Qiao and colleagues demonstrated singlet preparation, exchange-driven SWAPs and singlet-versus-triplet readout in a four-electron GaAs device. Their readout distinguishes the singlet from the entire triplet subspace in the reported mode, and their entanglement-swapping experiment uses the central exchange link. Wang and colleagues demonstrated four-spin singlet-product dynamics, independently tunable exchange links, and sequential joint pair readout in a germanium quantum-dot array. These are component precedents. A chirality implementation needs to establish the field exposure and spectator bounds, pulse isotropy, and matched calibrated readout in its own device. [Qiao et al., Nature Communications 11, 3022 (2020)](https://doi.org/10.1038/s41467-020-16745-0) · [Wang et al., npj Quantum Information 9, 58 (2023)](https://doi.org/10.1038/s41534-023-00727-3)
