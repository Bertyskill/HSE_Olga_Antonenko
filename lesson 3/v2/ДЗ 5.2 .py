import json
import re


# Скомпилируем регекс заранее, чтобы не компилировать его потом каждый раз.
email_regex_pattern = '[a-z0-9][a-z0-9_+-]*@[0-9a-z.-]+'
email_regex = re.compile(email_regex_pattern, re.I)

def find_emails_in_text(text):
    result = set()
    for match in email_regex.findall(text):
        email = match.lower().rstrip('.-')
        result.add(email)

    return result


def load_messages_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    messages_json = load_messages_json('100000_efrsb_messages.json')
    # В гит файл json на 100 000 не загрузился из-за размера
    result = {}
    for m in messages_json:
        publisher_inn = m['publisher_inn']
        msg_text = m['msg_text']
        emails = find_emails_in_text(msg_text)

        # Сообщения, в которых нет имейлов, даже не будет записывать в файл.
        if not emails:
            continue

        if publisher_inn not in result:
            result[publisher_inn] = emails
        else:
            result[publisher_inn].update(emails)

    # JSON не поддерживает множества, поэтому сконвертируем их в списки.
    final_result = {}
    for k, v in result.items():
        final_result[k] = list(v)

    with open('emails.json', 'w', encoding='utf-8') as f:
        json.dump(final_result, f, indent=4)


if __name__ == '__main__':
    main()

