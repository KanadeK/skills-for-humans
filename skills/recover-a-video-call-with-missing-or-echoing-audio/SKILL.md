---
name: recover-a-video-call-with-missing-or-echoing-audio
description: "Human-readable UI-level recovery during an ordinary video call with missing audio or echo, ending in a short two-way test or a permitted text/phone fallback."
---
# 视频通话无声或有回声时先恢复交流 / Recover a Video Call with Missing or Echoing Audio

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Moderate / 中等 |
| Time / 预计时间 | 2–5 分钟检查，再决定降级 / 2–5 minutes to check, then downgrade if needed |
| Requirements / 必要物品 | 正在进行的普通通话、应用音频设置、可用的文字或电话渠道 / Ordinary live call, app audio controls, available text or phone route |
| Side effects / 现实副作用 | 你会暂停一小段对话，换回能听懂的话 / A brief pause may restore intelligible conversation |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当一次普通视频通话已经开始，你听不到别人、别人听不到你，或回声让交流困难时，加载这份 Skill。目标是**用当前应用和设备界面找出音频方向问题，做少量可逆检查，恢复双向交流或及时改用允许的文字/电话方式**。会前自检是另一任务；反复掉线属于网络参与恢复。

只做用户界面里能看见的低风险动作。不运行终端命令、不改驱动、不拆设备、不要求别人交账号，也不把某个平台的高级会议室功能当作所有人都有。若这次通话有特殊安全或正式调度要求，遵守主办方渠道。

### 准备与输入

先用聊天或简短手势告诉对方“我在查声音，稍等两分钟”，如果有此渠道。确认是**你听不到他们**、**他们听不到你**、**双方都无声**，还是**回声**；问一个其他参与者看到的情况，别一边乱调三台设备一边让全员猜。记住当前选中的麦克风和扬声器，便于改回。

### 执行

1. **先排静音与方向。** 看应用内麦克风是否静音，耳机或设备上是否另有静音；音量是否关到零。只改与你的症状有关的一项。若大家都听不到同一个人，而其他人互相听得见，也可能是那个人的输入，不强行改你自己的系统。
2. **你听不到时查输出。** 在通话应用的音频设备菜单看“扬声器/输出”是否指向耳机、蓝牙或实际能听到的设备。选正确输出，使用应用允许的测试声或请对方说一句短话。不要因显示器被选为扬声器就提高所有系统音量到刺耳程度。
3. **别人听不到你时查输入。** 看“麦克风/输入”是否选了实际设备，应用里的输入指示是否在说话时动；检查可见的权限提示和应用/硬件静音。改一项再请一人反馈，避免几个人同时说“现在呢”。
4. **有回声时减少重复音频路径。** 同一个房间若两台设备同时开麦与扬声器，请有权操作者让其中一台静音或退出其音频；能用耳机就用耳机，或适当降低扬声器音量、非发言时静音。不要随便静音远方所有人来掩盖本地回授。
5. **做一次双向短测。** 你说一句，对方复述关键字；对方说一句，你复述。双方能听懂且回声不再妨碍，才回到正常通话。输入条动、你听到测试音或一人说“好了”，都不足以证明双向已通。
6. **到时间就降级并通知。** 两三分钟仍不通时，在可用聊天里说明“我的音频仍不可用，接下来用 [实际可用的文字/电话方式]”；若邀请中允许电话拨入，用电话做唯一活跃音频端，并关闭另一设备的会议音频以免再生回声。没有备用渠道就请组织者改期，不继续占用整场。

### 完成条件

两边完成了短句互听确认，回声不再妨碍交流；或对方知道你已转入其允许的文字/电话参与方式及尚未解决的音频问题。若某一方向仍未验证，就明确说“只能听不能说”或相反，不把局部改善报告为已恢复。

### 常见报错与补救

- **麦克风输入条动但对方仍听不到：** 核对应用内是否仍静音、所处会议的音频参与模式，并请一人反馈；不要只盯输入条。
- **能听测试音却听不到某个人：** 问其他人能否听到该人，区分你的输出与对方输入；不要重置所有设备设置。
- **戴上耳机仍有回声：** 查同房间是否还有设备开着会议音频，按有权范围关掉重复路径；回声也可能来自别人，先问谁听到。
- **电话和电脑同时入会：** 保留一个音频端，另一个设为不使用会议音频或静音，防止循环。
- **文字/电话不被组织者允许：** 说明未能恢复并询问改期或后续材料，不擅自假装已参与讨论。

### 假设、替代与现实副作用

应用的静音、设备菜单、测试功能和电话拨入条件不同，以当前会议实际选项为准。Google Meet 和 Teams 的官方帮助都支持在界面中选麦克风/扬声器；Google 也建议耳机、降低外放和静音来减轻回声。本 Skill 不诊断硬件或网络。短暂暂停可能让你错过一句话，必要时请对方重复，而不是补造听到的内容。

### 来源

