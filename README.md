# workshop

1. Общая информация о продукте и вендоре
Bitbucket - это платформа, предназначенная для совместной разработки программного обеспечения. Продукт разработан компанией Atlassian, которая специализируется на создании инструментов для управления проектами и совместной работы.
Bitbucket поддерживает системы контроля версий Git и Mercurial, что позволяет разработчикам управлять и отслеживать изменения в коде. Это полезно для совместной разработки, проверки кода, управления задачами и интеграции с CI/CD процессами.
1.	Управление репозиториями: Bitbucket позволяет создавать и хранить репозитории, которые содержат историю изменений кода. Вы можете создавать как публичные, так и приватные репозитории.
2.	Коллаборация: Пользователи могут совместно работать над кодом, создавая ветки для различных функциональных изменений и объединяя их в главную ветвь.
3.	Pull Requests (Запросы на слияние): Это механизм, который позволяет разработчикам предложить изменения в коде и запросить их интеграцию в основную ветку. Остальные разработчики могут рассматривать, комментировать и одобрять эти изменения.
4.	Интеграция с CI/CD: Bitbucket интегрируется с системами непрерывной интеграции и непрерывной доставки (CI/CD), такими как Jenkins, Bamboo и другими. Это позволяет автоматизировать тестирование и развертывание приложений.
5.	Внутренние и внешние баг-трекеры: Вы можете связать репозитории с внутренними баг-трекерами Bitbucket или внешними инструментами, такими как Jira, для управления задачами и ошибками.
2. Архитектура продукта (Bitbucket + PostgreSQL)
Архитектура Bitbucket включает в себя клиентскую и серверную части. Клиентская часть представлена веб-интерфейсом, доступным через веб-браузер. Серверная часть работает на серверах и включает в себя компоненты для обработки запросов, управления репозиториями и другие службы.
Для хранения данных Bitbucket использует базу данных. В стандартной конфигурации продукта в качестве базы данных используется PostgreSQL. База данных хранит информацию о репозиториях, пользователях, разрешениях, задачах и других аспектах системы.
3. Установка
Установка Bitbucket начинается с подготовки сервера. Это включает в себя установку Java Runtime Environment (JRE), настройку сетевых параметров и подготовку базы данных. После этого необходимо загрузить и установить сам Bitbucket на сервер.
4. Обновление
Обновление Bitbucket требует осторожности и планирования. Прежде чем начать процесс обновления, следует сделать резервное копирование всех данных, включая конфигурационные файлы и базу данных. После этого можно установить новую версию Bitbucket и выполнить необходимые миграции базы данных.
5. Лицензирование
5.1. Виды лицензий
Bitbucket предлагает несколько видов лицензий: бесплатные версии для небольших команд (обычно с ограниченным количеством пользователей) и платные версии для больших организаций и проектов.
5.2. Политика лицензирования
Политика лицензирования Bitbucket зависит от числа активных пользователей. Лицензия определяет максимальное количество пользователей, которые могут использовать систему. Для бесплатных версий это обычно ограниченное число, а для платных версий количество может быть значительно больше.
15 февраля 2024 г. поддержка продуктов Server будет прекращена. С 15 февраля 2022 г. (по тихоокеанскому времени) вы больше не сможете повысить или понизить уровень своих лицензий Bitbucket Server. Чтобы изменить уровень после указанной даты, вам потребуется выполнить миграцию на версию Cloud или Data Center.
Существует 3 типа лицензий: Cloud, Data Center, Server
Server больше не продаётся и перестанет поддерживаться 15 февраля 2024 г.
Bitbucket Data Center — это решение с самостоятельным управлением, которое обеспечивает взаимодействие профессиональных команд любого размера при работе с исходным кодом, невзирая на расстояния.

6. Конфигурирование
6.1. ldaps
Интеграция с LDAP или LDAPS позволяет автоматически синхронизировать пользователей и группы между Bitbucket и корпоративной директорией. Это упрощает управление доступом и аутентификацией.
6.2. База данных
Настройка базы данных включает в себя оптимизацию параметров для обеспечения хорошей производительности. Это включает настройку пулов подключений, параметров кэширования и других параметров, влияющих на работу Bitbucket.
7. Пользователи и группы
7.1. Виды разрешений
Bitbucket предоставляет различные уровни доступа, такие как "Чтение", "Запись" и "Администрирование". Эти права можно настраивать для пользователей и групп на уровне проектов и репозиториев.

Bitbucket Server предоставляет 4 уровня разрешений, управляемых через веб-интерфейс. Все разрешения могут быть назначены для пользователей или групп пользователей. Группы пользователей могут использоваться для упрощения управления разрешениями. 
Иерархия разрешений следующая:

