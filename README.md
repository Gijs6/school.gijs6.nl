# [school.gijs6.nl](https://school.gijs6.nl)

So this is basically where I put all my school summaries.

## What's this about

I got tired of Google Docs being a mess so I moved everything to Markdown. So now I can use *proper* LaTeX math and actually organize things without going insane. And version control via Git is actually very handy for notes.

You can find the site at [school.gijs6.nl](https://school.gijs6.nl).

## How it works behind the scenes

All the magic happens in `binder.py`. It's basically my own static site generator that:

- Crawls through all the Markdown files in the `site/` folder
- Converts them to HTML using Jinja2 templates
- Generates an RSS and Atom feed because why not
- Builds a nice homepage that organizes everything by school year and period, based on the test codes
- Has a dev server with file watching

## Running it locally

```bash
# Install deps
pip install -r requirements.txt

# Start dev server with hot reload
bake serve

# Or build static files
bake build
```

The `bake` command is just a simple alternative to `make`. To use it, you'll need to install `[bake](https://git.dupunkto.org/~meta/dotfiles/blob/master/bin/bake)` in your `PATH`. Or you can run the Python commands directly: `python binder.py serve` or `python binder.py build`.

---

Huge thanks to [Robin](https://github.com/RobinBoers) for the original inspiration. His [school site](https://github.com/RobinBoers/school.geheimesite.nl) is what got me started on this whole workflow.
