# LibraryProject

## Introduction
LibraryProject is a Django web application designed to manage a library's book inventory and user records.

## Requirements
- Python 3.x
- Django

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Alx_DjangoLearnLab.git


## Permissions and Groups Setup

### Custom Permissions
This application defines custom permissions for the `Book` model:
- `can_view`: Permission to view books.
- `can_create`: Permission to create books.
- `can_edit`: Permission to edit books.
- `can_delete`: Permission to delete books.

### User Groups
- **Viewers**: Assigned `can_view` permission.
- **Editors**: Assigned `can_view`, `can_create`, and `can_edit` permissions.
- **Admins**: Assigned all permissions.

### Usage
The views in `views.py` use decorators to enforce permissions. For example, the `edit_book` view requires `can_edit` permission to allow editing.
