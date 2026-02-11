import streamlit as st
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("fitness_progress_model.keras")

st.set_page_config(page_title="Fitness Progress Predictor")

st.title("🏋️ Fitness Progress Predictor")
st.write("Predict your 4-week weight change based on lifestyle factors.")

# -----------------------------
# User Inputs
# -----------------------------

calories = st.number_input("Daily Calories", 1800, 4000, 2500)
protein = st.number_input("Protein (g)", 50, 250, 150)
sleep = st.number_input("Sleep (hours)", 4.0, 10.0, 7.0)
initial_weight = st.number_input("Initial Weight (kg)", 40.0, 120.0, 70.0)
age = st.number_input("Age", 16, 70, 22)
gender = st.selectbox("Gender", ["Female", "Male"])

# Clean activity mapping dictionary
activity_options = {
    "Sedentary (little to no exercise, <5k steps/day)": 0,
    "Light (1–3 workouts/week, 6–8k steps/day)": 1,
    "Moderate (3–5 workouts/week, 8–12k steps/day)": 2,
    "Very Active (6–7 workouts/week, 12k+ steps/day)": 3
}

activity = st.selectbox("Activity Level", list(activity_options.keys()))

# Convert categorical inputs to numeric
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
