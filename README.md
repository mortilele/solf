# solf
Solf - Online Booking System for Wellness

TODO:
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
- [ ] Document README.md
- [x] Transferring passed classes to logs (periodic task)
- [ ] Secrets from Environment variables (environ)

Generate UML Class Diagram
```shell script
./manage.py graph_models solf.apps -g -o diagram.png  
```