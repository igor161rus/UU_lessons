import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, ttk
from PIL import Image, ImageDraw


class DrawingApp:
    def __init__(self, root):
        # Инициализация option_var
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

    def choose_color(self):
        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]

    def save_image(self):
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


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
