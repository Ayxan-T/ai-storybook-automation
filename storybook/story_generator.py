from google import genai

try:
    client = genai.Client(api_key="GEMINI_API_KEY")
except Exception as e:
    print(f"Error initializing client: {e}")
    client = None

def generate_story_gemini(topic = "adventures of a small robot"):
    if not client:
        print("Client is not initialized. Cannot generate story.")
        return []

    # Construct the Prompt (System instruction included)
    prompt = (
        f"You are a professional children's storyteller. Write a 3-chapter story "
        f"about {topic}. Each chapter should be around 100 words. "
        f"Use ONLY a double newline ('\\n\\n') to strictly separate the chapters."
    )

    # Make API Call and parse response
    try:
        print(f"Generating story for topic: '{topic}'...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        story_text = response.text

        chapters = [c.strip() for c in story_text.split("\n\n") if c.strip()]
        
        return chapters

    except Exception as e:
        print(f"An API error occurred during generation: {e}")
        return []
    

