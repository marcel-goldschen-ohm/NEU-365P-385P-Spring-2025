import numpy as np
import MyNeuron


brain_region = "hippocampus"


def create_three_random_neurons():
    random_spike_rates_per_sec = 10 / np.random.random(3)
    neurons = []
    for rate in random_spike_rates_per_sec:
        neurons.append(MyNeuron.MySpikingNeuron(rate))
    return neurons