# Implementation plan: Skills for Humans v0.1.0

## Overview

Build a clean Human Runtime repository in thin, reviewable slices. The dependency order is: product contract → validator/build contract → content groups → storefront and CI → GitHub release → separate Harvester correction. A slice is complete only after its focused tests pass and it is committed.

## Confirmed decisions

- Product name: Skills for Humans / 给人类的 Skill.
- Repository: KanadeK/skills-for-humans.
- Human readers execute real SKILL.md files.
- Simplified Chinese is original; English is a complete first localization.
- v0.1.0 contains 15 independent Skills: 9 rewritten evidence-seeded chores and 6 first-attempt/awkward/recovery Skills.
- Python 3.12+ standard library owns validation and deterministic packaging.
- No Plugin layer, database, web UI, App, account, search service, locale framework, or high-risk Skill.

## Dependency map

    idea and spec
        |
        +-- Human Skill format + template
        |       |
        |       +-- validator tests -> validator
        |       +-- release tests -> deterministic builder
        |
        +-- 15 content Skills
                |
                +-- catalog and bilingual READMEs
                        |
                        +-- CI + five-axis/fresh-reader review
                                |
                                +-- GitHub PR, merge, tag, Release, download proof
                                        |
                                        +-- Harvester documentation-only correction

## Phase 0: boundaries and research

- [x] Confirm D:\我的\GitHub\skills-for-humans does not exist before creation.
- [x] Confirm KanadeK/skills-for-humans is unoccupied and GitHub authentication is available.
- [x] Confirm D:\我的\GitHub is an outer Git repository and the new directory has its own .git.
- [x] Complete the five-query prior-art review and current official OpenAI Skill format check.

Checkpoint: the product is differentiated, the slug is available, and no outer file has been staged.

## Phase 1: specification bootstrap

- [x] Save the confirmed idea, assumptions, MVP, non-goals, full spec, repository rules, plan, and task list.
- [x] Validate links and scope mechanically where possible.
- [x] Commit a minimal documentation-only main baseline.
- [x] Create the public GitHub repository and push bootstrap main without creating a release.

Checkpoint: public main is a truthful specification baseline, not an empty shell presented as a finished product.

## Phase 2: Human Skill format and deterministic tooling

- [x] Add RED tests for frontmatter, Human Runtime fields, bilingual completeness, direct human address, Agent-language rejection, placeholders, local links, duplicate names, flat catalog consistency, safety scope, and high-risk category rejection.
- [x] Implement docs/human-skill-format.md, templates/SKILL.md, and scripts/validate_skills.py with no third-party runtime dependency.
- [x] Add RED tests for a path-safe deterministic skills-for-humans-v0.1.0.zip and SHA256SUMS.txt.
- [x] Implement scripts/build_release.py and prove two builds are byte-identical and the extracted repository revalidates.

Checkpoint: one fixture Human Skill can travel from source tree through validation, release build, extraction, and revalidation.

## Phase 3: content slices

- [x] Chores A: market planning, choosing perishables, putting groceries away.
- [x] Chores B: sorting laundry, choosing washer settings, washing wool knitwear.
- [x] Chores C: planning a meal, substituting ingredients, checking doneness/storing leftovers.
- [ ] First Attempts: eating alone at an unfamiliar restaurant; trying a hobby before buying full gear.
- [ ] Awkward Social Tasks: calling customer service; returning a wrong or unsuitable item.
- [ ] Recovery: rescuing over-salted food; making a realistic late-arrival downgrade.

Each content slice:

- contains complete original Chinese and natural English;
- uses direct human address and visible Human Runtime metadata;
- states success, errors, recovery, side effects, assumptions, safety, and sources;
- passes repository and official validation before commit;
- touches at most three Skill files.

Checkpoint: exactly 15 distinct MVP Skills exist; no title-only duplicate or high-risk content was added.

## Phase 4: storefront, contribution, and review

- [ ] Write the Chinese-first README first screen with the two approved taglines and a real SKILL.md excerpt.
- [ ] Write a complete English README and a flat bilingual SKILLS.md catalog grouped by Chores, First Attempts, Awkward Social Tasks, and Recovery.
- [ ] Add CONTRIBUTING.md and CHANGELOG.md; never claim human runtime testing without evidence.
- [ ] Add Ubuntu/Windows CI for tests, validator, deterministic build, extraction/revalidation, and clean tracked state.
- [ ] Run automated Agent-voice and safety checks across all 15 Skills.
- [ ] Have fresh-context Codex readers review at least five randomly selected Skills for no-AI usability, humor balance, assumptions, dignity, and recovery.
- [ ] Complete five-axis review and resolve every Required/Critical finding.

Checkpoint: the repository is useful to a human reader, not merely structurally valid.

## Phase 5: publish v0.1.0

- [ ] Open codex/initial-human-skills PR to main with product difference, inventory, sources, safety, and verification.
- [ ] Wait for Ubuntu/Windows CI; merge only after every gate is green.
- [ ] Create annotated v0.1.0 at verified main.
- [ ] Publish bilingual Release notes with skills-for-humans-v0.1.0.zip and SHA256SUMS.txt.
- [ ] Re-download the Release assets into isolation, verify checksum, extract, run validator, and open at least five random Skill files.
- [ ] Read back public visibility, tag/target/main alignment, Release state/assets, CI, contributor, and MIT license.

Rollback: do not rewrite a published tag or Release. Stop promotion and use a reviewed fix/revert PR for a material defect.

## Phase 6: restore Harvester identity

- [ ] In D:\我的\GitHub\codex-skill-harvester, create a separate codex/ branch from clean current main.
- [ ] Make the minimum README/documentation correction: Harvester is the backend discovery/evidence/deduplication engine; link Skills for Humans; label v0.2.0 an immutable historical technical prototype.
- [ ] Run its documentation tests and full relevant validator.
- [ ] Open a separate PR, wait for Ubuntu/Windows CI, review, and merge. Do not tag or release Harvester.

Checkpoint: the two repositories have separate histories, responsibilities, PRs, and release policies.

## Risks and mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Agent voice leaks into Human Skills | Product thesis fails | Direct-language validator plus fresh-reader review |
| Humor obscures safety | Unsafe or unusable instructions | Keep jokes outside critical steps; dedicated food/laundry/fire review |
| Bilingual drift | One audience gets an incomplete workflow | Validate both sections and manually compare facts/success/recovery |
| Validator overfits prose | Contributions become rigid | Check semantic presence and invariants, not exact headings or jokes |
| Source copying | License/copyright risk | Use links and necessary facts; write original prose |
| False human testing claim | Trust failure | Default to Not yet field; require recorded evidence before changing it |
| First remote launch fails | Half-published state | Bootstrap main first, PR/CI before tag, Release after verified merge |

## Open questions

No identity-level question blocks v0.1.0. Later language architecture, real human-runtime badges, and any helper installer require new evidence and approval.
