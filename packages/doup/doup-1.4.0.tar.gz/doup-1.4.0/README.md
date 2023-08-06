# 🚀 doup

A command line tool to find and update Docker-Image-Strings in project files.

[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)
[![pipeline main](https://gitlab.com/doup1/doup/badges/main/pipeline.svg)](https://gitlab.com/doup1/doup/blob/feature/update_readme/README.md)

## Why you should using doup

The version of docker images should not set to `latest` to avoid upgrade nightmares.
But containers should also be upgraded regulary to get new features and fixes of security issues.

So you have to check for each container individually if a new version is published on dockerhub.
`doup` can save you a lot of time and is doing this task for you.

### Example

![example-image](./docs/images/example1.jpg)

## Prepare your project for doup

Each Docker-Image-String has to be marked in the previous line:

```yml
# doup:bullseye:prod
haproxy_docker_image: haproxy:2.6.2-bullseye
```

- `doup`: doup is looking for lines which contains `doup:*`
- `bullseye`: is the container tag on dockerhub which is used to get the newest version
- `prod` (optional): add this Docker-Image-String to a specific group

## QuickSetup

`doup` is published on PyPi and can be installed with `pip install doup`.
Afterwards you should mark some Docker-Version-Strings in your project and run `doup --dry-run`.

## Incoming features

- add output: release date of docker image
- add command: `doup list groups`
- add command: `doup list images`
    - list marked Docker-Image-Strings
- add command:`doup find images`
    - finds not marked Docker-Image-Strings
