# Social Media API: Posts and Comments Functionality

## Overview
This module adds functionality for managing posts and comments within the Social Media API. Users can create, view, update, and delete posts, as well as engage with posts through comments.

---

## Features
- **Posts**: Users can create posts, view all posts, update their posts, and delete their posts.
- **Comments**: Users can comment on posts, view all comments, update their comments, and delete their comments.
- **Pagination**: API responses for posts and comments include pagination for better performance.
- **Filtering**: Posts can be filtered by title or content using query parameters.

---

## API Endpoints

### Posts Endpoints
| Method | Endpoint         | Description                          |
|--------|------------------|--------------------------------------|
| GET    | `/api/posts/`    | Retrieve a list of posts.           |
| POST   | `/api/posts/`    | Create a new post.                  |
| GET    | `/api/posts/{id}/` | Retrieve a single post by ID.      |
| PUT    | `/api/posts/{id}/` | Update a post (only by the author).|
| DELETE | `/api/posts/{id}/` | Delete a post (only by the author).|

#### Example Request: Create a Post
```json
POST /api/posts/
{
  "title": "My First Post",
  "content": "This is the content of my first post."
}
```

#### Example Response: Create a Post
```json
{
  "id": 1,
  "author": "user123",
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "created_at": "2024-12-14T10:00:00Z",
  "updated_at": "2024-12-14T10:00:00Z"
}
```

---

### Comments Endpoints
| Method | Endpoint             | Description                              |
|--------|----------------------|------------------------------------------|
| GET    | `/api/posts/comments/` | Retrieve a list of comments.            |
| POST   | `/api/posts/comments/` | Create a new comment.                   |
| GET    | `/api/posts/comments/{id}/` | Retrieve a single comment by ID.     |
| PUT    | `/api/posts/comments/{id}/` | Update a comment (only by the author).|
| DELETE | `/api/posts/comments/{id}/` | Delete a comment (only by the author).|

#### Example Request: Create a Comment
```json
POST /api/posts/comments/
{
  "post": 1,
  "content": "This is a comment on the first post."
}
```

#### Example Response: Create a Comment
```json
{
  "id": 1,
  "post": 1,
  "author": "user123",
  "content": "This is a comment on the first post.",
  "created_at": "2024-12-14T10:10:00Z",
  "updated_at": "2024-12-14T10:10:00Z"
}
```

---

## Pagination
Both `GET /api/posts/` and `GET /api/posts/comments/` endpoints include pagination.  
By default, 10 items are returned per page. 

### Query Parameters:
- `page`: Specify the page number.

#### Example Request
```bash
GET /api/posts/?page=2
```

---

## Filtering
Posts can be filtered by `title` or `content` using query parameters.

### Query Parameters:
- `search`: The keyword to filter posts by.

#### Example Request
```bash
GET /api/posts/?search=first
```

---

## Permissions
- Only authenticated users can create, update, or delete posts and comments.
- Users can update or delete only their own posts and comments.
- All users can view posts and comments.

---

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Alx_DjangoLearnLab/social_media_api
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## Testing the API
Use tools like **Postman** or **cURL** to interact with the API.

### Example cURL Command
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
-H "Authorization: Token <your_token>" \
-H "Content-Type: application/json" \
-d '{"title": "My Test Post", "content": "This is test content"}'
```

---

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

User Follow and Feed Functionality
Follow and Unfollow Endpoints
Method	Endpoint	Description
POST	/accounts/follow/<id>/	Follow a user
POST	/accounts/unfollow/<id>/	Unfollow a user
Example Request: Follow a User
bash
Copy code
POST /accounts/follow/2/
Authorization: Token <your_token>
Example Response
json
Copy code
{
  "message": "You are now following user123"
}
Feed Endpoint
Method	Endpoint	Description
GET	/posts/feed/	Get posts from followed users
Example Request: Retrieve Feed
bash
Copy code
GET /posts/feed/
Authorization: Token <your_token>
Example Response
json
Copy code
[
  {
    "id": 1,
    "author": "user123",
    "title": "My First Post",
    "content": "This is the content of my first post.",
    "created_at": "2024-12-14T10:00:00Z"
  },
  {
    "id": 2,
    "author": "user456",
    "title": "Another Post",
    "content": "This is another post content.",
    "created_at": "2024-12-14T09:30:00Z"
  }
]

# Documentation for Likes and Notifications Functionality

This document provides an overview of the implementation, usage, and benefits of the likes and notifications features for the **Social Media API**. These features enhance user engagement by enabling users to like posts and receive notifications for various activities.

---

## Features Overview

1. **Likes Functionality:**
   - Users can like or unlike posts.
   - Prevents multiple likes by the same user on the same post.

2. **Notifications Functionality:**
   - Notifications are generated for events like new followers, post likes, and comments.
   - Users can view their unread and read notifications.

---

## Endpoints and Usage

### **Likes Functionality**

#### Like a Post
- **Endpoint:** `/posts/<post_id>/like/`
- **Method:** `POST`
- **Authentication Required:** Yes

##### Request Example:
```bash
POST /posts/1/like/ HTTP/1.1
Authorization: Bearer <your_token>
```

##### Response Example (Success):
```json
{
    "message": "Post liked successfully."
}
```

##### Response Example (Already Liked):
```json
{
    "message": "You already liked this post."
}
```

#### Unlike a Post
- **Endpoint:** `/posts/<post_id>/unlike/`
- **Method:** `POST`
- **Authentication Required:** Yes

##### Request Example:
```bash
POST /posts/1/unlike/ HTTP/1.1
Authorization: Bearer <your_token>
```

##### Response Example (Success):
```json
{
    "message": "Post unliked successfully."
}
```

##### Response Example (Not Liked):
```json
{
    "message": "You haven't liked this post."
}
```

---

### **Notifications Functionality**

#### Fetch Notifications
- **Endpoint:** `/notifications/`
- **Method:** `GET`
- **Authentication Required:** Yes

##### Request Example:
```bash
GET /notifications/ HTTP/1.1
Authorization: Bearer <your_token>
```

##### Response Example:
```json
[
    {
        "id": 1,
        "recipient": "user1",
        "actor": "user2",
        "verb": "liked your post",
        "target": "Post 1",
        "created_at": "2024-12-15T12:00:00Z",
        "read": false
    },
    {
        "id": 2,
        "recipient": "user1",
        "actor": "user3",
        "verb": "started following you",
        "target": null,
        "created_at": "2024-12-15T12:10:00Z",
        "read": true
    }
]
```

---

## Models Overview

### Like Model
Tracks the users who have liked specific posts.

```python
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
```

### Notification Model
Records notifications for user activities.

```python
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor_notifications')
    verb = models.CharField(max_length=255)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
```

---

## Benefits

- **User Engagement:** Notifications keep users informed about interactions, encouraging more activity.
- **Transparency:** Users can see who liked their posts or followed them.
- **Scalability:** The system can easily handle additional notification types in the future.

---

## Testing

### Likes Testing
1. Use Postman to test liking/unliking posts.
2. Verify that a user cannot like the same post multiple times.

### Notifications Testing
1. Ensure notifications are created for the following scenarios:
   - A user likes a post.
   - A user starts following another user.
2. Check the `/notifications/` endpoint to confirm correct retrieval.

---

For further questions or troubleshooting, refer to the code repository at [Alx_DjangoLearnLab](https://github.com/your-repo-link).

