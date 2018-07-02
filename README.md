[![Build Status](https://travis-ci.org/sqxccdy/sql-tricks.svg?branch=master)](https://travis-ci.org/sqxccdy/sql-tricks)
# sql-tricks
Python用\~SQL语句生成戏法\~
又一个SQL构建的轮子呢~

### 创建语法简写
```python
from sqltricks.create import *
from sqltricks.fields import *

CreateTable('test', drop=True, runner=db.conn.execute)(
    VARCHAR(128, name='name', primary_key=True, not_null=True),
    INT(name='age', not_null=True),
    FLOAT(name='money'),
    DATE(name='update'),
)
```
* 执行日志 * 
```text
2018-06-29 13:57:22,967 DEBUG::::Drop TABLE IF EXISTS test;
2018-06-29 13:57:23,026 INFO::::Table drop successfully
2018-06-29 13:57:23,026 DEBUG::::
CREATE TABLE IF NOT EXISTS `test` (
`name` VARCHAR(128) PRIMARY KEY NOT NULL,
`age` INT NOT NULL,
`money` FLOAT,
`update` DATE
);
2018-06-29 13:57:23,167 INFO::::Table created successfully
```
### 插入
```python
from sqltricks.insert import *
from sqltricks.fields import *
InsertTable('test', runner=db.conn.execute)(
    name='name2',
    age=32,
    money=323.2
)

db.conn.commit()
```

```text
2018-06-29 16:01:01,473 DEBUG::::INSERT INTO `test` (money,age,name) values(323.2, 32, "name2");
2018-06-29 16:01:01,476 INFO::::Table insert successfully
```
### 查询
```python
from sqltricks.query import *
from sqltricks.fields import *
import db

def query(sql):
    c = db.conn.cursor()
    cursor = c.execute(sql)
    for row in cursor:
        print(row)

SelectTable('test', '*', runner=query)(
    Where(name='namxce')
)
```
日志
```text
2018-06-29 15:58:40,062 DEBUG::::SELECT * FROM `test` WHERE name="namxce";
2018-06-29 15:58:40,063 INFO::::Table jquery successfully
```

#### 更新
```python
from sqltricks.query import *
from sqltricks.update import *
from sqltricks.fields import *

UpdateTable('user', {'enable': 0}, runner=db.fast_exec)(Where(email='test@test.com'))
```


模块名字征集：模块名不甚满意，如有人有更好建议，邮件留言
sqxccdy@icloud.com