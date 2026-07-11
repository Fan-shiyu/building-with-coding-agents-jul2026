#!/usr/bin/env python3
"""Generate two self-contained HTML pages for the workshop from its markdown.

Run:  uv run --with markdown python build_docs.py

Reads workshop/exercise-*/README.md and solutions/exercise-*/*.md and writes
docs/workshop.html and docs/solutions.html. No project dependency is added:
the `markdown` library rides on `uv run --with`. Nothing under workshop/,
solutions/, data/ or pyproject.toml is modified. Output is deterministic, so
running twice produces byte-identical files (that's what GitHub Pages serves).
"""

import html
import os
import posixpath
import re

import markdown

# GitHub base for links to files we do NOT inline (templates, settings.json,
# the reference dashboard). Point this at your fork if you republish there.
GITHUB_BASE = "https://github.com/pyladiesams/building-with-coding-agents-jul2026"

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
LEDE = "materials for the PyLadies Amsterdam workshop, July 14, 2026"
MD_EXTENSIONS = ["fenced_code", "tables", "sane_lists"]


def slug(text):
    """Lowercase, alnum-only slug; drops emoji/punctuation, collapses dashes."""
    out = [c if c.isalnum() else "-" for c in text.lower()]
    s = re.sub(r"-+", "-", "".join(out))
    return s.strip("-")


def first_h1(md_text):
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def dedent_list_fences(md_text):
    """Move fenced code blocks that are indented inside list items out to the
    left margin. Python-Markdown's fenced_code does not recognise a fence nested
    under a list item (it renders the ``` literally), so we lift each such block
    to column 0 with blank lines around it. The list resumes afterward via an
    <ol start=N>, so step numbering is preserved."""
    lines = md_text.split("\n")
    out, i = [], 0
    fence_re = re.compile(r"^(\s+)(```|~~~)")
    while i < len(lines):
        m = fence_re.match(lines[i])
        if m:
            indent = m.group(1)
            if out and out[-1].strip():
                out.append("")
            out.append(lines[i].lstrip())
            i += 1
            while i < len(lines):
                out.append(lines[i][len(indent):]
                           if lines[i].startswith(indent) else lines[i].lstrip())
                closing = lines[i].strip() in ("```", "~~~")
                i += 1
                if closing:
                    break
            if i < len(lines) and lines[i].strip():
                out.append("")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def preprocess(md_text):
    """Re-wrap a leading YAML frontmatter block as a ```yaml fence so it renders
    faithfully as code instead of being mangled into an <hr> + setext heading,
    and lift indented fenced blocks out of list items so they render as code."""
    md_text = dedent_list_fences(md_text)
    lines = md_text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                body = "\n".join(lines[1:i])
                rest = "\n".join(lines[i + 1:])
                return "```yaml\n" + body + "\n```\n" + rest
    return md_text


def render(md_text):
    """Markdown -> HTML with the edge cases this repo actually contains handled:
    frontmatter (above), task-list checkboxes, and horizontally-scrollable
    tables. A fresh convert each call keeps output deterministic."""
    out = markdown.markdown(preprocess(md_text), extensions=MD_EXTENSIONS)
    out = out.replace(
        "<li>[ ] ", '<li class="task"><input type="checkbox" disabled> '
    )
    out = out.replace(
        "<li>[x] ",
        '<li class="task"><input type="checkbox" checked disabled> ',
    )
    out = out.replace("<table>", '<div class="tw"><table>')
    out = out.replace("</table>", "</table></div>")
    return out


def rewrite_hrefs(html_text, src_dir, page, file_anchor, dir_anchor):
    """Rewrite relative links (in rendered HTML, so code samples are untouched)
    to in-page anchors, the sibling page's anchor, or a GitHub URL."""

    def repl(m):
        href = m.group(2)
        if re.match(r"(https?:|#|mailto:)", href):
            return m.group(0)
        norm = posixpath.normpath(posixpath.join(src_dir, href))
        target = file_anchor.get(norm) or dir_anchor.get(norm)
        if target:
            tpage, anchor = target
            new = "#" + anchor if tpage == page else tpage + ".html#" + anchor
        else:
            is_dir = href.endswith("/") or "." not in posixpath.basename(norm)
            kind = "tree" if is_dir else "blob"
            new = "%s/%s/main/%s" % (GITHUB_BASE, kind, norm)
        return m.group(1) + new + m.group(3)

    return re.sub(r'(<a\s+href=")([^"]+)(")', repl, html_text)


