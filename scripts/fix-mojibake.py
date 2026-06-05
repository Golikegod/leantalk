#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leantalk 文章页 mojibake 批量修复
根因：源文件曾以 GBK 写入后被 UTF-8 读取，渲染时出现"路"(U+8DEF)/"鈫?"/"闈㈠悜..."/"aram" 错位
修复：以 UTF-8 (无 BOM) 写回正确字符
"""
import os
import sys
import io
from pathlib import Path

# 强制 stdout/stderr 为 UTF-8（Windows 默认 GBK）
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "src" / "article"

REPLACEMENTS = {
    "路": "\u00b7",                                       # ·
    "鈫?": "\u2190",                                      # ←
    "杩斿洖棣栭〉": "返回首页",
    "闈㈠悜鍒堕€犱笟鐨凙I瀹炴垬鐭ヨ瘑骞冲彴": "面向制造业的 AI 实战知识平台",
    "操作员不知道aram 的数据怎么用": "操作员不知道系统的数据怎么用",
}


def fix_file(path: Path) -> tuple[int, int]:
    raw = path.read_bytes()
    # 去掉 BOM
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
        had_bom = True
    else:
        had_bom = False
    text = raw.decode("utf-8")
    original = text
    for k, v in REPLACEMENTS.items():
        text = text.replace(k, v)
    if text == original:
        return (0, 0)
    out = text.encode("utf-8")
    if had_bom:
        out = b"\xef\xbb\xbf" + out
    # 保留原文件末尾换行
    if raw.endswith(b"\n") and not out.endswith(b"\n"):
        out += b"\n"
    delta = len(out) - len(raw)
    path.write_bytes(out)
    return (1, delta)


def main() -> int:
    if not ARTICLES.is_dir():
        print(f"✗ 目录不存在: {ARTICLES}", file=sys.stderr)
        return 1
    files = sorted(ARTICLES.glob("*.html"))
    modified = 0
    unchanged = 0
    net_bytes = 0
    print(f"扫描 {len(files)} 个 HTML 文件于 {ARTICLES}\n")
    for f in files:
        m, d = fix_file(f)
        if m:
            modified += 1
            net_bytes += d
            sign = "+" if d >= 0 else ""
            print(f"  [EDIT] {f.name:<48}  {sign}{d} B")
        else:
            unchanged += 1
    print(
        f"\n[OK] 修复完成 -- modified: {modified}, unchanged: {unchanged}, net bytes: {net_bytes:+d}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
