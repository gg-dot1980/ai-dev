[繁體中文](#zh-tw) | [English](#english)

<a id="zh-tw"></a>

# 執行規則

- 預設保持專案中立：文件、範例與證據使用通用名稱及合成資料，不加入來源專案名稱、識別碼、路由或專屬驗收細節。

- 先讀 README、SPEC 及本次任務授權，確認目標、驗收與禁止範圍。
- 每任務一位主執行者；先比較來源版本，只重讀有變化的證據。
- 每輪只驗證明確假設，保留固定／失敗樣本；相同條件錯誤先取得新證據再重試。
- 所有改動與失敗可追溯。不得將模擬、HTTP、瀏覽器、應用效能或發布驗收混為一談。
- 不上傳圖片、機密、私人 URL／ID 或真實使用者資料。範例僅使用合成資料。
- 不自行新增排程、改權限、啟用 CI、推送、合併或部署。發布需具體授權及驗證。
- 執行 `python3 -m unittest discover -s tests -v` 與正／負示例；保留實際結果，不虛稱成功。

- ai-dev 後續所有文件變更須在同一次修改同步維護同頁完整繁體中文與英文；共用程式與資料維持單一來源。僅 `templates/PROJECT-INTAKE.zh-TW.md` 與 `templates/PROJECT-INTAKE.en.md` 依明確要求例外分檔，兩者須同批同步。

## AI 新專案詢問義務

AI 啟動新專案時（不是單純瀏覽或維護既有專案），必須向使用者呈現全部八題或預填答案供確認，直接詢問每個缺漏或未確認的答案，可合併提問，並記錄回覆及待辦。已明確提供的答案沿用，不重複詢問、不猜測、不推定授權。第 1–5 題確認前，不得把範圍或 POC 計畫當作已議定，也不得把實作當作已批准；第 6–8 題可明確標記待定，但在相關 repo、分享、合併或部署操作前須解決。使用者無法回覆時，列出未答項並停在相關步驟之前。

[English ↓](#english)

<a id="english"></a>

# Execution rules

- Remain project-agnostic by default: use generic names and synthetic data in documentation, examples and evidence; do not add source-project names, identifiers, routes or project-specific acceptance details.

- Read README, SPEC and the current task authorization first; identify objectives, acceptance and prohibited scope.
- Assign one primary executor per task. Compare source versions before rereading changed evidence.
- Test one explicit hypothesis per round; retain fixed and failing samples. Obtain new evidence before retrying the same error under unchanged conditions.
- Keep changes and failures traceable. Never conflate simulation, HTTP, browser, application performance and publication acceptance.
- Do not upload images, secrets, private URLs/IDs or real user data. Examples use synthetic data only.
- Do not independently add schedules, change permissions, enable CI, push, merge or deploy. Publication requires specific authorization and verification.
- Run `python3 -m unittest discover -s tests -v` and the positive/negative examples. Preserve actual outcomes; never claim an unverified success.

- Every future ai-dev documentation change must update full Traditional Chinese and English together on the same page in the same change; shared code and data remain single-source. Only `templates/PROJECT-INTAKE.zh-TW.md` and `templates/PROJECT-INTAKE.en.md` are explicitly exempted as separate language files; update both together.

## Mandatory AI project intake

When AI initiates a new project (not merely browsing or maintaining an existing project), it MUST present all eight questions or prefilled answers for confirmation, directly ask the user for every missing or unconfirmed answer (questions may be batched), and record replies and open items. Reuse explicitly provided answers without asking again; do not guess or imply authorization. Confirm questions 1–5 before treating scope or a POC plan as agreed, or implementation as approved. Questions 6–8 may be explicitly marked TBD, but must be resolved before relevant repository, sharing, merge or deployment actions. If the user is unavailable, list unanswered items and stop before those steps.

[繁體中文 ↑](#zh-tw)
