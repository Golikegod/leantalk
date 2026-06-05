# Leantalk Design System

> AI 时代的设计规范 — 让 AI 生成的每个页面，都符合 Leantalk 品牌语言。
> 实施日期：2026-06-05 · 版本：v0.1 草案
> 依据：design-md 技能 M1-M9 框架 + web-design v1.1 规范

---

## M1 — Visual Theme & Atmosphere

Leantalk 的视觉气质：

- **核心关键词**：工业 × 知性 × 实战
- **情绪版**：制造业一线的专业感，但不像传统工业媒体那么冷；像一位懂技术也懂车间的 CIO 朋友
- **设计哲学**：功能清晰，视觉减负；CIO 不需要在 UI 里感到压力，制造业从业者要的是「这能落地」
- **密度**：中等偏低，内容之间留有充分呼吸空间
- **明暗**：整体偏亮（白底 + 灰表面），避免大面积深色带来的距离感

**视觉参照**：
- 气质靠近 Stripe 文档（专业 + 雅致 + 强排版）
- 远离 CSDN 类（信息堆砌 + 杂乱广告）
- 比 Linear 多一分「制造业」暖意，比 Vercel 多一分「内容沉淀」

---

## M2 — Color Palette & Roles

| 角色 | 色值 | OKLCH | 使用场景 |
|------|------|-------|---------|
| **Primary** | `#00C9A7` | `oklch(0.78 0.13 175)` | 主操作、链接激活态、Logo 强调、关键数据高亮 |
| Primary Light | `#1FD9B8` | `oklch(0.82 0.13 175)` | Hover 态、次级强调 |
| Primary Dark | `#00A88A` | `oklch(0.68 0.13 175)` | Active 态、深色背景 |
| **Accent-2** | `#8B5CF6` | `oklch(0.65 0.18 285)` | 知识库类别、AI 相关标签 |
| **Neutral-900** | `#111111` | `oklch(0.15 0 0)` | 标题、Logo、正文强调 |
| Neutral-700 | `#444444` | `oklch(0.35 0 0)` | 正文 |
| Neutral-500 | `#999999` | `oklch(0.62 0 0)` | **⚠ 需调整** — 现 `#999` 对比 2.85:1 不达 AA |
| Neutral-300 | `#E5E5E5` | `oklch(0.88 0 0)` | 边框、分割线 |
| Neutral-100 | `#F7F7F7` | `oklch(0.96 0 0)` | 次级表面、文章页引用块背景 |
| Neutral-50 | `#FAFAFA` | `oklch(0.98 0 0)` | 卡片底色 |
| **Surface-0** | `#FFFFFF` | `oklch(1 0 0)` | 全局背景、卡片 |
| **Semantic-Danger** | `#E53E3E` | `oklch(0.62 0.22 25)` | hot-high 热门标签 |
| Semantic-Warning | `#C2410C` | `oklch(0.58 0.18 50)` | hot-medium 中等热度 |
| Semantic-Success | `#00A88A` | `oklch(0.68 0.13 175)` | 完成态、成功提示 |

**对比要求**：
- 正文 vs 背景：≥ 4.5:1 (WCAG AA)
- text-muted (现 `#999`) 必须改 `#777` 以上，对比 ≥ 4.5:1
- 大字 / UI 元件：≥ 3:1

**暗色模式**（`@media (prefers-color-scheme: dark)`）：
- 背景：`oklch(0.16 0 0)` (近黑)
- 表面：`oklch(0.22 0 0)` (卡片)
- 文字：`oklch(0.96 0 0)` (白)
- muted：`oklch(0.72 0 0)` (浅灰)
- Accent 保持 `#00C9A7`，暗背景对比度更佳

---

## M3 — Typography Rules

### 字体族

```css
--font-zh: 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'Noto Sans SC', sans-serif;
--font-en: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', ui-monospace, monospace;
```

**规则**：
- 中文内容统一用 `--font-zh`（无衬线，UI 友好）
- 数字、英文标题用 `--font-en`
- 代码块用 `--font-mono`
- **禁止**：宋体、楷体、苹方以外的衬线（杂志感）用于正文