def discover():
    """Return ordered (num, folder, [md files]) for workshop and solutions."""
    wf = sorted(d for d in os.listdir(os.path.join(ROOT, "workshop"))
                if re.match(r"exercise-\d", d))
    workshop = [(int(re.search(r"\d+", d).group()), d, ["README.md"]) for d in wf]
    sf = sorted(d for d in os.listdir(os.path.join(ROOT, "solutions"))
                if re.match(r"exercise-\d", d))
    solutions = []
    for d in sf:
        mds = [f for f in os.listdir(os.path.join(ROOT, "solutions", d))
               if f.endswith(".md")]
        head = ["SOLUTION.md"] if "SOLUTION.md" in mds else []
        ordered = head + sorted(f for f in mds if f != "SOLUTION.md")
        solutions.append((int(re.search(r"\d+", d).group()), d, ordered))
    return workshop, solutions


def build_anchor_maps(workshop, solutions):
    file_anchor, dir_anchor = {}, {}
    for num, folder, _ in workshop:
        a = ("workshop", "exercise-%d" % num)
        dir_anchor["workshop/" + folder] = a
        file_anchor["workshop/%s/README.md" % folder] = a
    for num, folder, files in solutions:
        dir_anchor["solutions/" + folder] = ("solutions", "exercise-%d" % num)
        for f in files:
            stem = os.path.splitext(f)[0]
            file_anchor["solutions/%s/%s" % (folder, f)] = (
                "solutions", "exercise-%d-%s" % (num, slug(stem)))
    return file_anchor, dir_anchor


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as fh:
        return fh.read()


def build_workshop(workshop, fa, da):
    toc, body = [], []
    for num, folder, _ in workshop:
        md = read("workshop", folder, "README.md")
        label = first_h1(md) or ("Exercise %d" % num)
        toc.append('<li><a href="#exercise-%d">%s</a></li>'
                   % (num, html.escape(label)))
        content = rewrite_hrefs(render(md), "workshop/" + folder,
                                "workshop", fa, da)
        body.append('<section id="exercise-%d" class="ex">%s</section>'
                    % (num, content))
    toc_html = '<strong>Exercises</strong><ol class="toc-list">%s</ol>' \
        % "".join(toc)
    return toc_html, "\n".join(body)


def build_solutions(solutions, fa, da):
    toc, body = [], []
    for num, folder, files in solutions:
        subs, blocks = [], []
        for f in files:
            anchor = "exercise-%d-%s" % (num, slug(os.path.splitext(f)[0]))
            subs.append('<li><a href="#%s">%s</a></li>'
                        % (anchor, html.escape(f)))
            content = rewrite_hrefs(render(read("solutions", folder, f)),
                                    "solutions/" + folder, "solutions", fa, da)
            blocks.append(
                '<section class="file" id="%s"><details>'
                '<summary>%s &mdash; click to reveal</summary>'
                '<div class="md">%s</div></details></section>'
                % (anchor, html.escape(f), content))
        toc.append('<li><a href="#exercise-%d">Exercise %d</a>'
                   '<ul class="toc-sub">%s</ul></li>'
                   % (num, num, "".join(subs)))
        body.append('<section id="exercise-%d" class="ex">'
                    '<h2 class="ex-h">Exercise %d</h2>%s</section>'
                    % (num, num, "".join(blocks)))
    body.append(
        '<section class="refdash"><h2>Reference dashboard</h2>'
        '<p>The full working dashboard is on GitHub, not inlined here: '
        '<a href="%s/tree/main/solutions/reference-dashboard">'
        'solutions/reference-dashboard/</a>.</p></section>' % GITHUB_BASE)
    toc_html = '<strong>Solutions</strong><ol class="toc-list">%s</ol>' \
        % "".join(toc)
    return toc_html, "\n".join(body)


