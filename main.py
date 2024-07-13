from textblob import TextBlob

def generate_color_and_shape():
    user_text = input("Describe your mood and characteristics: ").lower()

    # Analyze sentiment using TextBlob
    blob = TextBlob(user_text)
    sentiment = blob.sentiment.polarity  # Get sentiment polarity (-1 to 1)

    # Determine color based on sentiment polarity
    if sentiment > 0.75:
        color = 'yellow'
    elif sentiment > 0.5:
        color = 'orange'
    elif sentiment > 0.25:
        color = 'light green'
    elif sentiment > 0:
        color = 'green'
    elif sentiment > -0.25:
        color = 'light blue'
    elif sentiment > -0.5:
        color = 'blue'
    elif sentiment > -0.75:
        color = 'purple'
    else:
        color = 'dark blue'

    # List of possible shapes
    shapes = {
        'energetic': 'triangle',
        'gentle': 'circle',
        'strong': 'square',
        'soft': 'ellipse',
        'creative': 'star',
        'confident': 'hexagon',
        'balanced': 'octagon',
        'playful': 'pentagon',
        'focused': 'diamond',
        'calm': 'oval'
    }

    # Determine shape based on characteristics in the text
    shape = 'rectangle'  # Default shape if no specific characteristics match
    for char, shape_value in shapes.items():
        if char in user_text:
            shape = shape_value
            break  # Exit loop on first match

    # Print the generated color and shape
    print(f"Based on your description,")
    print(f"Your generated color is: {color}")
    print(f"Your generated shape is: {shape}")

# Calling the function to generate color and shape based on user input
generate_color_and_shape()
