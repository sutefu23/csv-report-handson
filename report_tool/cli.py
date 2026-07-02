import argparse

from .aggregate import category_summary, filter_by_month, total_sales
from .loader import load_sales


def build_report(summary, month):
    lines = [f"# 売上レポート {month}", ""]
    lines.append(f"総売上: {total_sales(summary)}円")
    lines.append("")
    lines.append("| カテゴリ | 売上合計 | 数量合計 | 平均単価 |")
    lines.append("|---|---|---|---|")
    for cat, v in summary.items():
        lines.append(
            f"| {cat} | {v['売上合計']}円 | {v['数量合計']} | {v['平均単価']:.0f}円 |"
        )
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description="売上CSVから月次レポートを生成する")
    parser.add_argument("csv_path", help="売上CSVのパス")
    parser.add_argument("--month", required=True, help="対象月 (例: 2026-05)")
    parser.add_argument("--out", default=None, help="出力先 (省略時: report_<月>.md)")
    args = parser.parse_args()

    rows = load_sales(args.csv_path)
    monthly = filter_by_month(rows, args.month)
    summary = category_summary(monthly)
    report = build_report(summary, args.month)

    out_path = args.out or f"report_{args.month}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"レポートを書き出しました: {out_path}")


if __name__ == "__main__":
    main()
