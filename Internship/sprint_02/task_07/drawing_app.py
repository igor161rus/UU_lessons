import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, ttk
from PIL import Image, ImageDraw


class DrawingApp:
    def __init__(self, root):
        # Инициализация option_var
        self.preview_color = None
        self.text_past = None
        self.option_var = tk.StringVar(root)
        self.root = root
        self.root.title("Рисовалка с сохранением в PNG")

        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.setup_ui()

        self.last_x, self.last_y = None, None
        self.pen_color = 'black'
        self.last_color = self.pen_color

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        # Привязываем обработчик события <Button-3> к холсту, чтобы выбрать цвет
        self.canvas.bind('<Button-3>', self.pick_color)

        # Привязываем обработчик события <Control-s> для сохранения изображения
        self.root.bind('<Control-s>', self.save_image)

        # Привязываем обработчик события <Control-c> для выбора цвета
        self.root.bind('<Control-c>', self.choose_color)

        # Окно предварительного просмотра текущего цвета
        self.preview_color = tk.Canvas(root, width=20, height=20, bg=self.pen_color)
        self.preview_color.pack(side=tk.LEFT)

        # Привязываем обработчик события <Button-1> к холсту, чтобы вставлять текст
        self.canvas.bind('<Button-1>', self.past_text)

    def setup_ui(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X)

        clear_button = tk.Button(control_frame, text="Очистить", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        color_button = tk.Button(control_frame, text="Выбрать цвет", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        save_button = tk.Button(control_frame, text="Сохранить", command=self.save_image)
        save_button.pack(side=tk.LEFT)

        # Добавляем метку для размера кисти
        label = ttk.Label(control_frame, text='Размер кисти:')
        label.pack(side=tk.LEFT)

        # Выпадающее меню для выбора размера кисти
        sizes = ['1', '2', '5', '10']
        combo = ttk.OptionMenu(control_frame, self.option_var, sizes[0], *sizes)
        combo.pack(side=tk.LEFT)

        # Кнопка "Ластик"
        eraser_button = tk.Button(control_frame, text="Ластик", command=self.eraser)
        eraser_button.pack(side=tk.LEFT)

        # Кнопка "Карандаш"
        pencil_button = tk.Button(control_frame, text="Карандаш", command=self.pencil)
        pencil_button.pack(side=tk.LEFT)

        # Кнопка "Изменить размкр холста"
        size_button = tk.Button(control_frame, text="Размер холста", command=self.resize_canvas)
        size_button.pack(side=tk.LEFT)

        # Кнопка "Добавить текст"
        text_button = tk.Button(control_frame, text="Текст", command=self.text)
        text_button.pack(side=tk.LEFT)

        # Кнопка "Изменить цвет холста"
        text_button = tk.Button(control_frame, text="Цвет холста", command=self.change_canvas_color)
        text_button.pack(side=tk.LEFT)

    def paint(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=self.option_var.get(), fill=self.pen_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.pen_color,
                           width=int(self.option_var.get()))

        self.last_x = event.x
        self.last_y = event.y

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

    def choose_color(self, event=None):
        """
        Функция для выбора цвета.
        Args:
            self: Экземпляр класса DrawingApp.
        """
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]
        self.preview_color.configure(bg=self.pen_color)

    def save_image(self, event=None):
        """
        Функция для сохранения изображения.
        Args:
            self: Экземпляр класса DrawingApp.
        """
        file_path = filedialog.asksaveasfilename(filetypes=[('PNG files', '*.png')])
        if file_path:
            if not file_path.endswith('.png'):
                file_path += '.png'
            self.image.save(file_path)
            messagebox.showinfo("Информация", "Изображение успешно сохранено!")

    def eraser(self):
        """
        Функция "Ластик", устанавливающая цвет кисти на белый.
        """
        self.last_color = self.pen_color
        self.pen_color = 'white'

    def pencil(self):
        """
        Функция устанавливает цвет кисти на предыдущий цвет.
        """
        self.pen_color = self.last_color

    def pick_color(self, event):
        """
        Функция "Пипетка", которая обновляет цвет пера на основе цвета пикселя изображения в координатах события.
        Args:
            self: Экземпляр класса DrawingApp.
            event: Событие, содержащее координаты пикселя в холсте.
        """
        self.pen_color = '#%02x%02x%02x' % self.image.getpixel((event.x, event.y))

    def resize_canvas(self):
        """
        Функция для изменения размера холста.
        Args:
            self: Экземпляр класса DrawingApp.
        """
        width = tk.simpledialog.askinteger(title="Изменить размер холста", prompt="Ширина холста:")
        height = tk.simpledialog.askinteger(title="Изменить размер холста", prompt="Высота холста:")
        self.canvas.config(width=width, height=height)
        self.image = self.image.resize((width, height))
        self.draw = ImageDraw.Draw(self.image)

    def text(self):
        """
        Функция выводит диалоговое окно для ввода текста.
        Args:
            self: Экземпляр класса DrawingApp.
            :param event:
        """
        text = tk.simpledialog.askstring(title="Добавить текст", prompt="Текст:")
        if text:
            self.text_past = text

    def past_text(self, event):
        """
        Функция вставляет текст на холст в координатах щелчка левой кнопки мыши.
        Args:
            self: Экземпляр класса DrawingApp.
            event: Событие, содержащее координаты клика мыши.
        """
        self.last_x = event.x
        self.last_y = event.y
        self.canvas.create_text(self.last_x, self.last_y, text=self.text_past, fill=self.pen_color)
        self.text_past = None

    def change_canvas_color(self):
        """
        Функция изменяет цвет холста.
        Args:
            self: Экземпляр класса DrawingApp.
        """
        color = tk.colorchooser.askcolor()
        print(color)
        self.canvas.config(bg=color[1])


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
