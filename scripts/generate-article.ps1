param(
    [string]$slug,
    [string]$title,
    [string]$author,
    [string]$date,
    [string]$category,
    [string]$content,
    [string]$outputDir
)

$ogTitle = "Leantalk - $title"
$canonical = "https://www.leantalk.cn/article/$slug.html"

$html = @"
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>$ogTitle</title>
<meta name="description" content="$title"/>
<link rel="canonical" href="$canonical"/>
<link rel="icon" type="image/png" sizes="32x32" href="/favicon.png"/>
<meta property="og:type" content="article"/>
<meta property="og:title" content="$ogTitle"/>
<meta property="og:description" content="$title"/>
<meta property="og:url" content="$canonical"/>
<meta property="og:site_name" content="Leantalk"/>
<meta property="og:locale" content="zh_CN"/>
<style>
:root{--bg:#fff;--bg-secondary:#f7f7f7;--text-primary:#111;--text-secondary:#444;--text-muted:#999;--accent:#00C9A7;--border:#e5e5e5;--radius:14px;--font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:var(--font);background:var(--bg);color:var(--text-primary);line-height:1.7;-webkit-font-smoothing:antialiased}
.navbar{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.97);backdrop-filter:blur(16px);border-bottom:1px solid var(--border);padding:0 48px;height:64px;display:flex;align-items:center;justify-content:space-between}
.navbar-logo{font-size:18px;font-weight:800;letter-spacing:-.4px}
.navbar-logo span{color:var(--accent)}
.navbar-links{display:flex;gap:36px}
.navbar-links a{font-size:14px;color:var(--text-secondary);transition:color .15s}
.navbar-links a:hover{color:var(--accent)}
.nav-back{font-size:14px;color:var(--text-secondary);display:flex;align-items:center;gap:6px}
.article-header{padding:60px 48px 40px;max-width:860px;margin:0 auto}
.article-category{font-size:12px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:var(--accent);margin-bottom:16px}
.article-title{font-size:clamp(24px,4vw,36px);font-weight:800;letter-spacing:-.5px;line-height:1.2;margin-bottom:20px;color:var(--text-primary)}
.article-meta{font-size:13px;color:var(--text-muted);display:flex;gap:12px;align-items:center}
.article-meta .author{color:var(--text-secondary);font-weight:600}
.article-divider{height:1px;background:var(--border);max-width:860px;margin:0 auto 40px}
.article-body{padding:0 48px 80px;max-width:860px;margin:0 auto}
.article-body p{margin-bottom:20px;font-size:16px;color:var(--text-secondary)}
.article-body h2{font-size:20px;font-weight:700;margin:40px 0 16px;color:var(--text-primary)}
.article-body ul,.article-body ol{margin:0 0 20px 24px}
.article-body li{margin-bottom:8px;font-size:16px;color:var(--text-secondary)}
.article-body blockquote{border-left:3px solid var(--accent);padding:16px 20px;background:var(--bg-secondary);margin:24px 0;border-radius:0 8px 8px 0}
.article-body blockquote p{font-size:15px;font-style:italic;margin:0}
.footer{border-top:1px solid var(--border);padding:48px 24px;text-align:center;color:var(--text-muted);font-size:13px}
.footer a{color:var(--accent)}
@media(max-width:600px){.article-header,.article-body{padding-left:20px;padding-right:20px}.navbar{padding:0 20px}}
</style>
</head>
<body>
<nav class="navbar">
  <a class="navbar-logo" href="/">Lean<span>talk</span></a>
  <a class="nav-back" href="/">← 返回首页</a>
</nav>
<article>
  <header class="article-header">
    <div class="article-category">$category</div>
    <h1 class="article-title">$title</h1>
    <div class="article-meta">
      <span class="author">$author</span>
      <span>·</span>
      <span>$date</span>
      <span>·</span>
      <span>Leantalk</span>
    </div>
  </header>
  <div class="article-divider"></div>
  <div class="article-body">
$content
  </div>
</article>
<footer class="footer">
  <p>面向制造业的AI实战知识平台 · <a href="https://www.leantalk.cn">www.leantalk.cn</a></p>
</footer>
</body>
</html>
"@

$outPath = Join-Path $outputDir "$slug.html"
$html | Out-File -FilePath $outPath -Encoding utf8
Write-Host "Created: $outPath"