Глобальные разрешения: 
Они позволяют определить, кто может входить в Bitbucket Server, создавать проекты и репозитории, являться администраторами и системными администраторами:
Пользователь Bitbucket (Bitbucket User): Может войти в Bitbucket и получить доступ к проектам, которым явно предоставлено разрешение на это. Обратите внимание, что все пользователи Bitbucket учитываются при ограничении лицензии.
Создатель проекта (Project Creator): Может создавать новые проекты и репозитории. Для содействия сотрудничеству рекомендуется предоставлять разрешения на создание проектов как можно большему числу пользователей.
Администратор (Admin): Имеет доступ к большинству настроек, необходимых для ежедневного управления Bitbucket. Может добавлять новых пользователей, управлять разрешениями и изменять общие настройки приложения. Администраторы имеют полный доступ ко всем проектам и репозиториям.
Системный администратор (System Admin): Имеет полный контроль над Bitbucket - может изменять конфигурационные свойства системы и все настройки приложения, а также имеет полный доступ ко всем проектам и репозиториям. Рекомендуется предоставлять это разрешение как можно меньшему числу пользователей.
Разрешения проекта: 
Эти разрешения позволяют управлять доступом к репозиториям в рамках проекта агрегированным образом. Вы можете предоставлять разрешения на чтение, запись и администрирование:

Администратор: Может управлять проектом и создавать новые репозитории. Администраторы имеют полный доступ ко всем репозиториям в проекте.
Создание репозитория: Может создавать репозитории в рамках проекта. Пользователи становятся администраторами репозиториев, которые они создают. Все действия, разрешенные записью, также разрешены при наличии разрешения на создание репозитория.
Запись: Может загружать изменения в любой репозиторий в проекте и объединять запросы на слияние, нацеленные на эти репозитории, которые не имеют других ограничений. Все действия, разрешенные доступом на чтение, также разрешены пользователям с правами записи.
Чтение: Может клонировать, просматривать и создавать ответвления от любого репозитория в проекте. Может создавать и участвовать в запросах на слияние, нацеленных на любой из этих репозиториев.
Разрешения репозитория: 
Эти разрешения позволяют управлять доступом к репозиторию для отдельного пользователя или группы пользователей, дополнительно к разрешениям, уже предоставленным в рамках разрешений проекта. Вы можете предоставлять разрешения на чтение, запись и администрирование на индивидуальной основе для каждого репозитория.

Администратор: Может управлять репозиторием. Все действия, разрешенные доступом на чтение и запись, также разрешены администраторам.
Запись: Может загружать изменения в репозиторий и объединять запросы на слияние, нацеленные на этот репозиторий, которые не имеют других ограничений. Все действия, разрешенные доступом на чтение, также разрешены пользователям с правами записи.
Чтение: Может клонировать, просматривать и создавать ответвления от репозитория. Может создавать и участвовать в запросах на слияние, нацеленных на этот репозиторий.
Разрешения ветки: 
Разрешения на ветку обеспечивают дополнительный уровень безопасности в Bitbucket с аутентификацией пользователя и глобальными, проектными и репозиториальными разрешениями, которые в совокупности позволяют контролировать или обеспечивать собственные рабочие процессы или процедуры.
Вы можете контролировать действия, которые могут быть выполнены с следующими элементами в репозитории или проекте:

•	Одно имя ветки
•	Шаблон ветки
•	Модель ветвления (Разработка, Исправление ошибок, Функциональность, Горячее исправление, Релиз)
•	Ограничения, которые могут быть на них наложены:
•	Запретить все изменения, кроме случаев, когда они выполняются определенными пользователями, группами или ключами доступа.
•	Запретить удаления, кроме случаев, когда они выполняются определенными пользователями, группами или ключами доступа.
•	Запретить перезапись истории, кроме случаев, когда она выполняется определенными пользователями, группами или ключами доступа.
•	Запретить изменения без запроса на слияние, кроме случаев, когда они выполняются определенными пользователями, группами или ключами доступа.


8. Работа с проектами
8.1. Создание проекта
Создание проекта позволяет группировать связанные репозитории в логические единицы. Это упрощает организацию кода и задач в больших проектах.
8.2. Разрешения на проект
Настройка разрешений для проектов позволяет точно определить, кто может просматривать, редактировать и управлять проектами.

9. Работа с плагинами
9.1. Как добавить
Плагины могут быть установлены через центр управления плагинами в административной панели Bitbucket. Установка плагинов добавляет новые функциональные возможности.
9.2. Полезные плагины
Существует множество плагинов, расширяющих Bitbucket. Некоторые из них могут интегрироваться с CI/CD системами, предоставлять дополнительные отчеты о коде, улучшать систему управления задачами и многое другое.
10. Работа с API
10.1. Как взаимодействовать
Bitbucket предоставляет API для автоматизации задач и интеграции с другими системами. Это позволяет разработчикам создавать собственные сценарии и инструменты для работы с системой.
11. Мониторинг
Мониторинг Bitbucket включает отслеживание работы серверов, нагрузки на базу данных, доступности системы и других метрик производительности. Для этого можно использовать специализированные инструменты мониторинга, такие как Prometheus, Grafana и др.
Заключение
Эффективное администрирование Bitbucket является ключевым фактором для обеспечения стабильной и безопасной разработки программного обеспечения. Понимание основных аспектов установки, конфигурирования, управления пользователями и мониторинга позволяет максимально использовать возможности этой платформы в рамках ваших проектов.

https://confluence.atlassian.com/bitbucketserver/enabling-jmx-counters-for-performance-monitoring-776640189.html
https://confluence.atlassian.com/bitbucketserver/monitor-application-performance-1167692894.html

 


 

 

