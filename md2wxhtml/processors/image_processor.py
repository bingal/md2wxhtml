"""
Image processor for embedding local images as base64 in HTML.
Supports optional image compression and format conversion.
"""

import base64
import os
from pathlib import Path
from typing import Optional, Tuple, List
from urllib.parse import unquote

from bs4 import BeautifulSoup
from PIL import Image


def process_images(
    html: str,
    embed_images: bool = False,
    image_format: Optional[str] = None,
    image_quality: int = 85,
    max_width: Optional[int] = None,
    base_dir: Optional[Path] = None,
) -> Tuple[str, List[str], List[str]]:
    """
    Process images in HTML, embedding local images as base64 data URIs.

    Args:
        html: The HTML content to process
        embed_images: Whether to embed local images as base64
        image_format: Optional format to convert images to (e.g., 'webp', 'jpeg', 'png')
        image_quality: Quality for lossy formats (1-100, default 85)
        max_width: Optional max width to resize images to (in pixels)
        base_dir: Base directory for resolving relative image paths. If None, uses cwd.

    Returns:
        Tuple of (processed_html, warnings, errors)
    """
    if not embed_images:
        return html, [], []

    soup = BeautifulSoup(html, "html.parser")
    warnings = []
    errors = []

    for img in soup.find_all("img"):
        src = img.get("src")

        if src is None:
            continue

        src_str = str(src)

        if not src_str or src_str.startswith("data:"):
            continue

        if src_str.startswith("http://") or src_str.startswith("https://"):
            continue

        # URL decode to handle Chinese characters and special characters in filenames
        src_str = unquote(src_str)

        try:
            image_path = Path(src_str)
            if not image_path.is_absolute():
                if base_dir is not None:
                    image_path = base_dir / src_str
                else:
                    image_path = Path.cwd() / src_str

            if not image_path.exists():
                errors.append(f"Image not found: {image_path}")
                continue

            data_uri = _image_to_data_uri(
                image_path, format=image_format, quality=image_quality, max_width=max_width
            )
            img["src"] = data_uri

            size_kb = len(base64.b64decode(data_uri.split(",")[1])) / 1024
            if size_kb > 500:
                warnings.append(
                    f"Embedded image {image_path.name} is large ({size_kb:.1f} KB). "
                    "Consider using a smaller image or external hosting."
                )

        except FileNotFoundError:
            errors.append(f"Image file not found: {src_str}")
        except PermissionError:
            errors.append(f"Permission denied reading image: {src_str}")
        except Exception as e:
            errors.append(f"Error processing image {src_str}: {str(e)}")

    return str(soup), warnings, errors


def _image_to_data_uri(
    image_path: Path,
    format: Optional[str] = None,
    quality: int = 85,
    max_width: Optional[int] = None,
) -> str:
    """
    Convert an image file to a base64 data URI with optional compression.

    Args:
        image_path: Path to the image file
        format: Optional format to convert to (e.g., 'webp', 'jpeg')
        quality: Quality for lossy formats (1-100)
        max_width: Optional max width to resize to

    Returns:
        Data URI string (e.g., "data:image/jpeg;base64,...")
    """
    with Image.open(image_path) as img:
        # Convert RGBA to RGB if target format doesn't support transparency
        if format in ["jpeg", "jpg"] and img.mode == "RGBA":
            # Create white background
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
            img = background
        elif format and format.lower() in ["jpeg", "jpg"]:
            img = img.convert("RGB")

        # Resize if max_width is specified
        if max_width and img.width > max_width:
            # Calculate new height maintaining aspect ratio
            new_height = int(img.height * (max_width / img.width))
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # Determine output format
        output_format = format.upper() if format else img.format
        if output_format == "JPG":
            output_format = "JPEG"
        if not output_format:
            output_format = "PNG"

        # Save to bytes buffer
        from io import BytesIO

        buffer = BytesIO()

        # Handle compression parameters
        save_kwargs = {"format": output_format}

        # Add quality parameter for formats that support it
        if output_format in ["JPEG", "WEBP"]:
            save_kwargs["quality"] = quality

        # Handle PNG optimization
        if output_format == "PNG":
            save_kwargs["optimize"] = True

        img.save(buffer, **save_kwargs)

        # Encode to base64
        image_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

        # Determine MIME type
        mime_type = _format_to_mime_type(output_format)

        return f"data:{mime_type};base64,{image_data}"


def _format_to_mime_type(format: str) -> str:
    """
    Convert image format to MIME type.

    Args:
        format: Image format (e.g., "JPEG", "PNG", "WEBP")

    Returns:
        MIME type string (e.g., "image/jpeg")
    """
    format_map = {
        "JPEG": "image/jpeg",
        "JPG": "image/jpeg",
        "PNG": "image/png",
        "WEBP": "image/webp",
        "GIF": "image/gif",
        "BMP": "image/bmp",
        "SVG": "image/svg+xml",
        "ICO": "image/x-icon",
    }
    return format_map.get(format.upper(), "image/png")
