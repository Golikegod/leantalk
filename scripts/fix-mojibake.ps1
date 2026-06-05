# leantalk 文章页 mojibake 批量修复
# 根因：源文件曾以 GBK 保存/读取，UTF-8 渲染时出现"路"（U+8DEF）/ "鈫?" / "闈㈠悜..." / "aram" 错位
# 修复：替换为正确 UTF-8 字符
# 编码：写回 UTF-8 (no BOM)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot\..

$articlesDir = "src\article"
$files = Get-ChildItem $articlesDir -Filter "*.html"

$middleDot = [char]0x00B7   # ·
$leftArrow = [char]0x2190   # ←
$replacements = @{
    '路'                                  = $middleDot
    '鈫\?'                                 = $leftArrow
    '杩斿洖棣栭〉'                          = '返回首页'
    '闈㈠悜鍒堕€犱笟鐨凙I瀹炴垬鐭ヨ瘑骞冲彴' = '面向制造业的 AI 实战知识平台'
    '操作员不知道aram 的数据怎么用'         = '操作员不知道系统的数据怎么用'
}

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$stats = @{ 'modified' = 0; 'bytes' = 0; 'unchanged' = 0 }

foreach ($file in $files) {
    $orig = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
    $cur  = $orig
    foreach ($k in $replacements.Keys) {
        $cur = [regex]::Replace($cur, [regex]::Escape($k), $replacements[$k])
    }
    if ($cur -ne $orig) {
        $before = (Get-Item $file.FullName).Length
        [System.IO.File]::WriteAllText($file.FullName, $cur, $utf8NoBom)
        $after = (Get-Item $file.FullName).Length
        $stats.modified++
        $stats.bytes += ($after - $before)
        Write-Host ("  ✎ {0}  ({1:+#;-#;0} B)" -f $file.Name, ($after - $before))
    } else {
        $stats.unchanged++
    }
}

Write-Host ""
Write-Host ("✓ 修复完成 — modified: {0}, unchanged: {1}, net bytes: {2:+#;-#;0}" -f $stats.modified, $stats.unchanged, $stats.bytes)
