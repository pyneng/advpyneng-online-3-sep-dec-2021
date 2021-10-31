# Проблемы/нюансы с заданиями

* [Перехватываются не все исключения в функции задания 1.3](https://github.com/pyneng/advpyneng-online-3-sep-dec-2021/blob/main/known_task_issues.md#%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%B2%D0%B0%D1%82%D1%8B%D0%B2%D0%B0%D1%8E%D1%82%D1%81%D1%8F-%D0%BD%D0%B5-%D0%B2%D1%81%D0%B5-%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-13)
* [Задание 1.6. В описании задания остался кусок от другого задания про команду sh ip route](https://github.com/pyneng/advpyneng-online-3-sep-dec-2021/blob/main/known_task_issues.md#%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-16)
* [Задание 2.2. Использование TypedDict](https://github.com/pyneng/advpyneng-online-3-sep-dec-2021/blob/main/known_task_issues.md#%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-22-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-typeddict)
* [Ошибка в тесте test_task_4_2b.py](https://github.com/pyneng/advpyneng-online-3-sep-dec-2021/blob/main/known_task_issues.md#%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B0-%D0%B2-%D1%82%D0%B5%D1%81%D1%82%D0%B5-test_task_4_2bpy)
* [Неправильный номер задания в описании заданий 4.2b, 4.2c](https://github.com/pyneng/advpyneng-online-3-sep-dec-2021/blob/main/known_task_issues.md#%D0%BD%D0%B5%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BD%D0%BE%D0%BC%D0%B5%D1%80-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B2-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B8-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9-42b-42c)

## Перехватываются не все исключения в функции задания 1.3

можно исправить except в функции send_show
```python
    except (ScrapliException, SSHException, socket.timeout) as error:
        print(f"Device {host}, Transport {transport}, Error {error}")
```

на такой
```python
    except (ScrapliException, SSHException, socket.timeout, OSError) as error:
        print(f"Device {host}, Transport {transport}, Error {error}")
```

## Задание 1.6. В описании задания остался кусок от другого задания про команду sh ip route

В описании задания остался кусок от другого задания про команду sh ip route.
И не написано что можно править net_interfaces_up.yaml.

Ниже исправленная формулировка задания:

> Задание 1.6
> 
> Написать тест(ы), который проверяет находятся ли все интерфейсы, которые
> указаны в файле net_interfaces_up.yaml в состоянии up (например, столбец
> Protocol в выводе sh ip int br).
> 
> Для проверки надо подключиться к каждому маршрутизатору, который указан в файле
> net_interfaces_up.yaml с помощью scrapli/netmiko и проверить статус интерфейсов.
> Можно использовать параметры из devices_reachable.yaml.
> 
> Тест(ы) должен проходить, если все интерфейсы из файла net_interfaces_up.yaml
> в состоянии up. Тест может быть один или несколько. Файл net_interfaces_up.yaml
> можно менять - писать другие интерфейсы или IP-адреса, главное чтобы формат оставался таким же.
> 
> Тест(ы) написать в файле задания.
> 
> Для заданий этого раздела нет тестов для проверки тестов :)



## Задание 2.2. Использование TypedDict

Если вы хотите использовать TypedDict в задании, есть два варианта решения:

1. удалить файл теста
2. надо добавить в тесты строки (в импорте добавлен ``_TypedDictMeta`` и в конце двух тестов добавлены строки):

```python
# 1 новая строка (добавлен импорт _TypedDictMeta)
from typing import List, Dict, Any, Union, _TypedDictMeta


def test_send_show_params():
    """
    Проверка аннотации параметров
    """
    annotations = task_2_2.send_show.__annotations__
    assert annotations != {}, "Не написана аннотация для функции send_show"
    assert annotations.get("command") == str
    device_dict_annotations = annotations.get("device_dict")
    assert (
        device_dict_annotations == dict_with_str
        or device_dict_annotations == dict_with_str_any
        or device_dict_annotations == dict_with_str_bool_int
        or device_dict_annotations == dict[str, str]
        or device_dict_annotations == dict[str, Any]
        or device_dict_annotations == dict[str, Union[str, bool, int]]
        or device_dict_annotations == dict[Any, Any]
        # 1 новая строка
        or type(device_dict_annotations) == _TypedDictMeta
    )


def test_send_command_to_devices_params():
    """
    Проверка аннотации параметров
    """
    # 2 новые строки
    annotations_send_show = task_2_2.send_show.__annotations__
    device_dict_annotations = annotations_send_show.get("device_dict")
    annotations = task_2_2.send_command_to_devices.__annotations__

    assert (
        annotations != {}
    ), "Не написана аннотация для функции send_command_to_devices"
    assert annotations.get("command") == str
    assert annotations.get("max_workers") == int
    devices_annotations = annotations.get("devices")
    assert (
        devices_annotations == List[dict_with_str]
        or devices_annotations == List[dict_with_str_any]
        or devices_annotations == List[dict_with_str_bool_int]
        or devices_annotations == list[dict[str, str]]
        or devices_annotations == list[dict[str, Any]]
        or devices_annotations == list[dict[str, Union[str, bool, int]]]
        or devices_annotations == list[dict[Any, Any]]
        # 2 новые строки
        or devices_annotations == List[device_dict_annotations]
        or devices_annotations == list[device_dict_annotations]
    )
```

## Ошибка в тесте test_task_4_2b.py

Надо заменить предпоследнюю строку теста.

было так
```python
        correct_stdout in stdout.lower()
```

надо
```python
        correct_stdout in result.stdout.lower()
```

Для контекста (последние три строки теста в итоге должны выглядеть так):
```python
     assert (
        correct_stdout in result.stdout.lower()
     ), "На стандартный поток вывода не выведена информация о времени работы скрипта"
```

## Неправильный номер задания в описании заданий 4.2b, 4.2c

В задании 4.2b:

> Скопировать функцию cli и настройку click из задания 3.2a.

Речь о задании 4.2a и аналогично в 4.2c:

> Скопировать функцию cli и настройку click из задания 3.2a или 3.2b.

Речь о заданиях 4.2a или 4.2b.


## Ошибка в тесте 10.2

Надо заменить такие строки в конце теста test_class:
```python
    assert (
        return_value == correct_return_value
    ), "Функция возвращает неправильное значение"
```

на такие
```python
    reach, unreach = return_value
    assert (
        (sorted(reach), sorted(unreach)) == correct_return_value
    ), "Функция возвращает неправильное значение"

```
