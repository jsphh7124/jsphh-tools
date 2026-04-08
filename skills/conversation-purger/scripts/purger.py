import os
import shutil
import sys
import argparse
from datetime import datetime

# 基本目錄設定
BASE_DIR = os.path.join(os.path.expanduser('~'), '.gemini', 'antigravity')
CONV_DIR = os.path.join(BASE_DIR, 'conversations')
BRAIN_DIR = os.path.join(BASE_DIR, 'brain')

def list_conversations():
    if not os.path.exists(CONV_DIR):
        print("未找到對話目錄。")
        return []

    files = [f for f in os.listdir(CONV_DIR) if f.endswith('.pb')]
    convs = []
    
    for f in files:
        path = os.path.join(CONV_DIR, f)
        stat = os.stat(path)
        conv_id = f.replace('.pb', '')
        convs.append({
            'id': conv_id,
            'time': datetime.fromtimestamp(stat.st_mtime),
            'size': stat.st_size / 1024, # KB
            'path': path
        })
    
    # 按時間排序 (最新的在前面)
    convs.sort(key=lambda x: x['time'], reverse=True)
    
    print(f"{'Index':<6} {'Conversation ID':<40} {'Last Modified':<20} {'Size (KB)':<10}")
    print("-" * 80)
    for i, c in enumerate(convs):
        print(f"{i:<6} {c['id']:<40} {c['time'].strftime('%Y-%m-%d %H:%M:%S'):<20} {c['size']:<10.2f}")
    
    return convs

def delete_conversation(conv_id):
    deleted_items = []
    
    # 1. 刪除 .pb 檔案
    pb_file = os.path.join(CONV_DIR, f"{conv_id}.pb")
    if os.path.exists(pb_file):
        try:
            os.remove(pb_file)
            deleted_items.append(f"History file: {pb_file}")
        except Exception as e:
            print(f"無法刪除歷史檔案 {pb_file}: {e}")

    # 2. 刪除 brain 資料夾
    brain_folder = os.path.join(BRAIN_DIR, conv_id)
    if os.path.exists(brain_folder):
        try:
            shutil.rmtree(brain_folder)
            deleted_items.append(f"Brain folder: {brain_folder}")
        except Exception as e:
            print(f"無法刪除 Brain 資料夾 {brain_folder}: {e}")

    if deleted_items:
        print(f"成功清理對話 {conv_id}:")
        for item in deleted_items:
            print(f"  - {item}")
    else:
        print(f"未找到對話 {conv_id} 的相關檔案。")

def main():
    parser = argparse.ArgumentParser(description='Antigravity 對話紀錄清理工具')
    parser.add_argument('action', choices=['list', 'delete', 'purge-last'], help='操作類型')
    parser.add_argument('id', nargs='?', help='對話 ID (僅 delete 用)')

    args = parser.parse_args()

    if args.action == 'list':
        list_conversations()
    
    elif args.action == 'delete':
        if not args.id:
            print("錯誤: 執行 delete 操作需要提供對話 ID。")
            sys.exit(1)
        delete_conversation(args.id)
    
    elif args.action == 'purge-last':
        convs = list_conversations()
        if len(convs) < 2:
            print("沒有足夠的歷史對話可供清理。")
            return
        
        # 排除當前對話 (第一個通常是當前)，清理上一個
        last_conv = convs[1]
        print(f"\n準備清理上一個對話: {last_conv['id']}")
        delete_conversation(last_conv['id'])

if __name__ == "__main__":
    main()
