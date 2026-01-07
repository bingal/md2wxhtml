# md2wxhtml

English | [简体中文](README_CN.md)

A tool to convert Markdown files into a format suitable for WeChat articles, handling general content and code blocks with syntax highlighting.

## Features

*   Converts Markdown to HTML.
*   Separates and processes code blocks for syntax highlighting and horizontal scrolling.
*   Merges processed content and code blocks into a single HTML document.
*   Optional local image embedding as base64 data URIs for self-contained HTML.
*   Support for image format conversion (WebP, JPEG, PNG) and compression to reduce file size.

## Disclaimer

This project is an independent open-source tool and is not affiliated with, endorsed by, or officially connected to WeChat or Tencent.

## Installation

```bash
pip install md2wxhtml
```

## Usage

### Command-line Interface

```bash
md2wxhtml --input <input_file.md> --output <output_file.html>
```

**Image Embedding Options:**

```bash
# Embed local images as base64 (keeps original format)
md2wxhtml --input input.md --output output.html --embed-images

# Embed images and convert to WebP format with 80% quality
md2wxhtml --input input.md --output output.html --embed-images --image-format webp --image-quality 80

# Resize images to max width of 800px while maintaining aspect ratio
md2wxhtml --input input.md --output output.html --embed-images --image-max-width 800
```

### As a Python Library

```python
from md2wxhtml import WeChatConverter

converter = WeChatConverter(content_theme="blue", code_theme="monokai")
conversion_result = converter.convert("Your markdown content here.")
html_output = conversion_result.html
print(html_output)
```

**Image Embedding:**

```python
converter = WeChatConverter(
    content_theme="blue",
    code_theme="monokai",
    embed_local_images=True,
    image_format="webp",
    image_quality=80,
    image_max_width=800
)

result = converter.convert(markdown_content)

if result.success:
    print(f"Conversion successful")
    if result.warnings:
        print(f"Warnings: {result.warnings}")
else:
    print(f"Conversion failed: {result.errors}")
```

**Parameters:**

- `embed_local_images` (bool, default: `False`) - Embed local images as base64 data URIs
- `image_format` (str, optional) - Convert images to specified format: `webp`, `jpeg`, `png`, `gif`
- `image_quality` (int, default: `85`) - Quality for lossy formats (1-100)
- `image_max_width` (int, optional) - Resize images to max width while maintaining aspect ratio
- `base_dir` (Path, optional) - Base directory for resolving relative image paths. When using CLI, this is automatically set to the markdown file's directory. When using as a library, you should provide this to resolve relative paths correctly.

**Note**: The tool automatically handles URL-encoded image paths (e.g., Chinese characters in filenames) by decoding them before processing.

## Available Themes

The `content_theme` argument accepts the following built-in theme names:

- `default`
- `blue`
- `dark`
- `github`
- `green`
- `hammer`
- `red`

The `code_theme` argument uses [Pygments](https://pygments.org/docs/styles/) styles for code highlighting. You can specify any valid Pygments style name (e.g., `monokai`, `default`, `friendly`, `colorful`, etc.) to adjust the appearance of code blocks.

You can specify these names when creating a `WeChatConverter` instance. For example:

```python
converter = WeChatConverter(content_theme="github", code_theme="monokai")
```
