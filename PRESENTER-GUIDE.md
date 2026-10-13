# Part 2 讲解稿（mentor TA 用，hanzhen3）

用这个仓库在 team meeting 上给 Atomic / Symbol（10-13 周二）和 Gambit（10-14 周三）讲 Part 2
交付物。全程约 20 分钟，讲完直接按 `CHECKLIST.md` 过他们自己的仓库。

截止：2026-10-20 周二 17:00。Peer review：10-21 17:00，每人单独填。评分 0/2/3/4/5，无部分分。

## 0. 开场（1 分钟）

打开仓库的 **Wiki 标签页**（https://github.com/HozierDdd/CMPUT301-final/wiki），这就是学生要交的形式；`wiki/` 文件夹是源文件，改完用 `scripts/sync_wiki.sh` 同步。说三句话：
- Part 2 不写代码，交四样东西：backlog、mockup + storyboard、CRC 卡、GitHub 使用记录。
- 全部放在团队仓库的 wiki 里，图必须嵌进去，不能只给 Figma 链接。
- 评分最看重**一致性**：同一条 US 在三处用同一个编号，同一个概念用同一个名字。

Home 页顺便指一下"角色分工表"和"统一词汇"两块，让他们回去照抄结构。

## 1. Product backlog（5 分钟）

打开 `wiki/Product-Backlog.md`。
- 页首：总数 66 条、32 条 halfway、story point 标尺一句话。强调标尺写出来就行，数字本身不评分。
- 表格：每行 = 一条 US，列是 编号 / 原文 / points / risk / halfway / 负责人 / 屏幕 / issue。
  指一下 `-->` 的 6 条标成 optional，不放 halfway。
- "为什么这些进 halfway"那段：Part 3 要能跑通整条抽签链路 + Firestore，所以选的是
  设备登录 → 登记营地 → 发抽签 → 搜索/扫码 → 加入等待列表 → 自动抽签 → 通知 → 确认/拒绝。
- 翻到 `.github/ISSUE_TEMPLATE/user-story.md`：一条 issue 该有的五块内容。
  再打开 `scripts/create_issues.sh` 看两行，说明 label 体系：`role:*`、`risk:*`、`halfway`、`optional`、`task`。
- 常见错误：只建了 entrant 的 30 条；risk 写成数字；几条 US 合并成一个 issue；看板是空的。

练习：随机报一条 US（比如 02.04.07），让他们在自己的 issues 里找。

## 2. Mockup + Storyboard（6 分钟）

打开 `wiki/UI-Mockups.md`，滚到 M4（营地详情）和 M7（中签选日期）。
- 每张图下面两样东西：红圈编号对应的注释、Covers 的 US 列表。低保真就够，要的是"有什么控件、在哪"。
- M4 的第 5/6 点：Join 和 Leave 两个状态都画出来，mockup 是文档，不是截图。

打开 `wiki/Storyboards.md`：
- S1：方框 = 屏幕（带 M 编号和 US），**箭头上必须写动作**（taps 'Join waiting list'）。
  指"registration closes; system draws winners"那条：系统事件也是转换，要画出来。
- S2 的黄色 note：抽签是系统自动做的，不是 owner 点按钮。
- 拉到最后"bad storyboard"：没编号、没 US、箭头没字。这是本项最常见的扣分点。

打开 `wiki/US-to-Screen-Traceability.md`：66 条每条至少一个屏幕、一个 storyboard，
底部 "Stories with no screen: 0"。这张表是拿高分最省力的证据。

## 3. CRC 卡（5 分钟）

打开 `wiki/CRC-Cards.md`。
- 先看 Lottery 卡的 PNG：职责是动作（"期满后随机抽 N 个赢家"），协作者是领域类。
- 再看 bad example：字段列表 + FirebaseFirestore / ViewModel 当协作者。Part 2 不要界面类、不要数据库类。
- 协作关系图：每条线两张卡上都要有。让他们回去用这个方法互查。
- WaitingList 卡下面那句：等待列表 = 抽签报名池，不是"满员候补"。三个队都可能理解错，点名问一句。
- 顺带说：这些卡 Part 3 直接变 UML 类图，现在想清楚省后面的事。

## 4. Tool use（2 分钟）

打开 `wiki/Tool-Use.md`：
- 每人用自己账号提交，TA 按人查 commit 和 wiki 编辑记录。
- 禁 rebase / force push，`git config --global pull.rebase false`。
- `.gitignore` 现在就放好，Part 3 的 google-services.json 不能进仓库。
- 用了 AI 要在 README 里写（本仓库 README 最后一段就是示例）。

## 5. 收尾（1 分钟）

打开 `CHECKLIST.md`，告诉他们下周我就按这张表过。做"十秒测试"：随机报一条 US，
让某个成员在 10 秒内指出 issue、屏幕上的按钮、负责的类。

本周 meeting 顺手检查（来自 10-06 的计划）：backlog 初版是否在 issues 里；mockup 工具定了没；
CRC 草稿有没有；每人是否至少分到一条 issue；记考勤。

## 备注

- 仓库里的 issues 和看板没有真的建出来（demo 仓库没装 gh）。讲 issues 时直接开某个队自己的
  仓库，或者课前在本机 `gh auth login` 后跑 `bash scripts/create_issues.sh HozierDdd/CMPUT301-final`。
- 学生问"要画多少张"：按 M1–M18 的清单，三类角色主要页面 + 主要对话框，18 张左右；少于 10 张基本盖不住 66 条。
- 学生问 story point 怎么估：不评估得准不准，评有没有标尺、团队内部是否一致。
