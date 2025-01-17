#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-success">
# <font size="5", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Привет, Платон :) Спасибо за работу, все исправления и комментарии
#         
# Стоит поправить код удаления дубликатов и поработать над выводом по диаграмме размаха        
#         
# На проекте мы изучали и практиковали навыки из разделов о/об:
#                   
#  + выдвижении гипотез о пропусках в данных, заполнении или удалении,
#  + работе с категориальными данными
#  + подготовке данных для решения главной задачи проекта
#  + исследовании неочищенных данных,        
#  + подборе и создании графиков,
#  + программировании,
#  + автоматизации однотипных действий,
#  + выстраивании структуры проекта и обеспечении аккуратности кода,
#  + анализе данных,
#  + определении прибыльности и устойчивости продаж по выбранному параметру (жанр, платформа) на диаграмме размаха,
#  + составлении портрета пользователя, 
#  + формулировании и проверке двухсторонних гипотез, <b>интерпретации значения p-value - можно повторить недели через две </b>(для профилактики 🤝 )
#  + формировании рекомендаций для бизнеса 
#         
# <b>Навыки первого модуля освоены хорошо</b> 
# 
# <b>Поздравляю с успешно сданным сборным проектом и завершением первого модуля <br />на факультете дата-аналитики Я.Практикум</b>
# 
# <div class="alert alert-success">
#     <font size="5", color = "seagreen"><b>Успехов в дальнейшей учебе 🤝</b></font><br />
#     
# оставил комментарий про расшифровку р-значения, добавил бонус и несколько подсказок

# <div class="alert alert-success">
# <font size="5", color= "seagreen"><b>✔️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Привет, Платон :) Спасибо за доработки 🤝
#         
# Критические ❌ комментарии связаны с неточностями: 
# 
#  + выполнить проверку на дублирование записей
#  + переопределить актуальный период
#  + добавить диаграммы размаха в 100% масштабе
#  + в разделе проверки гипотез подправить выводы плюс можно более подробно расшифровать значение p_value 
#  + перепроверить промежуточные и итоговый выводы после всех исправлений
# 
# добавил новые подсказки        

# <div class="alert alert-success">
# <font size="4"><b>Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Привет, Платон :) Спасибо за доработки 🤝 К сожалению, вынужден прервать проверку, т.к. на проекте появились артефакты — неизвестные переменные, которые не позволяют запустить код проекта от первой до последней строчки без ошибок — возле ошибок я не нашел твоих вопросов об их причине 🤝
#         
# Если ты не понимаешь, как выполнить эти шаги, тогда стоит задать вопрос преподавателю по проектам в чате «пачки». Также ты можешь написать вопрос в проекте и опять отправить его на проверку — так я смогу тебе ответить        
#         
# __Стоит полностью проверить код проекта на ошибки в названиях переменных перед отправкой на ревью__        
#         
# ![image.png](attachment:image.png)        

# <div class="alert alert-success">
# <font size="4"><b>Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Привет, Платон :) Спасибо, что прислал задание 🤝 Меня зовут Ринат Хисамов и я буду проверять твой проект. Предлагаю обращаться друг к другу на ты. Так нам будет гораздо проще и удобней общаться
# 
# Мои комментарии обозначены пометкой <b>Комментарий ревьюера</b>. Далее в файле сможешь найти их в похожих ячейках (если фон комментария зелёный — всё сделано правильно (✔️), рекомендации таким же цветом. Отдельным цветом — блок ссылок (примеры ниже, 🍕). Оранжевым или светло желтым рекомендации, которые, хоть и не обязательны, но точно сделают ревью лучше. (⚠️); <u> красный комментарий</u>: код, график или вывод стоит переделать (❌)). 
# 
# Не удаляй все эти комментарии и постарайся учесть их в ходе выполнения данного проекта. 
# Будет замечательно, если добавишь свои комментарии и пояснения✍
#         
# Поехали 🚀
#     <br />
#     </font>
# 
# </div>

# <div style="border:solid steelblue 1px; padding: 20px">
#     
# <font size="4"><p style="text-align:center"><b>Примеры комментариев </b></p></font>
#     
# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4"><b>🍕 Пример комментария - совета, здесь м.б. просто ссылка</b></font>
#     <br /> 
#         <font size="3", color = "black">
# <br />
#     Тут всего такого разного и вкусного :), есть способы прокачать проект визуализациями (ценит большинство "боссов")  <br /><br />
#         <a href="https://devpractice.ru/matplotlib-book/">“Библиотека Matplotlib” доступна для скачивания БЕСПЛАТНО!</a>
#         На сайте много полезных материалов, мне самому очень помогло в свое время, до сих пор подсматриваю :)
# 
# 
# </div>
#     
# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
#     <font size="3"><b>⚠️ Пример оформления некритичного комментария</b>
#     <br /> 
#     <font size="2", color = "black">
# <br />
#     Рекомендации, которые, хоть и не обязательны, но точно сделают ревью лучше
#     <br />
#     </font>
# 
# </div>
#     
# <div class="alert alert-danger">
# <font size="3"><b>❌ Пример оформления комментария к блоку(строке) программного кода (или выводу), который стоит переделать</b></font>
#     <br /> 
#     <font size="2", color = "black">
# <br />
#     Отправлен не тот проект, напиши в своих комментариях, что случилось? жду — <b>это пример</b>
#     <br />
#     </font>
# 
# </div>
#     
# <div class="alert alert-success">
# <font size="4"><b>✔️ Пример оформления комментария, который нравится большинству студентов</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
#     Круто, молодец, отлично, логично, или — 👌, 👍, или — выводы отвечают на все вопросы к данным и проекту
#     <br />
#     </font>
# 
# </div>

# # Для твоих вопросов или комментариев оставлю такую ячейку, чтобы было удобнее взаимодействовать на проекте

# <div class="alert alert-info">
# <font size="4", color = "black"><b>✍ Комментарий студента</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> ... , вот мой вопрос ...
#         
#         

# In[ ]:





# # Сборный проект 
# 
# **Анализ интернет-магазина Стримчик**
# 
# 
# Вы работаете в интернет-магазине «Стримчик», который продаёт по всему миру компьютерные игры. Из открытых источников доступны исторические данные о продажах игр, оценки пользователей и экспертов, жанры и платформы (например, Xbox или PlayStation). Вам нужно выявить определяющие успешность игры закономерности. Это позволит сделать ставку на потенциально популярный продукт и спланировать рекламные кампании.
# Перед вами данные до 2016 года. Представим, что сейчас декабрь 2016 г., и вы планируете кампанию на 2017-й. Нужно отработать принцип работы с данными. Неважно, прогнозируете ли вы продажи на 2017 год по данным 2016-го или же 2027-й — по данным 2026 года.
# В наборе данных попадается аббревиатура ESRB (Entertainment Software Rating Board) — это ассоциация, определяющая возрастной рейтинг компьютерных игр. ESRB оценивает игровой контент и присваивает ему подходящую возрастную категорию, например, «Для взрослых», «Для детей младшего возраста» или «Для подростков».
# 
# Данные за 2016 год могут быть неполными

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Стоит добавить одну из ключевых особенностей описания проекта — данные за 2016 г. неполные

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Название со смыслом придаст вес проекту
#         
# План проекта поможет заказчику понять, что мы тут делали

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Название придаст вес проекту
#         
# а подробности выполнения проекта дадут возможность вспомнить через полгода — что мы тут делали 

# ### check

# 

# # Шаг 1
# Импортируем необходимые библиотеки

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import seaborn as sns
from scipy import stats as st


# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера </b></font>
# <br /> 
# <font size="3", color = "black">
# <br />   Кажется, весь код на проекте запускался вручную ... 10-я строка кода в начале проекта
#     
# ![image-3.png](attachment:image-3.png)    
#     
#     
# ![image-2.png](attachment:image-2.png)    
#     
#    
#     
# Проверить работоспособность кода — можно нажав на панели Jupiter Hub Kernel и Restart & Run All (см скриншот ниже).
# 
# ![image.png](attachment:image.png)

# Откроем файл

# In[2]:


games = pd.read_csv('/datasets/games.csv')


# Выведем первые 10 строк датасета

# In[3]:


games.head(10)


# In[4]:


games.shape[0]


# Количество строк-16715

# In[5]:


games.info()


# Можем заметить, что в столбцах много очень много пропущенных значений.

# In[6]:


games.isna().sum()


# Вывели таблицу количества NaN в датафрейме games.

# In[7]:


# check
# пропущенные значения бары

def pass_value_barh(dfg):
    try:
        (
            (dfg.isna().mean()*100)
            .to_frame()
            .rename(columns = {0:'space'})
            .query('space > 0')
            .sort_values(by = 'space', ascending = True)
            .plot(kind = 'barh', figsize = (19,6), rot = -5, legend = False, fontsize = 16)
            .set_title('Пример' + "\n", fontsize = 22, color = 'SteelBlue')    
        );    
    except:
        print('пропусков не осталось :) или произошла ошибка в первой части функции ')


# In[8]:


pass_value_barh(games)


# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера</b></font>
# <br /> 
# <font size="3", color = "black">
# <br /> Наглядность представления информации одна из важных составляющих работы дата-аналитика или дата-сайентиста
#     
# __мой график оформлен не совсем корректно, сможешь отметить, что стоило бы исправить в графике?__
#   

# <div class="alert alert-info">
# <font size="4", color = "black"><b>✍ Комментарий студента</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Думаю что необходимо выравнить, названия столбцов по оси Oy. Добавить подпись на оси Ox, непонятно что за значения указаны от 0 до 50.

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Принимается
#         
# Цвет у шрифта заголовка почти совпадает с цветом у баров
#         
# За поворот текста на оси `Y` отвечает параметр `rot`
#         
# Можно добавить обозначение оси `Х` (процент записей с пропусками)
#         
#         df.isna().mean()*100 — для расчета процента пропусков в колонке
#         
# На графике мы оцениваем масштаб проблемы с пропусками и возможное совпадение % пропущенных значений в колонках
#         
# добавить подписи к осям мешает строка кода
#         
#         .set_title('Пример' + "\n", fontsize = 22, color = 'SteelBlue')    
#         
# её можно заменить на        
#         
#         ;
#         plt.title('Пропущенные значения, %' + "\n", fontsize=22, color='SteelBlue')
#         plt.xlabel('Процент пропусков', fontsize=22)
#         plt.ylabel('Столбцы с пропусками')
# 
# плюс можно установить шкалу от 0 до 100       
#         
#         plt.xlim(0, 100)        
#         
# часть моих новых шрифтов оформлена не совсем корректно 🤝😉        

# Посмотрим отдельно на сами таблицы, в которых имеются NaN значения в каждом из столбцов.

# In[9]:


games[games['Name'].isna()]


# In[10]:


games[games['Platform'].isna()]


# In[11]:


games[games['Year_of_Release'].isna()]


# In[12]:


games[games['Genre'].isna()]


# In[13]:


games[games['Critic_Score'].isna()]


# In[14]:


games[games['User_Score'].isna()]


# In[15]:


games[games['Rating'].isna()]


# Пропущенных значений в столбце Genre - 2. Год выпуска игры 1993, данные могли просто затеряться и не подлежать восстановлению.

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Выбран метод .isnull() для поиска пропущенных значений, это отлично! 
#         
# isnull() и isna() делают одно и то же, но использование isna() предпочтительнее. Звучание методов: <b>isna(), notna() и  fillna(), dropna()</b> помогает запомнить их быстрее 🤝
#     <br /> 
#     </font>
# 
# </div>

