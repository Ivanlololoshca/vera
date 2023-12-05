from flask import Blueprint, redirect, url_for, render_template
lab1 = Blueprint('lab1', __name__)

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code=302)


@lab1.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБИ-11, Лабораторные работы</title>
    </head>
        <body>
        <header>
            НГТУ,ФБИ-11, WEB-программирование, часть 2. Список лабораторных
        </header>

       <ol> <a href='lab1'>/ПЕРВАЯ ЛАБОРАТОРНАЯ РАБОТА</a> </ol>

        <ol> <a href='lab2'>/ВТОРАЯ ЛАБОРАТОРНАЯ РАБОТА</a> </ol>

        <ol> <a href='lab3'>/ТРЕТЬЯ ЛАБОРАТОРНАЯ РАБОТА</a> </ol>

        <ol> <a href='lab4'>/ЧЕТВЁРТАЯ ЛАБОРАТОРНАЯ РАБОТА</a> </ol>

        <ol> <a href='lab5'>/ПЯТАЯ ЛАБОРАТОРНАЯ РАБОТА</a> </ol>
       
        <footer>
            @copy; Левенец Иван Вачеслав Григорович ФБИ-11 3курс,2023
        </footer>

    </body>

        
</html>
"""


@lab1.route("/lab1")
def lab():
    return """

<!DOCTYPE html>
<html>
<head>
    <title>Левенец, Григорович лаболаторная работа  1</title>

</head>
<body>
<header>
НГТУ ФБ ЛАБОРАТОРНАЯ РАБТОА 1
</header>

<p>Flask — фреймворк для создания веб-приложений на языке
программирования Python, использующий набор инструментов
Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
называемых микрофреймворков — минималистичных каркасов
веб-приложений, сознательно предоставляющих лишь самые базовые возможности
</p>

<a href='/menu'>Вернуться к меню</a>

<h2>РОУТЫ</h2>

<ul>
<li><a href='/lab1/oak'>ДУБ</a></li>
<li><a href='/lab1/student'>СТУДЕНТЫ</a></li>
<li><a href='/lab1/python'>ПИТОН</a></li>
<li><a href='/lab1/kyking'>РЕЦЕПТ</a></li>
</ul>

<footer>
 @copy; Левенец Иван Вачеслав Григорович ФБИ-11 3курс,2023
