from openai import OpenAI

client = OpenAI(api_key="API_KEY")

def generate_image(prompt, filename):
    response = client.images.generate(
        model = "gpt-image-1",
        prompt = prompt,
        size = "1024x1024"
    )

    image_base64 = response.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open(filename, "wb") as f:
        f.write(image_bytes)

    return filename