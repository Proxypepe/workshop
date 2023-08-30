
## **Команды которые могут пригодиться**
Создать новый чарт с заданным именем.
```bash
helm create <chart name>
```

Например, команда «helm create foo» создаст структуру каталогов, которая выглядит примерно так:

```
foo/
├── .helmignore    # Содержит шаблоны, которые следует игнорировать при упаковке диаграмм Helm.
├── Chart.yaml     # Информация о чарте
├── values.yaml    # Значения по умолчанию для шаблонов
├── charts/           # Чарты, от которых зависит этот чарт
└── templates/    # Файлы шаблонов
    └── tests/       # Тестовые файлы
```

Локально произвести рендер шаблоны. Выводит заполненные шаблоны.
```bash
helm template <chart name> --debug
```

Изучить чарт на предмет возможных проблем
```bash
helm lint <chart name>
```

Упаковать каталог чартов в архив чарта
```bash
helm package <chart name>
```


## **best practice**

Имена переменных должны начинаться со строчной буквы, а слова разделяться верблюжьим регистром
```yaml
chicken: true
chickenNoodleSoup: true
```

**Плоские или вложенные значения**

Плоские или вложенные значения.YAML — это гибкий формат, значения могут быть глубоко вложенными или сглаженными.

Вложенный:
```yaml
server:
  name: nginx
  port: 80
```
Плоский:
```yaml
serverName: nginx
serverPort: 80
```

В большинстве случаев предпочтение отдается плоскому варианту, а не вложенному. Причина этого в том, что это проще для разработчиков шаблонов и пользователей.

Для оптимальной безопасности на каждом уровне необходимо проверять вложенное значение:
```yaml
{{ if .Values.server }}
  {{ default "none" .Values.server.name }}
{{ end }}
```

Для каждого уровня вложения необходимо выполнить проверку существования. Но для плоской конфигурации такие проверки можно пропустить, что упрощает чтение и использование шаблона.

```yaml
{{ default "none" .Values.serverName }}
```

Если имеется большое количество связанных переменных и хотя бы одна из них не является обязательной, для улучшения читаемости можно использовать вложенные значения.


