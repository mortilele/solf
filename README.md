### Solf - Online Booking System for Wellness

#### What's the point of the projects?
Разработать CRM прототип mindbody. Создания занятий на неделю, возможность записаться на занятия со стороны пользователя
В связи с ростом кол-во занятий, нужно было найти архитектурное решение по расписанию занятий.
Идея заключается в том, что у нас есть три связи таблиц
1. Шаблон занятия(Название, Фото и тд...)
2. Расписание занятий по шаблону на неделю
3. История занятий(сюда будут попадать занятия которые прошли)

Соответственно таким образом:
1. Запрос на актуальные расписания будут отвечать быстро
2. История занятий для бизнес аналитики и статистики не потеряются, (лежать в warehouse)

Недостаток:
1. Для подсчета статистики касательно занятий, нужно реализовать прокси модель(маппер) который включает в себя и текущие занятия и прошедщие
 


#### TODO:
- [x] Authentication (JWT)
- [x] Authorization (Permission classes)
- [ ] Dashboard analytics(Create Mapper for Class Logs and Schedule)
- [x] Booking(Design model)
- [x] File/Image serving (generating thumbnails via imagekit)
- [x] Determine admin theme (JET)
- [x] Implement Serializers, Endpoints
- [x] Implement Redis for message broker, caching
- [x] Implement Celery, Celery Beat
- [ ] Devops (Docker, Docker Compose, Deployment, CI/CD)
- [ ] Test coverage
- [ ] Find solution of timezone problem[Celery ignores timezone] (UTC, Asia/Almaty)
- [x] Provide API documentation (Spectacular)
- [x] Generate UML Class Diagram (django extensions)
- [x] User Pass model
- [x] Filters
- [x] Pagination
- [x] Signals
- [x] Logging
- [x] Document README.md
- [x] Transferring passed classes to logs (periodic task)
- [ ] Secrets from Environment variables (environ)

Generate UML Class Diagram
```shell script
./manage.py graph_models solf.apps -g -o diagram.png  
```