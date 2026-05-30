# Leantalk 网站迭代维护项目

## 基本信息

- **项目编号：** 20260003
- **项目名称：** Leantalk 网站迭代维护
- **创建时间：** 2026-05-30
- **状态：** 进行中
- **技术栈：** 静态网页（Cloudflare Pages 托管）

## 站点信息

- **域名：** www.leantalk.cn
- **托管平台：** Cloudflare Pages
- **Cloudflare 项目名：** leantalk
- **Cloudflare 项目ID：** `309d2ec0-3bc5-4951-bd58-3517f24d5e81`
- **生产部署地址：** https://eec262cc.leantalk.pages.dev
- **最新部署：** 2026-05-26（共32次部署）
- **部署方式：** 直接上传（非GitHub CI）
- **DNS：** 需验证 NS 记录

## Cloudflare 凭证

- **Account ID：** `900746d2bd673e683e84eeb58afd1f5b`
- **API Token：** 已安全存储（不写入本文档）

## 技术栈

- **形式：** 静态网页
- **框架：** 待确认
- **源码：** 待确认（未找到历史记录）

## 迭代计划

### Phase 1：现状摸底（当前）
- [x] 验证 Cloudflare 站点连接
- [x] 确认技术栈（纯静态 HTML + 动态 JSON 加载）
- [x] 确认源码结构（article_list.json + article/*.html）
- [x] 确认部署方式（直接上传，无GitHub集成）
- [ ] **关键：源码下落不明——需建立GitHub仓库**
- [ ] 确认自定义域名绑定状态

### Phase 2：源码重建 + 自动化（进行中）
- [ ] 创建 GitHub 私有仓库 leantalk
- [ ] 将现有前端源码迁入 Git
- [ ] 配置 GitHub Actions → Cloudflare Pages 自动化部署
- [ ] 整合发布 SOP（Markdown → 自动化构建）

### Phase 3：内容迭代
- [ ] 文章发布流程优化
- [ ] 配图生成流程整合（article-images-gen）
- [ ] 微信公众号发布自动化（wechat-article-publisher）

## 相关文档

- [站点检查报告](./reports/site-audit-20260530.md)

## Cloudflare 凭证

- **Account ID：** `900746d2bd673e683e84eeb58afd1f5b`
- **API Token：** 已安全存储
- **GitHub PAT：** MEMORY.md 中的 `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`

---

*🦞 项目由龙虾5号管理，最后更新 2026-05-30*