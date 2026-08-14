# Blog REST API

REST API for a simple blogging platform built with **Django REST Framework**.

## Features

* User registration and Token Authentication
* Create, retrieve, update and delete posts
* Create, retrieve, update and delete comments
* Only authenticated users can create posts and comments
* Users can modify or delete only their own posts and comments
* Published posts are publicly available
* Authors can see their own unpublished posts
* Approved comments are publicly available
* Authors can see their own unapproved comments
* Pagination for post lists
* PostgreSQL database
* Swagger / ReDoc API documentation

## API Endpoints

### Users

| Method | Endpoint                   | Description                      |
| ------ | -------------------------- | -------------------------------- |
| POST   | `/api/v1/users/register/`  | Register a user                  |
| POST   | `/api/v1/users/authorize/` | Authenticate and receive a token |

### Posts

| Method      | Endpoint              | Description          |
| ----------- | --------------------- | -------------------- |
| GET         | `/api/v1/posts/`      | List available posts |
| POST        | `/api/v1/posts/`      | Create a post        |
| GET         | `/api/v1/posts/{id}/` | Retrieve a post      |
| PUT / PATCH | `/api/v1/posts/{id}/` | Update own post      |
| DELETE      | `/api/v1/posts/{id}/` | Delete own post      |

### Comments

| Method      | Endpoint                                         | Description              |
| ----------- | ------------------------------------------------ | ------------------------ |
| GET         | `/api/v1/posts/{post_id}/comments/`              | List comments for a post |
| POST        | `/api/v1/posts/{post_id}/comments/`              | Create a comment         |
| GET         | `/api/v1/posts/{post_id}/comments/{comment_id}/` | Retrieve a comment       |
| PUT / PATCH | `/api/v1/posts/{post_id}/comments/{comment_id}/` | Update own comment       |
| DELETE      | `/api/v1/posts/{post_id}/comments/{comment_id}/` | Delete own comment       |

## Authentication

The API uses DRF Token Authentication. After authorization, the token is passed in the request header:

```text
Authorization: Token <token>
```

## Permissions

Guests have read-only access to published content.

Authenticated users can create posts and comments. The author is assigned automatically from the authenticated user and cannot be selected manually.

Only the author of a post or comment can update or delete it.

## Documentation

Interactive API documentation is available through **Swagger** and **ReDoc**.
