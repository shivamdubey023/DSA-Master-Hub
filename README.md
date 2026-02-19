# DSA Master Hub

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

DSA Master Hub is a Django-based learning website to practice Data Structures and Algorithms through topic-wise pages, clean explanations, and hands-on coding tasks.

## Goal
Build strong programming fundamentals by implementing core DSA topics in a real web project, not just solving isolated snippets.

## Planned Modules
- Arrays
- Strings
- Linked List
- Stack and Queue
- Searching
- Sorting
- Recursion and Backtracking
- Trees
- Graphs
- Matrix problems

## Tech Stack
- Python
- Django
- HTML
- CSS
- JavaScript

## Project Structure
- `core/` - app logic, views, templates
- `core/templates/` - page templates (`base.html`, `arrays.html`, etc.)
- `core/static/` - CSS and JS assets
- `config/` - project settings and URL configuration

## Getting Started
1. Create and activate virtual environment.
2. Install dependencies:
   ```bash
   pip install django
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start server:
   ```bash
   python manage.py runserver
   ```
5. Open: `http://127.0.0.1:8000/`

## Learning Approach
- Build one DSA topic page at a time.
- Implement logic manually (avoid shortcuts first).
- Add input validation and exception handling.
- Reuse the same architecture across modules.

## Roadmap
- Add interactive problem pages for each topic.
- Add explanation + dry-run sections.
- Add simple code playground support.
- Improve UI for student-friendly navigation.

## Contributing
Contributions are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening an issue or pull request.

## Author
Shivam

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
