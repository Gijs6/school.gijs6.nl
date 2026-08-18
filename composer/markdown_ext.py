import html
import re

from markdown import Markdown
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown.preprocessors import Preprocessor

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


THEAD_PATTERN = re.compile(r"<thead>.*?</thead>", re.DOTALL)
TH_TAG_PATTERN = re.compile(r"<th(?=[ >])")


class TableWrapPostprocessor(Postprocessor):
    def run(self, text):
        text = THEAD_PATTERN.sub(
            lambda m: TH_TAG_PATTERN.sub('<th scope="col"', m.group(0)), text
        )
        text = text.replace("<table>", '<div class="table-scroll"><table>')
        text = text.replace("</table>", "</table></div>")
        return text


class TableWrapExtension(Extension):
    def extendMarkdown(self, md):
        md.postprocessors.register(TableWrapPostprocessor(md), "table_wrap", 5)


IMG_TAG_PATTERN = re.compile(r"<img\b[^>]*>")
IMG_ALT_ATTR_PATTERN = re.compile(r'alt="([^"]*)"')
IMG_SIZE_TOKEN_PATTERN = re.compile(r"\s*\((img-[a-z0-9]+(?:-[a-z0-9]+)*)\)")


class ImageSizingPostprocessor(Postprocessor):
    """Moves `(img-xl)`-style layout hints out of the `alt` attribute (where
    screen readers would read them aloud as part of the image description)
    and into CSS classes instead."""

    def run(self, text):
        def process_tag(match):
            tag = match.group(0)
            alt_match = IMG_ALT_ATTR_PATTERN.search(tag)
            if not alt_match:
                return tag

            alt = alt_match.group(1)
            tokens = IMG_SIZE_TOKEN_PATTERN.findall(alt)
            if not tokens:
                return tag

            clean_alt = IMG_SIZE_TOKEN_PATTERN.sub("", alt).strip()
            tag = (
                tag[: alt_match.start()] + f'alt="{clean_alt}"' + tag[alt_match.end() :]
            )
            return tag.replace("<img ", f'<img class="{" ".join(tokens)}" ', 1)

        return IMG_TAG_PATTERN.sub(process_tag, text)


class ImageSizingExtension(Extension):
    def extendMarkdown(self, md):
        md.postprocessors.register(ImageSizingPostprocessor(md), "image_sizing", 4)


def setup_markdown_processor():
    return Markdown(
        extensions=[
            "meta",
            "codehilite",
            "tables",
            "toc",
            MathProtectExtension(),
            TableWrapExtension(),
            ImageSizingExtension(),
        ],
        extension_configs={
            "codehilite": {"css_class": "highlight", "use_pygments": False},
            "toc": {"toc_depth": "2-3"},
        },
        tab_length=2,
    )