# In[16]:


games.query('Critic_Score.isnull() & Rating.isnull() & User_Score.isnull()')


# И новые и старые игры имеют пропуски в столбцах Rating, User_Score,Critic_Score

# Вывод по знакомству  с данными:
# 
# Всего в таблице 16715 строк и 11 колонок в шести колонках имеются пропуски в данных
# Названия колонок имеют нарушение стилей
# Ряд колонок имеет неверный тип
# 

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Часть кода, где изучаются пропуски — стоит перенести во второй раздел — раздел предобработки данных

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️  Комментарий ревьюера</b></font>
#     <br />  
#     <font size="3", color = "black">
# <br />обзор данных проведен корректно, не помешает добавить обобщающий короткий вывод после первого знакомства с данными

# Обзор Данных:
# 
# Форматирование: Названия столбцов не соответствуют стандарту змеиного регистра.
# 
# Пропуски: В датафрейме присутствуют пропущенные значения, требующие обработки.
# 
# Типы Данных: Столбец User_Score должен быть числовым, но классифицируется как категориальный из-за наличия значения "tbd" (to be determined), часто используемого в анонсах игр для обозначения предстоящих, но еще не определенных дат выхода.
# 
# Возрастные Рейтинги: Столбец Rating указывает на возрастные ограничения игр:
# 
# EC: 3+ лет
# 
# E: 6+ лет
# 
# K-A: 6+ лет (использовалось до 1998 года, эквивалентно E)
# 
# E10+: 10+ лет
# 
# T: 13+ лет
# 
# M: 17+ лет
# 
# AO: 18+ лет
# 
# RP: Рейтинг ожидается
# 
# Рекомендации:
# 
# Привести названия столбцов к змеиному регистру.
# 
# Обработать пропущенные значения.
# 
# Преобразовать столбец User_Score в числовой тип данных, заменив или удалив нечисловые значения.
# 
# Проверить и, при необходимости, стандартизировать значения в столбце Rating для обеспечения единообразия.
# 
# 

# ### check

# # Шаг 2

# Приведем названия столбцов к нижнему регистру.

# In[17]:


games.columns = games.columns.str.lower()


# In[18]:


games.columns


# Также для удобства приведем к нижнему регистру столбцы name,platform,genre,rating

# In[19]:


for column in games[['name','platform','genre','rating']]:
    games[column]=games[column].str.lower()


# In[20]:


display(games[['name','platform','genre','rating']])


# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4"><b>🍕 Комментарий ревьюера</b></font>
#     <br /> 
#         <font size="3", color = "black">
#             <br />
# Можно без print(), если строка кода стоит последней

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ <b> Комментарий ревьюера</b></font>
# <br /> 
# <font size="3", color = "black">
# <br /> display() вместо print(), поможет навести красоту на проекте

# In[21]:


games = games.loc[games['name'].notna(),:]
games.shape


# Изменим тип данных в столбце year_of_release

# In[22]:


games['year_of_release'] = games['year_of_release'].astype('Int64')


# Посмотрим, возможно ли найти данные об year_of_release(Год выпуска).Может игра выпускалась на других платформах.

# In[23]:


years_range = list(map(str, list(range(int(games['year_of_release'].min()),
                        int(games['year_of_release'].max()) + 1))))
def extract_year(name_game):
   for year in years_range:
       if year in name_game:
           return float(year)
   return np.nan
games['extracted_year'] = games['name'].apply(extract_year)
games['extracted_year'].value_counts()


#  832 игры содержат в названии год выпуска. Теперь там где есть пропуски в df['year_of_release'] и есть новое значение из df['extracted_year'] проведем замену.

# In[24]:


games['year_of_release'].isna().sum()


# In[25]:


games.loc[games['year_of_release'].isna(), 'year_of_release'] = games['extracted_year'].copy()
games['year_of_release'].isna().sum()


# In[26]:


# check
games.info()


# In[27]:


games.loc[games['year_of_release'].isna(), 'year_of_release'] = -1
games['year_of_release'].isna().sum()


# In[28]:


games.drop('extracted_year', axis=1, inplace=True)
games.columns


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />проверим корректность алгоритма заполнения пропусков

# In[ ]:





# In[29]:


games['critic_score'].isna().sum()


# In[30]:


games.loc[games['critic_score'].isna(), 'critic_score'] = -1


# In[31]:


games['critic_score'].isna().sum()


# In[32]:


games.loc[games['user_score'] == 'tbd', 'user_score'].count()


# In[33]:


games.loc[games['user_score'] == 'tbd', 'user_score'] = np.NaN


# In[34]:


games['user_score'].isna().sum()


# In[35]:


games.loc[games['user_score'].isna(), 'user_score'] = -1


# In[36]:


games['rating'].value_counts()


# In[37]:


games['rating'].isna().sum()


# In[38]:


games.loc[games['rating'].isna(), 'rating'] = 'RP'
games['rating'].isna().sum()


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Отличное решение для столбца, который содержит категориальные данные, поможет определить ключевое различие в потрете пользователя
#         
#         games.loc[games['rating'].isna(), 'rating'] = 'RP'
#         
# Можно посмотреть на частотность использования категорий рейтинга, по отношению к остальным
#         
#         EC         8
#         K-A        3
#         RP         1
#         AO         1

# In[39]:


games.info()


# <div class="alert alert-dang er">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Мы внесли искажения в колонку год выпуска игры, которые приводят к ошибкам при определении срока жизни платформ
#         
# Стоит посмотреть на платформы, к которым относятся пропуски, __и с легкостью расстанешься с ними ...__
#         
# Рекомендуется прежде чем, выполнять проект минут 15-30 посвятить теме анализа (поиск в интернете), чтобы уверенно плавать в океане противоречивых данных :)   

# <div class="alert alert-info">
# <font size="4", color = "black"><b>✍ Комментарий студента</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Мы создали сводную таблицу, где внесли искажения. Данные в исходной таблице не изменятся при этом, а мы только посмотрели на примерные жизненные сроки различных платофрм.

# **Удалим данные с 0 продажами, ведь они не нужны для анализа**

# In[40]:


games_zero = games.query('na_sales == 0 and eu_sales == 0 and jp_sales == 0 and other_sales == 0')
games_zero


# In[41]:


games.shape


# In[42]:


games = games.drop(games_zero.index).reset_index(drop=True)


# In[43]:


games.shape


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Верно, по своей сути tbd и является Nan. Отлично, что определяешь неявные пропущенные значения.

# **Проверим на наличие дубликатов**

# In[44]:


games[['name', 'platform']].duplicated(keep=False).sum()


# In[45]:


games[games[['name', 'platform']].duplicated(keep=False)]


# In[46]:


games=games.drop_duplicates(subset=['name', 'platform'], keep=False)


# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит поправить код удаления, применяя параметр , keep=False, ты удаляешь и оригинал записи, и дубликат
#         
# Плюс, не все записи из этого списка являются дубликатами
#         
# ![image.png](attachment:image.png)
#         
# это две разные игры, которые были выпущены в разное время        

# In[47]:


games[['name', 'platform']].duplicated(keep=False).sum()


# Явных дубликатов нет

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Скажи пожалуйста, какое преимущество ты получаешь от заполнения пропусков в числовых колонках на этом проекте, с этой главной задачей?
#         
#         Вам нужно выявить определяющие успешность игры закономерности. Это позволит сделать ставку на потенциально популярный продукт и спланировать рекламные кампании.
#         

# <div class="alert alert-info">
# <font size="4", color = "black"><b>✍ Комментарий студента</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Заполнение пропусков в числовых колонках помогает обеспечить более точный и надёжный анализ, более точную визуализацию.
#         Далее нам понадобится корреляционный анализ, заполнение пропусков также поможет улучшить данный анализ

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Скажи пожалуйста, каким образом заполнение пропусков 
#         
#         games.loc[games['user_score'].isna(), 'user_score'] = -1
#         
# минус 1-ей поможет и улучшит качество   корреляционного анализа
#         
#         Далее нам понадобится корреляционный анализ, заполнение пропусков также поможет улучшить данный анализ
#         
# плюс, ты сам фильтруешь подобные значения при исследовании корреляционного анализа
#         
#          p1_critic_score = np.poly1d(np.polyfit(x_filter,
#                                            data_slice.query('critic_score > 0')...

# **Изменим типы данных**

# In[48]:


games['user_score'].dtypes


# In[49]:


games['user_score'] = pd.to_numeric(games['user_score'], errors='raise' )
games['user_score'].dtypes


# In[50]:


games['critic_score'].dtypes


# In[51]:


games['critic_score'] =games['critic_score'].astype('int')
games['critic_score'].dtypes


# In[52]:


games['year_of_release'] = games['year_of_release'].astype('int')
games['year_of_release'].dtypes


#  Мы изменили тип данных в столбце user_score на float64 и  [critic_score, year_of_release]  на int.

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера </b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />          
# Рейтинг ESRB — категориальные данные, стоит внимательно взглянуть на содержимое и предложить чем заполнить пропуски, возможно это поможет найти необычные различия в поведении клиентов, допом можно подумать над сокращением количества категорий
#         
# Т.к. записи с пропусками не учитываются при группировке данных, мы не сможем выявить реальный портрет игрока

# In[53]:


games['total_sales']=games[['na_sales','jp_sales','other_sales','eu_sales']].sum(axis=1)


# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Стоит поправить код 
#         
#         games['total_sales']=games[['na_sales','jp_sales','other_sales']].sum(axis=1)
#         
# пропущена значительная сумма продаж        

# In[54]:


# check
games.info()


# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Два пропуска в названии и жанре игры можно посмотреть и удалить, т.к. записи не помогут решить главную задачу проекта — на основе актуальных платформ сформировать рекомендации для проведения рекламной кампании в 2017 г. и само кол-во пропусков минимально 

# <div class="alert alert- dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Датасет не проверен на наличие простых дубликатов
#         
# __Особенно это станет важным, когда мы перейдем к более сложным задачам на втором модуле курса__

# <div class="alert alert-dang er">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />   
# На рабочих проектах стоит искать неполные дубликаты по ключевым столбцам, для примера по сумме параметров: 
#    
#     ['name', 'platform', 'year_of_release']
#     
# С обязательным приведением содержимого категориальных колонок к нижнему регистру — это уже выполнено
#         
# В сырой выборке имеется 2 строчки неполных дубликатов
#         
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html?highlight=duplicat#pandas.DataFrame.duplicated
#     

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />   
# На рабочих проектах стоит искать неполные дубликаты по ключевым столбцам, для примера по сумме параметров 
#         
# В статье имеется пример подобного поиска
#         
# https://www.codecamp.ru/blog/pandas-find-duplicates/        

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />         
#         
# Часть из этого списка — дубликаты, стоит корректно их найти, при помощи функции `.duplicated()` и удалить        
#         
# ![image.png](attachment:image.png)        

# ### check

# # Шаг 3

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />
# можно
#     
#     df['total_sales'] = df[['na_sales','eu_sales','jp_sales', 'other_sales']].sum(axis = 1)

# In[55]:


print(games['total_sales'])


# In[56]:


fig, ax = plt.subplots(nrows=1,ncols=1)
fig.set_size_inches(9, 7)
fig.tight_layout()
f_size = 15

games_group_by_year = games.pivot_table(index=['year_of_release'], values='name',aggfunc='count')
games_group_by_year.plot(
                       y='name',
                       kind='bar',
                       ax=ax,
                       legend = False,
                       grid = False)

