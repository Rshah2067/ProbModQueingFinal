import numpy as np
##L is the average customers in system
##LQ is the average customers in que
## gamma is the arrival to service ratio
##S is the Soujurn time (time spent in system)
##W is the wiating time (time spent in que)
def performance_metric(expected_arrival_rate, expected_service_rate,servers,customers__insys):
    L = np.mean(customers__insys)
    gamma = expected_arrival_rate/(expected_service_rate*servers)
    Lq = L - gamma
    S = L/expected_arrival_rate
    W = Lq/expected_arrival_rate
    return [L,gamma,S,W]