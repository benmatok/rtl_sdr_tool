FROM ubuntu:22.04

# Install system dependencies for RTL-SDR and Python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libusb-1.0-0-dev \
    git \
    cmake \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Build and install librtlsdr from source
RUN git clone https://github.com/osmocom/rtl-sdr.git \
    && cd rtl-sdr \
    && mkdir build \
    && cd build \
    && cmake ../ -DINSTALL_UDEV_RULES=ON \
    && make \
    && make install \
    && ldconfig \
    && cd ../.. \
    && rm -rf rtl-sdr

# Install Python dependencies
RUN pip3 install --no-cache-dir pyrtlsdr numpy matplotlib

# Copy the Python script into the container
RUN git clone https://github.com/benmatok/rtl_sdr_tool.git /app

# Set working directory
WORKDIR /app

# Default command (run the script)
CMD ["python3", "main.py"]