ax.yaxis.set(ticks=range(0,1450,50));
ax.set_title('Столбчатая диаграмма выпуска игр по годам')
ax.set_xlabel('Год выпуска игр')
ax.set_ylabel('Количество выпущенных игр');


# In[57]:


fig, ax = plt.subplots(nrows=1, ncols=1)
fig.set_size_inches(9, 7)
fig.tight_layout()
f_size = 15

games_group_by_year = games.pivot_table(index=['year_of_release'], values='name', aggfunc='count')
games_group_by_year.plot(
    y='name',
    kind='bar',
    ax=ax,
    legend=False,
    grid=False
)

ax.yaxis.set(ticks=range(0, 1450, 50))
ax.set_title('Столбчатая диаграмма выпуска игр по годам', fontsize=f_size)
ax.set_xlabel('Год выпуска игр', fontsize=f_size)
ax.set_ylabel('Количество выпущенных игр', fontsize=f_size)

# Устанавливаем подписи оси X с шагом 5 лет
years = games_group_by_year.index
xticks = range(0, len(years), 5)  # Шаг 5 лет
xticklabels = [str(years[i]) for i in xticks]
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels, rotation=45, ha='right')

plt.show()


# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит скрыть сетку, она отвлекает от графика и сократить кол-во подписей оси Х: 1980-1985-1990 ...

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит уменьшить размеры графика

# Для анализа данных за период с 1980 по 1992 годы доступно менее 50 наблюдений, что недостаточно для надежной статистики. В то же время, данные за другие годы будут корректными. Важно отметить, что количество пропусков в данных примерно соответствует количеству выпущенных игр за первое десятилетие, что может значительно исказить результаты анализа. Максимум популярности видеоигр приходится на 2005-2011 годы.

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит полностью оформить все графики на проекте
# 
# Подписи осей на графиках и название добавят ясности и читабельности.
# Это важные элементы любой визуализации. Как добавить подписи и названия, смотри [здесь](https://proproprogs.ru/modules/matplotlib-razmeshchaem-standartnye-tekstovye-elementy-na-grafike?ysclid=l6agtioc6f299002507)

# In[58]:


fig, ax = plt.subplots(nrows=1,ncols=1)
fig.set_size_inches(9, 7)
fig.tight_layout()
f_size = 15

games_group_by_platform_sum_sales = games.pivot_table(index=['platform'], values='total_sales',aggfunc='sum')
games_group_by_platform_sum_sales.plot(
                       y='total_sales',
                       kind='bar',
                       ax=ax,
                       legend = False,
                       grid = True)

ax.yaxis.set(ticks=range(0,1350,50));
ax.set_title('Столбчатая диаграмма суммарных продаж по типу платфромы')
ax.set_xlabel('Тип платформы')
ax.set_ylabel('Общие продажы игр (миллионы проданных копий)');


# In[59]:


top_platform = games_group_by_platform_sum_sales.sort_values(by='total_sales', ascending=False)[:10].index
top_platform


# In[60]:


fig, ax = plt.subplots(nrows=1,ncols=1)
fig.set_size_inches(9, 7)
fig.tight_layout()

groupby_platform_and_year = (
    games
    .query('platform in @top_platform and year_of_release > 0')
    .groupby(by=['platform','year_of_release'])['total_sales'].sum()
    .reset_index()
)

stat_time_live = {'platform': [], 'rise': [], 'live': [], 'fall': []}
for name, platform in groupby_platform_and_year.groupby(by='platform'):
    platform.plot(
        ax=ax,
        kind='line',
        x='year_of_release',
        y='total_sales',
        style='-o',
        linewidth = 2.0,
        grid=True,
        label=name)

ax.set_xlabel('Тип платформы')
ax.set_ylabel('Доход по годам')
ax.set_title('Зависимость дохода от года для каждой платформы');


# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />          
# Стоит поправить код, у тебя нет такой переменной
#         
#         KeyError: 'Column not found: sum_sales'

# На графике для платформы DS наблюдается необычный зигзагообразный тренд. Согласно информации из внешних источников, платформа была запущена только в 2004 году. Поэтому необходимо отфильтровать данные, относящиеся к этой платформе, для более точного анализа.

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />
# Скрыть служ. информацию поможет точка с запятой на посл. строке кода
# 
#         Text(0, 0.5, 'Количество продаж')    
#     
# plt.ylabel("Количество продаж");    

# In[61]:


games.loc[(games['platform'] == 'DS') & (games['year_of_release'] < 2004), 'year_of_release'] = -1


#  Вывод
# В среднем за 5 лет на рынке появляются новые платформы, живут около 10 лет, а потом исчезают примерно за 5 лет. Но это в среднем, разброс значений достаточно велик ососбеннно у времени жизни. Платформы DS и PC живут аномально долго), а PS4 только начала свой путь.

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Стоит исключить предупреждения. Иногда их бывает слишком много, поэтому важно уметь их скрывать. В этом тебе поможет библиотека warnings. Попробуй найти подходящий метод и убрать предупреждения. 

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Странный выброс 1985 года у DS, можно посмотреть когда платформу выпустили на рынок, стоит удалить аномалию  

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Отличное определение жизненного цикла продаж у платформ, молодец

#  На основе вычисленного времени появления платформ на рынке выберем актуальный период с 2012 по 2016, т.е. за последние 5 лет, так мы будем ориентироваться на активных игроков рынка.

# In[62]:


decline_period_data = games[games['year_of_release'] > 2012]
decline_period_data.info()


# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Для целей прогнозирования продаж на следующий год даже в традиционных бизнесах редко берут данные более чем за 2-3 года. А в такой динамично меняющейся индустрии, как компьютерные игры и вовсе не стоит брать слишком большой временной интервал - иначе обязательно захватишь уже отжившие тренды. Но и слишком короткий период тоже брать не стоит
#         
#         decline_period_data = games[games['year_of_release'] > 2009]

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Для целей прогнозирования продаж на следующий год даже в традиционных бизнесах редко берут данные более чем за 2-3 года. А в такой динамично меняющейся индустрии, как компьютерные игры и вовсе не стоит брать слишком большой временной интервал - иначе обязательно захватишь уже отжившие тренды. Но и слишком короткий период тоже брать не стоит
#         
#         decline_period_data = games[games['year_of_release'] > 20011]
#         
# __Шум от данных за 2012-2013 гг. помешает корректно определить ТОП-5 платформ__        

# Посмотрим, какие платформы лидировали по продажам за этот период

# In[63]:


fig, ax = plt.subplots(nrows=1,ncols=1)
fig.set_size_inches(10, 7)
fig.tight_layout()

groupby_platform_and_year = (
    decline_period_data
    .groupby(by=['platform','year_of_release'])['total_sales'].sum()
    .reset_index()
)

stat_time_live = {'platform': [], 'rise': [], 'live': [], 'fall': []}
for name, platform in groupby_platform_and_year.groupby(by='platform'):
    platform.plot(
        ax=ax,
        kind='line',
        x='year_of_release',
        y='total_sales',
        style='-o',
        linewidth = 2.0,
        grid=True,
        label=name)
ax.set_xlabel('Тип платформы')
ax.set_ylabel('Доход по годам')
ax.set_title('Зависимость дохода от года для каждой платформы')
pass


# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит вынести легенду за пределы графика

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />          
# Стоит поправить код, у тебя нет такой переменной
#         
#         KeyError: 'Column not found: sum_sales'

# In[ ]:





# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Срезая старые платформы, например PS3, мы не узнаем реальную долю рынка, которую занимают PS3 + PS4, эту долю можно использовать как прогнозную, которую займет PS4, после полного ухода PS3
#         
# При создании актуальной выборки стоит удалить только старые игры, не изменяя перечень платформ

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Скажи пожалуйста, по какой причине мы фильтруем данные таким образом?
#         
#         games_top_6_platforms = games_top_6_platforms[games_top_6_platforms['total_sales']<1.4]
#                                                                                                 
#                                                                                                 

# In[64]:


fig, ax = plt.subplots(figsize=(18, 10))
sns.boxplot(y="platform", x="total_sales", data=decline_period_data, orient="h", ax=ax)
ax.grid()
ax.set_xlim(0, 2.0)
ax.set_title('Диаграмма распределения продаж игр по всем регионам в зависимости от платформы')

# Добавляем названия осей
ax.set_xlabel('Общие продажи (в млн. единиц)')
ax.set_ylabel('Платформа')

plt.show()


# <div class="alert alert-d anger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Все надписи для графиков стоит оформлять на языке выполнения проекта

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Стоит отсортировать ящики по размеру медианы, для быстрого сравнения заказчиком

# Данные представляют собой крайне нестабильную картину с множеством выбросов в любом регионе. Большинство игр, распределенных по платформам (50% от общего числа), продаются в количестве не более 750 тысяч копий. В каждом регионе наиболее успешными платформами оказались PS4, X360, XOne и Wii. В то же время, платформы PC, PSV и PSP демонстрируют низкие продажи в текущем временном интервале, их доход не превышает 250 тысяч копий.

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Ты используешь диаграмму размаха для определения успешности платформы, молодец
#         
# Для более полной оценки продаж на платформах стоит добавить график со 100% масштабом, посмотреть на максимальные продажи, плюс будет исправлена выборка для исследования и на диаграмме размаха будут представлены все платформы, которые попадут в актуальный период

#  В платформы возьмем X360 в датасете она является одной из самых популярных.

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Данные за 2016 год неполные, и делать вывод о падении продаж в 2016 году не стоит, можно сравнивать рост/падение на других промежутках, например 2015 год к 2014 ...
#         
#         эта информация имеется в описании проекта

# # example 1

# #### example 3

# ##### example 4

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />
# Стоит выделять разделы проекта заголовками разного уровня, за уровень отвечает количество знаков #
#     
#         # example 1
# 
#         #### example 3
# 
#         ##### example 4
#     
# Пожалуйста, воспользуйся методичкой по оформлению проектов. Ее можно найти в блоке курса: Полезные инструкции для учёбы - Оформление проекта - Рекомендации по выполнению проектов    

# In[65]:


games_actual_X360 = decline_period_data[decline_period_data['platform'] == 'x360']
games_actual_X360.info()


# Посмотрим, как влияют на продажи X360 отзывы пользователей и критиков. Построем диаграмму рассеяния и посчитаем корреляцию между отзывами и продажами.

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> на проектах стоит снижать размерность выводимой информации, где не требуется максимальная точность, до одного или двух знаков после запятой
#         
#         0.1159614931286009

# In[66]:



x_filter = games_actual_X360.query('user_score > 0')["total_sales"]

p1_user_score = np.poly1d(np.polyfit(x_filter,
                                     games_actual_X360.query('user_score > 0')["user_score"], 1))

approx_user_score = p1_user_score(x_filter)


# In[67]:


fig, ax = plt.subplots(figsize=(18,10))
sns.scatterplot(data=decline_period_data[decline_period_data['platform'] == 'x360'], x="total_sales", y="user_score")
ax.grid()
ax.set_xlim(0,5)

ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
ax.set_title('Диаграмма рассеяния продаж игр на платформе X360 от отзывов пользователей')
ax.plot(x_filter, approx_user_score, '-r', label='аппроксимация полиномом 1го порядка')
ax.legend(loc='upper right')
ax.set_xlabel('Общие продажи (в млн. единиц)')
ax.set_ylabel('Оценка пользователей')
pass