def page(title, sibling_label, sibling_href, toc_html, body_html):
    header = (
        '<header class="site"><h1>%s</h1><p class="lede">%s &middot; '
        '<a href="%s">%s</a></p></header>'
        % (html.escape(title), LEDE, sibling_href, html.escape(sibling_label)))
    return ("<!doctype html>\n<html lang=\"en\">\n<head>\n"
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, '
            'initial-scale=1">\n<link rel="icon" href="data:,">\n'
            '<title>%s</title>\n<style>%s</style>\n'
            "</head>\n<body>\n%s\n"
            '<div class="layout"><nav class="toc">%s</nav>'
            "<main>%s</main></div>\n<script>%s</script>\n</body>\n</html>\n"
            % (html.escape(title), CSS, header, toc_html, body_html, JS))


# Inline stylesheet (one CSS rule per line). Teal accent echoes the workshop
# dashboard's Set2 green; light + dark via prefers-color-scheme.
CSS = """
:root{--bg:#fff;--panel:#fafbfb;--fg:#1f2933;--muted:#5b6b73;--accent:#2a9d8f;--border:#e4eae9;--pre:#f3f6f5;--code:#e9efee;--sel:#e5f4f1}
@media (prefers-color-scheme:dark){:root{--bg:#0f1517;--panel:#141b1e;--fg:#e6edf0;--muted:#9db0b5;--accent:#4fd1c5;--border:#26333a;--pre:#161e22;--code:#1d272c;--sel:#173a37}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
.site{border-bottom:1px solid var(--border);padding:1.6rem 1.5rem;background:var(--panel)}
.site h1{margin:0 0 .2rem;font-size:1.5rem;letter-spacing:-.3px}
.lede{margin:0;color:var(--muted);font-size:.92rem}
.layout{display:grid;grid-template-columns:minmax(210px,250px) 1fr;gap:2rem;max-width:1150px;margin:0 auto;padding:1.5rem}
.toc{position:sticky;top:1rem;align-self:start;max-height:calc(100vh - 2rem);overflow:auto;font-size:.9rem}
.toc strong{display:block;text-transform:uppercase;letter-spacing:.5px;font-size:.72rem;color:var(--muted);margin-bottom:.5rem}
.toc-list{list-style:none;margin:0;padding:0}
.toc-list>li{margin:.15rem 0}
.toc-list a{display:block;padding:.25rem .5rem;border-radius:6px;color:var(--fg);border-left:2px solid transparent}
.toc-list a:hover{background:var(--sel);text-decoration:none}
.toc-list a.active{border-left-color:var(--accent);color:var(--accent);background:var(--sel);font-weight:600}
.toc-sub{list-style:none;margin:.1rem 0 .3rem;padding-left:.6rem}
.toc-sub a{font-size:.83rem;color:var(--muted)}
main{min-width:0;max-width:75ch}
main h1{font-size:1.6rem;letter-spacing:-.3px;margin-top:0}
main h2{font-size:1.25rem;margin-top:2rem;padding-top:.3rem}
.ex{scroll-margin-top:1rem;border-top:1px solid var(--border);padding-top:1.5rem;margin-top:2.5rem}
.ex:first-of-type{border-top:0;margin-top:0}
.file{scroll-margin-top:1rem}
code{font-family:"SF Mono",Menlo,Consolas,monospace;font-size:.88em;background:var(--code);padding:.1em .35em;border-radius:4px}
pre{position:relative;background:var(--pre);border:1px solid var(--border);border-radius:8px;padding:.9rem 1rem;overflow-x:auto}
pre code{background:none;padding:0;font-size:.85rem;line-height:1.5}
.copy{position:absolute;top:.5rem;right:.5rem;font:600 .72rem/1 inherit;color:var(--muted);background:var(--bg);border:1px solid var(--border);border-radius:6px;padding:.3rem .55rem;cursor:pointer;opacity:.75}
.copy:hover{opacity:1;color:var(--accent);border-color:var(--accent)}
.tw{overflow-x:auto;margin:1rem 0}
table{border-collapse:collapse;font-size:.9rem}
th,td{border:1px solid var(--border);padding:.4rem .6rem;text-align:left}
th{background:var(--panel)}
details{border:1px solid var(--border);border-radius:8px;margin:1rem 0;background:var(--panel)}
summary{cursor:pointer;padding:.7rem 1rem;font-weight:600;font-family:monospace;color:var(--accent)}
summary::marker{color:var(--accent)}
.md{padding:0 1rem 1rem}
.task{list-style:none}
.task input{margin-right:.5rem}
blockquote{border-left:3px solid var(--accent);margin:1rem 0;padding:.1rem 1rem;color:var(--muted)}
.refdash{margin-top:3rem;border-top:1px solid var(--border);padding-top:1.5rem}
@media (max-width:820px){.layout{grid-template-columns:1fr;gap:1rem}.toc{position:static;max-height:none;border-bottom:1px solid var(--border);padding-bottom:1rem}main{max-width:100%}}
"""

