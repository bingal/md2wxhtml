# md2wxhtml

[English](README.md) | 简体中文

将 Markdown 文件转换为适用于微信公众号文章格式的工具，支持普通内容和语法高亮代码块的处理。

## 功能特性

*   将 Markdown 转换为 HTML。
*   分离并处理代码块，实现语法高亮和横向滚动。
*   将处理后的内容和代码块合并到单个 HTML 文档中。
*   支持将本地图片以 base64 data URI 形式嵌入，生成完全独立的 HTML。
*   支持图片格式转换（WebP、JPEG、PNG）和压缩，有效减小文件体积。

## 免责声明

本项目是一个独立的开源工具，与微信或腾讯没有任何关联、背书或官方联系。

## 安装

```bash
pip install md2wxhtml
```

## 使用方法

### 命令行界面

```bash
md2wxhtml --input <input_file.md> --output <output_file.html>
```

**图片嵌入选项：**

```bash
# 将本地图片以 base64 形式嵌入（保持原始格式）
md2wxhtml --input input.md --output output.html --embed-images

# 嵌入图片并转换为 WebP 格式，质量为 80%
md2wxhtml --input input.md --output output.html --embed-images --image-format webp --image-quality 80

# 调整图片最大宽度为 800px，保持宽高比
md2wxhtml --input input.md --output output.html --embed-images --image-max-width 800
```

### 作为 Python 库使用

```python
from md2wxhtml import WeChatConverter

converter = WeChatConverter(content_theme="blue", code_theme="monokai")
conversion_result = converter.convert("你的 Markdown 内容。")
html_output = conversion_result.html
print(html_output)
```

**图片嵌入：**

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
    print(f"转换成功")
    if result.warnings:
        print(f"警告: {result.warnings}")
else:
    print(f"转换失败: {result.errors}")
```

**参数说明：**

- `embed_local_images` (bool, 默认: `False`) - 将本地图片以 base64 data URI 形式嵌入
- `image_format` (str, 可选) - 将图片转换为指定格式: `webp`、`jpeg`、`png`、`gif`
- `image_quality` (int, 默认: `85`) - 有损格式的质量 (1-100)
- `image_max_width` (int, 可选) - 调整图片最大宽度，保持宽高比
- `base_dir` (Path, 可选) - 用于解析相对图片路径的基础目录。使用 CLI 时，自动设置为 markdown 文件所在目录。作为库使用时，应提供此参数以正确解析相对路径。

**注意**：工具会自动处理 URL 编码的图片路径（例如文件名中的中文字符），在处理前进行解码。

## 可用主题

`content_theme` 参数支持以下内置主题名称：

- `default`
- `blue`
- `dark`
- `github`
- `green`
- `hammer`
- `red`

`code_theme` 参数使用 [Pygments](https://pygments.org/docs/styles/) 样式进行代码高亮。你可以指定任何有效的 Pygments 样式名称（如 `monokai`、`default`、`friendly`、`colorful` 等）来调整代码块的外观。

创建 `WeChatConverter` 实例时可以指定这些名称。例如：

```python
converter = WeChatConverter(content_theme="github", code_theme="monokai")
```

## 图片压缩建议

直接嵌入图片会导致 HTML 文件变大，推荐使用以下优化方案：

### 1. 格式转换（推荐 WebP）
WebP 格式比同等质量的 JPEG 小 25-35%，比同等质量的 PNG 小 80-90%。

### 2. 质量调整
- 默认质量 85 是一个很好的平衡点
- 对于不需要高保真的图片，可以降到 70-80
- 对于截图/图表，可以用 70-75

### 3. 尺寸调整
微信公众号文章中的图片通常不需要超过 800px，减小尺寸能显著减小文件大小。

### 实际效果对比
以一个 1024x768 的图片为例：
- 原始 PNG：~500KB
- 嵌入为 PNG base64：~670KB（base64 增加 ~33%）
- 转换为 WebP (质量 80)：~50KB
- 转换为 WebP + 限制宽度 800px：~30KB

**节省空间：95%+**

## 最佳实践

```bash
# 最优配置：WebP 格式 + 80% 质量 + 限制宽度 800px
md2wxhtml --input doc.md --output output.html \
  --embed-images \
  --image-format webp \
  --image-quality 80 \
  --image-max-width 800
```

```python
# Python 库最优配置
converter = WeChatConverter(
    embed_local_images=True,
    image_format="webp",
    image_quality=80,
    image_max_width=800
)
```
