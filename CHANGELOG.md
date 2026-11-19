# 變更紀錄

## 0.1.0 — 2026-11-19

- 初始公開 POC：工作流規格、AGENTS、PR／review／交接模板與 Sites adapter 指引。
- 純 Python 合成產物、SHA-256、fail-closed 模擬部署／健康／回復。
- 9 個固定測試、兩個乾淨目錄驗證、確定性建置及損毀負案例。
- 無實際部署設定、無外部 CI 配置、無獨立強制 review／merge gate；不是 OCR4 或 production 驗收。

## Patch 規則

每次 patch 記錄目的、真實程式改動、版本、測試命令、通過／失敗／未測、產物摘要與限制，並同步 evidence 與交接。不可只改版本號或 release note 冒充功能進度。
