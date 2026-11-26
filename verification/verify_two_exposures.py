"""Check the three-spin, two-window protocol by direct matrix evolution."""

import itertools

import numpy as np


IDENTITY = np.eye(2, dtype=complex)
PAULI = np.array([
    [[0, 1], [1, 0]],
    [[0, -1j], [1j, 0]],
    [[1, 0], [0, -1]],
])
BASIS = list(itertools.product(range(2), repeat=3))


def kron3(a, b, c):
    return np.kron(np.kron(a, b), c)


def cyclic_permutation():
    matrix = np.zeros((8, 8), dtype=complex)
    for column, (a, b, c) in enumerate(BASIS):
        matrix[BASIS.index((c, a, b)), column] = 1
    return matrix


def singlet_projector(i, j):
    projector = np.eye(8, dtype=complex)
    for axis in PAULI:
        factors = [IDENTITY, IDENTITY, IDENTITY]
        factors[i] = factors[j] = axis
        projector -= kron3(*factors)
    return projector / 4


def local_rotation(field, exposure):
    angle = exposure * np.linalg.norm(field) / 2
    vector = exposure * np.sinc(angle / np.pi) * field / 2
    scalar = np.cos(angle)
    unitary = scalar * IDENTITY - 1j * np.tensordot(vector, PAULI, axes=1)
    return scalar, vector, unitary


def direct_failure(unitary, route, preparation, test):
    total = unitary @ route @ unitary
    state = total @ (preparation / 2) @ total.conj().T
    return np.trace((np.eye(8) - test) @ state).real


def check_fields(fields, exposure, cycle, s12, s13):
    c, q, u = zip(*(local_rotation(field, exposure) for field in fields))
    full = kron3(*u)
    p_plus = direct_failure(full, cycle, s13, s12)
    p_minus = direct_failure(full, cycle.conj().T, s12, s13)
    first = np.trace(u[0] @ u[2] @ u[0].conj().T @ u[1].conj().T).real / 2
    second = np.trace(u[0] @ u[1] @ u[0].conj().T @ u[2].conj().T).real / 2
    signed_volume = q[0] @ np.cross(q[1], q[2])
    predicted = 4 * c[0] * (first + second) * signed_volume

    assert abs(p_plus - (1 - first**2)) < 1e-13
    assert abs(p_minus - (1 - second**2)) < 1e-13
    assert abs(p_plus - p_minus - predicted) < 1e-13
    assert 0 <= max(p_plus, p_minus) <= np.sin(exposure)**2 + 1e-13
    assert np.sign(p_plus - p_minus) == np.sign(np.linalg.det(fields))
    return p_plus, p_minus, abs(p_plus - p_minus - predicted)


def main():
    rng = np.random.default_rng(20261126)
    cycle = cyclic_permutation()
    s12 = singlet_projector(0, 1)
    s13 = singlet_projector(0, 2)
    count = 500
    worst_residual = 0.0

    for _ in range(count):
        fields = rng.normal(size=(3, 3))
        fields /= np.linalg.norm(fields, axis=1, keepdims=True)
        fields *= rng.uniform(0.05, 1, size=(3, 1))
        exposure = rng.uniform(0.02, np.pi / 4)
        _, _, residual = check_fields(fields, exposure, cycle, s12, s13)
        worst_residual = max(worst_residual, residual)

    exposure_values = np.geomspace(0.002, 0.08, 30)
    failure_rates = []
    contrasts = []
    hellinger_squared = []
    for exposure in exposure_values:
        p, q, _ = check_fields(np.eye(3), exposure, cycle, s12, s13)
        assert abs(p - q - np.sin(exposure)**3) < 1e-13
        failure_rates.append(p + q)
        contrasts.append(p - q)
        h2 = (np.sqrt(p) - np.sqrt(q))**2 + (np.sqrt(1-p) - np.sqrt(1-q))**2
        hellinger_squared.append(h2)

    slopes = np.array([
        np.polyfit(np.log(exposure_values), np.log(values), 1)[0]
        for values in (failure_rates, contrasts, hellinger_squared)
    ])
    assert np.allclose(slopes, [2, 3, 4], atol=0.01)
    print(f"Verified {count} random field triples. Max absolute residual {worst_residual:.3g}.")
    print("Weak-exposure slopes for total failure, contrast, and squared Hellinger:")
    print(" ".join(f"{slope:.6f}" for slope in slopes))


if __name__ == "__main__":
    main()
