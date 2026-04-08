---
name: conversation-purger
description: 用於刪除 Antigravity 對話歷史紀錄 (.pb 檔案) 及相關任務產出 (brain 資料夾)。提供列出歷史、刪除指定對話、清理最近一次對話等功能。
---

# 對話紀錄清理工具 (Conversation Purger)

本 Skill 提供自動化腳本，用於清理 Antigravity 的對話歷史紀錄與相關 artifacts，以維護隱私或維持系統整潔。

## 使用觸發條件 (Triggers)

- 使用者指示「刪除本次對話」或「這段對話不要記錄」。
- 使用者要求「清理舊的對話歷史」。
- 使用者希望「隱私瀏覽」或「不留痕跡」的操作。

## 核心功能與腳本路徑

- **腳本路徑**: `C:\Users\黃敦群\.gemini\antigravity\skills\conversation-purger\scripts\purger.py`
- **主要操作**:
  1. **列出歷史**: 列出所有 `.pb` 檔案及其時間、大小。
  2. **刪除指定對話**: 移除 `conversations/` 下的 `.pb` 檔案及 `brain/` 下的對應資料夾。
  3. **清理最後一次對話**: 自動識別最近結束的對話並清理。

## 使用指南 (How to Use)

### 1. 列出所有對話紀錄
使用 Python 執行腳本並帶入 `list` 參數：
```bash
python "C:\Users\黃敦群\.gemini\antigravity\skills\conversation-purger\scripts\purger.py" list
```

### 2. 刪除特定 ID 的對話
```bash
python "C:\Users\黃敦群\.gemini\antigravity\skills\conversation-purger\scripts\purger.py" delete <conversation-id>
```

### 3. 清理「上一個」對話 (不含當前)
```bash
python "C:\Users\黃敦群\.gemini\antigravity\skills\conversation-purger\scripts\purger.py" purge-last
```

## 重要聲明 (Warnings)

- **不可還原**: 刪除操作是永久性的，無法從資源回收筒還原。
- **當前對話限制**: 刪除「當前正在進行的對話」可能會導致系統行為異常，建議在對話結束後或開啟新對話前執行。
- **Notion 同步**: 本腳本**不會**刪除已同步到 Notion 的內容，需手動到 Notion 頁面處理。

---
*Created on: 2026-02-02*
