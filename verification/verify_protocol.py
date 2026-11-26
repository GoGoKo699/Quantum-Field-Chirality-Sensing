"""Check the single-exposure protocol on finite matrices."""

import itertools
import json
import numpy as np

I = np.eye(2)
pauli = [
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]),
]


def kron(*operators):
    result = operators[0]
    for operator in operators[1:]:
        result = np.kron(result, operator)
    return result


def local_unitary(angle, field):
    length = np.linalg.norm(field)
    vector = angle * np.sinc(angle * length / np.pi) * field
    scalar = np.cos(angle * length)
    matrix = scalar * I - 1j * sum(x * s for x, s in zip(vector, pauli))
    return matrix, scalar, vector


def pair_singlets(first_pair, second_pair):
    s = np.array([[0, 1], [-1, 0]]) / np.sqrt(2)
    return np.array([s[x[first_pair[0]], x[first_pair[1]]] *
                     s[x[second_pair[0]], x[second_pair[1]]]
                     for x in itertools.product(range(2), repeat=4)])


def pauli_product(qubits, operators, n):
    lookup = dict(zip(qubits, operators))
    return kron(*(lookup.get(site, I) for site in range(n)))


def pair_projection(i, j):
    return (np.eye(16) - sum(pauli_product((i, j), (s, s), 4) for s in pauli)) / 4


A = pair_singlets((0, 1), (2, 3))
B = pair_singlets((0, 2), (1, 3))
signs = [1, -1, -1, 1, 1, -1]
epsilon_ops = sum(sign * kron(*(pauli[i] for i in order))
                  for sign, order in zip(signs, itertools.permutations(range(3))))
invariants = [np.eye(8)] + [
    sum(pauli_product(pair, (s, s), 3) for s in pauli)
    for pair in itertools.combinations(range(3), 2)
] + [epsilon_ops]
Q_forward = pair_projection(0, 2) @ (np.eye(16) - pair_projection(1, 3))
Q_reverse = pair_projection(0, 1) @ (np.eye(16) - pair_projection(2, 3))


def prob(psi, projection):
    return np.real(psi.conj() @ projection @ psi)


def get_field_set(rng):
    fields = rng.normal(size=(3, 3))
    fields *= rng.uniform(0.05, 1, size=(3, 1)) / np.linalg.norm(fields, axis=1)[:, None]
    return fields


def main():
    rng = np.random.default_rng(20261126)
    largest = dict(amplitude=0., contrast=0., complementary_probability=0., inversion=0.)
    cases = 500
    for i in range(cases):
        fields = get_field_set(rng)
        angle = rng.uniform(1e-3, np.pi / 4) / 2
        ucs = [local_unitary(angle, b) for b in fields]
        u1, u2, u3 = [r[0] for r in ucs]
        c1, c2, c3 = [r[1] for r in ucs]
        q1, q2, q3 = [r[2] for r in ucs]
        C = c1*c2*c3 + c3*(q1@q2) + c2*(q1@q3) - c1*(q2@q3)
        D = q1 @ np.cross(q2, q3)
        U = kron(u1, u2, u3, I)
        psi_a, psi_b = U @ A, U @ B
        forward, reverse = B.conj() @ psi_a, A.conj() @ psi_b
        p_forward = prob(psi_a, Q_forward)
        p_reverse = prob(psi_b, Q_reverse)
        largest["amplitude"] = max(largest["amplitude"], abs(forward-(C-D)/2), abs(reverse-(C+D)/2))
        largest["contrast"] = max(largest["contrast"], abs(p_forward-p_reverse-C*D))
        largest["complementary_probability"] = max(
            largest["complementary_probability"],
            abs(p_forward - (0.25-abs(forward)**2)), abs(p_reverse - (0.25-abs(reverse)**2)))
        assert C >= np.cos(3 * angle)
        assert (p_forward - p_reverse) * np.linalg.det(fields) > 0
        U3 = kron(u1, u2, u3)
        observed = np.array([[np.trace(a @ U3 @ b @ U3.conj().T)
                              for b in invariants] for a in invariants])
        largest["inversion"] = max(largest["inversion"], float(np.max(np.abs(observed-observed.T))))

    assert max(largest.values()) < 5e-14
    ts = np.geomspace(1e-3, .08, 40)
    rare, contrast, hellinger = [], [], []
    for t in ts:
        unitary = kron(*(local_unitary(t / 2, field)[0] for field in np.eye(3)), I)
        p = prob(unitary @ A, Q_forward)
        q = prob(unitary @ B, Q_reverse)
        rare.append(p + q)
        contrast.append(abs(p-q))
        hellinger.append((np.sqrt(p) - np.sqrt(q)) ** 2 +
                         (np.sqrt(1-p) - np.sqrt(1-q)) ** 2)
    slopes = {k: float(np.polyfit(np.log(ts), np.log(v), 1)[0])
              for k, v in zip(("rare_rate", "contrast", "bernoulli_hellinger_squared"),
                              (rare, contrast, hellinger))}
    assert max(abs(x-y) for x, y in zip(slopes.values(), [2, 3, 4])) < .01
    print(json.dumps({"random_cases": cases, "seed": 20261126, "max_absolute_residuals": largest,
                      "orthogonal_unit_field_log_log_slopes": slopes}, indent=2))


if __name__ == "__main__":
    main()
