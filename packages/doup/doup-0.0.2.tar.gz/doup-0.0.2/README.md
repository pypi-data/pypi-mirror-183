# doup

A command line tool for lazy people to maintain the pinned docker versions in project files.
You never have to check for newer image versions at dockerhub manually.

## What is the problem?

You want to pin the version of your docker images in your project files to avoid suprises.
But your applications should stay up2date and that leads to a repeatable task.
With doup you can set loose tags like `latest` in a comment above the image and doup will seach for the most specific tag and update the file.

![example](docs/images/example_group_nextcloud.jpg)

## OMG I WANT THIS!

Each docker image tag have to be marked in the previous line:

```yml
# doup:bullseye:prod
haproxy_docker_image: haproxy:2.6.2-bullseye
```

- `doup`:  required marker
- `bullseye`: required tag to follow, see [haproxy:bullseye](https://hub.docker.com/layers/library/haproxy/bullseye/images/sha256-9f97cd4c52340cc4df4c1974678c1dea528b3c567bced021a5e0974914dda253?context=explore)
- `prod`: optional group name

## Quick setup

1. clone the git repository
2. run `make install`
3. add `~/.local/bin` to your path
4. run doup

```bash
git clone https://github.com/meomeo187/doup.git && cd doup
make install
source venv/bin/activate
doup --path .
```

## Links

- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
