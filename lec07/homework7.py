import numpy as np

def major_chord(f, Fs):
    '''
    Generate a one-half-second major chord, based at frequency f, with sampling frequency Fs.
    '''
    
    duration = 0.5
    N = int(Fs * duration)

    n = np.arange(N)

    # Frequencies of major chord
    f_root = f
    f_third = f * (2 ** (4/12))   # major third
    f_fifth = f * (2 ** (7/12))  # perfect fifth

    # Generate tones
    x1 = np.cos(2 * np.pi * f_root * n / Fs)
    x2 = np.cos(2 * np.pi * f_third * n / Fs)
    x3 = np.cos(2 * np.pi * f_fifth * n / Fs)

    # Combine tones
    x = x1 + x2 + x3

    return x


def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    '''

    n = np.arange(N)
    k = n.reshape((N, 1))

    W = np.cos(2 * np.pi * k * n / N) - 1j * np.sin(2 * np.pi * k * n / N)

    return W


def spectral_analysis(x, Fs):
    '''
    Find the three loudest frequencies in x.
    '''

    N = len(x)

    # FFT
    X = np.fft.fft(x)

    # Magnitudes
    magnitude = np.abs(X)

    # Frequency axis
    freqs = np.fft.fftfreq(N, d=1/Fs)

    # Use only positive frequencies
    positive = freqs >= 0
    freqs = freqs[positive]
    magnitude = magnitude[positive]

    # Find indices of 3 largest peaks
    indices = np.argsort(magnitude)[-3:]

    # Corresponding frequencies
    loudest_freqs = np.sort(freqs[indices])

    f1, f2, f3 = loudest_freqs

    return f1, f2, f3