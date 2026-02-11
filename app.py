import streamlit as st
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("fitness_progress_model.keras")

st.set_page_config(page_title="Fitness Progress Predictor")

st.title("🏋️ Fitness Progress Predictor")
st.write("Predict your 4-week weight change based on lifestyle factors.")

# -----------------------------
# User Inputs (UPDATED RANGES)
# -----------------------------

calories = st.number_input(
    "Daily Calories",
    min_value=1200,
    max_value=4500,
    value=2500,
    step=50
)

protein = st.number_input(
    "Protein (g)",
    min_value=40,
    max_value=250,
    value=150,
    step=5
)

sleep = st.number_input(
    "Sleep (hours)",
    min_value=3.5,
    max_value=9.5,
    value=7.0,
    step=0.5
)

initial_weight = st.number_input(
    "Initial Weight (kg)",
    min_value=45.0,
    max_value=120.0,
    value=70.0,
    step=1.0
)

age = st.number_input(
    "Age",
    min_value=16,
    max_value=65,
    value=22
)

gender = st.selectbox("Gender", ["Female", "Male"])

# Activity mapping (must match training encoding)
activity_options = {
    "Sedentary (little to no exercise, <5k steps/day)": 0,
    "Light (1–3 workouts/week, 6–8k steps/day)": 1,
    "Moderate (3–5 workouts/week, 8–12k steps/day)": 2,
    "Very Active (6–7 workouts/week, 12k+ steps/day)": 3
}

activity = st.selectbox("Activity Level", list(activity_options.keys()))

# Convert categorical inputs
gender_val = 1.0 if gender == "Male" else 0.0
activity_val = float(activity_options[activity])

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Progress"):

    user_input = np.array(
        [[calories, protein, sleep, initial_weight, age, gender_val, activity_val]],
        dtype=np.float32
    )

    prediction = model.predict(user_input, verbose=0)
    predicted_value = float(prediction[0][0])

    st.success(f"📈 Predicted 4-week weight change: {predicted_value:.2f} kg")

    if predicted_value > 0.5:
        st.info("Likely in a calorie surplus (muscle/fat gain expected).")
    elif predicted_value < -0.5:
        st.warning("Likely in a calorie deficit (weight loss expected).")
    else:
        st.write("Likely near maintenance.")
