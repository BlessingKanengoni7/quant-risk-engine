Quant Risk Engine
A Quantitative Risk Management & Capital Allocation System

<p align="center"> <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python Version"> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"> <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"> <img src="https://img.shields.io/badge/Status-Concept%20%2F%20Live-blueviolet?style=for-the-badge" alt="Status"> </p>
Quant Risk Engine
A Quantitative Risk Management & Capital Allocation System
Overview

Quant Risk Engine is a quantitative simulation framework designed to evaluate decision-making under uncertainty.

The system compares probabilistic forecasts against market prices, calculates statistical edge, applies Kelly-based capital allocation, and simulates long-term bankroll growth while measuring risk exposure.

Although demonstrated using sports market data, the architecture is generalizable to financial trading, portfolio allocation, and information systems risk management applications.

Core Objective

To model how capital should be allocated when:

Outcomes are uncertain

Probabilities are imperfect

Risk exposure must be controlled

Long-term growth must be optimized

This project focuses on risk-adjusted decision systems, not prediction itself.

System Architecture

The engine operates in four stages:

Probability Input Layer

Model probability (model_prob)

Market odds (market_odds)

Historical outcome (result)

Edge Detection

Convert odds to implied probability

Compute statistical edge

Capital Allocation

Apply Fractional Kelly Criterion

Adjust for risk appetite via Kelly multiplier

Filter trades using edge threshold

Performance & Risk Analytics

Final bankroll

ROI

Win rate

Sharpe ratio

Maximum drawdown

Equity curve

Risk Management Principles Implemented

This project directly applies quantitative risk management concepts:

Expected Value (EV)

Risk-Return Tradeoff

Capital Exposure Control

Drawdown Measurement

Volatility-Adjusted Performance (Sharpe Ratio)

Risk Appetite Adjustment (Fractional Kelly)

Relevance to Information Systems Risk Management (ISS2202)

This system demonstrates applied risk management within an information system context:

Structured data processing for risk evaluation

Quantitative exposure measurement

Algorithmic governance of capital allocation

Risk appetite calibration

Loss containment via drawdown control

Decision-support system design

Rather than qualitative “High/Medium/Low” risk assessment, this project implements measurable probabilistic risk evaluation.

Practical Applications

The framework can be adapted to:

Algorithmic trading strategy evaluation

Portfolio allocation models

Arbitrage detection systems

Hedge fund backtesting tools

Capital growth optimization problems

Financial risk simulation environments

Technologies Used

Python

Pandas

NumPy

Streamlit

Quantitative finance mathematics

What This Project Demonstrates

Understanding of probabilistic modeling

Capital allocation theory

Risk-adjusted performance metrics

Simulation and backtesting logic

Applied quantitative risk management

Decision-support system design

Future Enhancements

Monte Carlo simulation

Automated historical data ingestion

Predictive modeling integration

Parameter optimization layer

Multi-strategy portfolio simulation

Author

Developed as a quantitative risk modeling and decision-support system.
