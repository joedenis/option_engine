# Multi-Asset Options Pricing and Hedging Simulator

option-engine/
├── backtests/        # Scripts for backtesting hedging strategies, P&L, stress tests
├── data/             # Market data, CSVs, helpers to load them
├── market/           # Market objects: spot, volatility surfaces, correlation, yield curves
├── pricing/          # Pricing models, Monte Carlo engine, analytical formulas
├── risk/             # Greeks, hedging, P&L calculation
├── tests/            # Unit tests for all modules
├── examples/         # Example scripts to run pricing / hedging / backtests
├── requirements.txt
└── README.md





## Overview
This project implements a simulator for pricing and hedging European and barrier options on single and multiple assets.
It is designed to showcase quantitative finance knowledge, numerical methods, and software engineering skills, making it suitable for quant developer interviews.

Key features:
- Pricing European and barrier options using Monte Carlo simulation and analytical formulas
- Greeks calculation: Delta, Gamma, Vega
- Multi-asset options pricing with correlation
- Dynamic hedging backtesting
- Performance optimizations using NumPy and Numba

## Installation

```bash
git clone <repo_url>
cd quant-dev-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