### 字号层级（1.25 比率，major third）

| 层级 | 字号 | 字重 | 行高 | 字间距 | 用途 |
|------|------|------|------|--------|------|
| Hero | `clamp(2.25rem, 5.5vw, 4.25rem)` | 800 | 1.12 | -0.025em | 首页主标题 |
| H1 | `clamp(1.5rem, 4vw, 2.25rem)` | 800 | 1.2 | -0.015em | 文章页大标题 |
| H2 | `1.25rem` (20px) | 700 | 1.4 | -0.01em | 文章章节、模块标题 |
| H3 | `1.125rem` (18px) | 800 | 1.3 | -0.008em | 卡片标题 |
| Body | `1rem` (16px) | 400 | 1.7 | 0 | 正文 |
| Body-sm | `0.875rem` (14px) | 400 | 1.65 | 0 | 卡片摘要、元信息 |
| Caption | `0.8125rem` (13px) | 400 | 1.5 | 0 | 标签、辅助说明 |
| XS | `0.6875rem` (11px) | 700 | 1.4 | 0.15em (uppercase) | 类别标签、eyebrow |

**规则**：
- 标题用负字间距压缩感（-0.5px ~ -1px）
- 正文保持标准字间距
- 正文 16px 起步，最小 14px

---

## M4 — Component Stylings

### 4.1 按钮 (Button)

```
主按钮 (btn-primary)        次按钮 (btn-ghost)         链接 (link)
Default: bg=#111,text=#fff   Default: bg=transparent,    Default: text=#00C9A7
                              border=1.5px #E5E5E5
Hover:   bg=#333,shadow      Hover:   border=#00C9A7,    Hover:   underline
                              text=#00C9A7
Active:  scale(0.98)         Active:  bg=#00C9A710       Active:  opacity 0.8
Focus:   ring 2px #00C9A7    Focus:   ring 2px #00C9A7   Focus:   ring 2px #00C9A7
Disabled: opacity 0.4        Disabled: opacity 0.4       Disabled: 灰色禁用
Loading:  spinner + 灰文字
```

**Token**：
- padding: `0.875rem 2rem` (14px 32px)
- border-radius: `0.625rem` (10px)
- font-size: 15px / font-weight: 600
- letter-spacing: -0.2px

### 4.2 卡片 (Card)

```
article-card / kb-card / skill-card
Default:  bg=Surface-0, border=1px Neutral-300, radius=14px
Hover:    translateY(-3px), shadow=hover, border-color=#00C9A740
Active:   scale(0.99)
Focus:    ring 2px #00C9A7
Padding:  1.75rem 1.75rem 1.5rem (28/28/24)
```

**内部层级**：
- Eyebrow: 11px uppercase `#00C9A7`
- 标题: 18px 800
- 摘要: 13px muted 1.65 行高, 3 行截断 (`-webkit-line-clamp: 3`)
- Meta: 12px muted，分隔用 `<span class="dot">` (3px 圆点)

### 4.3 导航 (Navbar)

- sticky top-0, height 64px
- bg: `rgba(255,255,255,0.97)` + `backdrop-filter: blur(8px) saturate(180%)`
- 边框: `1px solid Neutral-300`
- Logo: 18px 800, `<span>` 部分用 accent 色
- 链接: 14px 500 muted, hover 变主色
- 移动端: `<details>` 汉堡菜单 (0 JS)

### 4.4 标签 / 类别 (Tag)

```
.article-tag (文章)         .kb-tag (知识库)              hot-tag (资讯)
Default: text=#00C9A7       Default: text=#8B5CF6         high:   bg=#fff0f0 text=#E53E3E
                              bg=#8B5CF615,                 medium: bg=#fff7ed text=#C2410C
                              border=#8B5CF640              low:    bg=#f7f7f7 text=#999
Padding: 3-6px 8-12px
Radius:  100px (pill)
Font:    11px 700, letter-spacing 1.5px uppercase
```

### 4.5 输入 (Input)

