# MkDocs Obsidian Plugin
This is a fork of the [MkDocs Roamlinks Plugin](https://github.com/Jackiexiao/mkdocs-roamlinks-plugin) with added support for the custom admonition type for the syntax used in [Obsidian Admonition](https://github.com/valentine195/obsidian-admonition).




An MkDocs plugin that simplifies relative linking between documents and convert [[roamlinks]] for [vscode-foam](https://github.com/foambubble/foam) & [obsidian](https://obsidian.md) 

## Setup 

Install the plugin and activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - roamlinks 
```

## Usage

To use this plugin, simply create a link that only contains the filename of file you wish to link to.

| origin                  | convert                             |
| ----------------------- | ----------------------------------- |
| `[Git Flow](git_flow.md)` | `[Git Flow](../software/git_flow.md)` |
| `[[Git Flow]]`            | `[Git Flow](../software/git_flow.md)` |
| `![[image.png]]`           | `![image.png](../image/imag.png)`      |
| `[[#Heading identifiers]]` | `[Heading identifiers in HTML](#heading-identifiers-in-html)`|
| `[[Git Flow#Heading]]`     |  `[Git Flow](../software/git_flow.md#heading)` |
