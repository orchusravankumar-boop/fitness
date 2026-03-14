import streamlit as st

st.title(" Gym Planner")

def calculate_nutrition(weight, goal):
    if goal == "reduce":
        calories = round(weight * 24 * 0.85)
        protein_g = round(weight * 2.2)
        carbs_g = round(weight * 2.0)
        fat_g = round(weight * 0.8)
    else:
        calories = round(weight * 24 * 1.15)
        protein_g = round(weight * 2.0)
        carbs_g = round(weight * 4.0)
        fat_g = round(weight * 1.0)
    return {
        "daily_calories": calories,
        "protein_g": protein_g,
        "carbs_g": carbs_g,
        "fat_g": fat_g,
        "water_liters": round(weight * 0.033, 1)
    }

def get_workout_plan(goal):
    if goal == "reduce":
        plan = {
            "Monday":    {"muscles": ["Chest", "Triceps"],    "exercises": ["Bench Press 4x12", "Incline Dumbbell Press 3x15", "Cable Flyes 3x15", "Tricep Pushdown 3x15", "Skull Crushers 3x12"]},
            "Tuesday":   {"muscles": ["Back", "Biceps"],      "exercises": ["Pull-Ups 4x12", "Bent Over Row 4x12", "Lat Pulldown 3x15", "Barbell Curl 3x15", "Hammer Curl 3x15"]},
            "Wednesday": {"muscles": ["Legs", "Glutes"],      "exercises": ["Squats 4x15", "Leg Press 4x15", "Romanian Deadlift 3x15", "Leg Curl 3x15", "Calf Raises 4x20"]},
            "Thursday":  {"muscles": ["Shoulders", "Abs"],    "exercises": ["Overhead Press 4x12", "Lateral Raises 3x15", "Front Raises 3x15", "Plank 3x60s", "Crunches 3x20"]},
            "Friday":    {"muscles": ["Full Body", "Cardio"], "exercises": ["Deadlift 3x12", "Burpees 3x15", "Mountain Climbers 3x30s", "Jump Squats 3x15", "20 min HIIT Cardio"]},
        }
    else:
        plan = {
            "Monday":    {"muscles": ["Chest", "Triceps"],   "exercises": ["Bench Press 5x5", "Incline Barbell Press 4x8", "Dips 3x10", "Tricep Overhead Extension 3x10", "Close Grip Bench 3x8"]},
            "Tuesday":   {"muscles": ["Back", "Biceps"],     "exercises": ["Deadlift 5x5", "Barbell Row 4x8", "Weighted Pull-Ups 3x8", "Barbell Curl 4x10", "Preacher Curl 3x10"]},
            "Wednesday": {"muscles": ["Legs", "Glutes"],     "exercises": ["Squats 5x5", "Leg Press 4x10", "Bulgarian Split Squat 3x10", "Hip Thrust 4x10", "Leg Extension 3x12"]},
            "Thursday":  {"muscles": ["Shoulders", "Traps"], "exercises": ["Overhead Press 5x5", "Arnold Press 3x10", "Lateral Raises 4x12", "Shrugs 4x12", "Face Pulls 3x15"]},
            "Friday":    {"muscles": ["Chest", "Back"],      "exercises": ["Incline Dumbbell Press 4x10", "Cable Crossover 3x12", "Seated Cable Row 4x10", "T-Bar Row 3x10", "Chest Supported Row 3x12"]},
        }
    return plan

body_weight = st.number_input("Body weight (kg)", min_value=30.0, max_value=200.0)
goal = st.radio("Goal", ["reduce", "bulk"])
if st.button("Get My Plan"):
    nutrition = calculate_nutrition(body_weight, goal)
    workout = get_workout_plan(goal)

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