```
Default: bg=white, border=1px #E5E5E5, radius=10px
Hover:   border=#999
Focus:   border=#00C9A7, ring=2px #00C9A720
Error:   border=#E53E3E, ring=2px #E53E3E20
Padding: 0.75rem 1rem
Font:    15px 400
```

---

## M5 — Layout Principles

### 间距系统（8px 基准）

| Token | 值 | 用途 |
|-------|-----|------|
| `--space-1` | 4px | 图标与文字 |
| `--space-2` | 8px | 紧凑间距 |
| `--space-3` | 12px | 标准元素 |
| `--space-4` | 16px | 默认间距 |
| `--space-6` | 24px | 卡片内 |
| `--space-8` | 32px | 区块内 |
| `--space-12` | 48px | 区块间 |
| `--space-16` | 64px | 大区块 |
| `--space-24` | 96px | Section padding |

### 页面布局

| 区块 | 最大宽度 | 水平内边距 |
|------|---------|----------|
| 首页 section | `min(90vw, 78rem)` (≈1100px) | 24px |
| 文章页正文 | 860px | 48px (桌面) / 20px (移动) |
| Hero 标题 | 780px | — |
| Hero 副标题 | 520px | — |
| CTA 卡片 | 320px | 40px 48px |

### 网格

- 卡片网格：`grid-template-columns: repeat(auto-fit, minmax(min(100%, 20rem), 1fr))`
- gap: 20px (1.25rem)
- 桌面端 2-3 列，移动端 1 列自动堆叠

### 节奏

- Section padding: `clamp(3.75rem, 5vw + 2rem, 6rem)` (60-96px)
- Section 标题区下边距: 40px

---

## M6 — Depth & Elevation

| Level | 用途 | 样式 |
|-------|------|------|
| L0 | 默认无层级 | 无 |
| L1 | 卡片默认 | `0 2px 8px rgba(0,0,0,0.06)` |
| L2 | 卡片 hover / 按钮 hover | `0 4px 20px rgba(0,0,0,0.10)` |
| L3 | Modal / Popover | `0 10px 40px rgba(0,0,0,0.15)` |
| L4 | Toast / Notification | `0 20px 60px rgba(0,0,0,0.20)` |

**规则**：
- 阴影 opacity 不超过 0.2（制造业专业感）
- 优先用 border + 表面色区分层级
- 暗色模式阴影更深（opacity 0.4+）以在黑底可见

---

## M7 — Do's and Don'ts

### ✅ 正确做法

- 用 Primary 绿（`#00C9A7`）做主操作
- 链接、Logo 强调、关键数据用 accent
- 卡片内 padding 28/28/24，标题区用 eyebrow
- 用 `<span class="dot">` (3px 圆点) 作元信息分隔
- 移动端文字 ≥ 14px，正文 16px
- 所有交互元素有 focus-visible 状态

### ❌ 错误做法

- 禁用 **蓝色** 作主色（与品牌绿冲突）
- 禁用 **大面积深色**（CIO 群体偏好明亮）
- 禁用 **纯黑** `#000000` 正文（用 `#111` 减少压迫感）
- 禁用 **`transition: all`**（性能问题，违反 web-animation-design 性能金律）
- 禁用 **`filter: blur()` 循环动画**（Safari 卡顿）
- 禁用 **Emoji 作 UI 图标**（跨平台渲染不一，改用 SVG / 字符符号）
- 禁用 **无 `prefers-reduced-motion` 的动画**
- 禁用 **嵌套 `<a>`**
- 禁用 **`<h*>` 跳级**（h1 → h3）

---

## M8 — Responsive Behavior

### 断点

| 断点 | 宽度 | 设备 |
|------|------|------|
| `sm` | 640px | 手机横屏 / 小平板 |
| `md` | 900px | 平板竖屏 |
| `lg` | 1200px | 桌面 |
| `xl` | 1440px | 大屏 |

### 关键适配

