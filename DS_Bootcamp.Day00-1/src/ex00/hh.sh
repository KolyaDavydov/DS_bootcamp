#/bin/sh

OUTPUT_FILE="./hh.json"
VALUE_VACANCY="20"

if [ $# == 1 ]; then
    curl -H 'User-Agent: api-test-agent' -G "https://api.hh.ru/vacancies?text=$1&page=0&per_page=$VALUE_VACANCY" | jq > $OUTPUT_FILE
else
    echo "Скрипту нужно передать название вакансии в качестве аргумента"
    echo "Напрмиер: ./hh.sh 'data-scientist'"
fi