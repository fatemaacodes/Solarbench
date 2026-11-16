import streamlit as st
import numpy as np
import pandas as pd

# Page config
st.set_page_config(page_title="Solar AI Bench", layout="wide")

# Title
st.title("🌞 Solar Powered Charging Bench - AI System")
st.markdown("Smart energy prediction & charging optimization")

# Sidebar inputs
st.sidebar.header("🔧 Control Panel")

sunlight = st.sidebar.slider("Sunlight Intensity (%)", 0, 100, 70)
users = st.sidebar.slider("Number of Users", 0, 10, 3)
weather = st.sidebar.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy"])

# Weather impact factor
weather_factor = {
    "Sunny": 1.0,
    "Cloudy": 0.6,
    "Rainy": 0.3
}

# AI-like energy calculation
base_energy = sunlight * weather_factor[weather]
energy = base_energy - (users * 5)
energy = max(0, min(100, energy))

# Layout
col1, col2, col3 = st.columns(3)

# Metrics
col1.metric("🔋 Battery Level", f"{int(energy)}%")
col2.metric("👥 Active Users", users)
col3.metric("☀️ Solar Input", f"{int(base_energy)}%")

st.markdown("---")

# AI Decision System
st.subheader("🤖 AI Recommendation System")

if energy > 75:
    st.success("✅ High Energy: Charge freely, all ports available!")
elif energy > 40:
    st.warning("⚠️ Moderate Energy: Limited charging recommended.")
else:
    st.error("❌ Low Energy: Please wait or reduce usage.")

# Charging slots logic
max_slots = int(energy // 10)
st.info(f"🔌 Available Charging Slots: {max_slots}")

# Graph simulation
st.subheader("📊 Energy Generation Trend (Simulation)")

time = np.arange(0, 24)
simulated_energy = np.clip(
    (np.sin((time - 6) / 24 * 2 * np.pi) * 50 + 50) * weather_factor[weather],
    0, 100
)

df = pd.DataFrame({
    "Time (Hours)": time,
    "Energy Level (%)": simulated_energy
})

st.line_chart(df.set_index("Time (Hours)"))

# Footer
st.markdown("---")
st.markdown("💡 *This system uses AI-based logic to optimize solar energy usage and improve efficiency.*")