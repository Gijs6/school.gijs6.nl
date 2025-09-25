# [school.gijs6.nl](https://school.gijs6.nl)

The *famous* place I dump all my school summaries.

## Why

Google Docs got really messy to distribute. And Markdown, LaTeX and Git make my life so much easier.

## How it works

[`binder.py`](binder.py) is a simple static site generator that just builds the HTML, feeds and allows me to do really nice Jinja templating.

## Running locally

```bash
pip install -r requirements.txt

bake serve   # dev server
bake build   # static site
```

The `bake` command is just a simple alternative to `make`. To use it, install [`bake`](https://git.dupunkto.org/~meta/dotfiles/blob/master/bin/bake) in your `PATH`.  
Or just run the Python commands directly: `python binder.py serve` or `python binder.py build`.

---

Inspired by [Robin](https://github.com/RobinBoers)'s school site workflow.
