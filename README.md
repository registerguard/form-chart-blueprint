Made from https://github.com/rgpages/ncaa-form-charts

## Getting started

```
workon tarbell
tarbell install-template https://github.com/registerguard/form-chart-blueprint
tarbell newproject 20xx-form-chart
# Yes, generate spreadsheet dynamically
tarbell spreadsheet
tarbell serve
```

## Dev work

Make changes and push commit. Delete two lines from `.tarbell/settings.yaml` and re-install. Then try a new project. Repeat.
