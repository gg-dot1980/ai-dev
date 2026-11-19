[繁體中文](#zh-tw) | [English](#english)

<a id="zh-tw"></a>

# AI 開發工作流 v0.1.0 POC

這是已獲准公開的 v0.1.0 概念驗證（POC）。公開此工具包不等於完整部署流程或生產驗收。目標是把規格、測試、可追溯產物、部署、健康檢查、回復與交接拆成可驗證步驟。**不是 OCR4 策略或生產發布許可。**

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
2. 已觀察的 Slime 流程：私人 staging 基線、候選、回復各 9/9 HTTP，回復 hash 一致；CI Worker 位元一致，平台重新封裝 manifest，所以整包位元一致未成立。v2.13 瀏覽器啟動、輸入與停止已成功。這是有限範圍流程證據，不代表各版本遊戲勝率、正式站或生產發布門檻通過。
3. 獨立強制 review／merge gate：Slime 未配置或核實；本草稿也不配置。作者自己勾選 review、CI 綠燈或 Draft PR 不能替代獨立審查與平台強制措施。

## 發布規則

先讀最新規格、來源 commit、證據及限制，再由不同於作者的審查者檢查。記錄欲發布的確切 commit／digest、目的地、資料可見性、範圍、回復方案，以及使用者明確授權。公開文件推送、合併、staging 部署及 production 部署各是不同動作；一者不推定授權其他動作。此包沒有外部 CI workflow 或部署設定，避免把文件誤當已啟用的安全措施。

## 後續 patches

每個增量 patch 同步修改程式、固定測試、合成證據與 [CHANGELOG](CHANGELOG.md)，更新 [VERSION](VERSION)。保留原失敗案例，對相同來源 SHA 重新驗證；未測項不能列為通過。使用 Draft PR 進行審查，發布前核對授權範圍與遠端內容。

各 Markdown 頁完整中英文並存並提供語言導覽；程式與 JSON 維持單一來源。

[English ↓](#english)

<a id="english"></a>

# AI Development Workflow v0.1.0 POC

This v0.1.0 proof of concept is authorized for public publication. Publishing this toolkit is not acceptance of a complete deployment workflow or production readiness. Its purpose is to separate specifications, tests, traceable artifacts, deployment, health checks, rollback and handoff into verifiable stages. **It is neither an OCR4 strategy nor production-release permission.**

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
2. Observed Slime workflow: private staging baseline, candidate and rollback each passed 9/9 HTTP checks, with matching rollback hashes. CI Worker bytes matched, but the platform repackaged the manifest, so whole-package byte identity was not established. Browser startup, input and stop succeeded for v2.13. This limited workflow evidence does not establish cross-version game win rates, production-site acceptance or production release gates.
3. Independently enforced review/merge gates: not configured or verified in Slime; this POC does not configure them either. An author's checkbox, green CI or Draft PR cannot substitute for independent review and platform enforcement.

## Publication rules

Read the current specification, source commit, evidence and limitations, then obtain review by someone other than the author. Record the exact commit/digest, destination, data visibility, scope, rollback plan and explicit user authorization. Public document push, merge, staging deployment and production deployment are separate actions; permission for one does not imply the others. This package includes no external CI workflow or deployment configuration; documentation is not an enabled security control.

## Subsequent patches

Each incremental patch must synchronize code, fixed tests, synthetic evidence and [CHANGELOG](CHANGELOG.md), and update [VERSION](VERSION). Retain failure cases and revalidate against the same source SHA. Untested items cannot be marked passed. Use Draft PR review, then verify authorization scope and remote contents before publication. Full Traditional Chinese and English documentation coexist on each page; code and JSON remain single-source.

[繁體中文 ↑](#zh-tw)
