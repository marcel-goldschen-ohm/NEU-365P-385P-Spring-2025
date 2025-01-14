class MySpikingNeuron:
    """ My cool neuron
    
    This neuron can spike
    and stuff!
    """
    
    def __init__(self, rate=10):
        self.spike_rate_per_sec = rate
    
    def get_avg_seconds_to_next_spike(self):
        return 1 / self.spike_rate_per_sec