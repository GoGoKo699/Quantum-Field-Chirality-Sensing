# Two coherent exposures with three spins

The one-exposure result prices the sheltered spin when the sensor array admits one uninterrupted field window. A device with two coherent windows can recover the same handedness using its three sensing spins. The protocol routes the spin states around a cycle between the windows and measures singlet failures. Each run uses six local field exposures. All three spins see the fields during both windows.

## Protocol and exact contrast

Let $`U_i=\exp(-it\,\mathbf b_i\cdot\boldsymbol\sigma/2)`$ and $`U=U_1\otimes U_2\otimes U_3`$. The fields are unchanged between the two windows of a run. A common proper rotation of the fields may vary across independent runs. Let $`P|a,b,c\rangle=|c,a,b\rangle`$, so $`PUP^\dagger=U_3\otimes U_1\otimes U_2`$. Write $`S_{ij}`$ for the two-spin singlet projector, and write $`T_{ij}=I-S_{ij}`$ for the corresponding triplet projector.

| Setting | Prepare | Route between windows | Declare a failure |
| --- | --- | --- | --- |
| $`+`$ | Singlet on $`13`$, other spin maximally mixed | $`P`$ | Pair $`12`$ is triplet |
| $`-`$ | Singlet on $`12`$, other spin maximally mixed | $`P^\dagger`$ | Pair $`13`$ is triplet |

The cyclic permutation uses two sequential SWAPs. With SWAPs on pairs $`12`$ and $`23`$, swapping $`23`$ first and $`12`$ second gives $`P`$. Reversing the order gives $`P^\dagger`$. Both preparation settings and both measurements are invariant under a common spin rotation. Every run begins with a fresh preparation and produces one classical bit.

The $`+`$ setting is equivalent to preparing a singlet on $`12`$, then applying $`UPUP^\dagger`$ and testing pair $`12`$. The three local factors of this effective unitary are $`U_1 U_3,\ U_2 U_1,\ U_3 U_2`$. The $`-`$ setting is equivalent to preparing a singlet on $`13`$, then applying $`UP^\dagger UP`$ and testing pair $`13`$. Its factors are $`U_1 U_2,\ U_2 U_3,\ U_3 U_1`$. The two factors determining each singlet survival amplitude follow from $`\langle s|(V\otimes W)|s\rangle=\mathrm{Tr}(VW^\dagger)/2`$ for $`V,W\in SU(2)`$.

Write $`U_i=c_i I-i\mathbf q_i\cdot\boldsymbol\sigma`$, with $`c_i=\cos(\theta_i)`$, $`\mathbf q_i=(t/2)\mathrm{sinc}(\theta_i)\mathbf b_i`$, $`\theta_i=t\|\mathbf b_i\|/2`$, and $`\mathrm{sinc}(z)=\sin(z)/z`$ extended continuously at zero. Let $`R_1`$ be the proper rotation satisfying $`U_1(\mathbf w\cdot\boldsymbol\sigma)U_1^\dagger=(R_1\mathbf w)\cdot\boldsymbol\sigma`$. The singlet survival amplitudes are real and equal to
```math
\begin{aligned}
x&=\tfrac12\mathrm{Tr}(U_1 U_3 U_1^\dagger U_2^\dagger)=c_2 c_3+\mathbf q_2\cdot R_1\mathbf q_3,\\
y&=\tfrac12\mathrm{Tr}(U_1 U_2 U_1^\dagger U_3^\dagger)=c_2 c_3+\mathbf q_3\cdot R_1\mathbf q_2.
\end{aligned}
```
Rodrigues' formula gives $`(R_1-R_1^\mathsf{T})\mathbf w=4c_1\mathbf q_1\times\mathbf w`$. Thus $`x-y=-4c_1 D`$, where $`D=\mathbf q_1\cdot(\mathbf q_2\times\mathbf q_3)`$. The difference of triplet probabilities is
```math
p_+-p_-=(1-x^2)-(1-y^2)=4c_1(x+y)D.
```
If $`0\lt tB\le\pi/4`$ and $`\|\mathbf b_i\|\le B`$, then $`x,y\ge c_2 c_3-\|\mathbf q_2\|\|\mathbf q_3\|=\cos(\theta_2+\theta_3)\ge\cos(tB)>0`$. Also $`c_1>0`$ and every sinc factor is positive. The sign of $`p_+-p_-`$ is therefore the sign of $`\chi=\mathbf b_1\cdot(\mathbf b_2\times\mathbf b_3)`$. For the orthogonal unit-field triad $`(\mathbf e_x,\mathbf e_y,\mathbf e_z)`$, the contrast is exactly $`\sin^3 t`$.

