# Проблемы/нюансы с заданиями


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

## Задание 1.6

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
