def get_css() -> str:
    """Get the GreenSimple theme CSS."""
    return """
.wechat-content {
  max-width: 720px;
  margin: 0 auto;
  padding: 8px;
  font-family:
    PingFang SC,
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    'Helvetica Neue',
    'Hiragino Sans GB',
    'Microsoft YaHei UI',
    'Microsoft YaHei',
    Arial,
    sans-serif;
  font-size: 16px;
  line-height: 1.75;
  word-wrap: break-word;
  color: #2c2c2c;
}

.wechat-content h1,
.wechat-content h2,
.wechat-content h3,
.wechat-content h4,
.wechat-content h5,
.wechat-content h6 {
  color: #2bae85;
  font-weight: 700;
  line-height: 1.4em;
  word-break: break-all;
  letter-spacing: -0.02em;
  font-family:
    PingFang SC,
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    'Helvetica Neue',
    'Hiragino Sans GB',
    'Microsoft YaHei UI',
    'Microsoft YaHei',
    Arial,
    sans-serif;
}

.wechat-content h1 {
  font-size: 32px;
  margin-top: 0;
  margin-bottom: 24px;
}

.wechat-content h2 {
  font-size: 24px;
  margin-top: 36px;
  margin-bottom: 24px;
}

.wechat-content > h1:first-child,
.wechat-content > h2:first-child,
.wechat-content > h3:first-child,
.wechat-content > h4:first-child,
.wechat-content > h5:first-child,
.wechat-content > h6:first-child {
  margin-top: 0;
}

.wechat-content h3 {
  font-size: 20px;
  margin-top: 28px;
  margin-bottom: 20px;
  letter-spacing: -0.01em;
}

.wechat-content h4,
.wechat-content h5,
.wechat-content h6 {
  font-size: 18px;
  margin-top: 24px;
  margin-bottom: 16px;
  letter-spacing: -0.01em;
  color: #25936c;
}

.wechat-content p {
  margin: 5px 0 20px;
  line-height: 1.75em;
  text-align: start;
  font-size: 16px;
  font-weight: 400;
  color: #2c2c2c;
  word-break: break-all;
}

.wechat-content p:last-child {
  margin-bottom: 0;
}

.wechat-content strong,
.wechat-content b {
  font-weight: 700;
  color: #2bae85;
}

.wechat-content em,
.wechat-content i {
  font-style: italic;
}

.wechat-content del,
.wechat-content s,
.wechat-content strike {
  text-decoration: line-through;
  color: #999;
}

.wechat-content mark {
  background: #fff3cd;
  padding: 2px 4px;
  border-radius: 2px;
}

.wechat-content small {
  font-size: 0.875em;
  color: #666;
}

.wechat-content sup {
  vertical-align: super;
  font-size: 0.75em;
}

.wechat-content sub {
  vertical-align: sub;
  font-size: 0.75em;
}

.wechat-content ins {
  text-decoration: underline;
  background: #d4edda;
  padding: 2px 4px;
}

.wechat-content q {
  quotes: '「' '」' '『' '』';
  font-style: italic;
  color: #666;
}

.wechat-content var {
  font-family: 'SF Mono', Consolas, Monaco, 'Courier New', monospace;
  background: rgba(0, 0, 0, 0.05);
  padding: 2px 4px;
  border-radius: 2px;
  font-size: 0.9em;
}

.wechat-content samp,
.wechat-content tt {
  font-family: 'SF Mono', Consolas, Monaco, 'Courier New', monospace;
  background: rgba(0, 0, 0, 0.05);
  padding: 2px 4px;
  border-radius: 2px;
  font-size: 0.9em;
}

.wechat-content abbr[title] {
  text-decoration: underline dotted;
  cursor: help;
}

.wechat-content a {
  color: #2bae85;
  text-decoration: none;
  border-bottom: 1px solid #2bae85;
  transition: border-bottom-color 0.2s ease;
}

.wechat-content a:hover {
  border-bottom-color: #23956b;
}

.wechat-content ruby,
.wechat-content rt,
.wechat-content rp {
  line-height: 1.4;
}

.wechat-content ul,
.wechat-content ol {
  margin: 8px 0;
  padding-left: 20px;
  list-style-type: disc;
  color: #2bae85;
}

.wechat-content ol {
  list-style-type: decimal;
}

.wechat-content li {
  margin: 0;
  line-height: 1.6;
  padding-left: 0;
  font-family:
    PingFang SC,
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    'Helvetica Neue',
    'Hiragino Sans GB',
    'Microsoft YaHei UI',
    'Microsoft YaHei',
    Arial,
    sans-serif;
}

.wechat-content li > p {
  margin: 6px 0;
}

.wechat-content li > ul,
.wechat-content li > ol {
  margin: 4px 0;
}

.wechat-content ul ul,
.wechat-content ul ul ul {
  color: #25936c;
}

.wechat-content ul.contains-task-list {
  list-style-type: none;
  padding-left: 0;
}

.wechat-content li.task-list-item {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  margin: 6px 0;
}

.wechat-content input[type='checkbox'] {
  margin-top: 4px;
  cursor: pointer;
}

.wechat-content blockquote {
  margin: 20px 0;
  padding: 16px 20px;
  border-left: 4px solid #2bae85;
  background: rgba(43, 174, 133, 0.05);
  border-radius: 0 4px 4px 0;
}

.wechat-content blockquote p {
  margin: 8px 0;
  color: #666;
}

.wechat-content blockquote p:last-child {
  margin-bottom: 0;
}

.wechat-content blockquote blockquote {
  margin-top: 12px;
  border-left-color: #25936c;
  background: rgba(37, 147, 108, 0.05);
}

.wechat-content code {
  font-family: 'SF Mono', Consolas, Monaco, 'Courier New', monospace;
  font-size: 14px;
  padding: 2px 4px;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: 2px;
  color: #2c2c2c;
}

.wechat-content pre {
  margin: 20px 0;
  padding: 0;
  background: #f6faf8;
  border: 1px solid #d4e5de;
  border-left: 3px solid #2bae85;
  border-radius: 4px;
  overflow: hidden;
}

.wechat-content pre code {
  display: block;
  padding: 16px 20px;
  background: transparent;
  color: #2c2c2c;
  font-family: 'SF Mono', Consolas, Monaco, 'Courier New', monospace;
  font-size: 14px;
  line-height: 1.6;
  border: none;
  border-radius: 0;
  overflow-x: auto;
}

.wechat-content table {
  width: 100%;
  margin: 16px 0;
  border-collapse: collapse;
  font-size: 15px;
}

.wechat-content thead {
  background: #f8f9fa;
  border-bottom: 2px solid #2bae85;
}

.wechat-content tfoot {
  background: #f8f9fa;
  border-top: 2px solid #2bae85;
}

.wechat-content th {
  padding: 12px;
  text-align: left;
  font-weight: 700;
  color: #2c2c2c;
  border-bottom: 1px solid #e0e0e0;
}

.wechat-content td {
  padding: 12px;
  border-bottom: 1px solid #e0e0e0;
  color: #2c2c2c;
}

.wechat-content tbody tr:nth-child(even) {
  background: #f8f9fa;
}

.wechat-content tbody tr:hover {
  background: rgba(43, 174, 133, 0.05);
}

.wechat-content .frontmatter-table {
  margin: 16px 0;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
}

.wechat-content .frontmatter-table td {
  padding: 10px 16px;
  border: none;
  border-bottom: 1px solid #e0e0e0;
}

.wechat-content .frontmatter-table tr:last-child td {
  border-bottom: none;
}

.wechat-content .frontmatter-key {
  font-weight: 700;
  color: #2bae85;
  background: rgba(43, 174, 133, 0.05);
  width: 140px;
}

.wechat-content .frontmatter-value {
  color: #2c2c2c;
}

.wechat-content hr {
  border: none;
  height: 2px;
  background: linear-gradient(to right, transparent, #2bae85, transparent);
  margin: 32px 0;
}

.wechat-content img {
  max-width: 100%;
  height: auto;
  display: block;
  border-radius: 4px;
  margin: 20px 0;
}

.wechat-content picture {
  display: block;
  max-width: 100%;
}

.wechat-content picture img {
  display: block;
  width: 100%;
  height: auto;
}

.wechat-content figure {
  margin: 20px 0;
}

.wechat-content figure img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 4px;
}

.wechat-content figcaption {
  text-align: center;
  margin-top: 8px;
  font-size: 14px;
  color: #666;
  font-style: italic;
}

.wechat-content .footnotes {
  margin-top: 32px;
  padding-top: 16px;
  border-top: 1px solid #e0e0e0;
}

.wechat-content .footnotes ol {
  list-style: decimal;
  padding-left: 24px;
  color: #2c2c2c;
}

.wechat-content .footnote-ref {
  color: #2bae85;
  text-decoration: none;
  border-bottom: 1px dotted #2bae85;
  cursor: pointer;
}

.wechat-content .footnote-backref,
.wechat-content .data-footnote-backref {
  color: #2bae85;
  text-decoration: none;
  font-size: 0.875em;
}

.wechat-content dl {
  margin: 16px 0;
}

.wechat-content dt {
  font-weight: 700;
  color: #2bae85;
  margin: 8px 0 4px;
}

.wechat-content dd {
  margin: 4px 0 16px 20px;
  color: #2c2c2c;
  line-height: 1.6;
}

.wechat-content kbd {
  display: inline-block;
  padding: 2px 6px;
  font-family: 'SF Mono', Consolas, Monaco, 'Courier New', monospace;
  font-size: 12px;
  line-height: 1.4;
  color: #2c2c2c;
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 3px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.wechat-content .markdown-alert {
  margin: 16px 0;
  padding: 16px;
  border-left: 4px solid;
  border-radius: 4px;
  background: #f8f9fa;
}

.wechat-content .markdown-alert-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  margin-bottom: 8px;
  font-size: 16px;
}

.wechat-content .markdown-alert p {
  margin: 8px 0;
  font-size: 14px;
}

.wechat-content .markdown-alert-note {
  border-left-color: #2bae85;
  background: rgba(43, 174, 133, 0.05);
}

.wechat-content .markdown-alert-note .markdown-alert-title {
  color: #2bae85;
}

.wechat-content .markdown-alert-tip {
  border-left-color: #35cd4b;
  background: rgba(53, 205, 75, 0.05);
}

.wechat-content .markdown-alert-tip .markdown-alert-title {
  color: #35cd4b;
}

.wechat-content .markdown-alert-important {
  border-left-color: #fdbc40;
  background: rgba(253, 188, 64, 0.05);
}

.wechat-content .markdown-alert-important .markdown-alert-title {
  color: #fdbc40;
}

.wechat-content .markdown-alert-warning {
  border-left-color: #fc625d;
  background: rgba(252, 98, 93, 0.05);
}

.wechat-content .markdown-alert-warning .markdown-alert-title {
  color: #fc625d;
}

.wechat-content .markdown-alert-caution {
  border-left-color: #e57373;
  background: rgba(229, 115, 115, 0.05);
}

.wechat-content .markdown-alert-caution .markdown-alert-title {
  color: #e57373;
}

.wechat-content .math-inline {
  font-family: 'SF Mono', Consolas, Monaco, 'Courier New', monospace;
  background: rgba(0, 0, 0, 0.03);
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 0.9em;
}

.wechat-content .math-display {
  display: block;
  margin: 16px 0;
  padding: 16px;
  background: #f8f9fa;
  border-radius: 4px;
  overflow-x: auto;
  font-size: 1em;
}

.wechat-content details {
  margin: 16px 0;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  background: #f8f9fa;
}

.wechat-content summary {
  padding: 12px 16px;
  cursor: pointer;
  font-weight: 700;
  color: #2bae85;
  user-select: none;
  transition: background 0.2s ease;
}

.wechat-content summary:hover {
  background: rgba(43, 174, 133, 0.05);
}

.wechat-content details[open] summary {
  border-bottom: 1px solid #e0e0e0;
}

.wechat-content details > div {
  padding: 16px;
}

.wechat-content iframe,
.wechat-content video {
  max-width: 100%;
  border-radius: 4px;
  margin: 16px 0;
}

.wechat-content .meta {
  font-size: 12px;
  color: #999;
  margin: 8px 0;
  text-align: center;
}

.wechat-content time {
  color: #999;
  font-size: 12px;
}

.wechat-content.indent-first-line p {
  text-indent: 2em;
}

.wechat-content.indent-first-line p:first-of-type {
  text-indent: 0;
}
"""
