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

- ai-dev 後續所有文件變更須在同一次修改同步維護同頁完整繁體中文與英文；共用程式與資料維持單一來源。

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

- Every future ai-dev documentation change must update full Traditional Chinese and English together on the same page in the same change; shared code and data remain single-source.

[繁體中文 ↑](#zh-tw)