- [Google Meet：修复音频问题](https://support.google.com/meet/answer/10620276?hl=en)：应用静音、实际输入/输出及权限是可见检查项；本 Skill 不采用其命令行或高级修复部分。
- [Google Meet：连接视频与音频](https://support.google.com/meet/answer/10409699?hl=en)；[会议质量与回声](https://support.google.com/meet/answer/10620583?hl=en-GB)：设备选择、耳机、降低外放和静音可用于减少回声。
- [Microsoft Teams：管理会议音频](https://support.microsoft.com/en-us/teams/meetings/manage-audio-settings-in-microsoft-teams-meetings)：会议界面可选择音频来源，具体能力依应用而定。

## English

Load this Skill when an ordinary video call is underway and you cannot hear others, they cannot hear you, or echo disrupts the conversation. **Use visible app and device controls to identify the audio direction, make a few reversible checks, and restore two-way speech or move promptly to an allowed text/phone route.** Prejoin testing and repeated connection drops have separate tasks.

Use only low-risk actions visible in the UI. Do not run terminal commands, change drivers, open hardware, request another person's account, or assume that an advanced room feature exists everywhere. Follow the organizer's route when this call has special safety or formal coordination requirements.

### Preparation and inputs

If chat or a brief gesture works, tell the others, “I am checking audio; give me two minutes.” Identify whether **you cannot hear them**, **they cannot hear you**, **both directions are silent**, or **there is echo**. Ask one participant what they observe. Do not change three devices at once while everyone guesses. Note the selected mic and speaker so you can undo a change.

### Execution

1. **Check mute and direction first.** Inspect the app mic mute, any headset or device mute, and whether volume is zero. Change one thing relevant to the symptom. If everyone misses the same speaker while other people hear one another, that person's input may be the issue; do not force a change to your own system.
2. **If you cannot hear, check output.** In the meeting app's audio menu, see whether Speaker/Output points to a headset, Bluetooth device, or something you can actually hear. Select the intended output and use a supported test sound or ask for one short phrase. A monitor selected as a speaker is not a reason to raise every system volume to painful levels.
3. **If they cannot hear you, check input.** Inspect whether Microphone/Input is the real device and whether the input indicator responds when you speak. Check visible permission prompts and app/hardware mute. Change one item, then ask one person for feedback instead of several people speaking at once.
4. **For echo, reduce duplicate audio paths.** If two devices in one room both have mic and speaker active, ask their authorized operators to mute or disconnect one audio path. Use headphones when available, lower speaker volume where appropriate, or mute between speaking turns. Do not mute everyone far away to hide a local feedback loop.
5. **Run a short two-way test.** Say one sentence and have someone repeat a key word; have them say one and repeat it back. Return to the conversation when both directions are intelligible and echo no longer blocks it. A moving input meter, a local test sound, or one “fixed” report does not prove both directions.
6. **Downgrade and notify at the time limit.** If it still fails after a couple of minutes, write in available chat: “My audio is still unavailable. I will use [actually available text/phone route].” If the invitation permits phone dial-in, keep the phone as the one active audio endpoint and disable the other device's meeting audio to avoid echo. Ask for a new time if no usable fallback exists rather than occupying the whole call.

### Success

Both sides verified a short exchange and echo no longer blocks conversation, or the others know your allowed text/phone participation route and the remaining audio limitation. Name an unverified direction as “I can hear but not speak,” or the reverse; do not report partial improvement as full recovery.

### Common errors and recovery

- **The input meter moves but nobody hears you:** Check app mute and the meeting's selected audio mode, then ask one person. Do not rely on the meter alone.
- **You hear a test tone but miss one speaker:** Ask whether others can hear that person to distinguish your output from their input. Do not reset every device setting.
- **Echo persists with headphones:** Check whether another in-room device still has meeting audio active and close the duplicate path within your authority. The echo may also be remote; ask who hears it.
- **Phone and computer both joined with audio:** Keep one audio endpoint; set the other to no meeting audio or mute it.
- **Text/phone is not allowed by the organizer:** Say the audio did not recover and ask for a new time or follow-up material; do not pretend you took part in the discussion.

### Assumptions, alternatives, and known side effects

Mute, device menus, tests, and dial-in availability vary by app and meeting. Google Meet and Teams official help both support choosing mic and speaker in their UI; Google also suggests headphones, lower speakers, and mute to reduce echo. This Skill does not diagnose hardware or network. A short interruption may cost you a sentence; ask for a repeat rather than inventing what you heard.

### Sources

- [Google Meet: Fix audio issues](https://support.google.com/meet/answer/10620276?hl=en): App mute, actual input/output, and permissions are visible checks. This Skill excludes its command-line and advanced repair material.
- [Google Meet: Connect video and audio](https://support.google.com/meet/answer/10409699?hl=en) and [meeting quality and echo](https://support.google.com/meet/answer/10620583?hl=en-GB): Device choice, headphones, lower speaker volume, and mute can reduce echo.
- [Microsoft Teams: Manage meeting audio](https://support.microsoft.com/en-us/teams/meetings/manage-audio-settings-in-microsoft-teams-meetings): Audio sources can be selected in the meeting UI, subject to app support.

If AI opens this file, it may help draft a short chat notice. You remain the Human Runtime and inspect the UI, test, tell others, or switch channels.
