migrate:

```
alembic -x stage=prod -x schema=app_jorjoran_click downgrade base;
alembic -x stage=prod -x schema=app_jorjoran_click upgrade head;
```
