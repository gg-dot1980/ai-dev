[繁體中文](PROJECT-INTAKE.zh-TW.md)

# ai-dev New Project Kickoff Form

Purpose: copy this blank form when starting a new project using the [ai-dev template](https://github.com/gg-dot1980/ai-dev). Fields 1–5 are sufficient to draft a specification and the first proof of concept (POC). Fields 6–8 may initially be marked “undecided”; confirm them before the relevant actions.

| Field | Guidance | Your response |
| --- | --- | --- |
| 1. Project name and one-sentence goal | What will it do, and what problem will it solve? | |
| 2. Users and use cases | Who will use it? What task will they most often complete? | |
| 3. First-version scope | List 1–3 must-have features and what this version explicitly excludes. | |
| 4. Acceptance criteria | What counts as success? For example, at least 18 correct results out of 20 fixed samples, with failure details retained. | |
| 5. Constraints and data sources | Is there existing code or data? What may be public? What cost, platform or API constraints apply? | |
| 6. Repository and execution environment | Which new or existing repository? Public or private? Where will development, builds and tests run? | |
| 7. Roles and permissions | Who owns, implements and independently reviews the work? What may external AI or humans submit, merge or deploy? | |
| 8. Testing and deployment | Which environments must be tested? Where are staging and production? Who approves? How will deployment be verified and rolled back? | |

Do not enter passwords, keys or private data. Completing this form does not authorize publication, merging or deployment. Reuse information already provided in the conversation or project documents; do not require it again.

When AI initiates a new project (not merely browsing or maintaining an existing project), it MUST present all eight questions or prefilled answers for confirmation, directly ask the user for every missing or unconfirmed answer (questions may be batched), and record replies and open items. Reuse explicitly provided answers without asking again; do not guess or imply authorization. Confirm questions 1–5 before treating scope or a POC plan as agreed, or implementation as approved. Questions 6–8 may be explicitly marked TBD, but must be resolved before relevant repository, sharing, merge or deployment actions. If the user is unavailable, list unanswered items and stop before those steps.
