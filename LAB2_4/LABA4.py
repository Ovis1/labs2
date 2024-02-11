if __name__ == "__main__":
    class ProgrammingLanguage:
        """
        Базовый класс, представляющий язык программирования.
        """

        def __init__(self, name: str, paradigm: str):
            self._name = name  # Инкапсуляция: Имя сделано приватным для предотвращения прямого доступа
            self._paradigm = paradigm

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта ProgrammingLanguage.
            """
            return f"{self._name} - это {self._paradigm} язык программирования"

        def __repr__(self) -> str:
            """
            Возвращает детальное представление объекта ProgrammingLanguage.
            """
            return f"ProgrammingLanguage({self._name}, {self._paradigm})"


    class Python(ProgrammingLanguage):
        """
        Подкласс, представляющий язык программирования Python.
        """

        def __init__(self, version: str, popularity: float, name: str = "Python"):
            super().__init__(name, "объектно-ориентированный")
            self._version = version  # Инкапсуляция: Версия сделана приватной для предотвращения прямого доступа
            self._popularity = popularity

        def debug(self) -> str:
            """
            Симулирует процесс отладки, специфичный для Python.
            """
            return "Отладка Python кода..."

        def execute(self, script: str) -> str:
            """
            Выполняет скрипт на Python и возвращает результат.

            Причина перегрузки метода: Этот метод специфичен для Python и позволяет выполнять скрипты на Python.
            """
            return f"Выполнение скрипта на Python: {script}"

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта Python.
            """
            return f"{self._name} - это популярный {self._paradigm} язык с версией {self._version}"

        def __repr__(self) -> str:
            """
            Возвращает детальное представление объекта Python.
            """
            return f"Python({self._version}, популярность={self._popularity})"
    pass
