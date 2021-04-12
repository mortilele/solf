# solf
Solf - Online Booking System for Wellness

TODO:
- [x] Authentication (JWT)
- [ ] Authorization (Permission classes)
- [ ] Dashboard analytics(Create Mapper for Class Logs and Schedule)
- [x] Booking(Design model)
- [x] File/Image serving (generating thumbnails via imagekit)
- [x] Determine admin theme (JET)
- [x] Implement Serializers, Endpoints
- [ ] Implement Redis for message broker, caching
- [ ] Implement Celery, Flower
- [ ] Devops (Docker, Docker Compose, Deployment, CI/CD)
- [ ] Test coverage
- [ ] Find solution of timezone problem (UTC, Asia/Almaty)
- [x] Provide API documentation (Spectacular)
- [x] Generate UML Class Diagram (django extensions)
- [x] User Pass model
- [ ] Filters
- [ ] Signals
- [x] Logging
- [ ] Document README.md
- [ ] Transferring passed classes to logs (periodic task)
- [ ] Secrets from Environment variables (environ)

Generate UML Class Diagram
```shell script
./manage.py graph_models solf.apps -g -o diagram.png  
```