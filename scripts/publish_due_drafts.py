#!/usr/bin/env python3
"""定时发布：把「已到期」的草稿文章自动转正。

规则：
  - 扫描 src/content/posts/ 下的所有 .md / .mdx
  - frontmatter 中 draft: true 且 published <= 今天（北京时间）→ 改为 draft: false
  - 其余文件一律不动

改动后由 workflow 提交回仓库，Cloudflare 会自动触发重新构建，文章即上线。
"""

import os
import re
import sys
from datetime import datetime, timedelta, timezone

POSTS_DIR = "src/content/posts"
TZ = timezone(timedelta(hours=8))


def main() -> int:
    today = datetime.now(TZ).strftime("%Y-%m-%d")
    print(f"今天（北京时间）: {today}")

    if not os.path.isdir(POSTS_DIR):
        print(f"目录不存在: {POSTS_DIR}")
        return 1

    changed = []
    for root, _dirs, files in os.walk(POSTS_DIR):
        for fn in files:
            if not fn.endswith((".md", ".mdx")):
                continue
            path = os.path.join(root, fn)
            src = open(path, encoding="utf-8").read()

            m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", src, re.S)
            if not m:
                continue

            fm = m.group(1)
            if not re.search(r"^\s*draft:\s*true\s*$", fm, re.M):
                continue

            dm = re.search(r"^\s*published:\s*(.+?)\s*$", fm, re.M)
            if not dm:
                print(f"  跳过（draft 但无 published 日期）: {path}")
                continue

            pub = dm.group(1).strip().strip("\"'")
            if len(pub) > 10:  # 兼容带时间的写法，只取日期部分
                pub = pub[:10]

            if pub <= today:
                new_fm = re.sub(r"^\s*draft:\s*true\s*$", "draft: false", fm, flags=re.M)
                new_src = src[: m.start(1)] + new_fm + src[m.end(1) :]
                if new_src != src:
                    open(path, "w", encoding="utf-8", newline="").write(new_src)
                    changed.append((path, pub))

    if changed:
        print(f"\n本次发布 {len(changed)} 篇：")
        for path, pub in changed:
            print(f"  ✅ {path}（计划发布日 {pub}）")
    else:
        print("\n没有到期需要发布的草稿。")

    return 0


if __name__ == "__main__":
    sys.exit(main())
