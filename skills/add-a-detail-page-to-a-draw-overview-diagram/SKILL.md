---
name: add-a-detail-page-to-a-draw-overview-diagram
description: "Human-readable addition of one separate Draw detail page for an overfull branch while keeping the first page as a readable overview."
---
# 给 Draw 总览流程另加一张细节页 / Add a Detail Page to a Draw Overview Diagram

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 15–25 分钟 / 15–25 minutes |
| Requirements / 必要物品 | 已有普通流程总览 ODG 副本、一个需展开的已知分支 / Ordinary overview ODG copy and one known branch needing detail |
| Side effects / 现实副作用 | 总览不拥挤，细节页有对应入口与返回线索 / Overview stays clear and detail page has a matching reference |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

你的一张 Draw 总览图因一条分支细节太多而读不清，想让首页只保留入口并在第二页展开时使用本篇。成果是第一页仍显示整体路径、细节页清楚标出它解释哪一分支，两页没有相互矛盾的步骤。它不是为了计数而复制整张图。

### 准备与输入

保存 ODG 副本，指出要展开的分支入口及哪些节点留在总览、哪些转细节。写下细节页标题和与入口完全一致的短标识。检查页窗格已有页面数，计划新页放在总览后。

### 执行

1. 在 Pages pane 选总览页，使用 Page > New Page 建第二页，命名为该分支细节。
2. 在总览入口放简短“详见第 2 页/对应名称”线索，别把主流程切断。
3. 在新页只展开该分支的真实步骤，用同一入口名称，并核结果能回到总览所示出口。
4. 在页窗格来回切换核两页一致与总页数，保存重开；若细节无独立信息就合回总览。

### 完成、常见问题与恢复

总览与细节页各有明确职责，入口/出口对应，原图不因拆页丢关系。

- **第二页只是复制：** 删重复，保留真正展开内容。
- **入口名字不一致：** 用同一短标识修两处。
- **细节没有回路：** 标清该分支结束后去向。

### 假设与边界

只拆一条普通流程细节，不建立正式跨页超链接或业务制度。你负责两页语义一致。

### 来源

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26211-AdvancedDrawTechniques.html)（英文，官方手册）— Draw Pages pane 可在选中页后插入新页并重新命名。
- Original synthesis — 将一个图示结果、原稿对照和失败停点组合为可核流程。

## English

Use this Skill when one branch's detail overcrowds a Draw overview and a separate page would clarify it. Finish with page one still showing the overall route and a second page explicitly tied to that branch, with no contradictory duplicated steps. Do not copy the whole diagram merely to increase page count.

### Preparation and inputs

Save ODG copy. Identify branch entry and which nodes stay in overview versus move to detail. Draft detail title and a short matching identifier shared with entry. Note existing page count and insert detail after overview.

### Execution

1. Select overview in Pages pane, use Page > New Page and name it for branch detail.
2. Place a concise see-detail cue at branch entry without breaking main path.
3. Draw only that branch's real steps on new page with matching entry name and an outcome corresponding to overview exit.
4. Switch between pages for consistency and count, save/reopen; merge back if detail adds no independent information.

### Success, common problems, and recovery

Overview and detail have clear roles, entry/outcome agree and no relation is lost.

- **Second page only duplicates:** Remove redundancy and keep real details.
- **Entry names differ:** Use one shared identifier.
- **No return context:** State next destination.

### Assumptions and limits

This splits one ordinary branch detail, not a formal cross-page link or policy. You own semantic consistency.

### Sources

- [LibreOffice Draw Guide 26.2](https://books.libreoffice.org/en/DG262/DG26211-AdvancedDrawTechniques.html) — Draw Pages pane can insert a page after selected page and rename it.
- Original synthesis — one diagram outcome, original-draft comparison and stop point make a checkable workflow.

If AI opens this file, it may explain Draw controls. You choose the content, perform the steps and verify the result.