# На графике также представлена линейная аппроксимация данных. Угол наклона прямой в 45 градусов указывает на максимальную корреляцию (равной 1), а при 0 градусах корреляция отсутствует (равна 0). В данном случае прямая почти горизонтальна, что свидетельствует о отсутствии связи между продажами и мнениями пользователей. Точки вблизи нуля соответствуют отсутствующим данным, что наглядно демонстрирует количество недостающей информации. Далее рассмотрим связь между продажами и оценками критиков.

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Подсвечу еще раз — стоит полностью оформить все графики на проекте (все надписи у графиков оформляются на языке выполнения проекта)
#  

# In[68]:


x_filter = games_actual_X360.query('critic_score > 0')["total_sales"]
p1_critic_score = np.poly1d(np.polyfit(x_filter,
                                     games_actual_X360.query('critic_score > 0')["critic_score"], 1))
approx_critic_score = p1_critic_score(x_filter)


# <div class="alert alert-dang er">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />          
# Стоит поправить код, у тебя нет такой переменной
#         
#         KeyError: 'Column not found: sum_sales'

# In[69]:


fig, ax = plt.subplots(figsize=(18,10))
sns.scatterplot(data=decline_period_data[decline_period_data['platform'] == 'x360'], x="total_sales", y="critic_score")
ax.grid()
ax.set_xlim(0,5)
# нужно чтобы оси графика были одинаковыми и неискажали преставление
ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
ax.set_title('Диаграмма рассеяния продаж игр на платформе X360 от оценки критиков')
ax.plot(x_filter, approx_critic_score, '-r', label='аппроксимация полиномом 1го порядка')
ax.legend(loc='upper right')
ax.set_xlabel('Общие продажи (в млн. единиц)')
ax.set_ylabel('Оценка критиков')
pass


# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Широкие строки кода рекомендуется делить на всем проекте
#         
# <a href="https://qastack.ru/programming/53162/how-can-i-do-a-line-break-line-continuation-in-python">Перенос длинных строк кода</a>. 
#     
# </div>

# In[70]:


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
sns.heatmap(games_actual_X360.query('user_score > 0')[['total_sales', 'user_score']].corr(), ax=ax1, annot=True, fmt='.2f', vmin=0,vmax=1, square=True)

sns.heatmap(games_actual_X360.query('critic_score > 0')[['total_sales', 'critic_score']].corr(), ax=ax2, annot=True, fmt='.2f', vmin=0,vmax=1, square=True)


# Да, так и есть корреляция подтвердила наше предположение. Зависимости между продажами и отзывами пользователей нет, корреляция близка к 0. Зависимость между продажами и оценкой критиков слабая, корреляция меньше 0.5. Действительно, популярные журналы и порталы о видеоиграх своими рецензиями могут повлиять на продаваемость игр.

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Стоит избавиться от любых видов заглушек (маркеров, которыми заполнили пропуски) при расчете коэф. корреляции и строительстве графиков (нулевых, отрицательных, положительных)
#         
# Стоит поправить все расчеты в этом подразделе        

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Широкие строки кода рекомендуется делить на всем проекте
#         
# <a href="https://qastack.ru/programming/53162/how-can-i-do-a-line-break-line-continuation-in-python">Перенос длинных строк кода</a>. 
#     
# </div>

# In[71]:


games_actual_other_name = decline_period_data.groupby(by=['platform'])['total_sales'].agg('sum').sort_values(ascending=False)[:7]
games_actual_other_name


# Уберем платформу x360 из списка

# In[72]:


games_actual_other_name = games_actual_other_name[~games_actual_other_name.index.isin(['x360'])]
games_actual_other_name


#  Выделим данные в отдельную таблицу games_actual_other.

# In[73]:


games_actual_other = decline_period_data[decline_period_data['platform'].isin(games_actual_other_name.index)]
games_actual_other.info()


# In[74]:


fig, axes = plt.subplots(nrows=6, ncols=2, figsize=(25,25*3))
for ax, (name_platform, data_slice) in zip(axes[:,0], games_actual_other.groupby(by='platform')):
    # полином будем строить на основе чистых данных
    x_filter = data_slice.query('user_score > 0')["total_sales"]
    # выислить коэффициенты полинома и создать объект полинома
    p1_user_score = np.poly1d(np.polyfit(x_filter,
                                         data_slice.query('user_score > 0')["user_score"], 1))
    # аппроксимированные значения
    approx_user_score = p1_user_score(x_filter)

    sns.scatterplot(ax=ax, data=data_slice[data_slice['platform'] == name_platform], x="total_sales", y="user_score")
    ax.grid()
    ax.set_xlim(0,5)
    # нужно чтобы оси графика были одинаковыми и неискажали преставление
    ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
    ax.set_title('Диаграмма рассеяния продаж игр на платформе ' + name_platform + ' от отзывов пользователей')
    ax.plot(x_filter, approx_user_score, '-r', label='аппроксимация полиномом 1го порядка')
    ax.legend(loc='upper right')
    
for ax, (name_platform, data_slice) in zip(axes[:,1], games_actual_other.groupby(by='platform')):
    # полином будем строить на основе чистых данных
    x_filter = data_slice.query('critic_score > 0')["total_sales"]
    # выислить коэффициенты полинома и создать объект полинома
    p1_critic_score = np.poly1d(np.polyfit(x_filter,
                                           data_slice.query('critic_score > 0')["critic_score"], 1))
    # аппроксимированные значения
    approx_critic_score = p1_critic_score(x_filter)

    sns.scatterplot(ax=ax, data=data_slice[data_slice['platform'] == name_platform], x="total_sales", y="critic_score")
    ax.grid()
    ax.set_xlim(0,5)
    # нужно чтобы оси графика были одинаковыми и неискажали преставление
    ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')
    ax.set_title('Диаграмма рассеяния продаж игр на платформе ' + name_platform + ' от оценки критиков')
    ax.plot(x_filter, approx_critic_score, '-r', label='аппроксимация полиномом 1го порядка')
    ax.legend(loc='upper right')


# В общем, динамика зависимости мнений пользователей и оценок критиков от продаж игр на определенной платформе остается схожей. Продажи не зависят от мнения пользователей и лишь слегка зависят от оценок критиков. На платформе Wii зависимости продаж от оценок пользователей и критиков совпадают. Давайте рассмотрим корреляцию мнений пользователей.

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />К сожалению, этот код часто встречается в интернете, стоит поменять местами два графика: слева расположить оценки критиков, а оценки пользователей справа
#         
# ![image.png](attachment:image.png)        

# In[75]:


fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(7*3,7*2))
for ax, (name_platform, data_slice) in zip(axes.ravel(), games_actual_other.groupby(by='platform')):
    data_slice = data_slice.query('user_score > 0')
    sns.heatmap(data_slice[['total_sales', 'user_score']].corr(),
                ax=ax, annot=True, fmt='.2f', vmin=0,vmax=1, square=True,
                annot_kws={"size": 18})
    ax.set_title('Корреляция платформы ' + name_platform)


# In[76]:


fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(7*3,7*2))
for ax, (name_platform, data_slice) in zip(axes.ravel(), games_actual_other.groupby(by='platform')):
    data_slice = data_slice.query('critic_score > 0')
    sns.heatmap(data_slice[['total_sales', 'critic_score']].corr(),
                ax=ax, annot=True, fmt='.2f', vmin=0,vmax=1, square=True,
                annot_kws={"size": 18})
    ax.set_title('Корреляция платформы ' + name_platform)


#  Кроме платформы PC, остальные платформы показывают слабую зависимость между оценкой критиков и продажами. Результаты на графиках в основном согласуются со значениями корреляции по каждой платформе, но есть исключения. Например, визуально на платформе PC  на графике зависимость оценок критиков от продаж кажется выше, чем показывает корреляция. Это связано с тем, что данные кучкуются в одном месте, а разброс не большой. Вывод
# От мнения пользователй продажи не зависят, а от оценок критиков зависят слабо, эти результаты согласуются с результатми сделанными по популярной платформе X360.

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Возможно пользователи более критичны к играм, чем критики, но мы не сможем оценить какие действия повлияли на рост продаж в рамках нашего проекта (ограниченность имеющихся данных)
#         
#     
# __Достаточно много игр с высокой оценкой критиков и слабой выручкой__
#         
# Приведу пример ложной корреляции, весьма известный в статистической литературе. Была исследована корреляционная связь между числом аистов, свивших гнезда в южных районах Швеции, и рождаемостью в эти же годы в Швеции. Расчёты, выполненные ради шутки, показали существенную положительную корреляцию между этими явлениями, хотя любому понятно, что это ложная корреляция.
# 
# Ещё пример ложной корреляции между приемом на работу новых менеджеров и созданием новых производственных мощностей. Возможно, именно менеджеры являются «причиной» капиталовложений в новые производственные мощности? Или же, наоборот, создание новых производственных мощностей послужило «причиной» приема на работу новых менеджеров?
# 
# Например, можно обнаружить сильную положительную связь (корреляцию) между разрушениями, вызванными пожаром, и числом пожарных, тушивших пожар. Следует ли заключить, что пожарные вызывают разрушения? Конечно, наиболее вероятное объяснение этой корреляции состоит в том, что размер пожара (внешняя переменная, которую забыли включить в исследование) оказывает влияние, как на масштаб разрушений, так и на числе привлеченных пожарных (т. е. чем больше пожар, тем большее количество пожарных вызывается на его тушение) .

# # Зависимость продаж от жанра

# In[77]:


fig, ax = plt.subplots(figsize=(18,10))
sns.boxplot(y="genre", x="total_sales", data=decline_period_data, orient="h", ax=ax)
ax.grid()
ax.set_xlim(0,2.0)
ax.xaxis.set(ticks=np.arange(0,2.1,0.1));
ax.set_title('Диаграмма распределения продаж игр по всем регионам в зависимости от жанра')
pass


# In[78]:


fig2, ax2 = plt.subplots(figsize=(18, 10))
sns.boxplot(y="genre", x="total_sales", data=decline_period_data, orient="h", ax=ax2, showfliers=False)
ax2.grid()
ax2.set_xlim(0, 2.0)
ax2.xaxis.set(ticks=np.arange(0, 2.1, 0.1))
ax2.set_title('Диаграмма распределения продаж игр по всем регионам в зависимости от жанра (без выбросов)')

plt.show()


# Самым популярным (продаваемым) жанром является action, который с большим отрывом уходит вперед. Медианное значение проданных игровых копий превышает для него 400 тысяч. За ним следует жанр Sports с отставанием в 200 тысяч копий, далее жанр Platform с похожими показателями. Самые же невостребованные на рынке жанры это Adventure и Puzzle. Значение медианных продаж не превышает 50 тысяч проданных копий.

# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />        
# Стоит  поправить вывод
#         
# В выводе нет ни слова про жанр shooter, хотя он показывает самый значительный ящик среди всех жанров. То что для экшена считается как выброс, для шутера обычное дело и попадает в третий квартиль

# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />        
# Стоит  поправить вывод
#         
#         Наиболее востребованным (продаваемым) жанром является action, который значительно опережает остальные. Медиана продаж для этого жанра превышает 400 тысяч копий. Второе место занимает жанр Sports, уступая action примерно на 200 тысяч копий. За ним следует жанр Platform с аналогичными результатами. Самыми малопопулярными на рынке являются жанры Adventure и Puzzle, где медианные продажи не превышают 50 тысяч копий.
#         
# диаграмма размаха показывает немного другую картину        
#         
# ![image.png](attachment:image.png)        

