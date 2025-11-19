from google import genai
import os

try:
    client = genai.Client(api_key="GEMINI_API_KEY")
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
        response = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt=prompt,
            config=dict(
                number_of_images=1,
                # Specify the desired aspect ratio (equivalent to 'size' in the original code)
                aspect_ratio="1:1" 
            )
        )

        if not response.generated_images:
            print("Image generation failed. No images were returned by the API.")
            return None

        # Extract the Image Data
        image_bytes = response.generated_images[0].image.image_bytes
        
        if not image_bytes:
             print("Image bytes could not be extracted from the response.")
             return None

        # 4. Save the image bytes to a file
        with open(filename, "wb") as f:
            f.write(image_bytes)
        
        print(f"Image successfully saved to {os.path.abspath(filename)}")
        return filename

    except Exception as e:
        print(f"An API error occurred during image generation: {e}")
        return None