from typing import Optional
from pathlib import Path
from .markdown_parser import extract_code_blocks
from ..processors.content_processor import process_content
from ..processors.code_processor import process_code_block
from ..processors.image_processor import process_images
from ..models.code_block import ConversionResult


# Main orchestrator for the conversion process
class WeChatConverter:
    def __init__(
        self,
        content_theme: str = "default",
        code_theme: str = "default",
        embed_local_images: bool = False,
        image_format: Optional[str] = None,
        image_quality: int = 85,
        image_max_width: Optional[int] = None,
    ):
        self.content_theme = content_theme
        self.code_theme = code_theme
        self.embed_local_images = embed_local_images
        self.image_format = image_format
        self.image_quality = image_quality
        self.image_max_width = image_max_width

    def convert(self, markdown: str, base_dir: Optional[Path] = None) -> ConversionResult:
        # 1. Extract code blocks
        clean_md, code_blocks, placeholder_map = extract_code_blocks(markdown)
        # 2. Process general content
        html_with_placeholders = process_content(clean_md, theme=self.content_theme)
        # 3. Process code blocks
        code_html_map = {}
        for cb in code_blocks:
            code_html_map[cb.placeholder] = process_code_block(cb, theme=self.code_theme)
        # 4. Merge components
        for placeholder, code_html in code_html_map.items():
            html_with_placeholders = html_with_placeholders.replace(placeholder, code_html)
        all_warnings = []
        all_errors = []
        if self.embed_local_images:
            html_with_placeholders, img_warnings, img_errors = process_images(
                html_with_placeholders,
                embed_images=True,
                image_format=self.image_format,
                image_quality=self.image_quality,
                max_width=self.image_max_width,
                base_dir=base_dir,
            )
            all_warnings.extend(img_warnings)
            all_errors.extend(img_errors)
        return ConversionResult(
            html=html_with_placeholders,
            code_blocks=code_html_map,
            success=len(all_errors) == 0,
            errors=all_errors,
            warnings=all_warnings,
        )
