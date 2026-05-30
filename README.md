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

## 技术栈

- **形式：** 静态网页
- **框架：** 纯静态 HTML + 动态 JSON 加载
- **源码：** 已下载至 `src/` 目录，共32个文件

## 迭代计划

### Phase 1：现状摸底
- [x] 验证 Cloudflare 站点连接
- [x] 确认技术栈（纯静态 HTML + 动态 JSON 加载）
- [x] 确认源码结构（article_list.json + article/*.html）
- [x] 确认部署方式（直接上传，无GitHub集成）
- [x] 下载全站源码至 `src/` 目录
- [ ] 确认自定义域名绑定状态

### Phase 2：GitHub 仓库重建（进行中）
- [x] 创建 GitHub 公开仓库 leantalk
- [x] 导入全站源码
- [x] 配置 GitHub Actions → Cloudflare Pages 自动化部署
- [ ] **待修复：** 首次 commit 含 PAT，需重建干净 history
- [ ] 配置 GitHub Secrets（CLOUDFLARE_API_TOKEN + CLOUDFLARE_ACCOUNT_ID）

### Phase 3：内容迭代
- [ ] 文章发布流程优化
- [ ] 配图生成流程整合（article-images-gen）
- [ ] 微信公众号发布自动化（wechat-article-publisher）

## 相关文档

- [站点检查报告](./reports/site-audit-20260530.md)

---

*🦞 项目由龙虾5号管理，最后更新 2026-05-30*