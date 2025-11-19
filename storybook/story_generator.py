from openai import OpenAI

client = OpenAI(api_key="API_KEY")

def generate_story(topic="adventures of a small robot"):
    prompt = f"Write a 5-chapter children's story about {topic}. Each chapter should be 100 words."

    response = response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are a children's storyteller."},
            {"role": "user", "content": prompt},
        ]
    )

    story_text = response.choices[0].message.content
    chapters = story_text.split("\n\n")
    return chapters
