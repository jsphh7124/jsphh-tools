---
name: gogcli
description: 使用 gogcli (gog) 指令列工具存取 Google 服務（Gmail, Calendar, Drive, Sheets 等），適用於自動化腳本與 AI Agent 資料存取。Mac 使用 ~/bin/gog；Windows 使用 gog.exe（需另行安裝）。
---

# gogcli — Google Suite 終端機存取技能

## 概述

`gogcli`（指令名稱為 `gog`）是一個開源的 Google Suite CLI 工具，可透過終端機指令直接存取 Gmail、Google Calendar、Google Drive、Google Sheets 等服務。輸出為 JSON 格式，適合 AI Agent 解析與自動化流程整合。

- **版本**：v0.11.0（2026-02-15 發布）
- **GitHub**：https://github.com/steipete/gogcli
- **Mac 安裝路徑**：`~/bin/gog`
- **Windows 安裝**：下載 `gogcli_0.11.0_windows_amd64.zip` 並加入 PATH

---

## 安裝（Mac，首次設定）

```bash
# 下載並安裝 binary（Apple Silicon M系列）
mkdir -p ~/bin
curl -L "https://github.com/steipete/gogcli/releases/download/v0.11.0/gogcli_0.11.0_darwin_arm64.tar.gz" -o /tmp/gogcli.tar.gz
tar -xzf /tmp/gogcli.tar.gz -C /tmp/
mv /tmp/gog ~/bin/gog
chmod +x ~/bin/gog

# 確保 ~/bin 在 PATH 中（加入 ~/.zprofile）
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# 驗證安裝
gog --version
```

## 安裝（Windows，首次設定）

1. 下載：https://github.com/steipete/gogcli/releases/download/v0.11.0/gogcli_0.11.0_windows_amd64.zip
2. 解壓縮，將 `gog.exe` 移至 `C:\Users\<YourName>\bin\`
3. 將該資料夾加入系統 PATH
4. 在 PowerShell 中執行 `gog --version` 驗證

---

## 首次授權（OAuth2 設定）

首次使用前需設定 Google OAuth2 憑證：

```bash
# 初始化授權（會開啟瀏覽器進行 Google 登入）
gog auth login

# 確認授權狀態
gog auth status
```

詳細 OAuth2 設定步驟請參考官方文件：https://github.com/steipete/gogcli#quick-start

---

## 常用指令參考

### Gmail
```bash
gog gmail list                          # 列出最新信件
gog gmail search "subject:ESM研究"      # 搜尋信件
gog gmail send --to user@example.com --subject "主旨" --body "內容"
```

### Google Calendar
```bash
gog calendar list                       # 列出近期行程
gog calendar list --days 7              # 列出未來 7 天行程
gog calendar create --title "研究會議" --start "2026-03-01T14:00" --end "2026-03-01T15:00"
```

### Google Drive
```bash
gog drive ls                            # 列出 Drive 根目錄
gog drive search "問卷資料"             # 搜尋檔案
gog drive download <file_id>            # 下載檔案
```

### Google Sheets
```bash
gog sheets read <spreadsheet_id>        # 讀取試算表全部內容
gog sheets read <spreadsheet_id> --sheet "Sheet1" --range "A1:D100"
gog sheets write <spreadsheet_id> --range "A1" --values '[["資料1","資料2"]]'
```

### Google Tasks
```bash
gog tasks list                          # 列出所有任務
gog tasks add --title "新增任務"
```

---

## JSON 輸出模式

所有指令加上 `--json` 旗標可輸出結構化 JSON，適合 AI Agent 解析：

```bash
gog calendar list --json
gog gmail list --json | jq '.[]  .subject'
```

---

## 多帳號管理

```bash
gog auth login --account work           # 登入研究室帳號
gog auth login --account personal       # 登入個人帳號
gog calendar list --account work        # 用特定帳號執行指令
```

---

## 對喬瑟夫教授的應用場景

1. **ESM 研究資料監控**：直接讀取 Google Sheets 中的每日問卷填答，Anita/安安即時分析
2. **行程整合**：查詢 Google Calendar 行程，協助安排研究會議或截止日提醒
3. **文件自動下載**：從 Google Drive 取得最新版本的研究文件或量表
4. **Gmail 快速搜尋**：在不開啟瀏覽器的情況下搜尋特定郵件

---

## 升級指令

```bash
# Mac：重新下載最新版本（替換舊 binary）
curl -L "https://github.com/steipete/gogcli/releases/latest/download/gogcli_darwin_arm64.tar.gz" -o /tmp/gogcli.tar.gz
tar -xzf /tmp/gogcli.tar.gz -C ~/bin/ --overwrite
```