# In[79]:


fig2, ax2 = plt.subplots(figsize=(14, 6))
sns.boxplot(y="genre", x="total_sales", data=decline_period_data, orient="h", ax=ax2)
ax2.set_title('Диаграмма распределения продаж игр по всем регионам в зависимости от жанра (без выбросов)')

plt.show()


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Что показывают нам две диаграммы размаха — кол-во выбросов, это игры, которые принесли максимум выручки. Т.е. можно платформы/жанры сравнить по кол-ву игр-рекордсменов, а значит определить, какая из них способна выпустить наиболее привлекательные для игроманов игры. Это про выбросы
#         
# Второй вид мы используем для того, чтобы сравнить медианные продажи по платформе/жанру, чтобы уточнить в каком кол-ве продаются игры на платформе/жанре, какая из них более стабильна в продажах...
#         
#         
# Две хорошие статьи про диаграмму размаха
#         
# [Ящики, усы и скрипки](https://habr.com/ru/articles/533726/) 
#         
# [Исследуем отношение между переменными](https://dfedorov.spb.ru/pandas/downey/%D0%98%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D0%B5%D0%BC%20%D0%BE%D1%82%D0%BD%D0%BE%D1%88%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BC%D0%B5%D0%B6%D0%B4%D1%83%20%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8.html?)
#         

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />        
# Стоит проанализировать прибыльность жанров на диаграмме размаха, сравнить медианные продажи на каждом жанре и проверить какая из них более стабильна и имеет более длинный ряд успешно продающихся игр
#         
# График нарисовать __в двух масштабах с выбросами и без__ (чтобы было видно 0.75-квантиль)

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />        
# Стоит  добавить второй вид диаграммы — в 100% масштабе, без ограничений
#         
#         ax.set_xlim(0,2.0)

# # Вывод
# Анализ данных за период с 1980 по 1992 годы затруднен из-за малого количества данных (менее 50). Статистика за другие годы является корректной. Количество пропусков в данных примерно соответствует количеству выпущенных игр за первое десятилетие, что может привести к значительным искажениям в выводах. Пик популярности видеоигр пришелся на 2005-2011 годы. В среднем каждые 5 лет на рынке появляются новые платформы, которые функционируют около 10 лет, а затем исчезают примерно за 5 лет. Однако это среднее значение, разброс фактических данных достаточно велик, особенно в отношении продолжительности жизни платформ. Платформы DS и PC демонстрируют аномально долгую жизнь, в то время как PS4 только начинает свой путь. Выберем актуальный период с 2012 по 2016 годы для анализа, чтобы ориентироваться на активных игроков рынка. На момент 2016 года молодыми и наиболее прибыльными платформами являются PS4, XOne и 3DS. К этому времени продажи многих платформ значительно снизились, что указывает на завершение их жизненного цикла. В 2013 году появилось несколько новых платформ. Платформа PC может быть отнесена к аномальным, так как ее продажи низкие (в среднем 211 тысяч копий), однако она существует уже долгое время и, скорее всего, в следующем году ее доход останется на том же уровне. Данные очень нестабильны, с множеством выбросов в любом регионе. Основная часть игр, распределенных по платформам (50% от общего числа), продается в количестве не более 750 тысяч копий. В каждом регионе наиболее успешными платформами оказались PS4, X360, XOne и Wii. В то же время, платформы PC, PSV и PSP демонстрируют низкие продажи в текущем временном интервале, их доход не превышает 250 тысяч копий. Корреляция подтвердила наше предположение: зависимость между продажами и отзывами пользователей отсутствует, корреляция близка к 0. Зависимость между продажами и оценками критиков слабая, корреляция меньше 0.5. Действительно, популярные журналы и порталы о видеоиграх своими рецензиями могут повлиять на продаваемость игр. Продажи не зависят от мнения пользователей, а от оценок критиков зависят слабо, что согласуется с результатами, полученными для популярной платформы X360.
# 
# 

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит поправить нюансы ⬆⬆
#         
#         Платформы DS и PC демонстрируют аномально долгую жизнь, в то время как PS4 только начинает свой путь
#         
# в промежуточном выводе не хватает части про жанры        

# # Шаг 4
# 

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Стоит добавить короткий обобщающий вывод по результатам выполнения раздела проекта

# ### check

# In[80]:


regions = ['na_sales','eu_sales','jp_sales']
def get_top_5(region, by_col):
    df_temp = decline_period_data.groupby(by=by_col)[region].agg('sum').sort_values(ascending=False).to_frame()
    top_5 = df_temp[:5].index
    df_temp.index = df_temp.index.where(df_temp.index.isin(top_5),'other')
    return df_temp.groupby(by=df_temp.index)[region].agg('sum').sort_values(ascending=False)


# In[81]:


top_5_sales_by_regions = pd.concat([get_top_5(regions[0], 'platform'),
                                    get_top_5(regions[1], 'platform'),
                                    get_top_5(regions[2], 'platform')], axis=1)
top_5_sales_by_regions


# In[82]:


ax = top_5_sales_by_regions.sum().plot(
    kind='pie',
    autopct=lambda p: '{:.2f}%({:.0f})'.format(p,(p/100)*top_5_sales_by_regions.sum().sum()),
    textprops={'fontsize': 15},
    figsize=(6,6),
    title='Общие продажи в регионах')

ax.axis('off');


# Самые заядлые игроки живут в Северной Америке, более половины всех покупок видеоигр (45%) приходится на них - 591 миллионов копий. На втором месте расположился Европейский регион (40%), 507 миллионов копий. Ну а самый маленький это Японский всего (14.5%), 193 миллион копий.

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Портреты клиентов нарисованы, молодец, значительное влияние на портрет оказывает период с 1980 г. ..., можем совершить ошибку при формировании рекомендации маркетологам
#         
# Стоит оформить графики раздела TOП-5:
# 
# + выбрать актуальный период;
# + оформить "двухуровневый заголовок" - и у всех трех графиков вместе, и у каждого из трех по отдельности;
# + при анализе платформ и жанров стоит все, что не вошло в ТОП-5, объединять в категорию "другие" - так картина анализа будет более полной
# 
#         
# Если столкнешься с трудностью выполнения данного пункта — присылай код, который не получился и вопрос, подумаем вместе
#         
# https://proproprogs.ru/modules/matplotlib-otobrazhenie-neskolkih-koordinatnyh-osey-v-odnom-okne
#         
#     

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> пример графиков
#         
# ![image.png](attachment:image.png)        
#         
# 
# __Если столкнешься с трудностью выполнения данного пункта — присылай код, который не получился и вопрос, подумаем вместе__
# 

# In[83]:


axes = top_5_sales_by_regions.plot.pie(subplots=True,
                                figsize=(20, 8),
                                autopct=lambda p: '{:.2f}%'.format(p) if p > 0 else '',
                                textprops={'fontsize': 15},
                                legend=False,
                                title='ТОП-5 платформ в регионах')
for id_,ax in enumerate(axes):
    ax.axis('off')
    ax.set_title(regions[id_].upper().split('_')[0])


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Отличный график, молодец
#         
#         если уменьшить высоту, сократится разрыв между заголовком и диаграммами

# Вкусы в Северной Америке и Европе схожи: и там, и там живут фанаты экшнов, спортивных игр и шутеров. В Северной Америке больше играют в платформеры, в Европе же чаще выбирают гонки.
# 
# 
# В Японии вкус совершенно иной - на первом месте ролевые игры, причем с большим отрывом. Далее экшны и спортивные игры.

# In[84]:


top_5_sales_by_genre = pd.concat([get_top_5(regions[0], 'genre'),
                                    get_top_5(regions[1], 'genre'),
                                    get_top_5(regions[2], 'genre')], axis=1)
top_5_sales_by_genre


# In[85]:


axes = top_5_sales_by_genre.plot.pie(subplots=True,
                                figsize=(20, 8),
                                autopct=lambda p: '{:.2f}%'.format(p) if p > 0 else '',
                                textprops={'fontsize': 15},
                                legend=False,
                                title='ТОП-5 жанров в регионах')
for id_,ax in enumerate(axes):
    ax.axis('off')
    ax.set_title(regions[id_].upper().split('_')[0])


#  Влияние рейтинга ESRB на продажи

# <div class="alert alert-d anger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит поправить код категоризации, у тебя словарь не соответствует данным в колонке ['rating']
#         
#         ESRB_dict = {'E': 'Для всех', 'M': '> 17 лет', 'T': '13-19 лет', 'E10+': '>10 лет', 'K-A': 'Для всех(устар.)'}
#         
# по этой причине ломается код отрисовки графиков        

# In[86]:


def get_ESRB(region, by_col):
    return decline_period_data.groupby(by=by_col)[region].agg('sum').sort_values(ascending=False)


# In[87]:


sales_by_ESRB = pd.concat([get_ESRB(regions[0], 'rating'),
                           get_ESRB(regions[1], 'rating'),
                           get_ESRB(regions[2], 'rating')], axis=1)
sales_by_ESRB


#  Напомним возрастной рейтинг ESRB содержит информацию о принадлежности игры той или иной возрастной группе:
# EC      от 3 летE       от 6 летK-A     от 6 лет (тоже что и E, использовался до 1998)E10+    от 10 летT       от 13 летM       от 17 летAO      от 18 летRP      рейтинг ожидается

# In[88]:


axes = sales_by_ESRB.plot.pie(subplots=True,
                                figsize=(20, 8),
                                autopct=lambda p: '{:.2f}%'.format(p) if p > 0 else '',
                                textprops={'fontsize': 15},
                                legend=False,
                                title='рейтинг ESRB в регионах')
for id_,ax in enumerate(axes):
    ax.axis('off')
    ax.set_title(regions[id_].upper().split('_')[0])


# Игроки из разных регионов одинаково распределяются по возрастным группам пропорционально численности игроков в регионе за актуальный период. Больше всего покупают игры с рейтнгом E и M. Игры с рейтингом EC, AO не покупают совсем. Количество игр с неопределнным рейтингом (RP) в Японии велико, так как рейтинг ESRB в этой стране не используется (только в Канаде и США), бизнес-процессы в этой стране отражает другой рейтинг.

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Заполнение пропусков в рейтинге позволило определить отличия региональных рынков, молодец

