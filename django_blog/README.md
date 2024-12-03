# Django Blog Authentication System

## Features
- User registration
- User login
- User logout
- Profile management

## Usage
1. Register a new user at `/register`.
2. Log in at `/login`.
3. Access the profile page at `/profile`.
4. Log out at `/logout`.

## Notes
- Profile management currently allows viewing basic user information. Additional features can be implemented as needed.

Blog Post Management:

- Post List: Displays all blog posts at `/`.
- Post Detail: Displays a single blog post with details at `/post/<id>/`.
- Post Creation: Authenticated users can create a new post at `/post/new/`.
- Post Editing: Authenticated users can edit their posts at `/post/<id>/edit/`.
- Post Deletion: Authenticated users can delete their posts at `/post/<id>/delete/`.

Permissions:
- Only authenticated users can create posts.
- Only the author of a post can edit or delete their post.