**Структура templates/**
Каталог templates/ должен быть структурирован следующим образом:

1. Файлы шаблонов должны иметь расширение .yaml, если они создают выходные данные YAML. Расширение .tpl можно использовать для файлов шаблонов, которые не создают форматированного содержимого.
2. В именах файлов шаблонов следует использовать пунктирную запись (my-example-configmap.yaml), а не верблюжий регистр.
3. Каждое определение ресурса должно находиться в отдельном файле шаблона.
4. Имена файлов шаблонов должны отражать тип ресурса в названии. например foo-pod.yaml, bar-svc.yaml

Шаблоны форматирования
Шаблоны должны иметь отступы в два пробела (никогда не использовать табуляцию).

Директивы шаблона должны иметь пробелы после открывающих и перед закрывающими скобками:

Правильный:

```yaml
{{ .foo }}
{{ print "foo" }}
{{- print "bar" -}}
```

Неверно:

```yaml
{{.foo}}
{{print "foo"}}
{{-print "bar"-}}
```

Шаблоны должны по возможности удалять пробелы:

```yaml
foo:
  {{- range .Values.items }}
  {{ . }}
  {{ end -}}
```

Блоки (такие как структуры управления) могут иметь отступы для обозначения потока кода шаблона.

```yaml
{{ if $foo -}}
  {{- with .Bar }}Hello{{ end -}}
{{- end -}}
```

**Пробелы в созданных шаблонах**

Предпочтительно свести к минимуму количество пробелов в создаваемых шаблонах. В частности, многочисленные пустые строки не должны располагаться рядом друг с другом. Но случайные пустые строки (особенно между логическими разделами) — это нормально.

Это лучше всего:
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: example
  labels:
    first: first
    second: second
```
Это нормально:
```yaml
apiVersion: batch/v1
kind: Job

metadata:
  name: example

  labels:
    first: first
    second: second
```
Но этого следует избегать:
```yaml
apiVersion: batch/v1
kind: Job

metadata:
  name: example





  labels:
    first: first

    second: second
```

Основы 

Чтобы определить переменную необходимо использовать следующий синтаксис {{ var }}

## Pipelines

Одной из мощных особенностей языка шаблонов является концепция конвейеров. Основываясь на концепции UNIX, конвейеры представляют собой инструмент для объединения серии команд шаблона для компактного выражения серии преобразований. Другими словами, конвейеры — это эффективный способ последовательного выполнения нескольких задач. Давайте перепишем приведенный выше пример, используя конвейер.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  drink: {{ .Values.favorite.drink | quote }}
  food: {{ .Values.favorite.food | quote }}
```

После подставки

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: trendsetting-p-configmap
data:
  myvalue: "Hello World"
  drink: "coffee"
  food: "PIZZA"
```

Запись 
.Values.favorite.drink | quote
Равносильна
 quote .Values.favorite.drink 

## Встроенные функции 

**Использование default**

Одной из часто используемых в шаблонах функций является функция по умолчанию: default DEFAULT_VALUE GIVEN_VALUE. Эта функция позволяет вам указать значение по умолчанию внутри шаблона, если значение опущено. Давайте используем его, чтобы изменить приведенный выше пример напитка:

```yaml
drink: {{ .Values.favorite.drink | default "tea" }}
```

Использование quote

Эти функции заключают строку в двойные кавычки.
```yaml
drink: {{ .Values.favorite.drink | quote }}
```

Использование indent
Функция indent выполняет отступ каждой строки заданной строки до указанной ширины отступа.



Использование nindent
Функция nindent аналогична функции отступа, но добавляет новую строку в начало строки.


Использование title
todo

Flow Control
Структуры управления предоставляют вам, автору шаблона, возможность контролировать процесс создания шаблона. Язык шаблонов Helm предоставляет следующие структуры управления:

- `if/else` для создания условных блоков
- `with` для указания области действия
- `range`, который обеспечивает цикл в стиле "для каждого"

## if/else

Базовая структура условного оператора выглядит следующим образом:

```fallback
{{ if PIPELINE }}
  # Do something
{{ else if OTHER PIPELINE }}
  # Do something else
{{ else }}
  # Default case
{{ end }}
```

Cтруктуры управления могут выполнять весь конвейер, а не только оценивать значение.

Конвейер оценивается как ложный, если значение:

- логическое значение false
- числовой ноль
- пустая строка
- ноль (пустой или нулевой)
- пустая коллекция (карта, срез, кортеж, словарь, массив)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  drink: {{ .Values.favorite.drink | default "tea" | quote }}
  food: {{ .Values.favorite.food | upper | quote }}
  {{ if eq .Values.favorite.drink "coffee" }}mug: "true"{{ end }}
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  drink: {{ .Values.favorite.drink | default "tea" | quote }}
  food: {{ .Values.favorite.food | upper | quote }}
  {{- if eq .Values.favorite.drink "coffee" }}
  mug: "true"
  {{- end }}
```
Вывод:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: eyewitness-elk-configmap
data:
  myvalue: "Hello World"
  drink: "coffee"
  food: "PIZZA"
  mug: "true"
```

## With

**values.yaml** extract:
```yaml

nodeSelector: 
  disktype: ssd 
  gpu: Nvidia
```
**deployment.yaml** extract:
```yaml
{{- with .Values.nodeSelector }} 
nodeSelector: 
  {{- toYaml . | nindent 8 }} 
{{- end }}
```
Отображается как:
```
      nodeSelector: 
        disktype: ssd 
        gpu: Nvidia
```

Перед визуализированными двумя селекторами стоит 8 пробелов, поскольку в `deployment.yaml` есть `{{- toYaml. | nindent 8}}`

`nindent 8` делает отступ на 8 пробелов.

`with` — конструкция цикла. Со значениями в `.Values.nodeSelector`: преобразуйте его в Yaml (`toYaml`).  
Точка после `toYaml` — это текущее значение `.Values.nodeSelector` в цикле. Это должно быть там.

## range

Многие языки программирования поддерживают циклы с использованием циклов for, циклов foreach или подобных функциональных механизмов. В языке шаблонов Helm способ перебора коллекции заключается в использовании оператора `range`.

values.yaml файл:

```yaml
favorite:
  drink: coffee
  food: pizza
pizzaToppings:
  - mushrooms
  - cheese
  - peppers
  - onions
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  {{- with .Values.favorite }}
  drink: {{ .drink | default "tea" | quote }}
  food: {{ .food | upper | quote }}
  {{- end }}
  toppings: |-
    {{- range .Values.pizzaToppings }}
    - {{ . | title | quote }}
    {{- end }}   
```

