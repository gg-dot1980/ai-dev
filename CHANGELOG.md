[繁體中文](#zh-tw) | [English](#english)

<a id="zh-tw"></a>

# 變更紀錄

## 0.1.0 — 2026-11-19

- 初始公開 POC：工作流規格、AGENTS、PR／review／交接模板與 Sites adapter 指引。
- 純 Python 合成產物、SHA-256、fail-closed 模擬部署／健康／回復。
- 9 個固定測試、兩個乾淨目錄驗證、確定性建置及損毀負案例。
- 無實際部署設定、無外部 CI 配置、無獨立強制 review／merge gate；不是 OCR4 或 production 驗收。

- 文件 patch：每份 Markdown 同頁完整中英文與語言導覽，程式與 JSON 維持單一來源；程式行為與驗收門檻未變，重跑測試並同步證據。

## Patch 規則

每次 patch 記錄目的、真實程式改動、版本、測試命令、通過／失敗／未測、產物摘要與限制，並同步 evidence 與交接。不可只改版本號或 release note 冒充功能進度。

[English ↓](#english)

<a id="english"></a>

# Changelog

## 0.1.0 — 2026-11-19

- Initial public POC: workflow specification, AGENTS, PR/review/handoff templates and Sites adapter guidance.
- Pure Python synthetic artifacts, SHA-256 and fail-closed simulated deployment, health and rollback.
- Nine fixed tests, validation in two clean directories, deterministic builds and corrupted-artifact negative cases.
- No actual deployment setup, external CI configuration or independently enforced review/merge gate; not OCR4 or production acceptance.
- Documentation patch: full Traditional Chinese and English coexist on each Markdown page with language navigation; code and JSON remain single-source. Code behavior and acceptance thresholds are unchanged; tests and evidence were rerun/synchronized.

## Patch policy

Every patch records purpose, actual code changes, version, test commands, passed/failed/untested outcomes, artifact digests and limitations, synchronizing evidence and handoff. Changing only a version or release note is not functional progress.

[繁體中文 ↑](#zh-tw)