# Вывод по каждому региону.
# Анализ рынка видеоигр по регионам
# 
# **1. Распределение игроков по возрастным группам:**
# Игроки из разных регионов распределяются по возрастным группам пропорционально численности игроков в регионе за актуальный период. Наиболее популярными рейтингами являются E и M, в то время как игры с рейтингами EC и AO практически не покупаются. В Японии значительное количество игр имеет неопределенный рейтинг (RP), так как в этой стране не используется рейтинг ESRB.
# 
#  **2. Региональные особенности рынка:**
# 
# Северная Америка: Наиболее активные игроки, где более половины всех покупок видеоигр (46%) составляют 591 миллион копий. Предпочитают платформы PS4 и X360, а также жанры action, shooter и sports.
# 
# Европа: Второе место с долей в 39% и 507 миллионами копий. Также предпочитают PS4 и X360, а также жанры action и sports. Специфичным жанром для Европы является racing.
# 
# Япония: Наименьший рынок с долей в 15% и 193 миллионами копий. Предпочитают платформу 3DS и жанр RPG. Специфичными жанрами для Японии являются Simulation и Fighting.
# 
# **3. Платформы и жанры:**
# 
# Платформы: PS4 и X360 популярны в Северной Америке и Европе, в то время как 3DS доминирует в Японии. Платформа PS3 популярна во всех регионах.
# 
# Жанры: Action является популярным во всех регионах, но предпочтения в поджанрах различаются. Shooter и sports популярны в Северной Америке и Европе, в то время как RPG доминирует в Японии.
# 
# **4. Рейтинги игр:**
# 
# Рейтинги E и M: Наиболее популярны во всех регионах.
# 
# Рейтинги EC и AO: Практически не покупаются.
# 
# Рейтинг RP: Значительное количество в Японии, где не используется рейтинг ESRB.
# 
# **5. Выводы и рекомендации:**
# 
# Северная Америка и Европа: Следует продолжать фокусироваться на платформах PS4 и X360, а также на жанрах action, shooter и sports.
# 
# Япония: Важно учитывать специфику рынка, включая предпочтения в платформе 3DS и жанре RPG.
# 
# Обновление данных: Учитывая возраст платформы X360, рекомендуется обновить актуальный период и перепроверить выводы, чтобы учесть изменения на рынке.

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Х360 уже исполнилось 11 лет и она с малой вероятностью станет перспективной в 2017 году — стоит изменить актуальный период и перепроверить выводы
#         
#         Например, Северная Америка и Европа предпочитают PS4 и X360, которые составляют около 42% рынка в этих регионах. 

# # Шаг 5

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br />  
#     <font size="3", color = "black">
# <br />
# При твоем способе подсчета игры без рейтинга оказываются полностью исключенными из анализа. Но продажи именно этих игр могут указать на ключевое различие в регионах
#         
# Стоит поработать со столбцом рейтингов, заменить пропуски, посмотреть на частотность использования всех категорий рейтинга

# <div class="alert alert-dang er">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Стоит добавить короткий обобщающий вывод по результатам выполнения раздела проекта

# ### check

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Нулевая и альтернативная гипотезы не сформулированы

# Рассмотрим три ключевых условия для применения t-теста:
# 
# Независимость генеральных совокупностей: генеральные совокупности, из которых взяты выборки, не должны зависеть друг от друга. Если вы анализируете одну и ту же генеральную совокупность до и после изменения, следует использовать другой тип теста.
# 
# Нормальное распределение выборочных средних: выборочные средние должны быть распределены нормально. Если выборка одна, ее среднее значение должно иметь нормальное распределение, предполагая, что это справедливо для других выборок такого же размера из той же генеральной совокупности. Это условие обычно не является проблемой, так как Центральная Предельная Теорема (ЦПТ) утверждает, что при достаточно большом размере выборки (несколько десятков значений), выборочные средние будут нормально распределены вокруг истинного среднего генеральной совокупности, даже если сама генеральная совокупность не имеет нормального распределения.
# 
# Равенство дисперсий генеральных совокупностей: дисперсии генеральных совокупностей, из которых взяты выборки, должны быть равны. Это условие может быть сложным, так как точно определить равенство дисперсий не всегда возможно. По умолчанию, при выполнении t-теста предполагается, что дисперсии равны (equal_var=True), и выборки объединяются для более точной оценки дисперсии. Однако, если выборки достаточно велики (30 и более значений) и имеют одинаковый размер, такой подход оправдан. В случае, когда выборки имеют разный размер и/или есть основания полагать, что дисперсии генеральных совокупностей различаются, рекомендуется указать equal_var=False при вызове метода scipy.stats.ttest_ind(). В других случаях тест можно использовать без изменений.

# In[89]:


games_actual_pc_usr_score = decline_period_data[decline_period_data['platform'] == 'pc'].query('user_score > 0')['user_score']
games_actual_xone_usr_score = decline_period_data[decline_period_data['platform'] == 'xone'].query('user_score > 0')['user_score']


# In[90]:


stat_fun = ['count','mean','median','var', 'std','min','max']
PC_vs_Xone_user_score_descr = pd.concat([games_actual_pc_usr_score.agg(stat_fun).transpose(),
           games_actual_xone_usr_score.agg(stat_fun).transpose()], axis=1)
PC_vs_Xone_user_score_descr.columns = ['пользовательский рейтинг PC', 'пользовательский рейтинг XOne']
PC_vs_Xone_user_score_descr.loc['Стандартная ошибка (E.S.E.)'] =     PC_vs_Xone_user_score_descr.loc['std',:]/np.sqrt(PC_vs_Xone_user_score_descr.loc['count',:])
PC_vs_Xone_user_score_descr


# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера в2</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />          
# Стоит поправить код, у тебя нет такой переменной
#         
#         NameError: name 'games_actual_PC_usr_score' is not defined

#  Пологаю, что исходные данные являются выборками, и их генеральные совокупности не зависят друг от друга. Количество элементов в выборках различается, дисперсии равны. Средние показатели рейтингов двух приставок различаются но не сильно. Перед проведением теста, осталось выяснить, является распределение выборок нормальным (правда, есть авторитетное мнение что если, выборка больше 50 вид распределения можно не учитывать). Рейтинг пользователей является дискрентной величиной, поэтому будем использовать гистограмму для визуализации распределения.

# In[91]:


fornt_size = 15

fig, ax1 = plt.subplots(nrows=1,ncols=1)
fig.set_size_inches(15, 9)

games_actual_pc_usr_score.plot.hist(ax=ax1, grid=True, bins=40, label='распределение пользовательского рейтинга PC')
ax1.axvline(games_actual_pc_usr_score.median(), color='r', label='медиана  PC')
games_actual_xone_usr_score.plot.hist(ax=ax1, grid=True, bins=40, label='распределение пользовательского рейтинга XOne')
ax1.set_xlabel('пользовательский рейтинг платформ', fontsize=fornt_size)
ax1.set_ylabel('Частота', fontsize=fornt_size)
ax1.axvline(games_actual_xone_usr_score.median(), color='g', label='медиана  XOne')
ax1.legend()
pass


#  Вид распределения у двух платформ похоже на нормальное распределение, центры которых расположены в районе 7 с добавлением хвостов слева идущих от 0. Также наглядно видно в различии объема данных в двух выборках.По соборанной нами информации t-тест проводить не совсем корректно - размеры выборок не равны. Но попробуем, посмотрим что получится.И так, зададим ворота пошире (т.к. выборки сильно различаются по размеру) - выставим уровень статистической значимости alpha равным 1%. Выдвинем нулевую гипотезу H0 о равенстве средних двух генеральных совокупностей - пользовательского рейтинга платформ Xbox One и PC, и противоположную гипотезу H1 соотвественно что не равны.По «правилу большого пальца»: если выборки разного размера и/или можно предположить, что дисперсии у генеральных совокупностей разные — укажите equal_var = False

# In[92]:


alpha = 0.01 
results = st.ttest_ind(games_actual_pc_usr_score, games_actual_xone_usr_score, equal_var=False)

print('p-значение:', results.pvalue, 'статистика разности:', results.statistic)

if results.pvalue > alpha:
    print("Верна H0. Не получилось отвергнуть нулевую гипотезу - среднее выборок равны.") 
else:
    print("Верна H1. Отвергаем нулевую гипотезу - среднее выборок не равны.")


# Вывод
# По результатам t-теста, проведенного для сравнения средних значений пользовательского рейтинга платформ Xbox One и PC, не было обнаружено статистически значимых различий между средними значениями (p > α). Следовательно, на основе имеющихся данных нет оснований отвергать нулевую гипотезу о том, что средние значения пользовательского рейтинга для этих двух платформ равны.

# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> 
# Стоит исправить все подобные моменты
#         
#          Гипотеза H0 верна, или Верна H0
# 
# <b>Из теории на тренажере</b>
#         
# Формулирование двусторонних гипотез. <br>
#         
# <b>Никакие экспериментально полученные данные никогда не подтвердят какую-либо гипотезу. Это наше фундаментальное ограничение. </b>Данные могут лишь не противоречить ей или, наоборот, показывать крайне маловероятные результаты (при условии, что гипотеза верна). Но и в том, и в другом случае нет оснований утверждать, что выдвинутая гипотеза доказана.
# Допустим, данные гипотезе не противоречат, тогда мы её не отвергаем. Если же мы приходим к выводу, что получить такие данные в рамках этой гипотезы вряд ли возможно, у нас появляется основание отбросить эту гипотезу.
#         
# https://allatambov.github.io/psms/pdf/hypo-test.pdf
# 

# Cредние пользовательские рейтинги жанров Action  и Sports разные
# 
# 
# Подготовим данные, выделим нужную информацию в отдельные датафреймы и уберем лишние значения.

# In[93]:


games_actual_action = decline_period_data[decline_period_data['genre'] == 'action'].query('user_score > 0')['user_score']
games_actual_sports = decline_period_data[decline_period_data['genre'] == 'sports'].query('user_score > 0')['user_score']


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Важно удалить пропуски и «заглушки» перед проведением теста, молодец

# In[94]:


stat_fun = ['count','mean','median','var', 'std','min','max']
action_vs_sports_user_score_descr = pd.concat([games_actual_action.agg(stat_fun).transpose(),
           games_actual_sports.agg(stat_fun).transpose()], axis=1)
action_vs_sports_user_score_descr.columns = ['пользовательский рейтинг жанра Actions', 'пользовательский рейтинг жанра Sports']
action_vs_sports_user_score_descr.loc['Стандартная ошибка (E.S.E.)'] =     action_vs_sports_user_score_descr.loc['std',:]/np.sqrt(action_vs_sports_user_score_descr.loc['count',:])
action_vs_sports_user_score_descr


# Пологаю, что исходные данные являются выборками, и их генеральные совокупности не зависят друг от друга. Количество элементов в выборках сильно различается (в два раза), дисперсии равны. Средние показатели рейтингов двух жанров различаются но не сильно. Перед проведением теста, осталось выяснить, является распределение выборок нормальным (правда, есть авторитетное мнение что если, выборка больше 50 вид распределения можно не учитывать). Рейтинг пользователей является дискрентной величиной, поэтому будем использовать гистограмму для визуализации распределения.

# <div class="alert alert-warning", style="border:solid coral 3px; padding: 20px">
# <font size="4", color = "DimGrey"><b>⚠️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> 
#         
#         осталось выяснить, является распределение выборок нормальным (правда, есть авторитетное мнение что если, выборка больше 50 вид распределения можно не учитывать)
#         
#         
# Рассмотрим три аспекта, которые надо проверить, чтобы понять, можно ли применять t-тест:
#         
# Генеральные совокупности не должны зависеть друг от друга.
# 
# + Если вы рассматриваете одну генеральную совокупность до и после какого-то изменения, нужно использовать другой тест.
#         
# Выборочные средние должны быть нормально распределены.
#         
# + А если выборка всего одна, то её среднее должно иметь нормальное распределение для разных выборок этого размера из определённой генеральной совокупности.
#         
# + Это условие не препятствие. Благодаря ЦПТ, если размер выборки составляет хотя бы несколько десятков значений, выборочные средние, которые можно получить из одной и той же генеральной совокупности, будут распределены нормально вокруг истинного среднего этой совокупности. Напомним, это утверждение верно, даже если сама генеральная совокупность не распределена нормально.
#         
#         
# __☝🏻 Очень часто это условие путают с необходимостью нормального распределения самих генеральных совокупностей. Для корректного использования t-теста это необязательно.__
#         
# Дисперсии рассматриваемых генеральных совокупностей должны быть равны.
#         
# + Это коварное условие. С одной стороны, вы никогда точно не знаете, равны ли дисперсии рассматриваемых генеральных совокупностей. С другой — по умолчанию параметр equal_var принимает значение True: дисперсии считаются равными и тест объединяет обе выборки в одну, чтобы эту дисперсию поточнее оценить. При этом если выборки достаточно велики (30 и больше значений) и равны по размеру между собой, такой подход оправдан: симуляции, проведённые учёными, показывают, что даже если дисперсии на самом деле не равны, то тест редко ошибается.
#         
#         
# [Как правильно считать деньги, или Несколько слов в пользу теста Стьюдента](https://habr.com/ru/company/glowbyte/blog/594183/?)