</footer>
</body>
</html>
"""


@lab1.route("/lab1/oak")
def oak():
    return '''

<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''"  width=500px, height=500px>
    </body>
</html>
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Левенец Григорович лабораторная 1</title>
</head>
<body>
<header>
НГТУ ФБ ЛАБОРАТОРНАЯ РАБТОА 1
</header>
    
<h1>Левенец Иван Алексеевич</h1>
<h1>Григорович Вячеслав Сергеевич</h1>

<img src="''' + url_for('static', filename='ngta.jpg') + '''"  width=500px, height=500px>


<footer>
 @copy; Левенец Иван, Вачеслав Григорович ФБИ-11 3курс,2023
</footer>

</body>
</html>
'''


@lab1.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Левенец Григорович лабораторная 1</title>
</head>
<body>
   <header>НГТУ ФБ ЛАБОРАТОРНАЯ РАБТОА 1</header> 

   <h1>python</h1>

   <h2>Python, согласно данным из Google – язык программирования высокого
    уровня общего назначения. Обладает типизацией динамического строгого 
    характера. Имеет автоматическое управление памятью, за счет чего осуществляется
    повышение производительности контента, написанного на нем.
    Python – объектно-ориентированный язык программирования, пользующийся
    спросом у большинства современных разработчиков. Коды, написанные на
    нем, достаточно легко читать. Питон (или Пайтон) работает с несколькими
    парадигмами программирования. Основная реализация – Cpython. Google
    указывает на то, что она составлена на C (Си).</h2>

    <p>Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[24]
    или па́йтон[25]) — высокоуровневый язык программирования общего назначения 
    с динамической строгой типизацией и автоматическим управлением памятью[26][27],
    ориентированный на повышение производительности разработчика, читаемости кода 
    и его качества, а также на обеспечение переносимости написанных на нём программ[28].
    Язык является полностью объектно-ориентированным в том плане, что всё является 
    объектами[26]. Необычной особенностью языка является выделение блоков кода
    пробельными отступами[29]. Синтаксис ядра языка минималистичен, за счёт чего
    на практике редко возникает необходимость обращаться к документации[28]. 
    Сам же язык известен как интерпретируемый и используется в том числе для 
    написания скриптов[26]. Недостатками языка являются зачастую более низкая
    скорость работы и более высокое потребление памяти написанных на нём 
    программ по сравнению с аналогичным кодом, написанным на компилируемых 
    языках, таких как C или C++[26][28].Python является мультипарадигменным 
    языком программирования, поддерживающим императивное, процедурное, структурное,
    объектно-ориентированное программирование[26], метапрограммирование[30] и 
    функциональное программирование[26]. Задачи обобщённого программирования 
    решаются за счёт динамической типизации[31][32]. Аспектно-ориентированное
    программирование частично поддерживается через декораторы[33], 
    олее полноценная поддержка обеспечивается дополнительными фреймворками[34].
    Такие методики как контрактное и логическое программирование можно реализовать
    с помощью библиотек или расширений[35]. Основные архитектурные
    черты — динамическая типизация, автоматическое управление памятью[26],
    полная интроспекция, механизм обработки исключений, поддержка
    многопоточных вычислений с глобальной блокировкой интерпретатора
    (GIL)[36], высокоуровневые структуры данных. Поддерживается разбиение
    программ на модули, которые, в свою очередь, могут объединяться в 
    пакеты[37].Эталонной реализацией Python является интерпретатор 
    CPython, который поддерживает большинство активно используемых 
    платформ[38] и являющийся стандартом де-факто языка[39]. 
    Он распространяется под свободной лицензией Python Software
    Foundation License, позволяющей использовать его без ограничений
    в любых приложениях, включая проприетарные[40]. CPython компилирует
    исходные тексты в высокоуровневый байт-код, который исполняется 
    в стековой виртуальной машине[41]. К другим трём основным 
    реализациям языка относятся Jython (для JVM), IronPython 
    (для CLR/.NET) и PyPy[26][42]. PyPy написан на подмножестве
    языка Python (RPython) и разрабатывался как альтернатива
    CPython с целью повышения скорости исполнения программ,
    в том числе за счёт использования JIT-компиляции[42].
    Поддержка версии Python 2 закончилась в 2020 году[43].
    На текущий момент активно развивается версия языка Python
    3[44]. Разработка языка ведётся через предложения по расширению 
    языка PEP (англ. Python Enhancement Proposal), в которых
    описываются нововведения, делаются корректировки согласно 
    обратной связи от сообщества и документируются итоговые
    решения[45].</p>

    <img src="''' + url_for('static', filename='python.jpg') + '''" width=500px, height=500px>

    <footer>
    @copy; Левенец Иван, Вачеслав Григорович ФБИ-11 3курс,2023
    </footer>

</body>
</html>
'''


@lab1.route("/lab1/kyking")
def kyking():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Левенец Григорович лабораторная 1</title>
</head>
<body>
    <header>НГТУ ФБ ЛАБОРАТОРНАЯ РАБТОА 1</header> 

    <img src="''' + url_for('static', filename='kuk.jpg') + '''"  width=500px, height=500px>
 
    <h1>рецепт кротовухи</h1>
    <h2>Первое</h2>
    Крот на кротовуху берется дохлый. Он должен быть дохлым изначально,
    причем у него уже должно пройти окоченение, он должен немножко даже
    ферментироваться уже. Только такой крот подходит вообще. Ну, 
    оставщиками таких кротов, безусловно, являются наши домашние 
    питомцы, всякие кошаки. Ну, потому что тут как бы гарантия.
    Все-таки крот мог умереть и от старости, и своей смертью,
    из таких напиток уже не столь хорош.

    <h2>Второе</h2>
    заливают, упаси боже, не водкой, а спиртом. Причем чем суше спирт. 
    (Возвращаемся к моему напоминанию вам, почитать про свойства кротовой шкуры, 
    где она используется, для чего и вообще. Крот-то уникальное животное, поверьте
    мне. ) Чем суше спирт, тем лучше. Конкретно на эту кротовуху пошел спирт
    три девятки. Это спирт не пищевой, хотя он производится из пищевого 
    сырья и, разумеется, вполне съедобен. Но он используется в целом не в
    пищевой промышленности, и хорошо подходит для кротовухи.

    <footer>
    @copy; Левенец Иван, Вачеслав Григорович ФБИ-11 3курс,2023
    </footer>

</body>
</html>
'''
