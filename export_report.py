"""Export the executed notebook as a readable, accessible static report."""
from pathlib import Path
import nbformat
from nbconvert import HTMLExporter

ROOT = Path(__file__).resolve().parent
notebook = nbformat.read(ROOT / 'analysis.ipynb', as_version=4)
html, _ = HTMLExporter(template_name='lab', exclude_input=True,
    exclude_input_prompt=True, exclude_output_prompt=True).from_notebook_node(
        notebook, resources={'metadata': {'name': 'Triathlon Performance & Survey Analysis'}})
descriptions = [
    'Scatterplot of swim time versus run time, distinguishing 2018 and 2019 finishers.',
    'Overall finish time versus bike time, with observed points and the fitted regression line.',
    'Overall finish time versus run time, with observed points and the fitted regression line.',
    'Residuals versus fitted values for the bike-time and run-time regression models.',
    'Side-by-side boxplots of phone contact counts for respondents with and without employment.',
]
placeholder = 'alt="No description has been provided for this image"'
assert html.count(placeholder) == len(descriptions)
for description in descriptions:
    html = html.replace(placeholder, f'alt="{description}"', 1)
style = '''<style>
body {background:#f8fafc;color:#17283b;line-height:1.65;}
main {max-width:1040px;margin:0 auto;background:white;padding:24px 22px 60px;}
.jp-RenderedHTMLCommon p {max-width:85ch;line-height:1.75;}
.jp-OutputArea-output {max-width:100%;overflow-x:auto;}
.jp-RenderedImage img {max-width:100%;height:auto;}
.portfolio-nav {max-width:1040px;margin:0 auto;padding:16px 24px;display:flex;flex-wrap:wrap;gap:20px;font:600 13px system-ui,sans-serif;}
.portfolio-nav a {color:#20598c;text-decoration:none;}
.portfolio-nav a:hover {text-decoration:underline;}
@media(max-width:600px){main{padding:15px 8px 40px;} .jp-RenderedHTMLCommon h1{font-size:1.7rem;line-height:1.3;} .portfolio-nav{padding:14px 20px;}}
</style>'''
html = html.replace('</head>', style + '</head>')
nav = '''<nav class="portfolio-nav" aria-label="Project links"><a href="https://github.com/juanthom99/DTSC2301_HW">Project overview on GitHub</a><a href="https://github.com/juanthom99/DTSC2301_HW/blob/main/analysis.ipynb">Executed notebook and code</a></nav>'''
html = html.replace('<main>', nav + '<main>', 1)
(ROOT / 'docs/index.html').write_text(html, encoding='utf-8')
print('Exported report with five chart descriptions and responsive reading layout.')
