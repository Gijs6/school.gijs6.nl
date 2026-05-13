import html
import re
from markdown import Markdown
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension

MATH_DISPLAY_PATTERN = re.compile(r"\$\$([^\$]+)\$\$")
MATH_INLINE_PATTERN = re.compile(r"\$([^\$\n]+)\$")


class MathProtectPreprocessor(Preprocessor):
    def __init__(self, md):
        super().__init__(md)
        self.math_store = {}
        self.counter = 0

    def reset(self):
        self.math_store.clear()
        self.counter = 0

    def run(self, lines):
        text = "\n".join(lines)

        def replace_display(match):
            key = f"MATH_DISPLAY_{self.counter}"
            self.counter += 1
            self.math_store[key] = match.group(0)
            return key

        def replace_inline(match):
            key = f"MATH_INLINE_{self.counter}"
            self.counter += 1
            self.math_store[key] = match.group(0)
            return key

        text = MATH_DISPLAY_PATTERN.sub(replace_display, text)
        text = MATH_INLINE_PATTERN.sub(replace_inline, text)
        return text.split("\n")


class MathProtectPostprocessor(Postprocessor):
    def __init__(self, md, math_store):
        super().__init__(md)
        self.math_store = math_store

    def run(self, text):
        for key in sorted(self.math_store.keys(), key=len, reverse=True):
            math_content = html.escape(self.math_store[key])
            text = text.replace(key, math_content)
        return text


class MathProtectExtension(Extension):
    def extendMarkdown(self, md):
        preprocessor = MathProtectPreprocessor(md)
        md.preprocessors.register(preprocessor, "math_protect", 27)
        postprocessor = MathProtectPostprocessor(md, preprocessor.math_store)
        md.postprocessors.register(postprocessor, "math_restore", 0)


def setup_markdown_processor():
    return Markdown(
        extensions=[
            "meta",
            "codehilite",
            "tables",
            "toc",
            MathProtectExtension(),
        ],
        extension_configs={
            "codehilite": {"css_class": "highlight", "use_pygments": False},
        },
        tab_length=2,
    )