# In[95]:


fornt_size = 15

fig, ax1 = plt.subplots(nrows=1,ncols=1)
fig.set_size_inches(12, 12)

games_actual_action.plot.hist(ax=ax1, grid=True, bins=40, label='распределение пользовательского рейтинга жанра Action')
ax1.axvline(games_actual_action.median(), color='r', label='медиана  Action')

games_actual_sports.plot.hist(ax=ax1, grid=True, bins=40, label='распределение пользовательского рейтинга жанра Sports')
ax1.set_xlabel('пользовательский рейтинг жанров', fontsize=fornt_size)
ax1.set_ylabel('Частота', fontsize=fornt_size)
ax1.axvline(games_actual_sports.median(), color='g', label='медиана  Sports')
ax1.legend()
ax1.xaxis.set(ticks=range(0,11,1))
pass


# Распределение двух жанров напоминает нормальное распределение с центрами около 6 и 7, а также с легкими хвостами, идущими от 0. Также заметно различие в объеме данных между двумя выборками. Исходя из собранной информации, проведение t-теста может быть не совсем корректным, так как размеры выборок не равны. Однако, давайте попробуем и посмотрим, что получится.
# 
# Установим более широкие рамки, учитывая значительное различие в размерах выборок, и зададим уровень статистической значимости alpha равным 1%. Сформулируем нулевую гипотезу H0 о равенстве средних значений двух генеральных совокупностей - пользовательского рейтинга жанров Actions и Sports, и альтернативную гипотезу H1 о неравенстве средних значений.
# 
# Согласно "правилу большого пальца": если выборки имеют разный размер и/или можно предположить, что дисперсии генеральных совокупностей различаются, следует указать equal_var = False при проведении t-теста.

# In[96]:


alpha = .01 # критический уровень статистической значимости
# если p-value окажется меньше него - отвергнем гипотезу

results = st.ttest_ind(games_actual_action, games_actual_sports, equal_var=False)

print('p-значение:', results.pvalue, 'статистика разности:', results.statistic)

if results.pvalue > alpha:
    print("Верна H0. Не получилось отвергнуть нулевую гипотезу - среднее выборок равны.") 
else:
    print("Верна H1. Отвергаем нулевую гипотезу - среднее выборок не равны.")


#  Вывод
#  
#  
# Даже с заниженным порогом уровня статической значимости alpha в 1% гипотеза H0 не верна, величина Pvalue равна 0. Правда тест был не совсем корректный т.к. размер выборок был неодинаков. Статистика разности тоже имеет большое значение - 9.93. Итог, средняя пользовательского рейтинга жанров Action и Sports различается, у  жанра Action она на 1.45 выше.

# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Что означает на языке статистики p-значение: 3.551295319559386e-20

# <div class="alert alert-info">
# <font size="4", color = "black"><b>✍ Комментарий студента</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# p-значение: 3.551295319559386e-20 — это очень маленькое число, которое можно записать в десятичной форме как 0.00000000000000000003551295319559386. Это означает, что вероятность наблюдать такие или еще более экстремальные данные при условии, что нулевая гипотеза верна, чрезвычайно мала.
# 
# В статистических тестах обычно устанавливается пороговое значение, называемое уровнем значимости (α), которое обычно равно 0.05 (5%) или 0.01 (1%). Если p-значение меньше или равно этому пороговому значению, то нулевая гипотеза отвергается в пользу альтернативной гипотезы (H1), которая утверждает наличие различий или связи.
# 
# В вашем случае p-значение настолько мало (намного меньше 0.01), что можно с высокой степенью уверенности отвергнуть нулевую гипотезу и принять альтернативную гипотезу о наличии статистически значимых различий или связи между переменными.

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера в4</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />
# Приведу пример и теорию для понимания формулировок и интерпретации итогов проведения гипотез</b>
#         
#       
# Задача. Приведены два датасета: сумма покупок, совершённых за месяц посетителями, привлечёнными по двум разным каналам. В вашем распоряжении случайная выборка из 30 покупок для каждого канала.
#         
# H0 - средние чеки равны
#         
#         
# H1 - средние чеки НЕ равны
# 
# Да сама формулировка нулевой и альтернативной гипотезы звучит именно так, но результат теста интерпретируется другими словами
#     
#         
# Формулирование двусторонних гипотез. <br>
#         
# <b>Никакие экспериментально полученные данные никогда не подтвердят какую-либо гипотезу. Это наше фундаментальное ограничение. </b>Данные могут лишь не противоречить ей или, наоборот, показывать крайне маловероятные результаты (при условии, что гипотеза верна). Но и в том, и в другом случае нет оснований утверждать, что выдвинутая гипотеза доказана.
# Допустим, данные гипотезе не противоречат, тогда мы её не отвергаем. Если же мы приходим к выводу, что получить такие данные в рамках этой гипотезы вряд ли возможно, у нас появляется основание отбросить эту гипотезу.
#      

# In[97]:


# Приведены два датасета: сумма покупок, совершённых за месяц посетителями ...

sample_1 = [3071, 3636, 3454, 3151, 2185, 3259, 1727, 2263, 2015,
2582, 4815, 633, 3186, 887, 2028, 3589, 2564, 1422, 1785,
3180, 1770, 2716, 2546, 1848, 4644, 3134, 475, 2686,
1838, 3352]
sample_2 = [1211, 1228, 2157, 3699, 600, 1898, 1688, 1420, 5048, 3007,
509, 3777, 5583, 3949, 121, 1674, 4300, 1338, 3066,
3562, 1010, 2311, 462, 863, 2021, 528, 1849, 255,
1740, 2596]
alpha = .05 # критический уровень статистической значимости
# если p-value окажется меньше него - отвергнем гипотезу
results = st.ttest_ind(
sample_1,
sample_2)
print('p-значение:', results.pvalue)
if (results.pvalue < alpha):
    print("Отвергаем нулевую гипотезу")
else:
    print("Не получилось отвергнуть нулевую гипотезу")


# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера в4</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />
# Интерпретация результата:
# 
# Полученное значение p-value говорит о том, что хотя средний чек пришедших из разных каналов и неодинаков, <b>с вероятностью в почти 19% такое или большее различие можно получить случайно. </b>Это явно слишком большая вероятность, чтобы делать вывод о значимом различии между средними чеками.
#         
# А если p-value  будет равно 0,9999, то это значит, что с вероятностью почти 100% <u>такое различие</u> можно получить случайно — то есть почти никогда :)  (но учитываем, что тест проводится на выборке из генеральной совокупности, все может поменяться)
# 

# # Общий вывод по шагу 5 ##
# Был проведен t-тест для сравнения средних значений двух генеральных совокупностей - пользовательского рейтинга платформ Xbox One и PC с исходными выборками. Гипотеза H0 о равенстве средних значений не была отвергнута, так как статистика разности была незначительной при уровне статистической значимости alpha, равном 1%. Несмотря на то, что значение P-value составило 0, что обычно указывает на статистическую значимость, следует учесть, что тест мог быть не совсем корректным из-за неодинакового размера выборок. В результате, хотя средний пользовательский рейтинг жанров Action и Sports различается, причем рейтинг жанра Action на 1.45 выше, на основе данных t-теста нет достаточных оснований для отклонения гипотезы H0 о равенстве средних значений пользовательского рейтинга платформ Xbox One и PC.

# <div class="alert alert-dang er">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит поправить
#         
#          Гипотеза H0 о равенстве средних значений подтвердилась, так как 

# #  Общий Вывод
# В среднем, новые платформы появляются на рынке каждые 5 лет, проводят около 10 лет на рынке, а затем исчезают примерно за 5 лет. Однако, это среднее значение, и разброс данных достаточно велик, особенно в отношении времени жизни платформ. На основе рассчитанного времени появления платформ на рынке был выбран актуальный период с 2012 по 2016 год. К 2016 году молодыми и наиболее прибыльными платформами можно считать PS4, XOne и 3DS. Продажи многих других платформ к этому времени значительно снизились, что указывает на завершение их жизненного цикла. В 2013 году появилось несколько новых платформ. Аномальной платформой является PC, у которой низкие продажи (в среднем 211 тыс. копий), но она существует уже долгое время и, вероятно, в следующем году будет иметь аналогичный уровень дохода. Между продажами и отзывами пользователей нет зависимости, а между продажами и оценками критиков зависимость слабая.
# 
# Самыми продаваемыми платформами во всех регионах были PS4, XOne, 3DS и WiiU. Рецензии популярных журналов и сайтов о видеоиграх действительно могут влиять на продажи игр. Самым популярным (продаваемым) жанром является action, который значительно опережает другие жанры, количество проданных игровых копий для него превышает 400 тысяч.
# 
# Наиболее активные игроки находятся в Северной Америке, где более половины всех покупок видеоигр (46%) приходится на них. Различные виды платформ не одинаково популярны на рынке видеоигр в разных регионах, даже среди топ-5 платформ. Например, Северная Америка и Европа предпочитают PS4 и XOne, которые составляют около 42% рынка в этих регионах, в то время как японцы предпочитают 3DS (46%). Платформа PS3 пользуется популярностью во всех регионах, ее доля не ниже 18%. Игроки из разных регионов равномерно распределены по возрастным группам пропорционально численности игроков в регионе за актуальный период. Наиболее популярными являются игры с рейтингом E и M.
# 
# По результатам статистических гипотез, средний пользовательский рейтинг платформ Xbox One и PC совпадает, а жанров Action и Sports различается, причем рейтинг жанра Action на 1.45 выше.

# <div class="alert alert-danger">
# <font size="4"><b>❌ Комментарий ревьюера в3</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Стоит поправить нюансы с Х360 и Wii 
#         
#         Самыми продаваемыми платформами во всех регионах были PS4, X360, XOne и Wii. Рецензии популярных журналов и сайтов о видеоиграх действительно могут влиять на продажи игр. Самым популярным (продаваемым) жанром является action, который значительно опережает другие жанры, количество проданных игровых копий для него превышает 400 тысяч.
#         
# или 
#         
#         Например, Северная Америка и Европа предпочитают PS4 и X360
#         
# маркетологи могут потрать деньги на её рекламу  в 2017 году       
#         
# Они могут просто не заметить строчку в середине абзаца
#         
#         К 2016 году молодыми и наиболее прибыльными платформами можно считать PS4, XOne и 3DS. 

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Важно удалить пропуски и «заглушки» перед проведением теста, молодец

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />
# Стоит выравнивать периоды использования платформ, одна из приставок вышла на рынок совсем недавно ...

