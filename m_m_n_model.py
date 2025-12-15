import numpy as np


model_config = {
    "arrival_rate": 0.1,
    "service_rate": 2,
    "num_servers": 3,
    "num_steps": 1000,
    "arrival_dist": lambda rng, rate: rng.poisson(rate),
    "service_dist": lambda rng, rate, servers: rng.poisson(rate * servers),
}


def m_m_n_model(model_config):
    arrival_rate = model_config["arrival_rate"]
    service_rate = model_config["service_rate"]
    num_servers = model_config["num_servers"]
    num_steps = model_config["num_steps"]

    rng = np.random.default_rng()

    arrival_dist = model_config["arrival_dist"]
    service_dist = model_config["service_dist"]

    system_state = []
    in_system = 0

    for _ in range(num_steps):
        arrivals = int(max(0, arrival_dist(rng, arrival_rate)))
        active_servers = min(num_servers, in_system)
        departures = (
            int(max(0, service_dist(rng, service_rate, active_servers)))
            if active_servers
            else 0
        )

        in_system = max(0, in_system + arrivals - departures)
        system_state.append(in_system)

    return system_state


