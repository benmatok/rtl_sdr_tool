# RTL-SDR Spectrum Analyzer Tool

This repo provides a Dockerized Python tool to capture and plot the power spectrum centered at 11.43 MHz using an RTL-SDR dongle. It uses pyrtlsdr for device interaction, numpy for computations, and matplotlib for plotting.

### Prerequisites

* Docker installed on your host machine.
* RTL-SDR hardware (e.g., RTL2832U dongle) plugged into a USB port.
* Linux host (for USB passthrough; tested on Ubuntu).
* Internet connection for building the Docker image.

### How to Use

1. Clone this repo:
```
git clone https://github.com/benmatok/rtl_sdr_tool.git
cd rtl_sdr_tool
```

2. Build the Docker image:
```
sudo docker build -t rtl-sdr-tool .
```

3. Run the container (with USB device access):
```
sudo docker run -it --rm --privileged -v /dev:/dev -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix rtl-sdr-tool
```

- `--privileged` and `-v /dev:/dev`: Allows access to the RTL-SDR USB device.
- `-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix`: Enables GUI plotting with matplotlib (requires X11 forwarding; omit if running headless).
- If you encounter USB permission issues, add `--device /dev/bus/usb` or ensure the dongle is detected on the host with `lsusb`.

4. Inside the container, run the script:
```
python3 main.py
```

This will capture samples, compute the FFT-based spectrum, and display a plot (or save it if modified for headless use).

### Notes
- The spectrum covers approximately ±1.024 MHz around XXX (based on a 2.048 MHz sample rate).
- Customize `main.py` for different frequencies, sample rates, or to save plots (e.g., `plt.savefig('spectrum.png')`).
- If building fails, ensure your host has libusb and other deps; the Dockerfile handles this inside the container.
- For headless operation (no plot display), modify the script to save images instead of showing them.

## About
A simple Dockerized RTL-SDR tool for spectrum analysis in Python.
