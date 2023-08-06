# jupyterlab_theme_light_minimal

[![Github Actions Status](https://github.com/falconair/jupyterlab_theme_light_minimal/workflows/Build/badge.svg)](https://github.com/falconair/jupyterlab_theme_light_minimal/actions/workflows/build.yml)
A minimal JL theme

## Recreate theme

Steps to recreate:
```
cookiecutter https://github.com/jupyterlab/extension-cookiecutter-ts
```
* Pick 'theme'
* author_name: Shahbaz Chaudhary
* author_email: shahbazc@gmail.com
* labextension_name: jupyterlab_theme_light_minimal
* test: n
* repository: https://github.com/falconair/jupyterlab_theme_light_minimal

#### Colors
```
    --jp-cell-editor-border-color: var(--jp-layout-color0);
    --jp-cell-editor-background: var(--jp-layout-color0);
```

## Requirements

- JupyterLab >= 3.0

## Install

To install the extension, execute:

```bash
pip install jupyterlab_theme_light_minimal
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall jupyterlab_theme_light_minimal
```

## Contributing

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```bash
# Clone the repo to your local environment
# Change directory to the jupyterlab_theme_light_minimal directory
# Install package in development mode
pip install -e "."
# Link your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite
# Rebuild extension Typescript source after making changes
jlpm build
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```bash
jupyter lab build --minimize=False
```

### Development uninstall

```bash
pip uninstall jupyterlab_theme_light_minimal
```

In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `jupyterlab_theme_light_minimal` within that folder.

### Packaging the extension

See [RELEASE](RELEASE.md)
