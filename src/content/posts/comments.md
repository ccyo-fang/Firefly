---
title: 静态博客的评论系统怎么选
published: 2026-10-12
description: giscus、Twikoo、Waline、Disqus 各自适合谁，以及我最后为什么选了 giscus。
tags: ['技术', '博客', 'giscus']
category: 技术
slug: comments
pinned: false
comment: true
draft: true
---
## 🤔 问题的起点

静态博客没有后端，所以评论不能存在自己的数据库里。要么找个托管服务，要么借别人的平台。

我把主流的几个都看了一遍。

## 📋 四个选项

**Disqus** —— 老牌，功能全，但广告多、加载慢，国内访问体验很差。基本可以排除。

**Waline** —— 基于 LeanCloud，需要自己部署服务端 + 配数据库。功能强、可定制，但意味着要维护一个后端。

**Twikoo** —— 国内用得多，基于腾讯云开发，部署不算复杂，支持表情和邮件通知。缺点同样是要养一个服务。

**giscus** —— 基于 GitHub Discussions，评论直接存在你自己的仓库里，纯前端，不需要任何服务器。

## ✅ 为什么选 giscus

我的站跑在 Cloudflare 上，纯静态，不想为了个评论框再养一台服务器。

giscus 完全满足：

- 免费，无广告
- 评论数据存在我自己的 GitHub 仓库，随时能导出
- 访客要用 GitHub 账号登录才能留言，天然过滤了大部分垃圾评论
- 国内加载实测 1 秒出头，可以用

## ⚠️ 它的局限

- 访客必须有 GitHub 账号，对非技术读者不友好
- 不能匿名评论
- 样式定制空间有限

如果你的读者主要是普通人，Twikoo 会更合适；如果读者本来就混 GitHub，giscus 是最省心的。

## 🔑 一个容易踩的坑

giscus 用页面标题或 URL 来匹配评论。用**标题**匹配的话，哪天你改了站点副标题，所有文章的评论会集体失联。

所以务实用 `mapping: "pathname"` —— 靠 URL 匹配，文章链接不变就永远在。
