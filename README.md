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


模块名字征集：模块名不甚满意，如有人有更好建议，邮件留言
sqxccdy@icloud.com