import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

# Initialize the RTL-SDR device
sdr = RtlSdr()

# Configure the device parameters
sdr.sample_rate = 2.048e6  # Sample rate in Hz (2.048 MHz for good bandwidth)
sdr.center_freq = 11.43e6  # Center frequency in Hz (11.43 MHz)
sdr.gain = 'auto'          # Automatic gain control; can set to a specific value like 20.0 if needed
sdr.freq_correction = 0    # PPM correction; adjust if your device has drift (e.g., 60)

# Read a batch of complex samples
num_samples = 256 * 1024   # Number of samples to read (larger for better resolution, but slower)
samples = sdr.read_samples(num_samples)

# Close the device
sdr.close()

# Compute the FFT to get the spectrum
# Use FFT shift for centered spectrum
fft_values = np.fft.fftshift(np.fft.fft(samples))
power_spectrum = np.abs(fft_values)**2  # Power spectrum

# Generate frequency axis
freqs = np.fft.fftshift(np.fft.fftfreq(num_samples, 1 / sdr.sample_rate)) + sdr.center_freq

# Plot the spectrum
plt.figure(figsize=(10, 6))
plt.plot(freqs / 1e6, 10 * np.log10(power_spectrum + 1e-10))  # Add small epsilon to avoid log(0)
plt.xlabel('Frequency (MHz)')
plt.ylabel('Power (dB)')
plt.title('Power Spectrum Centered at 11.43 MHz')
plt.grid(True)
plt.show()
