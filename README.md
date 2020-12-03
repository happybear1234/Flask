# 更新日志
## 2020.12.3
- 修改年度图像时间选择器只展示年份





# 项目目录说明
```
/home/user/Projects/CShip
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   └── blog/
│   │       └── calculation.html
│   └── static/
│   │   ├── css/
│   │   ├── image/
│   │   ├── js/
│       └── plugin/
│
├── instance/
│ 
├── tests/
│   └── app.py
├── .gitignore
└── requirements.txt
```

[详细请查看文档](https://dormousehole.readthedocs.io/en/latest/tutorial/layout.html)

- `__init__.py`:配置文件

- `db.py`:数据库链接，操作

- `schema.sql`：sql语句

- `templates/`：模板，base.html整个主页作为母页，calculation为计算条件输入页面

- `static/`： 静态文件

- `instance`: 实例文件夹，放置运行时更改的文件和配置文件[详细](http://docs.jinkan.org/docs/flask/config.html#instance-folders)

- `tests/`： 测试文件不用管

- `.gitignore`:里面保存git命令push时会自动忽略掉的文件

- `requirements.txt`： 保存该项目需要用到的包，`pip >freeze requirements.txt`会更新该文档，使用命令`pip install -r requirements.txt`会一次性安装里面所有包
