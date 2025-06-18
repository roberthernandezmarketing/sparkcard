# 📁 Project Structure
## Sparkcard 🟦🟩🟥

```text
sparkcard
│   .env
│   .gitignore
│   README.md
│   requirements.txt
│   run.sh
│   
├───backend
│   └───src
│       │   main.py
│       │   
│       ├───api
│       │   └───v1
│       │       │   deps.py
│       │       │   
│       │       └───routes
│       │               card_routes.py
│       │               user.py
│       │               
│       ├───core
│       │       config.py
│       │       database.py
│       │       security.py
│       │       
│       ├───crud
│       │       card.py
│       │       user.py
│       │       
│       ├───db
│       │       base.py
│       │       base_class.py
│       │       session.py
│       │       
│       ├───models
│       │       author_model.py
│       │       card_model.py
│       │       list_model.py
│       │       __init__.py
│       │       
│       ├───schemas
│       │       card_schema.py
│       │       
│       ├───services
│       │       card_service.py
│       │       
│       └───utils
│               auth.py
│               
├───frontend
│               
└───scripts
        bulk_card_loader.py
        
```
