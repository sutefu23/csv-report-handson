import csv


def load_sales(path):
    """売上CSVを読み込んで辞書のリストを返す。"""
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(
                {
                    "日付": row["日付"],
                    "カテゴリ": row["カテゴリ"],
                    "商品名": row["商品名"],
                    "単価": int(row["単価"]),
                    "数量": int(row["数量"]),
                }
            )
    return rows
