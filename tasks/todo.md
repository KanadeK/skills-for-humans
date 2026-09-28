# Task list: Skills for Humans v0.1.0

## Task 1: bootstrap the independent specification repository

Description: establish the new Git boundary and save the user-confirmed product identity before implementation.

Acceptance:

- [x] Local and remote names are free; target Git root is independent from D:\我的\GitHub.
- [x] Idea, spec, AGENTS, plan, todo, README, license, and ignore rules exist.
- [x] Bootstrap main is committed and pushed to a new public KanadeK/skills-for-humans repository.

Verify:

- [x] git rev-parse --show-toplevel returns D:/我的/GitHub/skills-for-humans.
- [x] Local Markdown links resolve; outer Git index is untouched.

Files: bootstrap documents only.
Dependencies: none.

## Task 2: define and test the Human Skill contract

Description: create one visible Human Runtime format and a validator that checks stable compatibility/usability boundaries.

Acceptance:

- [x] Template frontmatter uses only name and description.
- [x] Runtime/status/difficulty/time/requirements/side effects/safety are visible in the first screen.
- [x] Both languages cover execution and recovery while Agent-facing wording fails validation.

Verify:

- [x] RED tests fail before implementation, then five focused tests and official quick_validate pass.

Files: docs/human-skill-format.md, templates/SKILL.md, scripts/validate_skills.py, one test file.
Dependencies: Task 1.

## Task 3: build deterministic release packaging

Description: package the readable repository without adding an installer or runtime.

Acceptance:

- [x] Build produces skills-for-humans-v0.1.0.zip and SHA256SUMS.txt only.
- [x] Archive paths are safe, timestamps stable, and two builds match byte-for-byte.
- [x] Extracted archive passes the same validator.

Verify:

- [x] RED/GREEN release tests and isolated extraction pass.

Files: scripts/build_release.py and one test file.
Dependencies: Task 2.

## Tasks 4–6: rewrite the nine evidence-seeded chores

Description: use Harvester sources as factual seeds but replace every Agent-oriented sentence with original Human Runtime instructions.

Acceptance:

- [x] Task 4 ships three grocery Skills.
- [x] Task 5 ships three laundry Skills.
- [x] Task 6 ships three cooking/food-handling Skills.
- [x] All nine include short sources, assumptions, safe stop/recovery, and no forbidden Agent phrases.

Verify:

- [x] Validator, official quick_validate, factual comparison, and dedicated food/laundry safety review pass after each group.

Files: three skills/<slug>/SKILL.md files per task.
Dependencies: Task 2.

## Tasks 7–9: add six distinct Human Skills

Description: prove the product extends beyond chores without becoming an AI prompt collection.

Acceptance:

- [x] Task 7 ships two First Attempts Skills.
- [x] Task 8 ships two Awkward Social Tasks Skills.
- [x] Task 9 ships two Recovery Skills.
- [x] Cultural, financial, mobility, sensory, and policy assumptions have alternatives.

Verify:

- [x] Each pair passes validator and an independence/non-duplication review.

Files: two skills/<slug>/SKILL.md files per task.
Dependencies: Task 2.

## Task 10: build the bilingual storefront

Description: make the repository understandable within ten seconds and navigable without an installer.

Acceptance:

- [x] Chinese README uses the approved title and taglines plus a real file excerpt.
- [x] English README is complete and natural.
- [x] SKILLS.md lists exactly 15 Skills in four experience categories with time, difficulty, side effects, and stable links.
- [x] CONTRIBUTING and CHANGELOG state honest quality/testing rules.

Verify:

- [x] Catalog, reciprocal language links, local links, and 15 paths pass automated checks.

Files: README.md, README.en.md, SKILLS.md, CONTRIBUTING.md, CHANGELOG.md.
Dependencies: Tasks 4–9.

## Task 11: add CI and complete content review

Description: enforce the stable contract on Ubuntu and Windows and test actual human readability.

Acceptance:

- [x] CI runs tests, validator, build, extraction/revalidation, and clean-tree check.
- [x] Fresh-context readers reviewed six random Skills; all seven Required findings were fixed and passed targeted re-review.
- [x] All 15 pass Agent-language, bilingual, safety, dignity, humor, and recovery review.

Verify:

- [x] Twelve tests, 15 official validations, repository/build/extraction checks, and five-axis review pass with no Required/Critical findings.

Files: .github/workflows/ci.yml plus review evidence in the PR description; no fake E2E files.
Dependencies: Tasks 3 and 10.

## Task 12: publish and verify v0.1.0

Description: use a PR-first release and prove the public download works independently of the worktree.

Acceptance:

- [x] PR merges with green Ubuntu/Windows CI.
- [x] Annotated v0.1.0 and public Release point at verified main.
- [x] ZIP and checksum download, validate, extract, and remain readable.
- [x] Public repo metadata, CI, assets, contributor, and license are read back.

Verify:

- [x] Remote evidence, not local intent, proves completion; immutable=false is reported rather than upgraded into a claim.

Files: release notes and GitHub state only.
Dependencies: Task 11 and explicit publication authorization already granted.

## Task 13: correct Harvester documentation separately

Description: restore codex-skill-harvester as the backend engine and point readers to the new frontstage project.

Acceptance:

- [x] Only Harvester documentation changed on its own branches and PRs (#14 and #15).
- [x] v0.2.0 is described as a retained historical prototype, not deleted or rewritten.
- [x] Harvester received no new tag or Release.

Verify:

- [x] Relevant tests/validator and Ubuntu/Windows CI passed before merge.

Files: minimal Harvester README/docs/tests needed for truthful identity.
Dependencies: Task 12.

## Task 14: coordinate the next Human Skill batches

- [x] Define unique batch ownership, overlap boundaries, worktree rules, PR gates, and 30 reviewable batch briefs in [expansion-program.md](expansion-program.md).
- [ ] Start B01, B13, and B19 in separate new conversations; collect their PR links and five-item decisions.
- [ ] Review and merge each PR serially after current-main validation; then assign the next three batches.
