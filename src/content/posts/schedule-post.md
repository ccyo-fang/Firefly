---
title: 给博客做定时发布
published: 2026-10-26
description: 静态站没有定时发布功能，我用 GitHub Actions 每天跑一次，把到期的草稿自动转正。
tags: ['技术', '自动化', '博客']
category: 技术
slug: schedule-post
pinned: false
comment: true
draft: false
---
## ⏰ 需求

想提前写好一堆文章，按日期一篇篇放出来，而不是写完立刻推。

静态博客没有这个功能——它只在构建那一刻决定有哪些页面，**未来日期的文章会立刻显示**，不会等到那天。

## 🧩 思路

主题支持 `draft: true`，草稿在生产构建时被排除（本地预览仍可见）。

所以问题变成：**怎么让 draft 在指定日期自动变成 false**。

答案是定时任务。

## 🛠 实现

两部分：

**1. 脚本**：扫描 `src/content/posts/`，找出 `draft: true` 且 `published` 日期已到（北京时间）的文章，改成 `draft: false`。

**2. GitHub Actions**：每天定时（比如北京时间 8 点和 20 点）跑一次脚本，如果有改动就自动 commit 并 push。

push 之后，Cloudflare 会自动触发构建，文章就上线了。

## ⚙️ 几个细节

- **时区**：Actions 的 cron 用的是 UTC，北京时间要减 8 小时
- **权限**：workflow 要显式声明 `permissions: contents: write`，否则提交会被拒
- **幂等**：没有到期文章时不要产生空提交，加个 `git diff --quiet` 判断
- **手动触发**：加上 `workflow_dispatch`，想立刻发某篇时手动点一下就行

## 🪵 好处

现在我一次写一批，设好日期，之后的三十天什么都不用管。

写作和发布解耦了——**写的时候集中写，发的时候自动发**。
