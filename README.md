# Benchmark Tool

This project is a benchmarking tool to measure the performance of CPU, RAM, and GPU using Python. It is designed to work on macOS, including support for the Apple M1 chip, using TensorFlow with Metal optimization for GPU tests.

## Prerequisites

Before running the project, make sure you have the following requirements:

- Python 3.8 or higher
- Pip (Python package manager)

## Installing Dependencies

To run the tool, install the following libraries using pip:

```bash
pip install numpy psutil tensorflow-macos tensorflow-metal
```

### Dependency Description
- **numpy**: used for mathematical operations and array management.
- **psutil**: used to collect system information such as memory usage.
- **tensorflow-macos** and **tensorflow-metal**: used for GPU acceleration via Apple's Metal framework.

## Running the Project

1. Make sure you have all the dependencies installed correctly.
2. Run the program using the following command:

```bash
python benchmark.py
```

## Included Tests

### 1. CPU Benchmark
Measures the time required to perform a sum of squares of numbers up to 1,000,000 to evaluate CPU performance.

### 2. RAM Benchmark
Allocates memory for a large array and measures memory usage before and after allocation.

### 3. GPU Benchmark
Performs matrix multiplication using TensorFlow with Metal optimization to measure GPU performance. This test only works if the GPU is available and detected by TensorFlow.

## Limitations
- The GPU test uses TensorFlow optimized for the Apple M1 chip via Metal. It will not work on devices that do not support this configuration.
- The RAM test allocates a large array; make sure you have enough memory available.

## System Information
The tool displays system information, such as the operating system, processor, and total available memory, before running the benchmarks.

## Contact
For questions or improvements, feel free to contribute or contact the author.
