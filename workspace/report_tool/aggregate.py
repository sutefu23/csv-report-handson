from collections import defaultdict


def filter_by_month(rows, month):
    """指定した月（例: "2026-05"）の行だけを返す。"""
    return [r for r in rows if r["日付"].startswith(month)]


def category_summary(rows):
    """カテゴリごとの売上合計・数量合計・平均単価を集計する。"""
    sales = defaultdict(int)
    qty = defaultdict(int)
    for r in rows:
        amount = r["単価"] * abs(r["数量"])
        sales[r["カテゴリ"]] += amount
        qty[r["カテゴリ"]] += r["数量"]

    summary = {}
    for cat in sales:
        summary[cat] = {
            "売上合計": sales[cat],
            "数量合計": qty[cat],
            "平均単価": sales[cat] / qty[cat],
        }
    return summary


def total_sales(summary):
    """全カテゴリの売上合計を返す。"""
    return sum(v["売上合計"] for v in summary.values())
