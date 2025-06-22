# ==============================
# 1. Intro & Instructions
# ==============================
def show_welcome():
    print('''Welcome to the "Interactive Story Generator"! 📖
You'll be asked to provide words that will fill in the blanks in a story.
Let's create something fun!''')

# ==============================
# 2. Input Collection
# ==============================
def get_user_inputs():
    print("\n=== Fill in the Blanks ===")
    
    # Using different quotation marks for variety
    inputs = {
        "character": input("Enter a character name: "),
        "adjective1": input('Describe the character (e.g., "brave", "mysterious"): '),
        "verb1": input('What does the character love to do? (e.g., "explore", "solve mysteries"): '),
        "place": input("Where does the story take place? "),
        "object": input("What magical object will appear? "),
        "adjective2": input('Describe the object (e.g., "shiny", "ancient"): '),
        "verb2": input('What happens when the object is touched? (e.g., "glows", "teleports"): ')
    }
    
    # Validate non-empty input
    for key, value in inputs.items():
        if not value.strip():
            raise ValueError(f"{key} cannot be empty!")
    
    return inputs

# ==============================
# 3. Story Templates
# ==============================
def generate_story(inputs):
    # Multiline string with dynamic formatting
    story = f'''Once upon a time, in the mystical land of "{inputs['place']}",
there lived a {inputs['adjective1']} adventurer named {inputs['character']}.
{inputs['character']} loved to {inputs['verb1']} and always carried a {inputs['adjective2']} {inputs['object']}.

One day, while exploring a hidden cave, {inputs['character']} noticed the {inputs['object']} began to {inputs['verb2']}!
A blinding light filled the room, and suddenly, the walls of the cave transformed into a portal...

Where did it lead? That's a story for another day...'''
    
    return story

# ==============================
# 4. Output Formatting
# ==============================
def format_output(story: str) -> str:
    # Add visual separators and formatting
    lines = story.split('\n')
    formatted_lines = []
    
    for line in lines:
        if line.strip():
            formatted_lines.append("  " + line)
        else:
            formatted_lines.append("")
    
    header = "\n=== Your Generated Story ===\n"
    separator = "\n" + "-"*50 + "\n"
    footer = "\nThank you for playing! 📝"
    
    return header + "\n".join(formatted_lines) + separator + footer

# ==============================
# 5. Main Program
# ==============================
def main():
    try:
        show_welcome()
        user_inputs = get_user_inputs()
        raw_story = generate_story(user_inputs)
        final_story = format_output(raw_story)
        print(final_story)
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please try again with valid inputs!")

# ==============================
# 6. Run the Program
# ==============================
if __name__ == "__main__":
    main()