JS = """
document.querySelectorAll('main pre').forEach(function(pre){
  var b=document.createElement('button');b.className='copy';b.type='button';
  b.textContent='Copy';
  b.addEventListener('click',function(){
    var c=pre.querySelector('code');var t=(c?c.innerText:pre.innerText);
    function ok(){b.textContent='Copied!';setTimeout(function(){
      b.textContent='Copy';},1500);}
    function fb(){var a=document.createElement('textarea');a.value=t;
      document.body.appendChild(a);a.select();
      try{document.execCommand('copy');}catch(e){}
      document.body.removeChild(a);ok();}
    if(navigator.clipboard&&navigator.clipboard.writeText){
      navigator.clipboard.writeText(t).then(ok,fb);}else{fb();}
  });
  pre.appendChild(b);
});
var links={};
document.querySelectorAll('nav.toc a').forEach(function(a){
  links[a.getAttribute('href').slice(1)]=a;});
var obs=new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(e.isIntersecting&&links[e.target.id]){
      document.querySelectorAll('nav.toc a.active').forEach(function(x){
        x.classList.remove('active');});
      links[e.target.id].classList.add('active');}
  });
},{rootMargin:'0px 0px -70% 0px'});
document.querySelectorAll('section[id]').forEach(function(s){obs.observe(s);});
function openTarget(){
  var h=decodeURIComponent(location.hash.slice(1));if(!h)return;
  var el=document.getElementById(h);if(!el)return;
  var d=el.tagName.toLowerCase()==='section'?el.querySelector('details')
    :el.closest('details');
  if(d)d.open=true;el.scrollIntoView();
}
document.querySelectorAll('nav.toc a').forEach(function(a){
  a.addEventListener('click',function(){setTimeout(openTarget,0);});});
window.addEventListener('hashchange',openTarget);
openTarget();
"""


def main():
    workshop, solutions = discover()
    fa, da = build_anchor_maps(workshop, solutions)

    w_toc, w_body = build_workshop(workshop, fa, da)
    w_html = page("Building with Coding Agents — Workshop",
                  "Solutions →", "solutions.html", w_toc, w_body)

    s_toc, s_body = build_solutions(solutions, fa, da)
    s_html = page("Building with Coding Agents — Solutions",
                  "← Workshop", "workshop.html", s_toc, s_body)

    os.makedirs(DOCS, exist_ok=True)
    for name, content in (("workshop.html", w_html), ("solutions.html", s_html)):
        with open(os.path.join(DOCS, name), "w", encoding="utf-8",
                  newline="\n") as fh:
            fh.write(content)

    print("Wrote docs/workshop.html (%d exercises)" % len(workshop))
    print("Wrote docs/solutions.html (%d exercises, %d files)"
          % (len(solutions), sum(len(f) for _, _, f in solutions)))


if __name__ == "__main__":
    main()
