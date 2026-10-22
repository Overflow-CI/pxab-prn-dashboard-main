"""Regenerate the precompiled Tailwind CSS inlined in nc_medicaid_bh_dashboard.html.
Run from handoff/tools after `npm install`:  python3 rebuild.py
It strips the existing CSS, scans the markup and scripts for classes, compiles, and pastes the result back."""
import os, re, subprocess
B = os.path.dirname(os.path.abspath(__file__))
p = os.path.abspath(os.path.join(B, '..', '..', 'nc_medicaid_bh_dashboard.html'))
s = open(p).read()
m = re.search(r'(and paste tw\.css here\. -->\n  <style>)(.*?)(</style>)', s, re.S)
open(B + '/src.html', 'w').write(s[:m.start(2)] + s[m.end(2):])
r = subprocess.run(['npx', 'tailwindcss', '-i', 'in.css', '--content', 'src.html', '--minify', '-o', 'new.css'], cwd=B, capture_output=True, text=True)
print(r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'built')
css = open(B + '/new.css').read().strip()
open(p, 'w').write(s[:m.start(2)] + css + s[m.end(2):])
print(len(css), 'bytes of CSS')
