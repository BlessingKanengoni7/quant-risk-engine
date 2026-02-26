import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from engine import run_engine
import tempfile

st.set_page_config(
    page_title="Quant Risk Engine",
    layout="wide"
)

st.title("🏦 Quant Risk Engine Dashboard")

# ---- SIDEBAR CONTROLS ----

st.sidebar.header("⚙ Strategy Settings")

initial_bankroll = st.sidebar.number_input(
    "Initial Bankroll",
    value=10000
)

edge_threshold = st.sidebar.slider(
    "Edge Threshold",
    min_value=0.0,
    max_value=0.2,
    value=0.05
)

half_kelly = st.sidebar.slider(
    "Kelly Multiplier",
    min_value=0.1,
    max_value=1.0,
    value=0.5
)

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

# ---- MAIN ----

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    results = run_engine(
        file_path=tmp_path,
        initial_bankroll=initial_bankroll,
        edge_threshold=edge_threshold,
        half_kelly=half_kelly
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Final Bankroll", f"{results['final_bankroll']:.2f}")
    col2.metric("ROI", f"{results['roi']*100:.2f}%")
    col3.metric("Win Rate", f"{results['win_rate']*100:.2f}%")
    col4.metric("Sharpe", f"{results['sharpe']:.3f}")
    col5.metric("Max Drawdown", f"{results['max_drawdown']*100:.2f}%")

    st.subheader("Equity Curve")

    fig, ax = plt.subplots()
    ax.plot(results["equity_curve"])
    ax.set_xlabel("Bets")
    ax.set_ylabel("Bankroll")
    st.pyplot(fig)

    st.subheader("Category Breakdown")

    category_df = pd.DataFrame(results["category_report"]).T
    st.dataframe(category_df)

else:
    st.info("Upload a CSV file to run the engine.")