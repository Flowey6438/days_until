from datetime import datetime

def days_until(target_date):
    today = datetime.today()
    delta = target_date - today
    return delta.days

if __name__ == "__main__":
    print("欢迎使用倒数计日器！")
    
    try:
        year = int(input("请输入目标年份（例如2024）："))
        month = int(input("请输入目标月份（例如8）："))
        day = int(input("请输入目标日期（例如20）："))

        target_date = datetime(year, month, day)
        days_left = days_until(target_date)

        if days_left > 0:
            print(f"距离 {year}-{month:02d}-{day:02d} 还有 {days_left} 天。")
        elif days_left == 0:
            print(f"今天就是 {year}-{month:02d}-{day:02d} ！")
        else:
            print(f"{year}-{month:02d}-{day:02d} 已经过了 {-days_left} 天。")
    except ValueError:
        print("无效的日期输入，请输入有效的日期。")
