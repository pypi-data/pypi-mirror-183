# e-Dnevnik API

e-Dnevnik API is an unofficial API for [e-Dnevnik](https://ocjene.skole.hr).

## Installation

pip:
```
pip install e-dnevnik-api
```

## Usage

### Login

```py
from e_dnevnik_api import EDnevnik

session = EDnevnik()
session.login("username", "password")
```

### Get all courses

```py
session.get_all_courses()
```

### Get course grades

```py
session.get_course_grades(id)
```

For more examples, check the documentation.

## License

This project is licensed under the MIT license. For more information, check `LICENSE`.
