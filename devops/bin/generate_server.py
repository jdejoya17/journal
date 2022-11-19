''' 
TODO: 
    1. Make a REST api request to swaggercodegen to generate a server stub 
    using journal/swagger.yaml
    2. Download generated server stub to journal/devops/
    3. Create temporary directory in journal/devops/server
    4. Extract server stub from journal/devops/ to journal/devops/server
    5. Replace everything in journal/swagger_server with 
    journal/devops/server except:
        - journal/swagger_server/controllers/__init__.py
        - journal/swagger_server/controllers/authorization_controller.py
        - journal/swagger_server/__main__.py
    6. Replace 'do some magic!' with appropriate functions defined in 
    journal/swagger_server/controllers/__init__.py
'''