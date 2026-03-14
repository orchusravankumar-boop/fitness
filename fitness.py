import streamlit as st
import requests

st.title("🏋️ Gym Planner")
st.write("Get your personalized nutrition and workout plan.")

body_weight = st.number_input("Enter your body weight (kg)", min_value=30.0, max_value=200.0, step=0.5)
goal = st.radio("What is your goal?", ["reduce", "bulk"], format_func=lambda x: "⚡ Lose Weight (Reduce)" if x == "reduce" else "💪 Gain Muscle (Bulk)")

if st.button("Get My Plan"):
    response = requests.post("http://127.0.0.1:8000/gym-plan", 
                             json={
        "body_weight_kg": body_weight,
        "goal": goal
    })

    if response.status_code == 200:
        data = response.json()
        nutrition = data["nutrition"]
        workout = data["workout_plan"]

        st.subheader("🥗 Daily Nutrition Targets")
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Calories", f"{nutrition['daily_calories']} kcal")
        col2.metric("Protein", f"{nutrition['protein_g']}g")
        col3.metric("Carbs", f"{nutrition['carbs_g']}g")
        col4.metric("Fat", f"{nutrition['fat_g']}g")
        col5.metric("Water", f"{nutrition['water_liters']}L")

        st.subheader("🗓️ 5-Day Workout Plan")
        for day, details in workout.items():
            with st.expander(f"{day} — {' + '.join(details['muscles'])}"):
                for exercise in details["exercises"]:
                    st.write(f"• {exercise}")
    else:
        st.error("Something went wrong. Make sure the API is running.")