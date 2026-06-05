#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leantalk 内容守卫（pre-commit / pre-deploy 必跑）
检查项：
  1. JSON 文件可解析 + 不含 ASCII U+0022 直引号（应用全角「」或转义 \\"）
  2. HTML 文件不含已知 mojibake 特征字符
  3. HTML 文件不含禁用模式（如 transition: all）
  4. HTML 文件使用 UTF-8 编码
退出码：发现问题为 1，全过为 0
"""
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

# 已知 mojibake 串（曾在仓库中真实出现）
MOJIBAKE_PATTERNS = [
    ("路 (· 的 GBK 错位)", "路"),
    ("鈫? (← 的 GBK 错位)", "鈫?"),
    ("杩斿洖棣栭〉 (返回首页 错位)", "杩斿洖棣栭〉"),
    ("闈㈠悜... (面向制造业 错位)", "闈㈠悜鍒堕€犱笟鐨凙I瀹炴垬鐭ヨ瘑骞冲彴"),
    ("aram (系统的 mojibake)", "aram 的数据怎么用"),
]

# 禁用模式（web-animation-design 性能金律）
FORBIDDEN_CSS_PATTERNS = [
    (r"transition\s*:\s*all\b", "transition: all 触发性能问题，只动 transform/opacity"),
    (r"@keyframes\s+[^{]*\b(blur|filter)\s*\(", "blur/filter 动画开销大，避免循环动画"),
]

# 字符编码白名单
ALLOWED_HTML_ENCODINGS = {"utf-8", "utf8"}


def check_json(path: Path) -> tuple[list[str], list[str]]:
    """返回 (errors, warnings)"""
    errors = []
    warnings = []
    try:
        raw = path.read_bytes()
    except Exception as e:
        errors.append(f"[{path.name}] 读取失败: {e}")
        return errors, warnings
    # 编码 — 用 utf-8-sig 自动剥离 BOM
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        errors.append(f"[{path.name}] 非 UTF-8 编码: {e}")
        return errors, warnings
    # 解析
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        errors.append(f"[{path.name}] JSON 解析失败: {e}")
        return errors, warnings
    # 内容中含 ASCII 直引号风险
    if '"' in text:
        def walk(obj, trail=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    walk(v, f"{trail}.{k}" if trail else k)
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    walk(v, f"{trail}[{i}]")
            elif isinstance(obj, str):
                if '"' in obj:
                    errors.append(
                        f"[{path.name}] {trail} 字符串内含 ASCII U+0022 直引号 — 改用「」或 \\\""
                    )
        walk(data)
    return errors, warnings


def check_html(path: Path) -> tuple[list[str], list[str]]:
    """返回 (errors, warnings)"""
    errors = []
    warnings = []
    try:
        raw = path.read_bytes()
    except Exception as e:
        errors.append(f"[{path.name}] 读取失败: {e}")
        return errors, warnings
    # 编码 — utf-8-sig 自动剥离 BOM
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as e:
        errors.append(f"[{path.name}] 非 UTF-8 编码: {e}")
        return errors, warnings
    # mojibake (ERROR)
    for label, pat in MOJIBAKE_PATTERNS:
        if pat in text:
            errors.append(f"[{path.name}] 含 mojibake: {label}")
    # 禁用模式 (WARNING) — 性能类问题，不阻断
    for pat, why in FORBIDDEN_CSS_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            warnings.append(f"[{path.name}] [WARN] {why}")
    return errors, warnings


def main() -> int:
    if not SRC.is_dir():
        print(f"[ERROR] 源目录不存在: {SRC}", file=sys.stderr)
        return 1
    all_errors: list[str] = []
    all_warnings: list[str] = []
    json_files = sorted(SRC.rglob("*.json"))
    html_files = sorted(SRC.rglob("*.html"))
    print(f"扫描 {len(json_files)} JSON + {len(html_files)} HTML 文件于 {SRC}\n")
    for f in json_files:
        e, w = check_json(f)
        all_errors.extend(e)
        all_warnings.extend(w)
    for f in html_files:
        e, w = check_html(f)
        all_errors.extend(e)
        all_warnings.extend(w)
    if all_warnings:
        print(f"[WARN] {len(all_warnings)} 个性能/风格告警（不阻断）:")
        for s in all_warnings:
            print(f"  ~ {s}")
        print()
    if all_errors:
        print(f"[FAIL] {len(all_errors)} 个错误（必须修）:")
        for s in all_errors:
            print(f"  x {s}")
        return 1
    print(f"[OK] {len(json_files)} JSON + {len(html_files)} HTML 全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
