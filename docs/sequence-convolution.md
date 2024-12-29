# Sequence and Convolution
In neuroscience it is common to work with **time series** and **image** data. A time series is a 1-D sequence of values, whereas an image is a 2-D sequence. A color image would be a 3-D sequence, and a color movie a 4-D sequence.

Sequences differ from independent random variables in that *nearby samples in the sequence are correlated* (unless just noise). These correlations require you to analyze sequences with special tools. Familiarizing yourself with the topics below will provide you a solid foundation for working with time series and image data.

- Autocorrelation
- Fourier transform
    - Power spectrum
    - Spectrogram
- Sampling (aliasing) artifacts
- Convolution
    - Filter
    - Feature kernel
    - Joint probability