# [school.gijs6.nl](https://school.gijs6.nl)

The place I dump all my school summaries.

It uses [`binder.py`](binder.py), a custom simple ssg that deals with the build output, templating and feeds.

## Running locally

```bash
pip install -r requirements.txt

bake serve  # dev server
bake build  # static site
```

> The `bake` command is just a simple alternative to `make`. To use it, install [`bake`](https://git.dupunkto.org/~meta/dotfiles/blob/master/bin/bake) in your `PATH`.  
> Or just run the Python commands directly: `python binder.py serve` or `python binder.py build`.

---

Thanks to [Robin](https://github.com/RobinBoers) for the original inspiration for this whole site, so do also check out his [school site](https://github.com/RobinBoers/school.geheimesite.nl) (or even his [university site](https://github.com/RobinBoers/uni.geheimesite.nl) :D)
