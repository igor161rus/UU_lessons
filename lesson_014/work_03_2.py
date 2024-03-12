import calendar

calendar_text = calendar.TextCalendar()
print(calendar_text.formatmonth(2024, 3))

calendar_html = calendar.HTMLCalendar()
print(calendar_html.formatmonth(2025, 1))

day_iterator = calendar_text.itermonthdays2(2025, 1)
number_of_working_days = 0

for data, weekday in day_iterator:
    if data > 0 and weekday < 5:
        number_of_working_days += 1
print(f'В январе 2025 {number_of_working_days} рабочих дней')
print(f'Дни февраля 2025 года в списках по неделям {calendar_text.monthdayscalendar(2025, 2)}')

for month in calendar.month_name:
    print(month)
for day in calendar.day_name:
    print(day)