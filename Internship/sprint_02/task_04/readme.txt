Задача №4. Реализовать функционал: Горячие клавиши для быстрых действий
Реализовать функционал: Горячие клавиши для быстрых действий

Ваша задача:
Горячие клавиши для быстрых действий

Реализация:
Для добавления горячих клавиш используйте метод self.root.bind('<Control-s>', self.save_image)
для сохранения и self.root.bind('<Control-c>', self.choose_color) для выбора цвета.
Функции обратного вызова должны принимать аргумент события, даже если они его не используют.

__________________________________________
Результат:
В конструкторе класса DrawingApp (32) привязываем обработчик события <Control-s> для сохранения изображения
В конструкторе класса DrawingApp (35) привязываем обработчик события <Control-c> для выбора цвета

В функции choose_color добавлен аргумент события
В функции save_image добавлен аргумент события

Другие изменения:

Пример выполнения: