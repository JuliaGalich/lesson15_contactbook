# template
template for django start project


1. Обрати розміщення для проєкту <br>
   `D:` - перейти на обраний диск<br>
   `cd <розміщення/назва теки>` - зайти до директорії<br>
   `cd..` - вийти до попередньої директорії<br>
   `dir..` - показативміст поточної теки
2. Створити теку
   ```bash
      md 'Назва теки'
   ```

3. клонувати
   ```bash
   git clone "<https://github.com/JuliaGalich/template.git>"
   ```

4. Віртуальне середовище 
   - Створити віртуальне середовище `.venv` або підключити існуюче
      ```bash
     #створення віртуального середовища
      python -m venv .venv
     ```
   - активація віртуального середовища
   ```bash
   .venv\Scripts\activate
   ```
   
5. встановлення необхідних модудей
   ```bash
   pip install request.txt
   ```
6. Створення нового проєкту Django

Ми практично завершили стандартний шаблон, лишилося лише розгорнути Django проєкт, виконайте цю дію виконавши команду:
```bash
    django-admin startproject <найменування_сайту> .
```

```bash
   django-admin startproject project .
```

Крапка вкінці вказує, що проєкт буде розгорнуто в обраній директорії.

7. Додамо додаток
```bash
python manage.py startapp <назва_додатку>
```
```bash
python manage.py startapp app
```