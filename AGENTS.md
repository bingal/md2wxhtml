# AGENTS.md - Agent Guidelines for md2wxhtml

## Project Overview

md2wxhtml is a Python tool (3.12.10+) that converts Markdown to WeChat-compatible HTML with syntax-highlighted code blocks. It separates content and code processing, applies themes, and inlines CSS for WeChat editor compatibility. Supports optional local image embedding with base64 encoding and format conversion.

## Build/Test Commands

**Manual testing:**
```bash
python test_run.py
```

**Library usage (from test_run.py pattern):**
```python
from md2wxhtml.core.converter import WeChatConverter

converter = WeChatConverter(
    content_theme="blue",
    code_theme="monokai",
    embed_local_images=True,
    image_format="webp",
    image_quality=80,
    image_max_width=800
)
result = converter.convert(markdown_content)
# result: ConversionResult with .html, .code_blocks, .success, .errors, .warnings
```

**CLI:**
```bash
# Basic usage
md2wxhtml --input input.md --output output.html

# With image embedding
md2wxhtml --input input.md --output output.html --embed-images --image-format webp
```

**No automated test framework** - use test_run.py as reference for integration testing patterns.

## Code Style Guidelines

### Imports
- Group imports: standard library → third-party → local
- Use absolute imports for local modules
- Use relative imports within the same package (e.g., `from ..models.code_block import CodeBlock`)

### Type Hints
**Required** for all function parameters and return values. Use `typing` module:
```python
from typing import Optional, Dict, Any, List, Tuple
def extract_code_blocks(markdown: str) -> Tuple[str, List[CodeBlock], dict]:
```

### Data Structures
**Use `@dataclass`** for data containers:
```python
from dataclasses import dataclass, field

@dataclass
class ConversionResult:
    html: str
    code_blocks: Dict[str, str] = field(default_factory=dict)
    success: bool = True
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
```

Note: `warnings` collects image-related warnings (e.g., large embedded files >500KB).

### WeChatConverter Parameters
```python
WeChatConverter(
    content_theme: str = "default",
    code_theme: str = "default",
    embed_local_images: bool = False,
    image_format: Optional[str] = None,
    image_quality: int = 85,
    image_max_width: Optional[int] = None,
)
```

- `content_theme`: Article theme (default, blue, dark, github, green, hammer, red)
- `code_theme`: Pygments style for code highlighting (any valid Pygments style name)
- `embed_local_images`: Embed local images as base64 data URIs
- `image_format`: Convert images to format (webp, jpeg, png, gif)
- `image_quality`: Quality for lossy formats (1-100, default 85)
- `image_max_width`: Resize images to max width while maintaining aspect ratio

### convert() Method
```python
converter.convert(markdown: str, base_dir: Optional[Path] = None) -> ConversionResult
```

- `markdown`: The markdown content to convert
- `base_dir`: Base directory for resolving relative image paths. When using CLI, this is automatically set to the markdown file's directory. When using as a library, provide this parameter to correctly resolve relative image paths.

### Functions & Classes
- Private functions use underscore prefix: `_auto_link_urls()`, `_build_pre_code_style()`
- Classes use PascalCase: `WeChatConverter`, `PlaceholderManager`, `CodeBlock`
- Functions use snake_case: `process_content()`, `extract_code_blocks()`

### Error Handling
- Use `try/except` with specific exceptions
- Return `ConversionResult` objects with `.success`, `.errors`, `.warnings` instead of raising for conversion issues
- Example: `main.py` catches `FileNotFoundError` and generic `Exception`

### Docstrings
Use triple-quoted docstrings:
```python
def process_content(clean_markdown: str, theme: str = "default") -> str:
    """
    Convert clean markdown to WeChat-styled HTML.
    Applies the selected article theme and injects its CSS as inline styles.
    """
```

### Formatting
- **No semicolons**
- 4-space indentation
- Max line length: ~100 chars (observed, not enforced)
- String formatting: f-strings preferred

