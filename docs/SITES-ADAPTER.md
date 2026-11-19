[繁體中文](#zh-tw) | [English](#english)

<a id="zh-tw"></a>

# Sites adapter 整合指引（未配置）

核心應輸出來源 commit、產物及可信摘要；adapter 負責平台格式、授權、隔離、部署、健康與回復。不要在 core 放平台憑證。每個真實 adapter 需另外實作並驗收，不能將本機模擬器直接改名為 Sites 部署。

1. 明確取得建立獨立私人 staging 的授權，使用官方 Sites skill／工具，先讀取能力與當前版本。不可改正式站可見性來繞過登入。
2. 建立獨立站點，只用空／合成資料；確認無 production DB、R2、排行榜或外部正式 API 綁定。
3. 取得 CI exact SHA 對應產物與 digest，檢查來源與不含秘密。若平台重新封裝 manifest，分別記錄原始整包、Worker、平台包摘要與可證明的等價範圍。
4. 部署可辨識 baseline，readback 平台版本，執行 HTTP 預期值及瀏覽器啟動、輸入、停止。未登入成功即記 BLOCKED，不循環重試。
5. 同樣部署 candidate 並驗健康。平台寫入需版本保護；衝突則停止並重新對照，不覆寫他人版本。
6. 使用平台支援方式回復已知 baseline，重新讀回、比對摘要及健康／瀏覽器操作；失敗就保留診斷並回報，不稱安全完成。
7. 確認原正式環境未變，記錄可見性、限制及不同驗證層。staging 成功不授權 production，公開規則需再經審查與發布授權。

本檔無實際 Site URL／ID、token、CLI 祕密或自動部署設定。

[English ↓](#english)

<a id="english"></a>

# Sites adapter integration guide (not configured)

Core produces the source commit, artifact and trusted digest; the adapter owns platform format, permission, isolation, deployment, health and rollback. Keep platform credentials out of core. Every real adapter requires separate implementation and acceptance; renaming a local simulator does not make it a Sites deployment.

1. Obtain explicit authorization for separate private staging. Use the official Sites skill/tools and inspect capabilities and current versions. Never make production public to bypass login.
2. Create a separate site using empty/synthetic data. Verify absence of production DB, R2, leaderboard and external production API bindings.
3. Retrieve the artifact and digest for the exact CI SHA. Check provenance and absence of secrets. If the platform repackages its manifest, record original-package, Worker and platform-package digests separately, including the precise equivalence that can be proved.
4. Deploy an identifiable baseline, read back the platform version, then check HTTP expected values and browser startup, input and stop. If login fails, record BLOCKED; do not retry in a loop.
5. Deploy the candidate and check health in the same way. Use version protection for platform writes. On conflict, stop and compare again; do not overwrite another writer's version.
6. Restore the known baseline using supported platform operations, then read back and compare digests, health and browser behavior. Preserve diagnostics and report failure instead of claiming safe completion.
7. Verify the original production environment is unchanged. Record visibility, limitations and separate validation layers. Staging success does not authorize production; publishing rules still requires review and publication permission.

This file contains no real Site URL/ID, token, CLI secret or automatic deployment configuration.

[繁體中文 ↑](#zh-tw)
