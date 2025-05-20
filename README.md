# BusinessSlideVQA
このリポジトリでは、ビジネス資料（スライド）を対象とした Visual Question Answering (VQA) ベンチマーク「BusinessSlideVQA」を提供しています。


各PDFファイルのライセンスの都合上、PDFや画像そのものは配布せず、代わりに利用者の方がダウンロード及び変換するためのスクリプトとQAペアのみを公開しています。

---

##  内容

- `pdf_urls.txt`：PDFスライドの公開URL一覧
- `vqa.json`：スライド画像に対する質問と回答のペア（画像ファイル名と対応）
- `scripts/download_and_convert.py`：PDFをダウンロードし、PNG画像に変換するスクリプト

---

## セットアップ手順

### 1. Pythonの依存ライブラリをインストール

Python 3.8以降が必要です。

```bash
pip install requests tqdm pdf2image
```

### 2. Poppler のインストール（PDF→画像変換に必要）

- **macOS**:
  ```bash
  brew install poppler
  ```

- **Ubuntu/Debian**:
  ```bash
  sudo apt install poppler-utils
  ```
---

##  PDFのダウンロードとPNG変換

次のコマンドを実行してください：

```bash
python scripts/download_and_convert.py
```

- PDFは `downloads/pdfs/` に保存されます。
- PNG画像は `downloads/pngs/` にページ単位で保存されます（例: `0a0b15306ac2e5b6e1bdcac515aa2e6b3257d17cd736df72f3a77b0a70c43c5c_page_001.png`）。

---

## QAデータセットについて

変換された画像に対する質問と回答の対応は `vqa.json` に記述されています。以下はその例です：

```json
{
  "question_id": 0,
  "image type": "テキスト",
  "image": "000ef93d430a2cbf484fa1577419bd709609cb5bede5627365e2e107a079cdc3_page_003.png",
  "question": "令和6年度1月判断では、総括判断はどのようになっていますか。",
  "answer": "10地域で据え置きとなりました。"
}
```

画像のおおまかな内訳は以下の通りです。
スライドのため厳密な分類をしていません。


| 画像種別           |         件数 |
| :----------------- | -----------: |
| 画像               |           51 |
| テキスト           |           36 |
| 表                 |           35 |
| 棒グラフ           |           30 |
| 折れ線グラフ       |           18 |
| 円グラフ           |           16 |
| 積み上げ棒グラフ   |           13 |
| その他             |           21 |
| **合計**           |      **220** |

---

##  ライセンス

QAペア（`vqa.json`）およびスクリプトは[MIT License](LICENSE)のもとで公開されています。

---
