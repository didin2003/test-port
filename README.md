# Django iPortfolio

This is a Django project scaffold that integrates your iPortfolio template.

## Quickstart

```bash
python -m venv .venv
.venv\Scripts\activate   # on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

### Notes
- Static assets are in `static/` and referenced via `{% static %}`.
- The original index.html was converted and saved in `templates/index.html`.
- To deploy, collect static: `python manage.py collectstatic`.
