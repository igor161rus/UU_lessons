import csv
import tkinter as tk
from tkinter import ttk, Toplevel, messagebox
import json
from datetime import datetime

# Файл для сохранения данных
data_file = 'training_log.json'


def load_data():
    """Загрузка данных о тренировках из файла."""
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(data):
    """Сохранение данных о тренировках в файл."""
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)


class TrainingLogApp:
    def __init__(self, root):
        self.root = root
        root.title("Дневник тренировок")
        self.create_widgets()

    def create_widgets(self):
        # Виджеты для ввода данных
        self.exercise_label = ttk.Label(self.root, text="Упражнение:")
        self.exercise_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.exercise_entry = ttk.Entry(self.root)
        self.exercise_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

        self.weight_label = ttk.Label(self.root, text="Вес:")
        self.weight_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.weight_entry = ttk.Entry(self.root)
        self.weight_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        self.repetitions_label = ttk.Label(self.root, text="Повторения:")
        self.repetitions_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.repetitions_entry = ttk.Entry(self.root)
        self.repetitions_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        self.add_button = ttk.Button(self.root, text="Добавить запись", command=self.add_entry)
        self.add_button.grid(column=0, row=3, columnspan=2, pady=10)

        self.record_label = ttk.Label(self.root, text="Просмотреть записи")
        self.record_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

        self.view_button = ttk.Button(self.root, text="Все", command=self.view_records)
        self.view_button.grid(column=0, row=5, columnspan=1)

        self.view_button_period = ttk.Button(self.root, text="За период", command=self.view_records_period)
        self.view_button_period.grid(column=1, row=5, columnspan=1)

        self.in_label = ttk.Label(self.root, text="c")
        self.in_label.grid(column=0, row=6, sticky=tk.E, padx=5, pady=5)

        self.date_entry_in = ttk.Entry(self.root)
        self.date_entry_in.grid(column=1, row=6, padx=5, pady=5)

        self.out_label = ttk.Label(self.root, text="по")
        self.out_label.grid(column=0, row=7, sticky=tk.E, pady=5)

        self.date_entry_out = ttk.Entry(self.root)
        self.date_entry_out.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)

        self.view_exercise = ttk.Label(self.root, text="Просмотр упражнения:")
        self.view_exercise.grid(column=0, row=8, sticky=tk.E, pady=5)

        self.view_exercise_entry = ttk.Entry(self.root)
        self.view_exercise_entry.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

        self.view_button_exercise = ttk.Button(self.root, text="Просмотр", command=self.view_record_exercise)
        self.view_button_exercise.grid(column=3, row=8, columnspan=1)

        self.button_csv = ttk.Button(self.root, text="Экспорт в CSV", command=self.export_all_records_csv)
        self.button_csv.grid(column=0, row=9, columnspan=1)

        self.button_iport_csv = ttk.Button(self.root, text="Импорт из CSV", command=self.import_records_csv)
        self.button_iport_csv.grid(column=1, row=9, columnspan=1)

    def add_entry(self):
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        exercise = self.exercise_entry.get()
        weight = self.weight_entry.get()
        repetitions = self.repetitions_entry.get()

        if not (exercise and weight and repetitions):
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
            return

        entry = {
            'date': date,
            'exercise': exercise,
            'weight': weight,
            'repetitions': repetitions
        }

        data = load_data()
        data.append(entry)
        save_data(data)

        # Очистка полей ввода после добавления
        self.exercise_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.repetitions_entry.delete(0, tk.END)
        messagebox.showinfo("Успешно", "Запись успешно добавлена!")

    def view_records(self):
        data = load_data()
        records_window = Toplevel(self.root)
        records_window.title("Записи тренировок")

        tree = ttk.Treeview(records_window, columns=("Дата", "Упражнение", "Вес", "Повторения"), show="headings")
        tree.heading('Дата', text="Дата")
        tree.heading('Упражнение', text="Упражнение")
        tree.heading('Вес', text="Вес")
        tree.heading('Повторения', text="Повторения")

        for entry in data:
            tree.insert('', tk.END, values=(entry['date'], entry['exercise'], entry['weight'], entry['repetitions']))

        tree.pack(expand=True, fill=tk.BOTH)

    def view_records_period(self):
        """
        Отображает данные о тренировках за период в новом окне.
        """
        data = load_data()
        records_window = Toplevel(self.root)
        records_window.title("Записи тренировок")

        tree = ttk.Treeview(records_window, columns=("Дата", "Упражнение", "Вес", "Повторения"), show="headings")
        tree.heading('Дата', text="Дата")
        tree.heading('Упражнение', text="Упражнение")
        tree.heading('Вес', text="Вес")
        tree.heading('Повторения', text="Повторения")

        for entry in data:
            if entry['date'] >= self.date_entry_in.get() and entry['date'] <= self.date_entry_out.get() + " 23:59:59":
                tree.insert('', tk.END,
                            values=(entry['date'], entry['exercise'], entry['weight'], entry['repetitions']))
        tree.pack(expand=True, fill=tk.BOTH)

    def view_record_exercise(self):
        """
        Отображает данные о тренировке в новом окне.
        """
        data = load_data()
        records_window = Toplevel(self.root)
        records_window.title("Запись тренировки")

        tree = ttk.Treeview(records_window, columns=("Дата", "Упражнение", "Вес", "Повторения"), show="headings")
        tree.heading('Дата', text="Дата")
        tree.heading('Упражнение', text="Упражнение")
        tree.heading('Вес', text="Вес")
        tree.heading('Повторения', text="Повторения")

        for entry in data:
            if entry['exercise'] == self.view_exercise_entry.get():
                tree.insert('', tk.END,
                            values=(entry['date'], entry['exercise'], entry['weight'], entry['repetitions']))
        tree.pack(expand=True, fill=tk.BOTH)

    def export_all_records_csv(self):
        """
        Экспортирует данные о тренировках в CSV-файл.
        """
        data = load_data()
        with open('training_log.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'exercise', 'weight', 'repetitions'])
            for entry in data:
                writer.writerow([entry['date'], entry['exercise'], entry['weight'], entry['repetitions']])

    def import_records_csv(self):
        """
        Импортирует данные о тренировках из CSV-файла.
        """
        data = {}
        with open('training_log.csv', 'r', newline='') as file:
            csv_reader = csv.DictReader(file)
            # reader = csv.reader(file)
            for rows in csv_reader:
                # if row[0] == 'date' or row[1] == 'exercise' or row[2] == 'weight' or row[3] == 'repetitions':
                #     continue
                # self.add_entry(row[0], row[1], row[2], row[3])
                key = rows[0]

            next(reader)  # Пропускаем заголовок
            data = [row for row in reader]
            save_data(data)


def main():
    root = tk.Tk()
    app = TrainingLogApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
