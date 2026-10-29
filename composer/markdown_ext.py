import html
import re
import xml.etree.ElementTree as etree

from markdown import Markdown
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown.preprocessors import Preprocessor
from markdown.treeprocessors import Treeprocessor

MATH_DISPLAY_PATTERN = re.compile(r"\$\$([^\$]+)\$\$")
MATH_INLINE_PATTERN = re.compile(r"\$([^\$\n]+)\$")
MATH_KEY_PATTERN = re.compile(r"MATH_(?:DISPLAY|INLINE)_\d+")

THEAD_PATTERN = re.compile(r"<thead>.*?</thead>", re.DOTALL)
TH_TAG_PATTERN = re.compile(r"<th(?=[ >])")

IMG_TAG_PATTERN = re.compile(r"<img\b[^>]*>")
IMG_ALT_ATTR_PATTERN = re.compile(r'alt="([^"]*)"')
IMG_SIZE_TOKEN_PATTERN = re.compile(r"\s*\((img-[a-z0-9]+(?:-[a-z0-9]+)*)\)")


class MathProtectPreprocessor(Preprocessor):
    def __init__(self, md, math_store):
        super().__init__(md)
        self.math_store = math_store

    def run(self, lines):
        self.math_store.clear()
        text = "\n".join(lines)
        text = MATH_DISPLAY_PATTERN.sub(self._protect("DISPLAY"), text)
        text = MATH_INLINE_PATTERN.sub(self._protect("INLINE"), text)
        return text.split("\n")

    def _protect(self, kind):
        def replace(match):
            key = f"MATH_{kind}_{len(self.math_store)}"
            self.math_store[key] = match.group(0)
            return key

        return replace


class MathRestorePostprocessor(Postprocessor):
    def __init__(self, md, math_store):
        super().__init__(md)
        self.math_store = math_store

    def run(self, text):
        if not self.math_store:
            return text
        return MATH_KEY_PATTERN.sub(self._restore, text)

    def _restore(self, match):
        key = match.group(0)
        return html.escape(self.math_store[key]) if key in self.math_store else key


class MathProtectExtension(Extension):
    def extendMarkdown(self, md):
        math_store = {}
        md.preprocessors.register(
            MathProtectPreprocessor(md, math_store), "math_protect", 27
        )
        md.postprocessors.register(
            MathRestorePostprocessor(md, math_store), "math_restore", 0
        )


class TableWrapPostprocessor(Postprocessor):
    def run(self, text):
        text = THEAD_PATTERN.sub(
            lambda m: TH_TAG_PATTERN.sub('<th scope="col"', m.group(0)), text
        )
        text = text.replace("<table>", '<div class="table-scroll"><table>')
        return text.replace("</table>", "</table></div>")


class TableWrapExtension(Extension):
    def extendMarkdown(self, md):
        md.postprocessors.register(TableWrapPostprocessor(md), "table_wrap", 5)


class ImageSizingPostprocessor(Postprocessor):
    def run(self, text):
        return IMG_TAG_PATTERN.sub(self._process_tag, text)

    def _process_tag(self, match):
        tag = match.group(0)
        alt_match = IMG_ALT_ATTR_PATTERN.search(tag)
        if not alt_match:
            return tag

        alt = alt_match.group(1)
        tokens = IMG_SIZE_TOKEN_PATTERN.findall(alt)
        if not tokens:
            return tag

        clean_alt = IMG_SIZE_TOKEN_PATTERN.sub("", alt).strip()
        tag = tag[: alt_match.start()] + f'alt="{clean_alt}"' + tag[alt_match.end() :]
        return tag.replace("<img ", f'<img class="{" ".join(tokens)}" ', 1)


class ImageSizingExtension(Extension):
    def extendMarkdown(self, md):
        md.postprocessors.register(ImageSizingPostprocessor(md), "image_sizing", 4)


class SectionWrapTreeprocessor(Treeprocessor):
    def run(self, root):
        children = list(root)
        if not any(child.tag == "h2" for child in children):
            return

        for child in children:
            root.remove(child)

        section = None
        for child in children:
            if child.tag == "h2":
                section = etree.SubElement(root, "section")
            (root if section is None else section).append(child)


class SectionWrapExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(SectionWrapTreeprocessor(md), "section_wrap", 4)


def create_markdown():
    return Markdown(
        extensions=[
            "codehilite",
            "tables",
            "toc",
            MathProtectExtension(),
            TableWrapExtension(),
            ImageSizingExtension(),
            SectionWrapExtension(),
        ],
        extension_configs={
            "codehilite": {"css_class": "highlight", "use_pygments": False},
            "toc": {"toc_depth": "2-3"},
        },
        tab_length=2,
    )
