# 🧮 Math-Toolkit

A comprehensive collection of **mathematical calculators, unit & base converters, numerical analysis scripts, and math visualizations** built in MicroPython for the **NumWorks** calculator.

---

## 📂 Repository Structure

```
Math-Toolkit/
├── base_converter.py                # Flagship all-in-one Binary / Decimal / Hexadecimal converter
├── unit_converter.py                # Multi-category unit converter (distance, mass, currency, etc.)
├── geometry_trig_calculator.py      # Automated Trigonometry, Pythagoras, Thales & multiples solver
├── quadratic_canonical.py           # 2nd-degree polynomial analyzer (canonical, factored, roots & plot)
├── numerical_integral.py            # Definite integral calculator over a user-defined interval
├── simple_derivative.py             # Symbolic derivative calculator for basic functions
├── curve_plotter.py                 # Point-by-point interactive curve plotter
├── bar_chart_finance.py             # Simple bar-chart data visualizer
├── utilities/
│   ├── rounding.py                  # Custom rounding helper functions
│   ├── nearest_furthest.py          # Nearest and furthest value lookup helpers
│   └── wilson_primality.py          # Prime number verification via Wilson's theorem
├── experiments/
│   ├── eratosthenes_sieve.py        # Full-screen Sieve of Eratosthenes (71,040 values)
│   ├── fourier_transform_viz.py     # Polar Fourier Transform winding-machine visualization
│   └── fibonacci.py                 # Fibonacci sequence generator
└── history/
    └── base_conversions/            # Earlier standalone base conversion scripts
```

---

## 🛠️ Core Tools

### Base Converter *(Flagship)*
[`base_converter.py`](base_converter.py) · *Created February 15, 2025*

All-in-one numerical base converter unifying every conversion between **Binary**, **Decimal**, and **Hexadecimal** (replacing the 6 standalone scripts archived in `history/base_conversions/`).

### Unit Converter
[`unit_converter.py`](unit_converter.py) · *Created April 05, 2023*

Comprehensive unit converter supporting distances, weights, currencies, temperatures, speeds, time, volumes, pressures, and numerical values.

### Geometry & Trigonometry Solver
[`geometry_trig_calculator.py`](geometry_trig_calculator.py) · *Created April 14, 2023*

Automates common middle/high-school math calculations: **Trigonometry**, **Pythagorean theorem**, **Thales' theorem**, and finding multiples of a number.

### Quadratic Polynomial Analyzer
[`quadratic_canonical.py`](quadratic_canonical.py) · *Created November 18, 2023*

Computes the **canonical form**, **factored form** (when real roots exist), **equation solutions**, and draws a draft of the parabola on screen, exiting cleanly if no real factorization exists.

### Numerical Integral
[`numerical_integral.py`](numerical_integral.py) · *Created November 28, 2023*

Calculates the definite numerical integral of a user-defined function between two bounds.

### Simple Derivative
[`simple_derivative.py`](simple_derivative.py) · *Created November 04, 2023*

Prompts for a function and outputs its derivative. Functional for simple expressions, though limited on complex functions.

### Curve Plotter
[`curve_plotter.py`](curve_plotter.py) · *Created April 04, 2023*

Plots custom curves by asking for start/end coordinates and optional intermediate waypoints, displaying all entered points alongside the final trace. *(More of an exploratory plotter without a specific real-world use case.)*

### Bar Chart Visualizer
[`bar_chart_finance.py`](bar_chart_finance.py) · *Created April 03, 2023*

Simple script that takes a list of values and displays them as a bar chart.

---

## 🔧 Utilities (`utilities/`)

### Custom Rounding
[`utilities/rounding.py`](utilities/rounding.py) · *Created May 01, 2023*

Experimental functions implementing custom number-rounding approaches.

### Nearest & Furthest Values
[`utilities/nearest_furthest.py`](utilities/nearest_furthest.py) · *Created December 20, 2023*

Two utility functions returning the closest and furthest values relative to a given target.

### Wilson Primality Test
[`utilities/wilson_primality.py`](utilities/wilson_primality.py) · *Creation date unrecorded*

Verifies prime numbers within a range using **Wilson's theorem**: $(p - 1)! + 1 \equiv 0 \pmod{p}$. *(Mathematically exact, though computationally inefficient due to factorial growth.)*

---

## 🧪 Math Experiments & Visualizations (`experiments/`)

Exploratory scripts focused on visual or algorithmic curiosity rather than practical calculation:

### Sieve of Eratosthenes
[`experiments/eratosthenes_sieve.py`](experiments/eratosthenes_sieve.py) · *Created June 05, 2025*

Visualizes the **Sieve of Eratosthenes** across the full `320 × 222` screen (`1 pixel = 1 integer`, sieving **71,040 values**) and returns the first 3,000 primes found (capped by calculator RAM).

### Fourier Transform Visualization
[`experiments/fourier_transform_viz.py`](experiments/fourier_transform_viz.py) · *Creation date unrecorded*

Visualizes the **Fourier Transform "winding machine"**: wraps a multi-frequency cosine signal (`fq` in Hz) around the origin in polar coordinates and plots the resulting **center of mass** (green dot) relative to the central axis (red line). *Note: Purely a visual exploration — it does not output numerical frequency values.*

### Fibonacci Sequence
[`experiments/fibonacci.py`](experiments/fibonacci.py) · *Created April 26, 2023*

Computes and displays the requested number of terms from the Fibonacci sequence.

---

## 🕰️ Base Conversion History (`history/base_conversions/`)

Individual conversion scripts created prior to being unified into `base_converter.py`:

- [`bin_to_dec.py`](history/base_conversions/bin_to_dec.py) · *Created May 09, 2023*
- [`hex_to_dec.py`](history/base_conversions/hex_to_dec.py) · *Created May 09, 2023*
- [`bin_to_hex.py`](history/base_conversions/bin_to_hex.py) · *Created February 15, 2025*
- [`dec_to_bin.py`](history/base_conversions/dec_to_bin.py) · *Created February 15, 2025*
- [`dec_to_hex.py`](history/base_conversions/dec_to_hex.py) · *Created February 15, 2025*
- [`hex_to_bin.py`](history/base_conversions/hex_to_bin.py) · *Created February 15, 2025*

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `math`, `time`).
