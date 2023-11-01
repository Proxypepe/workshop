
![[Pasted image 20231031134902.png]]


![[Pasted image 20231031140128.png]]

|Наименование | Поддержка | Требования | Авторизация | Хранение | Метод развертывания | Принцип работы |
|-|-|-|-|-| - | - | 
|**[galactory](https://github.com/briantist/galactory)** | Поддерживается небольшой командой командой из 5 человек. Последний релиз 2 недели назад.  |  1. Необходим доступ до Artifactory     2. УЗ для деплоя артефактов     3. Доступ до ansible server     4. Доступ до инстанса   | Нет | Хранение происходит на стороне artifactory | 1. Просто скриптом. Создать сервис     2. Docker конейнер на машине с artifactory.     3. Kubernetes | Принцип работы |
|**[Ansible Galaxy NG](https://ansible.readthedocs.io/projects/galaxy-ng/en/latest/)** | Поддерживается RedHat | Сложная архитектура(Нужен postgres и redis). Доступы до web-интерфейса и api порта | LDAP keyclock | Локальное, PVC | docker, kubernetes | Позволяет проксировать запросы. Обширная ролевая модель |



| Команда  | galactory | Ansible Galaxy NG |
| -------- | --------- | ----------------- |
| download |  +        |                   |
| init     |  +        |                   |
| build    |  +        |                   |
| publish  |  +        |                   |
| install  |  +         |                   |
| list     |  +         |                   |
| verify   |  +         |                   |


| Команда | galactory | Ansible Galaxy NG |
| ------- | --------- | ----------------- |
| init    | +         |                   |
| remove  | +         |                   |
| delete  | -         |                   |
| list    | +         |                   |
| search  | -         |                   |
| import  | -         |                   |
| setup   | -         |                   |
| info    | -         |                   |
| install | -         |                   |

