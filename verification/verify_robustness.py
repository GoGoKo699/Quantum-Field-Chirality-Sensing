"""Check finite spectator leakage, exchange-area error and detector scaling."""

import itertools

import numpy as np

from verify_protocol import A, I, kron, local_unitary, pair_projection, pauli, prob


def swap_middle():
    basis = list(itertools.product(range(2), repeat=4))
    swap = np.zeros((16, 16))
    for column, (a, b, c, d) in enumerate(basis):
        swap[basis.index((a, c, b, d)), column] = 1
    return swap


def quaternion(matrix):
    scalar = np.trace(matrix).real / 2
    vector = np.array([(1j * np.trace(matrix @ s) / 2).real for s in pauli])
    return scalar, vector


def rare_rates(unitary, pulse, effect):
    return np.array([
        prob(pulse @ unitary @ A, effect),
        prob(unitary @ pulse @ A, effect),
    ])


def signed_contrast(rates):
    return rates[0] - rates[1]


def check_matrix_identities(rng, swap, effect):
    max_residual = dict(determinant=0.0, contrast=0.0, pulse_area=0.0)
    certified_cases = 0
    for _ in range(600):
        leakage = rng.uniform(0, 0.25)
        fields = rng.normal(size=(4, 3))
        fields /= np.linalg.norm(fields, axis=1)[:, None]
        fields *= (rng.uniform(0.1, 1, size=4) * np.array([1, 1, 1, leakage]))[:, None]
        exposure = rng.uniform(0.01, np.pi / 4 / (1 + leakage))
        local = [local_unitary(exposure / 2, field) for field in fields]
        local_gates = [item[0] for item in local]
        unitary = kron(*local_gates)
        ideal = rare_rates(unitary, swap, effect)

        relative = [quaternion(local_gates[3].conj().T @ gate) for gate in local_gates[:3]]
        c1, c2, c3 = [item[0] for item in relative]
        q1, q2, q3 = [item[1] for item in relative]
        even = c1*c2*c3 + c3*(q1@q2) + c2*(q1@q3) - c1*(q2@q3)
        odd = q1 @ np.cross(q2, q3)
        determinant = np.linalg.det([np.r_[c, q] for _, c, q in [local[3], *local[:3]]])
        max_residual["determinant"] = max(max_residual["determinant"], abs(determinant - odd))
        max_residual["contrast"] = max(max_residual["contrast"], abs(signed_contrast(ideal) - even*odd))

        chi = np.linalg.det(fields[:3])
        gap = np.cos(exposure * leakage / 2) * np.sinc(exposure / (2*np.pi))**3 * abs(chi) - 3*leakage
        if gap > 0:
            certified_cases += 1
            margin = np.cos(3*np.pi/8) * (exposure/2)**3 * gap
            assert np.sign(chi) * signed_contrast(ideal) >= margin - 1e-13

        area_error = rng.uniform(-np.pi, np.pi)
        cos = np.cos(area_error/2)
        sin = np.sin(area_error/2)
        pulse = cos*swap - 1j*sin*np.eye(16)
        expected = cos**2*ideal + sin**2*prob(unitary @ A, effect)
        observed = rare_rates(unitary, pulse, effect)
        max_residual["pulse_area"] = max(max_residual["pulse_area"], np.max(np.abs(observed - expected)))

    assert certified_cases > 0
    assert max(max_residual.values()) < 1e-12
    print(f"Robustness identities: 600 cases, largest residual {max(max_residual.values()):.3g}.")
    print(f"Spectator margin checked in {certified_cases} cases with a positive bound.")


def squared_hellinger(binary_probabilities):
    p, q = binary_probabilities
    return (np.sqrt(p)-np.sqrt(q))**2 + (np.sqrt(1-p)-np.sqrt(1-q))**2


def check_detector_scaling(swap, effect):
    exposures = np.geomspace(0.003, 0.05, 36)
    without_floor = []
    with_floor = []
    for exposure in exposures:
        unitary = kron(*(local_unitary(exposure/2, field)[0] for field in np.eye(3)), I)
        rates = rare_rates(unitary, swap, effect)
        without_floor.append(squared_hellinger(rates))
        with_floor.append(squared_hellinger(0.032 + 0.88*rates))
    slopes = [np.polyfit(np.log(exposures), np.log(data), 1)[0]
              for data in (without_floor, with_floor)]
    assert np.allclose(slopes, [4, 6], atol=0.01)
    print("Squared Hellinger slopes without and with a detector floor: "
          + ", ".join(f"{slope:.6f}" for slope in slopes))


def main():
    rng = np.random.default_rng(20261127)
    swap = swap_middle()
    effect = pair_projection(0, 1) @ (np.eye(16) - pair_projection(2, 3))
    check_matrix_identities(rng, swap, effect)
    check_detector_scaling(swap, effect)


if __name__ == "__main__":
    main()