## Samples and exposure accounting

The same bounds give $`p_\pm\le\sin^2(tB)`$ and
```math
|p_+-p_-|\ge t^3\cos(\pi/8)\cos(\pi/4)\mathrm{sinc}^3(\pi/8)|\chi|.
```
With one independent run of each setting, their indicator difference has variance at most $`p_++p_-\le 2(tB)^2`$ and takes values in $`\{-1,0,1\}`$. Repeat the pair and decide from the sign of its empirical mean. Bernstein's inequality gives error at most $`\delta`$ with $`O(B^2t^{-4}\chi_0^{-2}\log(1/\delta))`$ runs under $`|\chi|\ge\chi_0>0`$. Every run counts, including the runs that return to the singlet. The linear term in the Bernstein bound is absorbed using $`|p_+-p_-|\le p_++p_-`$.

The sheltered-spin protocol spends one three-site exposure and one unexposed spin per run. The cyclic protocol spends two three-site exposures, two invariant SWAPs between them, and no unexposed spin. The second window must retain quantum coherence with the first and use the same fields. Fresh preparations between the two windows would instead implement two independent, inversion-blind tests when only the three sensing spins are available.

## Converse with two fixed field windows

Consider two field exposures of durations $`\tau_1,\tau_2\le t`$, an arbitrary rotation-covariant trace-preserving operation between them, and invariant preparation and readout. The intermediate operation is independent of the unknown fields. The converse permits any number of unexposed ancillary spins within each round. Across rounds it permits classical adaptation, with a fresh quantum preparation each time.

Fix an admissible triad and its simultaneous inversion. Let $`g`$ be a Haar-distributed common rotation and $`K_g=\sum_i(R_g\mathbf b_i)\cdot\boldsymbol\sigma_i/2`$ be the generator on the sensing spins. Its norm is at most $`k=3B/2`$ and its Haar mean vanishes. Invariance and covariance allow averaging each outcome probability over $`g`$. Deferring the intermediate operation to an isometry $`W`$, the resulting square root of the probability for outcome $`j`$ is the $`L^2(dg)`$ Hilbert–Schmidt norm of
```math
(M_j^{1/2}\otimes I_E)F_\pm(1,g)\sqrt{\rho},
\qquad
F_\pm(s,g)=(e^{\mp is\tau_2 K_g}\otimes I_E)\,W\, e^{\mp is\tau_1 K_g}.
```
Here $`E`$ is the unused isometry output and the field generators act trivially on unexposed ancillas. The affine approximation at $`s=0`$ is $`W+sF_\pm'(0,g)`$. Its outcome norms agree for the two signs because $`F_-^\prime(0,g)=-F_+^\prime(0,g)`$ and the Haar mean of either derivative is zero. The second derivative satisfies $`\|F_\pm''(s,g)\|\le k^2(\tau_1+\tau_2)^2`$. By the integral Taylor bound and $`\sum_j M_j=I`$, the sum of squared outcome remainder norms for either sign is at most $`k^4(\tau_1+\tau_2)^4/4`$. The reverse triangle inequality then gives the one-round affinity bound
```math
\sum_j\sqrt{p_j^+p_j^-}\ \ge\ 1-\tfrac12k^4(\tau_1+\tau_2)^4\ \ge\ 1-\tfrac12(3Bt)^4 .
```

This bound is uniform in the conditional setting selected from a classical history, so the $`n`$-round transcript affinity is at least $`[1-(3Bt)^4/2]^n`$ in the weak-exposure regime. A decision with error at most $`\delta`$ on both alternatives implies affinity at most $`2\sqrt{\delta(1-\delta)}`$ by the bound between affinity and total variation. Consequently, $`\Omega(t^{-4}\log(1/\delta))`$ runs are necessary as $`t\to0`$ at fixed feasible $`B,\chi_0`$, uniformly over $`\delta\le1/8`$. This comparison matches the short-exposure and confidence exponents for the fixed two-window class.

For a single field window, see the [three-spin inversion-blindness proof](converse.md). The coherent cyclic route uses the order of successive local rotations to obtain the signal.
