import argparse
from pathlib import Path
from . import WeChatConverter

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to WeChat HTML.")
    parser.add_argument("--input", required=True, help="Input Markdown file path.")
    parser.add_argument("--output", required=True, help="Output HTML file path.")

    parser.add_argument("--content-theme", default="default", help="Content theme for styling.")
    parser.add_argument("--code-theme", default="default", help="Pygments code highlighting theme.")

    image_group = parser.add_argument_group("Image Options")
    image_group.add_argument(
        "--embed-images",
        action="store_true",
        help="Embed local images as base64 in HTML output.",
    )
    image_group.add_argument(
        "--image-format",
        choices=["webp", "jpeg", "png", "gif"],
        help="Convert images to specified format before embedding (requires --embed-images).",
    )
    image_group.add_argument(
        "--image-quality",
        type=int,
        default=85,
        metavar="1-100",
        help="Image quality for lossy formats (default: 85, requires --embed-images).",
    )
    image_group.add_argument(
        "--image-max-width",
        type=int,
        metavar="PIXELS",
        help="Resize images to max width while maintaining aspect ratio (requires --embed-images).",
    )

    args = parser.parse_args()

    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        converter = WeChatConverter(
            content_theme=args.content_theme,
            code_theme=args.code_theme,
            embed_local_images=args.embed_images,
            image_format=args.image_format,
            image_quality=args.image_quality,
            image_max_width=args.image_max_width,
        )

        input_file_path = Path(args.input)
        base_dir = input_file_path.parent.resolve()

        conversion_result = converter.convert(markdown_content, base_dir=base_dir)

        if conversion_result.success:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(conversion_result.html)

            print(f"Successfully converted '{args.input}' to '{args.output}'")

            if conversion_result.warnings:
                print("\nWarnings:")
                for warning in conversion_result.warnings:
                    print(f"  - {warning}")

            if conversion_result.errors:
                print("\nErrors:")
                for error in conversion_result.errors:
                    print(f"  - {error}")
        else:
            print(f"Conversion failed for '{args.input}'. Errors: {conversion_result.errors}")

    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
