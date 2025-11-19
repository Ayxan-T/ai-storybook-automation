from storybook.story_generator import generate_story
from storybook.image_generator import generate_image
from storybook.html_exporter import export_story_to_html

def main():
    chapters = generate_story("a young inventor who creates a flying bicycle")
    image_files = []

    for i, chapter in enumerate(chapters):
        prompt = f"Children's book illustration: {chapter}"
        image_file = f"chapter_{i+1}.png"
        generate_image(prompt, image_file)
        image_files.append(image_file)

    export_story_to_html(chapters, image_files)
    print("Storybook generated successfully!")

if __name__ == "__main__":
    main()
