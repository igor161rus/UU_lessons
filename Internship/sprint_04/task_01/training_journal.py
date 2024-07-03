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
        self.state = {'edit': False}

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

        self.edit_button_exercise = ttk.Button(self.root, text="Редактировать", command=self.edit_record_exercise)
        self.edit_button_exercise.grid(column=4, row=8, columnspan=1)

        self.delete_button_exercise = ttk.Button(self.root, text="Удалить", command=self.delete_record_exercise)
        self.delete_button_exercise.grid(column=5, row=8, columnspan=1)

        self.button_csv = ttk.Button(self.root, text="Экспорт в CSV", command=self.export_all_records_csv)
        self.button_csv.grid(column=0, row=9, columnspan=1)

        self.button_iport_csv = ttk.Button(self.root, text="Импорт из CSV", command=self.import_records_csv)
        self.button_iport_csv.grid(column=1, row=9, columnspan=1)

        self.stat_label = ttk.Label(self.root, text="Статистика:")
        self.stat_label.grid(column=4, row=0, pady=5)

        self.stat_label_exercise = ttk.Label(self.root, text="Кол-во упражнении:")
        self.stat_label_exercise.grid(column=3, row=1, pady=5)

        self.stat_label_weight = ttk.Label(self.root, text="Суммарный вес:")
        self.stat_label_weight.grid(column=3, row=2, pady=5)

        self.stat_label_exercise_sum = ttk.Label(self.root, text="0")
        self.stat_label_exercise_sum.grid(column=4, row=1, pady=5)

        self.stat_label_weight_sum = ttk.Label(self.root, text="0")
        self.stat_label_weight_sum.grid(column=4, row=2, pady=5)

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
        self.statistics()

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
        with open('training_log.csv', 'r', newline='') as file:
            csv_reader = csv.DictReader(file)
            data = []
            for row in csv_reader:
                data.append(row)
            save_data(data)

    def load_exercise(self):
        """
        Загружает список упражнение из JSON-файла.
        """
        data = load_data()
        for entry in data:
            if entry['exercise'] == self.view_exercise_entry.get():
                self.exercise_entry.delete(0, tk.END)
                self.weight_entry.delete(0, tk.END)
                self.repetitions_entry.delete(0, tk.END)
                self.exercise_entry.insert(0, entry['exercise'])
                self.weight_entry.insert(0, str(entry['weight']))
                self.repetitions_entry.insert(0, str(entry['repetitions']))
                self.view_button_exercise.config(text='Cохранить')
                self.state['edit'] = True
                break
        self.statistics()

    def edit_record_exercise(self):
        """
        Редактирует данные о тренировке.
        """
        if self.state['edit']:
            data = load_data()
            for entry in data:
                if entry['exercise'] == self.view_exercise_entry.get():
                    self.state['edit'] = False
                    self.view_button_exercise.config(text='Редактировать')
                    entry['exercise'] = self.exercise_entry.get()
                    entry['weight'] = self.weight_entry.get()
                    entry['repetitions'] = self.repetitions_entry.get()
                    save_data(data)
                    self.exercise_entry.delete(0, tk.END)
                    self.weight_entry.delete(0, tk.END)
                    self.repetitions_entry.delete(0, tk.END)
                    self.view_exercise_entry.delete(0, tk.END)
                    messagebox.showinfo("Успешно", "Запись успешно отредактирована!")
                    self.statistics()
                    break
            return
        else:
            self.load_exercise()

    def delete_record_exercise(self):
        """
        Удаляет данные о тренировке.
        """
        data = load_data()
        for entry in data:
            if entry['exercise'] == self.view_exercise_entry.get():
                data.remove(entry)
                save_data(data)
                self.exercise_entry.delete(0, tk.END)
                self.weight_entry.delete(0, tk.END)
                self.repetitions_entry.delete(0, tk.END)
                self.view_exercise_entry.delete(0, tk.END)
                messagebox.showinfo("Успешно", "Запись успешно удалена!")
                self.statistics()
                break

    def statistics(self):
        """
        Статистика по тренировкам.
        """
        data = load_data()
        data.sort(key=lambda x: x['date'])
        exercises = 0
        weights = 0
        for entry in data:
            exercises += 1
            weights += int(entry['weight'])
        self.stat_label_exercise_sum.config(text=exercises)
        self.stat_label_weight_sum.config(text=weights)


def main():
    root = tk.Tk()
    app = TrainingLogApp(root)
    root.after_idle(app.statistics)
    root.mainloop()


if __name__ == "__main__":
    main()
