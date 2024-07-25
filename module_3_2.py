def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not (recipient.endswith((".com", ".ru", ".net")) and '@' in recipient
            and sender.endswith((".com", ".ru", ".net")) and '@' in sender):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
send_email('Привет', 'university.help@gmail.com')
send_email('Добрый день', 'staff@gmail.ru')
send_email('Здравствуйте', 'staff@gmail.ru', sender='university.help@gmail.net')
send_email('Hello', 'staff@gmail.ru', sender='university.help@gmail.ne')
send_email('Hello 2', 'staffgmail.ru', sender='university.help@gmail.net')