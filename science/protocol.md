# A singlet experiment for the sign of three fields

Let $`|S\rangle=(|01\rangle-|10\rangle)/\sqrt2`$. For sites $i,j$ let $S_{ij}$ and $T_{ij}$ be the singlet and full triplet projectors. Prepare $`|a\rangle=|S_{12}\rangle|S_{34}\rangle`$ and use the same detector for $S_{12}T_{34}$ in both settings. Site 4 is sheltered. Exchange of sites 2 and 3 maps the preparation to $`|b\rangle=|S_{13}\rangle|S_{24}\rangle`$ and maps the detector effect to $S_{13}T_{24}$.

| Setting | Operation order | Equivalent rare event |
| --- | --- | --- |
| Swap after | Prepare, expose, swap, measure | Prepare $a$, expose, observe singlet on 13 and triplet on 24 |
| Swap before | Prepare, swap, expose, measure | Prepare $b$, expose, observe singlet on 12 and triplet on 34 |

Subtract the event frequency for swap before from that for swap after. Choose the sign of the difference, breaking ties by a fixed rule. The entire detector and source are shared.

## Exact contrast

Write $`U_i=c_i I-i\mathbf q_i\cdot\boldsymbol\sigma`$ with $`c_i=\cos(t\|\mathbf b_i\|/2)`$ and $`\mathbf q_i=\sin(t\|\mathbf b_i\|/2)\widehat{\mathbf b}_i`$. At a zero field the last expression has its continuous value. Define

```math
\begin{aligned}
C={}&c_1 c_2 c_3+c_3\,\mathbf q_1\cdot\mathbf q_2
       +c_2\,\mathbf q_1\cdot\mathbf q_3
       -c_1\,\mathbf q_2\cdot\mathbf q_3,\\
D={}&\mathbf q_1\cdot(\mathbf q_2\times\mathbf q_3).
\end{aligned}
```

The overlap of the two singlet pairings is $1/2$. Moving each single-site rotation along its singlet uses $`(V\otimes I)|S\rangle=(I\otimes V^\dagger)|S\rangle`$ for $`V\in\mathrm{SU}(2)`$. The closed contraction gives the trace of the ordered rotations with coefficient $1/4$. Expanding the Pauli product gives

```math
\langle b|(U\otimes I)|a\rangle
=\frac14\operatorname{Tr}(U_3^\dagger U_1U_2^\dagger)
=\frac{C-D}{2}.
```

The reversed amplitude is $`(C+D)/2`$ by conjugate transposition and simultaneous field reversal. Both amplitudes are real. In the swap-after setting, 13 crosses two independently prepared singlets, so its reduced density stays $I_4/4$ under local rotations. Its singlet probability equals $1/4$. The rare event subtracts the probability that both tested pairs are singlets. The same argument applies to 12 in the swap-before setting. Accordingly

```math
\begin{aligned}
p_{\rm after}&=\frac14-\frac{(C-D)^2}{4},\\
p_{\rm before}&=\frac14-\frac{(C+D)^2}{4},\\
p_{\rm after}-p_{\rm before}&=CD.
\end{aligned}
```

Each normalized trace $`C\pm D`$ is the cosine of an angle bounded by $3tB/2$ using the triangle inequality for the geodesic angle on $\mathrm{SU}(2)$. Thus $`C\ge\cos(3\pi/8)>0`$ in the stated window. With $`\operatorname{sinc}(x)=\sin(x)/x`$ and its continuous value at zero,

```math
|CD|\ge g\,t^3|\chi|,
\qquad
g=\frac{\cos(3\pi/8)\operatorname{sinc}^3(\pi/8)}{8}.
```

## Why a cubic signal needs quartically many rounds

Each rare effect annihilates its initial state at zero exposure. The rates are at most order $t^2$ because the corresponding amplitudes are at most order $t$. Either rate is bounded by $`\|(U\otimes I-I)|\psi\rangle\|^2\le(3tB/2)^2`$. Pair one trial of each type and let $Z$ be the difference between the rare-event indicators. Its mean is $CD$, its variance is bounded by the sum of the two probabilities, and $`|Z-\mathbb E Z|\le2`$.

The one-sided Bernstein inequality gives an error probability at most $\delta$ after

```math
N=O\!\left(\frac{B^2}{t^4\chi_0^2}\log\frac{1}{\delta}\right)
```

total exposures. The squared signal is at least $g^2t^6\chi_0^2$, and both the variance and absolute mean are at most a constant times $t^2 B^2$. A statistic built from the bright cross-singlet outcomes has a constant background rate at zero exposure. Choosing the complementary, physically identifiable rare event gives the smaller variance. The [rate converse](converse.md) matches the exposure dependence. [Detector and shelter errors](robustness.md) gives conditions for retaining the gain.
