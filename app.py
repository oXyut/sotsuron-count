# 卒論の締め切り（2024年1月9日）までの残り日数を表示するアプリをstreamlitで作成
import streamlit as st
import datetime

DEADLINE = datetime.datetime(2024, 1, 9)

def to_japan_time(dt: datetime.datetime):
    # 日本時間に変換する
    return dt + datetime.timedelta(hours=9)

def calc_remaining_days_without_weekend(today:datetime.datetime, remaining_days:int) -> int:
    # 土日を除いた残りの日付を計算
    today = to_japan_time(today)
    remaining_days_without_weekend = remaining_days
    for i in range(remaining_days):
        if today.weekday() in [5, 6]:
            remaining_days_without_weekend -= 1
        today += datetime.timedelta(days=1)
    return remaining_days_without_weekend

def calc_remaining_days() -> int:
    today = datetime.datetime.today()
    remaining_days = (to_japan_time(DEADLINE) - to_japan_time(today)).days
    return remaining_days


def main():
    st.title('卒論の締め切りまでの残り日数')
    st.write('2024年1月9日までの残り日数を表示します。')
    today = datetime.datetime.today()
    # 何時何分何秒も含めて表示
    # 例：2021年1月1日 12:34
    # 日本時間に変換する
    st.write(f'現在時刻は{to_japan_time(today).strftime("%Y年%m月%d日 %H時%M分")}です。')
    remaining_days = calc_remaining_days()
    st.write(f'土日を含めてあと{remaining_days}日です。')
    # 表示
    remaining_days_without_weekend = calc_remaining_days_without_weekend(today, remaining_days)
    st.write(f'土日を除いてあと{remaining_days_without_weekend}日です。')


if __name__ == '__main__':
    main()