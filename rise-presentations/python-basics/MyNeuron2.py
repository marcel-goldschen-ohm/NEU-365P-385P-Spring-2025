import numpy as np


brain_region = "hippocampus"


class MySpikingNeuron:
    """ My cool neuron
    
    This neuron can spike
    and stuff!
    """
    
    def __init__(self, rate=10):
        self.spike_rate_per_sec = rate
    
    def get_avg_seconds_to_next_spike(self):
        return 1 / self.spike_rate_per_sec


def create_three_random_neurons():
    random_spike_rates_per_sec = 10 / np.random.random(3)
    neurons = []
    for rate in random_spike_rates_per_sec:
        neurons.append(MySpikingNeuron(rate))
    return neurons