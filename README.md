[繁體中文](#zh-tw) | [English](#english)

<a id="zh-tw"></a>

# AI 開發工作流 v0.1.2 POC

這是已獲准公開的 v0.1.2 概念驗證（POC）。公開此工具包不等於完整部署流程或生產驗收。目標是把規格、測試、可追溯產物、部署、健康檢查、回復與交接拆成可驗證步驟。**不是特定應用程式的驗收或生產發布許可。**

## 新專案啟動表

複製空白表：[繁體中文](templates/PROJECT-INTAKE.zh-TW.md)／[English](templates/PROJECT-INTAKE.en.md)。先填前五項即可起草，其餘於相關操作前確認；沿用已知資訊，不填秘密，填表不授予發布權限。僅這兩份表格依明確要求分語言存放，其餘文件仍採同頁雙語。

## 零相依套件示例

需要 Python 3.10+，只使用標準函式庫，沒有網路、憑證或真實部署。

```sh
python3 -m unittest discover -s tests -v
python3 run_example.py --out /tmp/ai-dev-example-output
python3 run_example.py --out /tmp/ai-dev-negative-output --negative
# 最後一條預期 exit 2，顯示損毀包拒絕且基線未變。
```

示例建立固定 JSON 產物與 SHA-256，模擬基線→候選→基線。任何摘要、schema、授權或健康檢查失敗都不切換 active 狀態。傳入 `authorized=True` 只是單元測試情境，不是身分驗證或遠端權限控制。摘要證明內容一致，不證明來源可信；真實部署的預期摘要必須由獨立可信 CI 證據取得。

## 目錄

- `core/`：純產物建置與驗證，不接觸部署環境。
- `adapters/simulated.py`：可替換的記憶體部署模擬器。
- `docs/SPEC.md`：狀態、證據及驗收條件。
- `docs/SITES-ADAPTER.md`：手動整合指引，未配置任何網站。
- `templates/`：規格、PR、獨立 review、交接模板。
- `evidence/`：僅合成案例結果，不含私人位置、帳號、原始圖片或機密。

## 必須分開的三種結論

1. 本範例：本機合成測試與模擬回復，可重跑，不是真實 HTTP／瀏覽器驗證。
2. 真實環境整合：必須另行收集基線、候選與回復的 HTTP／瀏覽器證據，並核對來源與產物摘要；平台重封裝時區分檔案位元一致與整包一致。本工具包不提供此類實測證據。
3. 獨立強制 review／merge gate：本工具包未配置或核實。作者自己勾選 review、CI 綠燈或 Draft PR 不能替代獨立審查與平台強制措施。

## 發布規則

先讀最新規格、來源 commit、證據及限制，再由不同於作者的審查者檢查。記錄欲發布的確切 commit／digest、目的地、資料可見性、範圍、回復方案，以及使用者明確授權。公開文件推送、合併、staging 部署及 production 部署各是不同動作；一者不推定授權其他動作。此包沒有外部 CI workflow 或部署設定，避免把文件誤當已啟用的安全措施。

## 後續 patches

每個增量 patch 同步修改程式、固定測試、合成證據與 [CHANGELOG](CHANGELOG.md)，更新 [VERSION](VERSION)。保留原失敗案例，對相同來源 SHA 重新驗證；未測項不能列為通過。使用 Draft PR 進行審查，發布前核對授權範圍與遠端內容。

各 Markdown 頁完整中英文並存並提供語言導覽；程式與 JSON 維持單一來源。


## 共用協作基準與採用方式

這是供擁有者、人類協作者、內部／外部 AI 與維護者共同採用的供應商中立說明與規範，不是特定專案回顧或證據存檔庫。

- 擁有者指定範圍、驗收與發布授權；主執行者實作並記錄證據；不同於作者的審查者核對 diff 與測試；部署負責者在明確授權後執行健康檢查及回復。
- 外部協作者可提出變更及執行無特權的本機檢查；預設不取得憑證、正式環境、合併或部署權限。外部 AI 聯繫與資料分享仍須另有授權。
- 以 PR／review／handoff 模板協作。測試與 QA 必須分開列出通過、失敗、未測及驗收範圍；模型自評不能代替獨立審查。
- 各採用專案在自己的儲存庫建立最小 overlay：固定本規範版本／commit，列出建置與測試命令、驗收門檻、各角色負責人、允許環境、部署 adapter、回復步驟及授權範圍。專屬資料留在該專案，不混入共用核心。
- 採用這份規範本身不授予存取或發布權限，也不代表軟體授權條款已選定。沒有明確批准就停在提案或本機驗證。

## AI 新專案詢問義務

AI 啟動新專案時（不是單純瀏覽或維護既有專案），必須向使用者呈現全部八題或預填答案供確認，直接詢問每個缺漏或未確認的答案，可合併提問，並記錄回覆及待辦。已明確提供的答案沿用，不重複詢問、不猜測、不推定授權。第 1–5 題確認前，不得把範圍或 POC 計畫當作已議定，也不得把實作當作已批准；第 6–8 題可明確標記待定，但在相關 repo、分享、合併或部署操作前須解決。使用者無法回覆時，列出未答項並停在相關步驟之前。

[English ↓](#english)

<a id="english"></a>

# AI Development Workflow v0.1.2 POC

This v0.1.2 proof of concept is authorized for public publication. Publishing this toolkit is not acceptance of a complete deployment workflow or production readiness. Its purpose is to separate specifications, tests, traceable artifacts, deployment, health checks, rollback and handoff into verifiable stages. **It is not application-specific acceptance or production-release permission.**

## New project kickoff form

Copy a blank form: [Traditional Chinese](templates/PROJECT-INTAKE.zh-TW.md) / [English](templates/PROJECT-INTAKE.en.md). The first five fields suffice for a draft; confirm the rest before relevant actions. Reuse known information, omit secrets and do not infer publication rights from a completed form. Only these two forms are explicitly separated by language; other documentation remains bilingual on the same page.

## Dependency-free example

Requires Python 3.10+. Uses only the standard library: no network, credentials or real deployment.

```sh
python3 -m unittest discover -s tests -v
python3 run_example.py --out /tmp/ai-dev-example-output
python3 run_example.py --out /tmp/ai-dev-negative-output --negative
# The last command must exit 2: corrupted package rejected, baseline unchanged.
```

The example builds fixed JSON artifacts and SHA-256 digests, then simulates baseline → candidate → baseline. Digest, schema, authorization or health-check failures must not switch active state. `authorized=True` represents test-scenario permission, not authentication or remote access control. A digest demonstrates content equality, not trusted provenance; a real deployment must obtain its expected digest from independently trusted CI evidence.

## Layout

- `core/`: pure artifact building and validation, without deployment access.
- `adapters/simulated.py`: replaceable in-memory deployment simulator.
- `docs/SPEC.md`: states, evidence and acceptance criteria.
- `docs/SITES-ADAPTER.md`: manual integration guidance; no site is configured.
- `templates/`: specification, PR, independent review and handoff forms.
- `evidence/`: synthetic results only; no private locations, accounts, raw images or secrets.

## Three distinct conclusions

1. This example: repeatable local synthetic tests and simulated rollback, not real HTTP or browser validation.
2. Real-environment integration: separately collect baseline, candidate and rollback HTTP/browser evidence and verify source and artifact digests. If a platform repackages artifacts, distinguish file-byte equality from whole-package equality. This toolkit provides no such real-environment measurements.
3. Independently enforced review/merge gates: not configured or verified by this toolkit. An author's checkbox, green CI or Draft PR cannot substitute for independent review and platform enforcement.

## Publication rules

Read the current specification, source commit, evidence and limitations, then obtain review by someone other than the author. Record the exact commit/digest, destination, data visibility, scope, rollback plan and explicit user authorization. Public document push, merge, staging deployment and production deployment are separate actions; permission for one does not imply the others. This package includes no external CI workflow or deployment configuration; documentation is not an enabled security control.

## Subsequent patches

Each incremental patch must synchronize code, fixed tests, synthetic evidence and [CHANGELOG](CHANGELOG.md), and update [VERSION](VERSION). Retain failure cases and revalidate against the same source SHA. Untested items cannot be marked passed. Use Draft PR review, then verify authorization scope and remote contents before publication. Full Traditional Chinese and English documentation coexist on each page; code and JSON remain single-source.


## Shared collaboration baseline and adoption

This is a provider-neutral guide and specification for owners, human collaborators, internal/external AI and maintainers, not a project retrospective or evidence archive.

- The owner defines scope, acceptance and publication authorization. The primary executor implements and records evidence. A reviewer other than the author checks the diff and tests. The deployment owner performs health checks and rollback only after explicit authorization.
- External contributors may propose changes and run nonprivileged local checks. They receive no credentials, production access, merge or deployment rights by default. Contacting external AI and sharing data require separate authorization.
- Collaborate through the PR, review and handoff templates. Tests and QA must distinguish passed, failed, untested and acceptance scope; model self-assessment does not replace independent review.
- Each adopting project creates a minimal overlay in its own repository: pin this specification version/commit, define build/test commands, acceptance thresholds, role owners, allowed environments, deployment adapter, rollback steps and authorization scope. Keep project-specific data there, outside the shared core.
- Adoption grants no access or publication rights and does not imply a chosen software license. Without explicit approval, stop at a proposal or local validation.

## Mandatory AI project intake

When AI initiates a new project (not merely browsing or maintaining an existing project), it MUST present all eight questions or prefilled answers for confirmation, directly ask the user for every missing or unconfirmed answer (questions may be batched), and record replies and open items. Reuse explicitly provided answers without asking again; do not guess or imply authorization. Confirm questions 1–5 before treating scope or a POC plan as agreed, or implementation as approved. Questions 6–8 may be explicitly marked TBD, but must be resolved before relevant repository, sharing, merge or deployment actions. If the user is unavailable, list unanswered items and stop before those steps.

[繁體中文 ↑](#zh-tw)
