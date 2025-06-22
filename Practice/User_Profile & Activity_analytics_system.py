import math
import json

# 1. Text Type: str
user_name = "Alice"
email = "alice@example.com"
bio = """A fitness enthusiast who loves hiking and coding.
Currently training for a marathon."""

# 2. Numeric Types: int, float, complex
age = 28
daily_steps = 7532
calories_burned = 420.5
sensor_data = 3 + 4j  # Complex numbers for advanced calculations

# 3. Sequence Types: list, tuple, range
activity_logs = ["Walking", "Running", "Swimming", "Cycling"]  # list (mutable)
user_id = (1001, "USR")  # tuple (immutable)
workout_schedule = range(1, 6)  # range (for days 1-5)

# 4. Mapping Type: dict
user_profile = {
    "name": user_name,
    "age": age,
    "email": email,
    "bio": bio,
    "active": True,
    "preferences": {
        "theme": "dark",
        "notifications": True
    }
}

# 5. Set Types: set, frozenset
interests = {"hiking", "coding", "yoga", "photography"}  # set (mutable)
readonly_interests = frozenset(["reading", "chess"])  # frozenset (immutable)

# 6. Boolean Type: bool
is_active = True
has_subscription = False

# 7. Binary Types: bytes, bytearray, memoryview
encoded_bio = bio.encode()  # str → bytes
bio_bytes = bytearray(encoded_bio)  # bytes → bytearray
mem_view = memoryview(encoded_bio)  # memoryview of bytes

# 8. None Type: None
middle_name = None  # Optional field

# Function to analyze activity data
def analyze_activity(steps, calories):
    # Type checking
    if not isinstance(steps, int) or not isinstance(calories, (int, float)):
        raise ValueError("Steps must be integer, calories must be numeric")
    
    # Calculate step goal completion
    step_goal = 10000
    completion_rate = (steps / step_goal) * 100
    category = "Active" if completion_rate >= 80 else "Sedentary"
    
    # Return dictionary with mixed data types
    return {
        "completion_rate": round(completion_rate, 2),
        "category": category,
        "calories_burned": calories,
        "sensor_data": str(sensor_data)  # Convert complex to string for display
    }

# Function to compare user interests
def compare_interests(user1_interests, user2_interests):
    common = user1_interests.intersection(user2_interests)
    unique = user1_interests.symmetric_difference(user2_interests)
    return {
        "common_interests": list(common),
        "unique_interests": list(unique),
        "total_unique": len(unique)
    }

# Generate user report
def generate_report(user_data):
    report = f"""
=== USER PROFILE REPORT ===
Name: {user_data['name']}
Age: {user_data['age']}
Email: {user_data['email']}
Active Status: {'Active' if user_data['active'] else 'Inactive'}
Bio: {user_data['bio'][:50]}... (truncated)
Preferences: {json.dumps(user_data['preferences'], indent=2)}
"""
    return report

# Main program
def main():
    print("=== User Activity Analytics System ===\n")
    
    # Display user profile
    print("Basic Profile Info:")
    print(f"Name: {user_profile['name']}")
    print(f"Email: {user_profile['email']}")
    print(f"Theme Preference: {user_profile['preferences']['theme']}\n")
    
    # Analyze activity
    try:
        analysis = analyze_activity(daily_steps, calories_burned)
        print("Activity Analysis:")
        for key, value in analysis.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    except ValueError as e:
        print("Error in activity analysis:", e)
    
    # Compare interests with another user
    user2_interests = {"hiking", "coding", "gaming", "travel"}
    comparison = compare_interests(interests, user2_interests)
    print("\nInterest Comparison:")
    print(f"Common Interests: {comparison['common_interests']}")
    print(f"Unique Interests: {comparison['unique_interests']}")
    
    # Generate full report
    print(generate_report(user_profile))
    
    # Demonstrate binary data handling
    print("\nBinary Data Handling:")
    print("Encoded Bio (bytes):", encoded_bio)
    print("First byte:", bio_bytes[0])  # Access individual byte
    print("Memoryview slice [0:10]:", mem_view[0:10].tobytes().decode())

if __name__ == "__main__":
    main()