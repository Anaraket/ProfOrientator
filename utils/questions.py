questions_base = [
    {
        'number': 1,
        "question": "Легко знакомлюсь с людьми:"
    },
    {
        'number': 2,
        "question": "Охотно и подолгу могу что-нибудь мастерить:"
    },
    {
        'number': 3,
        "question": "Люблю ходить в музеи, театры, на выставки:"
    },
    {
        'number': 4,
        "question": "Охотно и постоянно ухаживаю за растениями, животными:"
    },
    {
        'number': 5,
        "question": "Охотно и подолгу могу что-нибудь вычислять, чертить:"
    },
    {
        'number': 6,
        "question": "С удовольствием общаюсь со сверстниками или малышами:"
    },
    {
        'number': 7,
        "question": "С интересом изучаю  растения и поведение животных."
    },
    {
        'number': 8,
        "question": "Обычно делаю мало ошибок в письменных работах:"
    },
    {
        'number': 9,
        "question": "Мои изделия обычно вызывают интерес у товарищей, старших:"
    },
    {
        'number': 10,
        "question": "Люди считают, что у меня есть художественные способности:"
    },
    {
        'number': 11,
        "question": "Охотно читаю о растениях, животных:"
    },
    {
        'number': 12,
        "question": "Принимаю участие в спектаклях, концертах:"
    },
    {
        'number': 13,
        "question": "Охотно читаю об устройстве механизмов, приборов, машин:"
    },
    {
        'number': 14,
        "question": "Подолгу могу разгадывать головоломки, задачи, ребусы:"
    },
    {
        'number': 15,
        "question": "Легко улаживаю разногласия между людьми:"
    },
    {
        'number': 16,
        "question": "Считают, что у меня есть способности к работе с техникой:"
    },
    {
        'number': 17,
        "question": "Людям нравится мое художественное творчество:"
    },
    {
        'number': 18,
        "question": "У меня есть способности к работе с растениями и животными:"
    },
    {
        'number': 19,
        "question": "Я могу ясно излагать свои мысли в письменной форме:"
    },
    {
        'number': 20,
        "question": "Я почти никогда ни с кем не ссорюсь:"
    },
    {
        'number': 21,
        "question": "Результаты моего технического творчества одобряют незнакомые люди:"
    },
    {
        'number': 22,
        "question": "Без особого труда усваиваю иностранные языки:"
    },
    {
        'number': 23,
        "question": "Мне часто случается помогать даже незнакомым людям:"
    },
    {
        'number': 24,
        "question": "Подолгу могу заниматься музыкой, рисованием, читать книги и т.д.:"
    },
    {
        'number': 25,
        "question": "Могу влиять на ход развития растений и животных:"
    },
    {
        'number': 26,
        "question": "Люблю разбираться в устройстве механизмов, приборов:"
    },
    {
        'number': 27,
        "question": "Мне обычно удается склонить людей на свою точку зрения:"
    },
    {
        'number': 28,
        "question": "Охотно наблюдаю за растениями или животными:"
    },
    {
        'number': 29,
        "question": "Охотно читаю научно-популярную, критическую литературу, публицистику:"
    },
    {
        'number': 30,
        "question": "Стараюсь понять секреты мастерства и пробую свои силы в живописи, музыке и т.п.:"
    }
]

scores = {'nature': 8, 'technic': 8, 'sign': 8, 'art': 8, 'human': 8}

description = {
    'nature': '— <b>"🍃Природный мир":</b>  Профессии, связанные с растениями и животными."\n\n'
              '👨‍🔬🧬Представители этого типа имеют дело с растительными и животными организмами, '
              'микроорганизмами и условиями их существования.\n'
              'Сюда можно отнести профессии, связанные с изучением живой и неживой природы, с уходом за '
              'растениями и животными, с профилактикой и лечением заболеваний растений и животных: '
              'микробиолог, геолог, овощевод, орнитолог, зоотехник, ветеринар, эколог, агрохимик, мелиоратор, '
              'лесовод и др.',
    'technic': '— <b>"⚙️Технологический мир":</b>  Технические и инженерные профессии.\n\n'
               '🚗🛠️Работники имеют дело с неживыми, техническими объектами труда. '
               'Этот тип включает в себя профессии, связанные с созданием, монтажом, '
               'сборкой и наладкой технических средств: газоэлектросварщик, токарь, инженер, конструктор, '
               'слесарь, монтажник, водитель, механик, машинист, технолог и др.',
    'sign': '— <b>"📱Мир знаков и цифр":</b>  Работа с текстами, цифрами и схемами.\n\n'
            '🧑‍💻💻Естественные и искусственные языки, условные знаки, символы, цифры, формулы - вот предметные миры, '
            'которые занимают представителей профессий этого типа. \nДанный тип '
            'объединяет профессии, связанные с текстами, цифрами, формулами, и таблицами, с чертежами, '
            'картами, схемами, звуковыми сигналами: переводчик, программист, бухгалтер, экономист, '
            'специалист по маркетингу, геодезист, телефонист, налоговый инспектор, чертежник и др.',
    'art': '— <b>"🖼️Творческий мир":</b>  Профессии в сфере искусства и дизайна.\n\n'
           '🎭🧑‍🎨Явления, факты художественного отображения действительности - вот что занимает '
           'представителей этого типа профессий. \nК типу "Творческий мир" '
           'можно отнести профессии, связанные с созданием, проектированием, моделированием художественных '
           'произведений, с изготовлением различных изделий по эскизу, образцу: '
           'журналист, художник, модельер, закройщик, ювелир, дизайнер, архитектор, парикмахер, '
           'гример-пастижер, декоратор-оформитель, актер и др. ',
    'human': '— <b>"👩‍⚕️Социальный мир":</b> Профессии, требующие взаимодействия с людьми.\n\n'
             '🧑‍🏫👮‍♂️Предметом интереса, распознавания, обслуживания, преобразования здесь являются социальные '
             'системы, сообщества, группы населения, люди разного возраста. '
             '\nК профессиям типа "Социальный мир" относятся профессии, связанные с медицинским '
             'обслуживанием и правовой защитой человека: врач, медсестра, фельдшер, преподаватель, '
             'психолог, референт, гувернер, менеджер, продавец, официант, агент по рекламе, экспедитор, '
             'юрист, следователь, инспектор ГИБДД и др.'
}
