# Skills for Humans / 给人类的 Skill

[简体中文](README.md)

[![CI](https://github.com/KanadeK/skills-for-humans/actions/workflows/ci.yml/badge.svg)](https://github.com/KanadeK/skills-for-humans/actions/workflows/ci.yml)

> **AI has Skills. Humans should too.**
>
> **Runtime: Human. Execution requires a body.**

This repository contains 15 real SKILL.md files written for people to read and execute directly. They cover groceries, laundry, cooking, a first solo restaurant visit, customer-service calls, returns, and recovery after something has gone slightly wrong.

A chat box is not a dependency. Open a file, read its inputs and stop conditions, then let the Human Runtime—you—execute it.

A real file looks like this:

    ---
    name: recover-when-you-are-running-late
    description: "Human-readable instructions for calculating an honest ETA..."
    ---
    # 出门前发现又要迟到了 / Recover When You Are Running Late

    | Runtime / 运行时 | Human / 人类 |
    | Time / 预计时间 | 5–15 minutes to decide and leave |
    | Side effects / 现实副作用 | Fewer rituals; physics gets no overtime request |

    ERR_CRITICAL_ITEM_NOT_FOUND:
    Set a short explicit search limit that fits your mobility, vision, and attention needs.
    If it has no substitute, notify and reschedule.

The machine format is serious. The life problem is real. The contrast earns the click; the instructions earn completion.

## How to “install”

1. Open the [Skill Catalog](SKILLS.md).
2. Choose the task that is actually happening.
3. Open its skills/<slug>/SKILL.md.
4. Read the Human Runtime information, preparation, and safety boundary.
5. Execute with your body. Success, downgrade, stop, and recovery are all valid outputs.

You can also download a published ZIP from [GitHub Releases](https://github.com/KanadeK/skills-for-humans/releases) and browse it offline. If v0.1.0 is not listed there yet, content on main remains a candidate; a local build is not a publication.

## What v0.1.0 contains

### Chores

- Plan a Market Trip
- Choose Fresh Perishables
- Put Away Groceries
- Sort a Laundry Load
- Choose Washer Settings
- Wash Wool Knitwear
- Plan a Meal from What You Have
- Substitute an Ingredient by Function
- Check Doneness and Store Leftovers

### First Attempts

- Eat Alone at an Unfamiliar Restaurant
- Try a Hobby Before Buying the Gear

### Awkward Social Tasks

- Call Customer Service
- Return the Wrong Item

### Recovery

- Rescue Salty Food
- Recover When You Are Running Late

Fifteen is the first-release scope, not a lifetime ceiling. We will not claim to cover the world by giving one job fifteen titles.

## Why this is not an AI prompt collection

- Every file addresses you; you observe, communicate, and perform the physical actions.
- Each Skill remains complete when no AI is present.
- AI may read aloud, explain, or localize the text as an optional observer.
- Files retain the official-compatible name, description, and SKILL.md structure. Human Runtime information stays in the body instead of inventing another metadata system.
- Every Skill has success, common errors, recovery, real side effects, and stated assumptions.

The envelope follows OpenAI's official [Build skills](https://developers.openai.com/codex/skills) documentation and every file is checked with the bundled quick_validate.py. The repository validator additionally checks bilingual completeness, catalog links, Human Runtime, and Agent-voice leakage.

## Seven parts useful, three parts extremely serious

Humour belongs around dependencies, harmless errors, and side effects—not temperatures, allergies, chemicals, payment, consent, or deadlines.

We do not mock people for not knowing chores, trying something for the first time, social anxiety, poverty, disability, or cultural difference. Remove the jokes and the Skill must still work. Remove the instructions and leave only jokes, and the build should fail.

## Safety boundaries

- Food appearance and smell cannot prove safety. Allergy, infant food, canning, fermentation, and illness are not casual patch targets.
- Laundry follows labels and the exact machine manual. It does not mix hazardous cleaners or repair electrical, gas, or mechanical equipment.
- Cooking stops on uncontrolled oil, flame, gas odour, or appliance failure and follows local emergency guidance.
- Medical, legal, financial, crisis-intervention, credential-heavy, and real-world-control Skills are excluded.
- Regional, cultural, price, equipment, mobility, visual, hearing, and communication assumptions must be stated with alternatives.

## Contributing

Start from the [template](templates/SKILL.md), then read the [Human Skill format](docs/human-skill-format.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

AI may help draft; it may not bulk-dump content. Prefer at least one real human walkthrough. Without that evidence, keep Not yet / 尚未 rather than treating a validator pass as Tested on human runtime.

## Project boundary

[codex-skill-harvester](https://github.com/KanadeK/codex-skill-harvester) is the background discovery, evidence, deduplication, and maintenance engine. This repository contains only the human-facing Skills—no SQLite, campaign, candidate queue, run report, or software Plugin.

## License

[MIT](LICENSE)
