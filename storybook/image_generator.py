from google import genai
import os

try:
    client = genai.Client(api_key="AIzaSyBrQos6LxYKj6utpu1y6KUUSfCEO3kOOTE")
except Exception as e:
    print(f"Error initializing client: {e}")
    client = None

def generate_image(prompt, filename = "generated_image.png"):

    if not client:
        print("Client is not initialized. Cannot generate image.")
        return None

    print(f"Generating image for prompt: '{prompt}'...")

    try:
        # Make  API Call
        response = client.models.generate_content(
            model='gemini-2.5-flash-image',
            contents=[prompt],
        )

        for part in response.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image = part.as_image()
                image.save(filename)
        
        print(f"Image successfully saved to {os.path.abspath(filename)}")
        return filename

    except Exception as e:
        print(f"An API error occurred during image generation: {e}")
        return None