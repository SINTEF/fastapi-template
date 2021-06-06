# FastAPI/Python Service Template

This is a template for building modular web services with a
best-practise organization of files using the FastAPI web framework.

## Run in Docker
### Development target
The development target will allow for automatic reloading when source code changes. This requires that the local directory is bind-mounted using the -v or --volume argument. To Build and run the development target from the command line:


	docker build --rm -q -f Dockerfile \
	  --label "sintef.fastservice-target=development" \
	  --target development \
	  -t "sintef/fastservice-development:latest" .
	  
	docker run --rm -i --user="$(id -u):$(id -g)" -p 8080:8080 -v "$PWD:/app" sintef/fastservice-development:latest

Open http://localhost:8080 on your browser to test the application.

### Production target
The production target will not reload itself on code change and will run a predictable version of the code on port 80. Also you might want to use a named container with the --restart=always option to ensure that the container is restarted indefinately regardless of the exit status. To build and run the production target from the command line:


	docker build --rm -q -f Dockerfile \
	  --label "sintef.fastservice-target=production" \
	  --target production \
	  -t "sintef/fastservice-production:latest" .
	  
	docker run -d -p 80:80 --user="$(id -u):$(id -g)" --name fastservice --restart=always sintef/fastservice-production:latest

