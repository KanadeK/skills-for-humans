---
name: check-a-video-call-before-joining
description: "Human-readable prejoin check for an ordinary video call: expected meeting, microphone, speaker, camera, privacy, and a permitted participation fallback."
---
# 视频通话前检查连接与参与方式 / Check a Video Call Before Joining

[中文](#中文) · [English](#english)

| Human Runtime 信息 | 值 |
| --- | --- |
| Runtime / 运行时 | Human / 人类 |
| Status / 状态 | Draft / 草稿 |
| Difficulty / 难度 | Easy / 简单 |
| Time / 预计时间 | 5–10 分钟 / 5–10 minutes |
| Requirements / 必要物品 | 预期会议邀请、已可用的设备与应用、参与方式 / Expected meeting invite, available device and app, participation mode |
| Side effects / 现实副作用 | 你可能发现麦克风选错了，但还没让全场听见 / You may find the wrong mic before the whole room does |
| Safety scope / 安全范围 | Everyday / 日常 |
| Human test / 人类实测 | Not yet / 尚未 |

## 中文

当一次普通视频通话快开始，你要在进入会议前确认自己能听、能被听、是否要开画面时，加载这份 Skill。目标是**在应用提供的预览或测试界面确认声音、画面与参与方式，或提前选一个对方允许的降级方式**。这不教会议中的讨论、屏幕共享，也不处理账号登录故障。

只用你已有权限的应用界面操作。不要运行修复命令、安装陌生工具、借账号或为了通话随意打开不想开放的摄像头/麦克风权限。设备或应用没有某项预览功能，就标记“未测”，不说已经正常。

### 准备与输入

确认邀请来自预期组织者，日期、时间和会议名称对得上；找到进入方式和组织者提供的文字、电话或改期联系渠道。决定本次是否必须开摄像头、是否可以只用声音、是否需要字幕或聊天支持。提前留出几分钟，不在开始时间才第一次找耳机。

### 执行

1. **先到预加入界面。** 打开预期会议的官方应用或链接，确认显示的是要去的会议。若名称、时间或来源明显不符，先向组织者核实，不把陌生页面的登录请求当成会前检查的一部分。
2. **选实际麦克风与扬声器。** 在应用的设备选择里看当前输入、输出是耳机、电脑还是其他设备。说一句普通测试话，看输入指示是否响应；按应用提供的“测试扬声器/测试通话”听回放。只有图标亮着，不等于对方一定听见。
3. **看摄像头预览和隐私。** 若这次需要画面，在预览里确认显示的是正确摄像头、脸和背景，没有意外露出的私人画面。若不需要或不愿开，就在进入前关闭；不要把摄像头关闭当成参与失败。
4. **检查预期参与方式。** 如果活动允许，确认字幕、聊天或电话拨入等你可能需要的入口是否在实际邀请或应用中可用。别假设每个会议都提供电话拨入，也别把字幕图标当成已有人为你开启。
5. **只做一轮界面内修正。** 输入没动、测试声听不到或预览黑屏时，先检查应用选的设备、静音开关与已弹出的权限提示；改一项后重测。仍不行就使用对方实际允许的文字/电话方式或提前通知无法按原方式参加，把深入故障留给后续处理。
6. **进入前确定初始状态。** 知道自己将以静音/开麦、关/开镜头的哪种状态进入，整理耳机与环境，然后加入。加入后再以实际对话确认能否交流；会前自测不是对整场连接的保证。

### 完成条件

你已核对会议对象、可用的输入和输出、需要时的画面，以及本次允许的参与方式；不能确认的一项有明确的替代或通知。预览通过只证明此时本机所见所听，不能保证会议中网络、他人设备或主办方权限持续正常。

### 常见报错与补救

- **输入条不动：** 查应用选中的麦克风、硬件/应用静音和当前权限提示；换实际可用设备再试一次，不用系统命令重置。
- **听不到测试声：** 看扬声器是否指向不在耳边的显示器或蓝牙设备，选正确输出后测试；无声时别等入会才报告。
- **预览画面不想给人看：** 关摄像头或调整背景/位置，按本次允许的参与方式进入；不强迫自己展示私人空间。
- **预加入功能缺失：** 记录未测，若可用则使用应用设置里的测试通话；入会时先静音并尽快确认交流，不假装测试过。
- **时间快到了仍未准备好：** 先用允许的渠道告诉组织者你将以声音/文字加入或需要改期，再继续一项关键检查；不要消失。

### 假设、替代与现实副作用

Google Meet、Microsoft Teams 等应用的设备预览、测试通话、字幕和电话选项随版本和会议设置不同。Google Meet 有预加入自检；Teams 的完整测试通话有设备/桌面应用限制。用当前界面为准。可以用键盘和屏幕阅读器检查设备名称与状态，不依赖图标颜色。检查花几分钟，但在门口找错麦克风比进会后全员帮你找更省时间。

### 来源

- [Google Meet：连接视频与音频](https://support.google.com/meet/answer/10409699?hl=en)：预加入界面可选择并测试麦克风、扬声器和摄像头。
- [Microsoft Teams：管理通话设置](https://support.microsoft.com/en-us/teams/calls-devices/manage-your-call-settings-in-microsoft-teams)：设备选择与桌面应用测试通话的实际入口和限制。
- [Microsoft Teams：管理会议音频设置](https://support.microsoft.com/en-us/teams/meetings/manage-audio-settings-in-microsoft-teams-meetings)：预加入时音频来源选项依应用与设备而定。

## English

Load this Skill when an ordinary video call is about to start and you want to know, before entering, whether you can hear, be heard, and use video if needed. **Check audio, video, and participation mode in the app's preview or test view, or choose a fallback the organizer actually allows.** This is not a guide to meeting discussion, screen sharing, or account-login repair.

Use only the app interfaces you are allowed to use. Do not run repair commands, install unfamiliar software, borrow accounts, or grant camera/microphone access you do not want merely for the call. If your app lacks a test feature, mark that part untested rather than claiming it works.

### Preparation and inputs

Check that the invitation came from the expected organizer and that its date, time, and meeting name match. Find the join route and any organizer-provided text, phone, or reschedule channel. Decide whether video is required, audio-only is allowed, or captions or chat support are needed. Leave a few minutes before start instead of finding headphones at the exact scheduled time.

### Execution

1. **Enter the prejoin view first.** Open the expected meeting in its official app or link and check the meeting shown. If name, time, or source is clearly wrong, confirm with the organizer. An unexpected login page is not part of a device test.
2. **Choose the real microphone and speaker.** In the app's device controls, see whether input and output point to your headset, computer, or another device. Speak a short test phrase and look for input activity. Use the app's speaker test or test call to hear playback. A lit icon alone does not prove others will hear you.
3. **Check camera preview and privacy.** If video matters, see the intended camera, your face, and background in preview without exposing unintended private material. If video is not required or wanted, switch it off before joining. A closed camera is not failed participation.
4. **Check the intended participation route.** Where permitted, see whether captions, chat, or phone dial-in that you may need are actually available in the invite or app. Do not assume every meeting has a dial-in number or that a caption icon means someone enabled it for you.
5. **Make one UI-level correction pass.** If input does not respond, playback is silent, or preview is black, first inspect the app's selected device, mute control, and permission prompt already shown. Change one thing and retest. If still broken, use a text or phone path the organizer actually permits, or notify them early that the original route will not work. Leave deeper troubleshooting for a later task.
6. **Know your entry state.** Decide whether you enter muted or with mic on, camera off or on, settle the headset and surroundings, then join. Confirm actual communication after entering; a preflight is not a guarantee for the whole call.

### Success

You checked the meeting, usable input and output, video if required, and participation mode allowed this time. An unconfirmed part has a clear fallback or notification. Passing a local preview proves only what your device showed at that moment; it cannot guarantee that the meeting network, other devices, or organizer permissions remain stable.

### Common errors and recovery

- **The input meter does not move:** Check the selected mic, hardware/app mute, and visible permission prompt. Choose an available device and try once more; do not reset the system with commands.
- **No test sound plays:** Check whether output points to a monitor or Bluetooth device you cannot hear. Select the intended speaker and retest before entering.
- **The camera preview exposes something you do not want shown:** Turn off video or change the background/position and join by an allowed mode. You need not show private space.
- **The app lacks a prejoin test:** Mark it untested. If available, use an app settings test call; otherwise enter muted and confirm communication quickly without pretending a test occurred.
- **Start time is near and setup remains unfinished:** Tell the organizer through an allowed channel that you will use audio/text or need another time, then do the one critical check. Do not simply vanish.

### Assumptions, alternatives, and known side effects

Device preview, test call, captions, and phone options vary by Google Meet, Microsoft Teams, version, and meeting settings. Meet has a prejoin check; Teams' full test call has desktop-app limits. Follow your actual UI. Keyboard or screen-reader controls can inspect device names and states without icon color. The check costs a few minutes; finding a wrong mic before entry is cheaper than recruiting everyone afterward.

### Sources

- [Google Meet: Connect your video and audio](https://support.google.com/meet/answer/10409699?hl=en): Prejoin device selection and mic, speaker, and camera tests.
- [Microsoft Teams: Manage call settings](https://support.microsoft.com/en-us/teams/calls-devices/manage-your-call-settings-in-microsoft-teams): Device selection and desktop test-call availability.
- [Microsoft Teams: Manage meeting audio settings](https://support.microsoft.com/en-us/teams/meetings/manage-audio-settings-in-microsoft-teams-meetings): Prejoin audio source choices vary by app and device.

If AI opens this file, it may help make a preflight list. You remain the Human Runtime and inspect, test, choose, notify, or join the call.
