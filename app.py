import streamlit as st
import datetime
import pytz

DEADLINE = datetime.datetime(2024, 1, 9, tzinfo=pytz.timezone('Asia/Tokyo'))

def calc_remaining_days_without_weekend(today:datetime.datetime, remaining_days:int) -> int:
    remaining_days_without_weekend = 0
    for i in range(remaining_days):
        day = today + datetime.timedelta(days=i)
        if day.weekday() < 5:  # 0-4 corresponds to Monday to Friday
            remaining_days_without_weekend += 1
    return remaining_days_without_weekend

def calc_remaining_days(today:datetime.datetime) -> int:
    remaining_days = (DEADLINE - today).days
    return max(0, remaining_days)

def main():
    st.title('卒論の締め切りまでの残り日数')
    st.write('2024年1月9日までの残り日数を表示します。')
    today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    st.write(f'現在時刻は{today.strftime("%Y年%m月%d日 %H時%M分")}です。')
    remaining_days = calc_remaining_days(today)
    st.write(f'土日を含めてあと{remaining_days}日です。')
    remaining_days_without_weekend = calc_remaining_days_without_weekend(today, remaining_days)
    st.write(f'土日を除いてあと{remaining_days_without_weekend}日です。')

if __name__ == '__main__':
    main()