# <div class="alert alert-d anger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Что означает на языке статистики p-значение: 0.5257376663729298

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> 
# Стоит исправить все подобные моменты
#         
#         Верно следующее утверждение:
# 
# <b>Из теории на тренажере</b>
#         
# Формулирование двусторонних гипотез. <br>
#         
# <b>Никакие экспериментально полученные данные никогда не подтвердят какую-либо гипотезу. Это наше фундаментальное ограничение. </b>Данные могут лишь не противоречить ей или, наоборот, показывать крайне маловероятные результаты (при условии, что гипотеза верна). Но и в том, и в другом случае нет оснований утверждать, что выдвинутая гипотеза доказана.
# Допустим, данные гипотезе не противоречат, тогда мы её не отвергаем. Если же мы приходим к выводу, что получить такие данные в рамках этой гипотезы вряд ли возможно, у нас появляется основание отбросить эту гипотезу.
#         
# https://allatambov.github.io/psms/pdf/hypo-test.pdf
# 

# <div class="alert alert-da nger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Нулевая и альтернативная гипотезы не сформулированы

# <div class="alert alert-dange r">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Стоит поправить вывод
#         
#         Таким образом, остается верным утверждение, что средние пользовательские рейтинги жанров Action и Sports одинаковые

# ### check

# По результатам проведенного анализа: наибольшее влияние на конечный доход, как правило, оказывают оценки критиков. Оценки пользователей не обладают такой силой влияния на доход. Следует обратить внимание на этот фактор.
# 
# В общем и целом, ситуация в игровой индустрии такова: рынок "немобильных" игр медленно умирает. В настоящее время все преследуют графику и новые технологии, что приводит к значительному увеличению среднего бюджета на разработку одной игры за последние годы. Более того, сегодня игроки не так высоко ценят идею и глубину игры; большинство игроков удовлетворяет только качественная графика и оптимизация, и им нравится играть только в том случае, если в игре есть направляющие стрелки. В противном случае игра кажется им слишком сложной.
# 
# В результате, крупные игровые компании стремятся к новым технологиям, а более мелкие фирмы, не обладающие такими бюджетами, вынуждены отступать, так как их единственное преимущество — способность создавать глубокие игры с атмосферой — сегодня не востребовано.
# 
# Все это привело к тому, что рынок уже несколько лет находится в состоянии упадка. Скорее всего, этот спад будет продолжаться, поскольку нет тенденций к возвращению к ценностям, которые преобладали всего десять лет назад.

# ### check

# <div class="alert alert-dan ger">
# <font size="4"><b>❌ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Итоговый вывод технически составлен грамотно
#         
# Стоит перепроверить 
#         
# + результаты после определения актуального периода и исправления всех комментариев, можно добавить названия самых актуальных платформ, жанров и рейтингов, какую долю они занимают на исследуемых рынках
#         
# + и частные предположения, например         
#         
#         По результатам проведенного анализа: наибольшее влияние на конечный доход, как правило, оказывают оценки критиков.       
#         
# Мы формируем рекомендацию не для производителя игр, а для интернет магазина, для продажи или наполнения ассортимента        

# <div class="alert alert-success">
# <font size="5", color= "seagreen"><b>✔️ Комментарий ревьюера</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />   
# Ты выполнил практически все пункты проекта, молодец! Проведен значительный объем исследования 
#         
# Критические ❌ комментарии связаны с неточностями: 
# 
#  + стоит проверить 100% работоспособность кода перед отправкой на ревью        
#  + добавить название и оформление проекту
#  + 2 старые игры с пропусками
#  + заполнение пропусков в колонке год выпуска
#  + добавить оформление проекту — заголовки разделов
#  + обработать пропуски и сократить категории в рейтингах ESRB — на твое усмотрение
#  + выполнить проверку на дублирование записей
#  + самое важное — переопределить актуальный период
#  + исправить диаграмму размаха для анализа продаж на актуальных платформах
#  + поправить исследование зависимости по платформам конкурентам (от оценок критиков и пользователей)        
#  + оценить прибыльность жанров на диаграмме размаха
#  + перестроить графики в ТОП-5 и поправить раздел рейтингов
#  + в разделе проверки гипотез подправить выборки, выводы, добавить формулировки плюс можно более подробно расшифровать значение p_value 
#  + перепроверить промежуточные и итоговый выводы после всех исправлений
# 
# Стоит обратить внимание на ⚠️ комментарии...        
#         
# Если будут вопросы про мои комментарии - задавай, если какой-то формат взаимодействия не устраивает или есть какие-то другие пожелания - пиши :)
# 
# <div class="alert alert-success">
#     <font size="5", color= "seagreen"><b>Жду твой проект и твои комментарии 🤝</b></font><br />

# <div style="border:solid steelblue 3px; padding: 20px">
# <font size="4">🍕<b> Комментарий ревьюера</b></font>
# <br /> 
# <font size="3", color = "black">
# <br />
# Может пригодиться  
#     
#    
# [Визуализация](https://dfedorov.spb.ru/pandas/%D0%AD%D1%84%D1%84%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20Matplotlib.html)
# 
# 
# [Искусство статистики](https://www.mann-ivanov-ferber.ru/books/iskusstvo-statistiki/)
#         
# [Постер «Графики, которые убеждают всех»](https://www.notion.so/6c5ae8ceb8b5411e907c93c9b5e6a44e)        
#         
#         
# В помощь — как реализовать интерактивный план проекта вручную (для собственных проектов), смотри по <a href="https://stackoverflow.com/questions/49535664/how-to-hyperlink-in-a-jupyter-notebook/49717704">ссылке</a>
#     
# пара ссылок и по разделам проекта можно будет переходить без пролистывания всего кода, особенно актуально на проектах длина которых >  10 страниц (и там где не установлен плагин TOC)   
#     
# Плюс    
#     
#     
# [Подборка статей о работе с библиотеками для анализа данных на языке Python](https://dfedorov.spb.ru/pandas/)    

# ### Бонус

# In[98]:


import numpy as np


# In[99]:


data_games = pd.read_csv('/datasets/games.csv')


# In[100]:


data_games.columns = map(str.lower, data_games.columns)


# In[101]:


data_games = data_games.dropna(subset = ['year_of_release', 'name', 'genre'])


# In[102]:


data_games['user_score'] = data_games['user_score'].replace('tbd', np.nan).astype('float')


# In[103]:


data_games['rating'] = data_games['rating'].fillna('unknown')


# In[104]:


data_games['total_sales'] = data_games[['na_sales','eu_sales','jp_sales', 'other_sales']].sum(axis = 1)


# In[105]:


# check
# круги + категория другие

# функция не работает на версии библиотеки pandas >= 2.0 (метод .append устарел)

def graph (df, year, region, name, axes):
    
# фильтруем выборку по переменной

    df = df.query('year_of_release >= @year')

# собираем ТОП-5

    sales = df.pivot_table(index='platform', 
                           values=region, 
                           aggfunc='sum').nlargest(5, region)
    
    sales = sales.reset_index()

# добавляем 6-ю категорию в ТОП-5

    sales = (
            sales.append({'platform': 'Other', region: df[region].sum() 
                       - sales[region].sum()}, ignore_index= True)
         )
    
# меняем названия колонок, но неоптимальным способом 🤝

    sales.columns = ['platform', 'sales']

# создаем словарь цветов    
# Цветовая гамма не подбиралась специально под платформы, кому-что попадется, 😉 
      
    labels_c=sales.platform
    colours = {'Wii':'C60', 'NES':'C1', 'GB':'C2', 'DS':'C3', 'X360':'C4', 
    'PS3':'C5', 'PS2':'C6', 'SNES':'C7', 'GBA':'C8',
               'PS4':'lightsteelblue', '3DS':'orange', 
               'N64':'C11', 'PS':'C12', 'XB':'C13', 'PC':'Fuchsia', '2600':'C15', 'PSP':'C48', 
               'XOne':'LimeGreen',
               'WiiU':'C18', 'GC':'C19', 'GEN':'C20', 'DC':'C21', 'PSV':'C22', 
               'SAT':'C23', 'SCD':'C24', 'WS':'C25', 'NG':'C26', 
               'TG16':'C27', '3DO':'C28', 'GG':'C29', 'PCFX':'C30', 'Other':'darkred'}
   
# рисуем графики

    sales.plot(kind='pie',
               y="sales",
               
               autopct='%1.0f%%',
               wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
               textprops={'size': 'x-large'}, 
               labels= labels_c,
               colors=[colours[key] for key in labels_c],
               legend=False, 
               title = f"Популярность платформ в {name} ", 
               ax = axes).set(ylabel='')
    
# устанавливаем границы для графиков, чтобы не перекрывали друг друга
    
    plt.tight_layout()


# In[106]:


# check
# круги в ряд

x_year = 2010

fig, axes = plt.subplots(1, 3, figsize = (15,6))
fig.suptitle(f'Обзор рынка платформ (портрет покупателя) с {x_year} г.  по 2016 г.', fontsize = 24, fontweight='bold')

graph(data_games, x_year, 'na_sales', 'Северной Америке', axes[0])
graph(data_games, x_year,'eu_sales', 'Европе', axes[1])
graph(data_games, x_year, 'jp_sales', 'Японии', axes[2])


# In[107]:


# check
# круги в ряд

x_year = 2012

fig, axes = plt.subplots(1, 3, figsize = (15,6))
fig.suptitle(f'Обзор рынка платформ (портрет покупателя) с {x_year} г.  по 2016 г.', fontsize = 24, fontweight='bold')

graph(data_games, x_year, 'na_sales', 'Северной Америке', axes[0])
graph(data_games, x_year,'eu_sales', 'Европе', axes[1])
graph(data_games, x_year, 'jp_sales', 'Японии', axes[2])


# In[108]:


# check
# круги в ряд

x_year = 2013

fig, axes = plt.subplots(1, 3, figsize = (15,6))
fig.suptitle(f'Обзор рынка платформ (портрет покупателя) с {x_year} г.  по 2016 г.', fontsize = 24, fontweight='bold')

graph(data_games, x_year, 'na_sales', 'Северной Америке', axes[0])
graph(data_games, x_year,'eu_sales', 'Европе', axes[1])
graph(data_games, x_year, 'jp_sales', 'Японии', axes[2])


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Оптимальный период для исследования 2014-2016 гг., т.к. данные за 2016 г. неполные

# In[109]:


# check
# круги в ряд

x_year = 2014

fig, axes = plt.subplots(1, 3, figsize = (15,6))
fig.suptitle(f'Обзор рынка платформ (портрет покупателя) с {x_year} г.  по 2016 г.', fontsize = 24, fontweight='bold')

graph(data_games, x_year, 'na_sales', 'Северной Америке', axes[0])
graph(data_games, x_year,'eu_sales', 'Европе', axes[1])
graph(data_games, x_year, 'jp_sales', 'Японии', axes[2])


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> 2015 год взят для акцентирования на изменении доли в продажах современных платформ

# In[110]:


# check
# круги в ряд

x_year = 2015

fig, axes = plt.subplots(1, 3, figsize = (15,6))
fig.suptitle(f'Обзор рынка платформ (портрет покупателя) с {x_year} г.  по 2016 г.', fontsize = 24, fontweight='bold')

graph(data_games, x_year, 'na_sales', 'Северной Америке', axes[0])
graph(data_games, x_year,'eu_sales', 'Европе', axes[1])
graph(data_games, x_year, 'jp_sales', 'Японии', axes[2])


# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br /> Стоит обратить внимание на словарь цветов, когда на любом графике каждая платформа имеет свой цвет

# <div class="alert alert-success">
# <font size="4", color= "seagreen"><b>✔️ Комментарий ревьюера в4</b></font>
#     <br /> 
#     <font size="3", color = "black">
# <br />Я выбрал неудачный цвет для категории — «Другие», на темном фоне не видно цифры

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




