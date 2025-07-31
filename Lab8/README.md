# CloudComputing_Lab7_SakshiPathrikar

1. Introduction To your project
    1. This  project is built to containarize MinIo, PostFix and Redis services in docker.

2. Description of your project
    1. The project consists of a Docker Compose file that sets up three services inside containers:
        1. MinIO - shared file system
        2. Postfix - email server
        3. Redis - shared memory system
    2. A Python script (cli.py) using the click library allows interaction with these services via command-line commands. These include starting/stopping containers, sending test emails, setting/getting Redis values, and uploading files to MinIO.

3. Design of your project
    1. This project contains:
        1. A docker-compose.yaml file to define and run the services
        2. A cli.py script which allows the user to interact with services using commands

4. Detailed instructions on how to run your project
    1. To start the containers using the CLI: 
        1. To start all containers, enter in terminal the command: python cli.py start
        2. To test redis:
            1. python cli.py redis-set testkey value
            2. python cli.py redis-get testkey
        3. To test minio:
            1. In your browser, go to: http://localhost:9001
            2. Login using: Username: minioadmin and Password: minioadmin
        4. To test postfix: 
            1. python cli.py send-email test@example.com "Hello" "This is a test email"
    2. To start the containers without the cli, using compose.yaml file: 
        1. cd into Lab8 folder.
        2. In the terminal type the command: docker compoe up
        3. To test postfix:
            1. In a new terminal, enter the command: docker exec -it postfix /bin/sh
            2. Once inside the container, enter: sendmail test@example.com
            3. After that enter any body for the email you want and press Ctrl+D
            4. In previous terminal, we should see a message like:  2025-07-31T01:01:53.376231+00:00 INFO    postfix/smtp[1678]: 792AB29DF6: to=<test@example.com>, relay=none, delay=404, delays=397/0.07/7.1/0, dsn=4.3.5, status=deferred (Host or domain name not found. Name service error for name=mailhog type=AAAA: Host not found)
        4. To test redis:
            1. In a new terminal type the command: docker exec -it redis redis-cli ping
        5. To test minio:
            1. Since the container is already running (because of docker compose up in step 2), in browser of choice enter localhost:9001
            2. Once minio image is loaded, enter minioadmin as username and password and you should see the minio object store.