| 元素 | 移动端 (< 640px) | 桌面端 (≥ 640px) |
|------|----------------|------------------|
| Navbar | `<details>` 汉堡菜单 | 横向 5 链接 |
| Hero 字号 | 36px | 68px |
| Hero 高度 | 80vh | 80vh (可减到 70vh) |
| Section padding | 60px 20px | 96px 24px |
| 卡片网格 | 1 列 | 2-3 列 |
| 文章页 padding | 20px | 48px |
| CTA 卡片 padding | 24px | 40px 48px |
| 字号 headline | `clamp(2.25rem, ...)` | `clamp(2.25rem, 5.5vw, 4.25rem)` |

### 流体技术

```css
/* 字号流体 */
h1 { font-size: clamp(2.25rem, 1.5rem + 2.5vw, 4.25rem); }

/* 间距流体 */
section { padding-block: clamp(3.75rem, 1rem + 4vw, 6rem); }

/* 容器查询（组件级别响应） */
@container (max-width: 600px) { .card { ... } }
```

### 触控热区

- 最小 `44 × 44px`
- 移动端按钮 padding 加大到 `12px 20px`

---

## M9 — Agent Prompt Guide

### AI 生成页面的快速参考

> "请按 Leantalk 规范生成页面：
> - 颜色：Primary `#00C9A7`，Accent-2 `#8B5CF6`，文字 `#111`，muted `#777`（不是 `#999`）
> - 字体：`PingFang SC`（中文），`-apple-system`（英文），JetBrains Mono（代码）
> - 字号：Hero `clamp(2.25rem, 5.5vw, 4.25rem)`，正文 16px/1.7
> - 圆角：卡片 14px，按钮 10px，输入框 10px
> - 间距：8px 基准 token，section padding 96px
> - 阴影：L1 卡片 `0 2px 8px rgba(0,0,0,.06)`，L2 hover `0 4px 20px rgba(0,0,0,.10)`
> - 动效：transition 列具体属性（禁 `all`），`ease-out` 入场 200-300ms，hover 150ms
> - 媒体查询：3 断点 640/900/1200，移动端 nav 用 `<details>`
> - 不要：深色大面积、纯黑正文、蓝色主色、`transition: all`、无 reduced-motion 动画"

### CSS 速查 (vanilla)

```css
.btn-primary {
  background: var(--color-text);
  color: white;
  padding: 0.875rem 2rem;
  border-radius: 0.625rem;
  font-weight: 600;
  transition: transform 200ms ease-out, box-shadow 200ms ease-out, background-color 200ms ease;
}
.btn-primary:hover { transform: translateY(-1px); box-shadow: var(--shadow-hover); }
.btn-primary:active { transform: scale(0.98); }
.btn-primary:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }

.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 1rem;
  transition: transform 200ms ease-out, box-shadow 200ms ease-out, border-color 200ms ease;
}
.card:hover { transform: translateY(-3px); box-shadow: var(--shadow-hover); border-color: var(--color-accent-soft); }
```

### 动效安全 (强制)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## 实施路线图

| 阶段 | 内容 | 状态 |
|------|------|------|
| **0** | P0 必修（4 处 mojibake + news URL + JSON 引号 + lint） | ✅ 2026-06-05 commit `e5651be` |
| **1** | DESIGN.md 草案 | ✅ 2026-06-05 (本文件) |
| **2** | 抽 `assets/styles/tokens.css` + `base.css` + `components.css` | 📋 待立项 |
| **3** | 改造 15 页面用 `<link>` 共享 CSS | 📋 待立项 |
| **4** | 补全组件 6 态 + focus-visible + reduced-motion | 📋 待立项 |
| **5** | 显式字体声明 + 可选自托管 Noto Sans SC 子集 | 📋 待立项 |
| **6** | 修 hot-tag / text-muted 对比度达 AA | 📋 待立项 |
| **7** | 移动端 navbar 汉堡 + scroll-reveal + TOC + 进度条 | 📋 待立项 |
| **8** | WebP/AVIF + responsive images + 暗色模式 | 📋 待立项 |

---

*🦞 Leantalk 设计系统 v0.1 · 草案 · 待老板裁决后正式生效*
