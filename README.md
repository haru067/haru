# haru
Spring color palette and color definitions for text editors  
https://haru067.github.io/haru/

## Usage
See ./dist

## Development

### Publish color schemes from color pallet
Colors are defined in yaml
```
cat src/haru.yml
yellow     : "deb757"
green      : "b7dd6c"
...
```

Append other formats
```
python format.py src/haru.yml
yellow     : "deb757"
yellow-r     : 0.3411764705882353
yellow-b     : 0.7176470588235294
yellow-g     : 0.8705882352941177
green      : "b7dd6c"
...
```

Replace template values with these colors. Template files are written by mustache
```
foo.html.mustache
<p style="color:#{{yellow}};">foo</p>
↓
foo.html
<p style="color:#deb757;">foo</p>
```

these tasks are executed by build.sh

### Create templates
Use convert script to create template files from editor-generate files.
This script simply replace matching colors from specified yaml file
```
python template-generator.py ./src/haru.yml ./sample/vscode-colortheme.json
```