### Theme Development
Theme files in `processors/themes/` follow pattern:
```python
def get_css() -> str:
    """Get the [theme name] theme CSS."""
    return """
        .wechat-content { ... }
        .wechat-content h1 { ... }
        .wechat-content p.list-highlight span.list-highlight-span { ... }
    """
```
Themes support optional `postprocess_html(html: str) -> str` method.

### WeChat-Specific Constraints
- **All CSS must be inlined** (use `premailer.transform()`)
- Use `overflow-x: auto` for horizontal scrolling code blocks
- Replace spaces with `&nbsp;` and `\n` with `<br />` in code blocks
- Remove `<style>` tags in final output
- Font stack: `-apple-system-font, BlinkMacSystemFont, 'Helvetica Neue', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei UI', 'Microsoft YaHei', Arial, sans-serif`
- Code font: `Menlo, 'Operator Mono', Consolas, Monaco, monospace`

### Code Block Processing
- Extract code blocks before markdown conversion (use placeholders)
- Process with Pygments (`HtmlFormatter(style=theme, noclasses=True, nowrap=True)`)
- Wrap in `<pre><code>` with inline styles
- Remove wrapper tags: `<div class="highlight"><pre>...</pre></div>`
- Strip outer tags to get inner content only

### Module Organization
```
md2wxhtml/
├── core/          # Orchestration (converter, markdown_parser, merger)
├── models/        # Dataclasses (CodeBlock, ConversionResult, ProcessingContext)
├── processors/    # Content, code, and image processing, themes
└── utils/         # Utilities (placeholder_manager)
```

## Key Dependencies
- `markdown` - Markdown to HTML with extensions: tables, fenced_code, codehilite, toc
- `pygments` - Code highlighting, any valid Pygments style for `code_theme`
- `beautifulsoup4` - HTML manipulation
- `premailer` - CSS inlining
- `pillow` - Image processing for embedding and format conversion

## Common Patterns

**Theme map lookup:**
```python
from ..processors.themes import blue, dark, default, github, green, hammer, red
theme_map = {"default": default, "blue": blue, ...}
theme_mod = theme_map.get(theme, default)
css = theme_mod.get_css()
```

**BS4 processing:**
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
# Process...
return str(soup)
```

**Regex patterns:**
```python
import re
pattern = re.compile(r'...', re.MULTILINE | re.IGNORECASE)
clean_text = pattern.sub(replacer_function, input_text)
```

**Image processing:**
```python
from md2wxhtml.processors.image_processor import process_images

# Process images in HTML
html, warnings, errors = process_images(
    html,
    embed_images=True,
    image_format="webp",
    image_quality=80,
    max_width=800
)
```

## Image Processing Guidelines

### Image Embedding Flow
1. Parse HTML with BeautifulSoup to find `<img>` tags
2. Filter for local images (skip http/https URLs)
3. URL-decode image paths to handle Chinese characters and special characters
4. Resolve relative paths from base_dir (markdown file's directory or provided base_dir)
5. Load and process images with Pillow:
    - Convert RGBA to RGB for JPEG format
    - Resize if `max_width` is specified
    - Convert to target format if specified
    - Apply quality settings
6. Encode as base64 and construct data URI
7. Replace image `src` attribute with data URI
8. Collect warnings/errors (large files, missing images)

### Image Path Handling
- Relative paths are resolved from markdown file's directory when using CLI
- When using library API, pass `base_dir` parameter to `convert()` method to specify base directory
- If `base_dir` is not provided, relative paths are resolved from `Path.cwd()`
- Absolute paths are used as-is
- Image paths are URL-decoded to handle Chinese characters and special characters in filenames

### Format Conversion Notes
- WebP: Best compression, supports transparency
- JPEG: No transparency support, good for photos
- PNG: Lossless, best for graphics with transparency
- GIF: Animated support, limited color palette

### Best Practices
- Use WebP format for optimal compression (25-35% smaller than JPEG)
- Set quality to 80-85 for good balance
- Limit width to 800px for WeChat articles
- Warn on files >500KB to alert user about large images
- Always wrap image processing in try/except for robustness
