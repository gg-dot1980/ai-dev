[繁體中文](#zh-tw) | [English](#english)

<a id="zh-tw"></a>

# 工作流規格 v0.1（草稿）

## 可量測狀態

| 狀態 | 必要證據 | 未滿足時 |
|---|---|---|
| DRAFT | 需求、範圍、接受條件、禁止事項、owner | 不開始外部動作 |
| CHECKED | 固定案例、命令、環境、總數／失敗／未測 | 留 DRAFT／BLOCKED |
| BUILT | 兩個乾淨建置、相同 digest、來源 commit、工具版本 | 不部署 |
| REVIEWED | 非作者審查、完整 diff、相同 head SHA、未解問題 | 不稱獨立通過 |
| STAGED | 明確授權、隔離檢查、平台版本、CI 來源及重封裝差異 | 不稱上線 |
| HEALTH_VERIFIED | HTTP 計數與預期值、瀏覽器啟動／輸入／停止 | 各自標未測 |
| ROLLBACK_VERIFIED | 同一基線回復、readback、digest／健康／瀏覽器重驗 | 不稱可回復 |
| ACCEPTED | 指定範圍全部條件符合、owner 驗收、殘餘風險 | 仍未准公開 |
| PUBLISHED | 具體發布授權、目的地、遠端 SHA 與內容回讀 | 不稱已發布 |

另設 WAITING／BLOCKED／FAILED，記錄原因、等待誰、最後證據時間、下一步；不得把「任務未結案」標成正在執行。狀態是工作紀錄，不是本範例程式已實作的完整發布控制器。

## 證據欄位

`schema_version, project, scope, hypothesis, source_commit, artifact_sha256, artifact_type, build_command, runtime_version, environment, adapter, platform_version, started_at, finished_at, state, passed, failed, untested, expected, observed, evidence_location, reviewer, review_head_sha, authorization_scope, authorization_time, rollback_baseline, limitations, next_step`。

時間用 ISO 8601 並註明時區。公開證據只保存可公開的摘要與合成資料，私有證據用受控保留政策，不將私人路徑或網址直接貼入公開模板。機器結果與人工驗收分欄，無證據填 `unknown`。

## 獨立強制 gate 的部署前查核

由 repo 管理者另行核實分支規則、required checks 的精確名稱、CODEOWNERS 覆蓋、非作者核准、更新 commit 後失效舊核准、對管理員／bypass 的限制、禁止未授權直推，以及受保護部署環境。保存規則實際讀回和一次被拒的負案例。這些未在本草稿配置，不能以模板或自我簽署宣稱已強制。

## 非目標

不設定 production，不連資料庫、不使用 API key、不自動修改 repo 權限，不把單版本功能 smoke 當成 OCR4 跨版本勝率驗收。

[English ↓](#english)

<a id="english"></a>

# Workflow specification v0.1 (POC)

## Measurable states

| State | Required evidence | If unmet |
|---|---|---|
| DRAFT | Requirements, scope, acceptance, prohibitions, owner | No external action |
| CHECKED | Fixed cases, commands, environment, totals/failures/untested | Stay DRAFT/BLOCKED |
| BUILT | Two clean builds, equal digest, source commit, tool versions | No deployment |
| REVIEWED | Non-author review, complete diff, same head SHA, open issues | Do not claim independent approval |
| STAGED | Explicit authorization, isolation checks, platform version, CI provenance and repackaging differences | Do not claim live deployment |
| HEALTH_VERIFIED | HTTP counts/expected values, browser startup/input/stop | Mark each missing check untested |
| ROLLBACK_VERIFIED | Restore same baseline, readback, digest/health/browser recheck | Do not claim recoverability |
| ACCEPTED | All scoped criteria satisfied, owner acceptance, residual risks | Still not publication permission |
| PUBLISHED | Specific publication permission, destination, remote SHA and content readback | Do not claim publication |

Also use WAITING/BLOCKED/FAILED with reason, waiting party, last evidence time and next step. An open task is not proof of active execution. These states specify the work record; the example does not implement a complete release-control system.

## Evidence fields

`schema_version, project, scope, hypothesis, source_commit, artifact_sha256, artifact_type, build_command, runtime_version, environment, adapter, platform_version, started_at, finished_at, state, passed, failed, untested, expected, observed, evidence_location, reviewer, review_head_sha, authorization_scope, authorization_time, rollback_baseline, limitations, next_step`.

Use ISO 8601 timestamps with timezone. Public evidence contains only publishable summaries and synthetic data. Keep private evidence under controlled retention; do not insert private paths or URLs into public templates. Separate machine outcomes from human acceptance; use `unknown` when evidence is absent.

## Independently enforced gate checks before deployment

A repository administrator must separately verify branch rules, exact required-check names, CODEOWNERS coverage, non-author approval, dismissal of stale approval after new commits, administrator/bypass restrictions, prevention of unauthorized direct pushes and protected deployment environments. Preserve actual configuration readback and a rejected negative case. This POC configures none of these; templates and self-signatures do not demonstrate enforcement.

## Non-goals

No production setup, database connections, API keys or automatic repository-permission changes. Single-version functional smoke tests do not establish OCR4 cross-version win-rate acceptance.

[繁體中文 ↑](#zh-tw)
