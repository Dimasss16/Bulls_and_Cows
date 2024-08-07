# Bulls_and_Cows
У игры три составляющих:
1) Пользователь угадывает загаданное компом число (я пишу файл user_guesses)
2) Комп угадвает загаданное пользователем число (Полина пишет файл computer_guesses)
3) Всё это красиво оформлено (Костя)

Описание хода игры:

Каждый раунд состоит из двух игр: число загадывает игрок и число загадывает компьютер. Игрок выбирает количество раундов, которые он намерен сыграть. Для каждого раунда рандомно выбирается, кто первый загадывает число. В каждой игре подсчитывается число ходов до угадывания, очки суммируются. После заданного числа раундов называется победитель, у которого общее число очков меньше.
Над этим модулем работает Костя. Модуль должен: спросить про количество раундов, разыграть очередность в каждом раунде, для каждой игры передать управление соответствующей подпрограмме, получить от неё количество очков и правильно их просуммировать.
и вывести победителя.
Подпрограмма для Димы: компьютер загадывает число, игрок угадывает. Подпрограмма возвращает число ходов, сделанных игроком для победы.
ПОдпрограмма для Полины: игрок загадывает число, компьютер угадывает. Подпрограмма возвращает число ходов, сделанных компьютером для победы.


Тайминг проекта:
1. Дима пишет подпрограмму user_guesses до 15 апреля
2. Полина пишет подпрограмму computer_guesses до 15 апреля
3. Костя прописывает архитектуру ввода, вывода и поддержки игрового процесса до 25 апреля
4. Bug fixing & testing -- до 30 апреля


| First half                              | Date         | Second half                                 | Date         |
|-----------------------------------------|--------------|---------------------------------------------|--------------|
| Introduction                            | Di 2024-04-22| XML                                         | Di 2024-06-11|
| Bits and Encodings                      | Fr 2024-04-26| XPath                                       | Fr 2024-06-14|
| Historical Encodings                    | Di 2024-04-30| XML Schema                                  | Di 2024-06-18|
| Unicode                                 | Fr 2024-05-03| JSON+YAML                                   | Fr 2024-06-21|
| Corpus Linguistics                      | Di 2024-05-07| HTML                                        | Di 2024-06-25|
| Copyright and Licenses                  | Fr 2024-05-10| CSS                                         | Fr 2024-06-28|
| Introduction to the Command Line        | Di 2024-05-14| Frontend Libraries                          | Di 2024-07-02|
| Unix Tools                              | Fr 2024-05-17| Text-Based File Formats for Linguistics      | Fr 2024-07-05|
| Unix Tools for Aggregation and Reshaping| Di 2024-05-28| Markdown                                    | Di 2024-07-09|
| Unix Tools for Editing and Manipulation | Fr 2024-05-31| LaTeX Basics                                | Fr 2024-07-12|
| NLP Tools on the Command Line           | Di 2024-06-04| Upcoming                                    | Di 2024-07-16|
| Challenges of Using NLP Tools           | Fr 2024-06-07| Upcoming                                    | Fr 2024-07-19|


# The Advantages of Markdown

Markdown is a lightweight markup language with plain-text formatting syntax. 
It was created by [John Gruber](https://daringfireball.net/projects/markdown/) 
in 2004 and this is how he introduces it:
> Markdown is a text-to-HTML conversion tool for web writers. 
> Markdown allows you to write using an easy-to-read, easy-to-write plain text 
> format, then convert it to structurally valid XHTML (or HTML).

## Usage

Markdown allows you to make text
1. with different attributes
    - **bold**
    - *italics*
2. look like code: `let x = 4;`

---

You can also include images

![Markdown Logo](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
